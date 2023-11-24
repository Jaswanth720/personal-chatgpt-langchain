
import os

import sys

import constants
from langchain.document_loaders import TextLoader 
from langchain.document_loaders import DirectoryLoader 
from langchain.indexes import VectorstoreIndexCreator 
from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI

os. environ ["OPENAI_API_KEY"] = constants.APIKEY

query = sys.argv[1]

loader = TextLoader ('GadeHistory.txt')
# loader = DirectoryLoader".", glob="*, txt" --This id to pass an entire directory of files
index = VectorstoreIndexCreator().from_loaders([loader])

# print(index.query(query,llm=ChatOpenAI())) --This is for 
print(index.query(query))