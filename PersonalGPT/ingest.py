# This file is for Loading the data to Vector Database

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DeepLake
from langchain.embeddings import HuggingFaceInstructEmbeddings, OpenAIEmbeddings, CohereEmbeddings, LlamaCppEmbeddings
from langchain.docstore.document import Document
from tqdm import tqdm
from typing import List
from glob import glob
from multiprocessing import Pool
from .engine import speak

# import environment vars from env_vars.py file
from .env_vars import *

chunk_size = 500
chunk_overlap = 50

class Ingest:
    def __init__(self) -> None:
        match MODEL_TYPE: 
            case 'OpenAI':
                self.embeddings= OpenAIEmbeddings(openai_api_key=API_KEY)
            case 'Cohere':
                self.embeddings = CohereEmbeddings(cohere_api_key=API_KEY)
            case 'LlamaCpp':
                self.embeddings = LlamaCppEmbeddings()
            case _default_:
                self.embeddings = HuggingFaceInstructEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)
        
    def load_single_document(self, file_path: str) -> List[Document]:
        """Loads single document at a time
        Args:
            file_path (str): Take filepath, where the file is that you want to load

        Raises:
            ValueError: If file not found or file extension not supported

        Returns:
            List[Document]: Content of the file
        """
        ext = "." + file_path.rsplit(".", 1)[-1]
        if ext in LOADER_MAP:
            loader_class, loader_args = LOADER_MAP[ext]
            loader = loader_class(file_path, **loader_args)
            return loader.load()
    
        raise ValueError(f"Unsupported file extension '{ext}'")

    def load_documents(self, source_dir: str, ignored_files: List[str] = []) -> List[Document]:
        """
        Loads all documents from the source documents directory, ignoring specified files
        """
        all_files = []
        for ext in LOADER_MAP:
            all_files.extend(
                glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True)
            )
        filtered_files = [file_path for file_path in all_files if file_path not in ignored_files]

        with Pool(processes=INGEST_THREADS) as pool:
            results = []
            with tqdm(total=len(filtered_files), desc='Loading new documents', ncols=80) as pbar:
                for i, docs in enumerate(pool.imap_unordered(self.load_single_document, filtered_files)):
                    results.extend(docs)
                    pbar.update()

        return results

    def process_documents(self, ignored_files: List[str] = []) -> List[Document]:
        """
        Load documents and split in chunks
        """
        print(f"Loading documents from {SOURCE_DIRECTORY}")
        documents = self.load_documents(SOURCE_DIRECTORY, ignored_files)
        if not documents:
            print("No new documents to load")
            exit(0)
        print(f"Loaded {len(documents)} new documents from {SOURCE_DIRECTORY}")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        texts = text_splitter.split_documents(documents)
        print(f"Split into {len(texts)} chunks of text (max. {chunk_size} tokens each)")
        return texts
    
    def does_vectorstore_exist(self, persist_directory: str) -> bool:
    
        if os.path.exists(os.path.join(persist_directory, 'index')):
            if os.path.exists(os.path.join(persist_directory, 'chroma-collections.parquet')) and os.path.exists(os.path.join(persist_directory, 'chroma-embeddings.parquet')):
                list_index_files = glob.glob(os.path.join(persist_directory, 'index/*.bin'))
                list_index_files += glob.glob(os.path.join(persist_directory, 'index/*.pkl'))
                # At least 3 documents are needed in a working vectorstore
                if len(list_index_files) > 3:
                    return True
        return False
    def load(self):
    # Create embeddings
        if self.does_vectorstore_exist(PERSIST_DIRECTORY):
            # Update and store locally vectorstore
            speak(f"Appending to existing vectorstore at {PERSIST_DIRECTORY}")
            self.db = DeepLake(embedding_function=self.embeddings, dataset_path=PERSIST_DIRECTORY, verbose=False)
            collection = self.db.get()
            texts = self.process_documents([metadata['source'] for metadata in collection['metadatas']])
            speak(f"Creating embeddings. May take some minutes...")
            self.db.add_documents(texts)
        else:
            # Create and store locally vectorstore
            speak("Creating new vectorstore")
            texts = self.process_documents()
            speak(f"Creating embeddings. May take some minutes...")
            self.db = DeepLake.from_documents(texts, self.embeddings, dataset_path=PERSIST_DIRECTORY, verbose=False)
        speak(f"Ingestion complete!")
        return self.db
