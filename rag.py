# * This is for Rag pipeline
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENROUTE_API_KEY')
def dataIngestion( document):
    loader = PyPDFLoader(document)
    ingested_docs = loader.load()

    return ingested_docs


def transform( ingested_docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    transformed_docs = text_splitter.split_documents(ingested_docs)
    return transformed_docs


def vectorStoreAndEmbeddings(docs, query):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(documents=docs, embedding=embeddings)
    return db.similarity_search(query)[0].page_content