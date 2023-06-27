from langchain.base_language import BaseLanguageModel
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.base import Embeddings
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.vectorstores import VectorStore


def load_pdf_vectorstore(file_path: str, embedding: Embeddings, chunk_size: int = 4000, chunk_overlap: int = 200):
    doc = PyPDFLoader(file_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = splitter.split_documents([doc])
    return FAISS.from_documents(docs, embedding=embedding)


def load_pdf_chain(llm: BaseLanguageModel, vectorstore: VectorStore):
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm, retriever=vectorstore.as_retriever(), memory=memory)
