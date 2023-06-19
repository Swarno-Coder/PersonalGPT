# This file is for configuration of the langchain package.
# The configuration is loaded from the langchain.config module.
#
# The configuration is a dictionary with the following keys:
#
# MODEL_TYPE: The type of model to use.
# MODEL: The name of the model to use.
# MODEL_PATH: The path to the model to use.
# EMBEDDINGS_MODEL_NAME: The name of the embeddings model to use.
# MODEL_N_CTX: The number of tokens to process
# TARGET_SOURCE_CHUNKS: The number of chunks to split the source into
# INGEST_THREADS: The number of threads to use for ingestion
# SOURCE_DIRECTORY: The folder to store the source documents
# PERSIST_DIRECTORY: The folder to store
# LOADER_MAP: A dictionary mapping file extensions to Document Loader classes

import os
# Import the Document Loaders
from langchain.document_loaders import (
        CSVLoader,
        PDFMinerLoader,
        TextLoader,
        EverNoteLoader,
        UnstructuredExcelLoader,
        UnstructuredEPubLoader,
        UnstructuredHTMLLoader,
        UnstructuredMarkdownLoader,
        UnstructuredODTLoader,
        UnstructuredPowerPointLoader,
        UnstructuredWordDocumentLoader,
)

# Set model name and path
MODEL_TYPE='GPT4All'
MODEL='ggml-gpt4all-j-v1.3-groovy.bin'
MODEL_PATH=f'models/{MODEL}'
EMBEDDINGS_MODEL_NAME='all-MiniLM-L6-v2'
MODEL_N_CTX=1000
TARGET_SOURCE_CHUNKS=4

# Set Voice model
VOICE_REC_MODEL='SpeechRecognition'
VOICE_ENGINE='pyttsx3'

#define root directory
ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
# Define the folder for storing database
SOURCE_DIRECTORY = f"{ROOT_DIRECTORY}/SOURCE_DOCUMENTS"
PERSIST_DIRECTORY = f"{ROOT_DIRECTORY}/DB"

# Change this to the number of threads you want to use for ingestion
INGEST_THREADS = os.cpu_count() or 8

# Map the Document Loader to its file extension
LOADER_MAP = {
    ".txt": TextLoader,
    ".pdf": PDFMinerLoader,
    ".csv": CSVLoader,
    ".xls": UnstructuredExcelLoader,
    ".xlsx": UnstructuredExcelLoader,
    ".ppt" : UnstructuredPowerPointLoader,
    ".doc" : UnstructuredWordDocumentLoader,
    ".docx" : UnstructuredWordDocumentLoader,
    ".html" : UnstructuredHTMLLoader,
    ".md" : UnstructuredMarkdownLoader,
    ".epub" : UnstructuredEPubLoader,
    ".odt" : UnstructuredODTLoader,
    ".enex" : EverNoteLoader,
}
