# This file is for Loading the data to Vector Database

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DeepLake
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

from env_vars import *

