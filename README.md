# PersonalGPT
Your own GPT-powered Personal Assistant to whom you can ORDER or INSTRUCT to do some task or search for something using your VOICE commands.
Built with [LangChain](https://github.com/hwchase17/langchain), [GPT4All](https://github.com/nomic-ai/gpt4all), [LlamaCpp](https://github.com/ggerganov/llama.cpp), [Chroma](https://www.trychroma.com/) and [SentenceTransformers](https://www.sbert.net/).
-Also Supports OpenAI's GPT3, GPT4 model, Cohere.

This project is Highly Inspired by [privateGPT](https://github.com/imartinez/privateGPT) for GPT assistance making but this project uses [DeepLake VectorStores](https://github.com/activeloopai/deeplake) to store your dataset/files.

# Installing dependencies

On Windows:
```shell
    pip install -r requirements.txt
```
On Linux / Mac:
```
    pip3 install -r requirements.txt
```
# Setting Environment Variables

Open the `PersonalGPT/env_vars.py`

and edit the variables appropriately in the `env_vars.py` file.

```
MODEL_TYPE: supports LlamaCpp, GPT4All, OpenAI & Cohere
PERSIST_DIRECTORY: is the folder you want your vectorstore in
MODEL_PATH: Path to your GPT4All or LlamaCpp supported LLM
MODEL_N_CTX: Maximum token limit for the LLM model
MODEL_N_BATCH: Number of tokens in the prompt that are fed into the model at a time. Optimal value differs a lot depending on the model (8 works well for GPT4All, and 1024 is better for LlamaCpp)
EMBEDDINGS_MODEL_NAME: SentenceTransformers embeddings model name (see https://www.sbert.net/docs/pretrained_models.html)
TARGET_SOURCE_CHUNKS: The amount of chunks (sources) that will be used to answer a question
VOICE_MODEL=pyttsx3
VOICE_REC_ENGINE=SpeechRecognition
API_KEY=OpeAI or Cohere API Key
```

## Instructions for ingesting your own dataset

Put any and all your files into the `source_documents` directory

The supported extensions are:

   - `.csv`: CSV,
   - `.docx`: Word Document,
   - `.doc`: Word Document,
   - `.enex`: EverNote,
   - `.eml`: Email,
   - `.epub`: EPub,
   - `.html`: HTML File,
   - `.md`: Markdown,
   - `.msg`: Outlook Message,
   - `.odt`: Open Document Text,
   - `.pdf`: Portable Document Format (PDF),
   - `.pptx`: PowerPoint Document,
   - `.ppt`: PowerPoint Document,
   - `.txt`: Text file (UTF-8),
   - `.xls`: Excel Spreadsheet
   - `.xlsx`: Excel Spreadsheet

Give the following command to ingest all the data.

# Run PersonalGPT
On Windows:
```shell
    python run_PersonalGPT.py
```
On Linux / Mac:
```shell
    python3 run_PersonalGPT.py
```
### Now Give Voice commands whatever you use
```shell
open browser
load my files
ask gpt
tell me a joke
open youtube
```
and many more

This module is free to use, modify, share

Contribution is open for everyone, if you find some issue feel free to pull an Issue request or you've fixed this then do a PR

Thank You, for reading this.
