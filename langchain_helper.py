# langchain_helper.py
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQAWithSourcesChain
import os

os.environ['MISTRAL_API_KEY'] = 'your-api-key'
model = init_chat_model('mistral-large-latest', model_provider='mistralai')

def get_chain_from_url(url):
    loader = UnstructuredURLLoader(urls=[url])
    data = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', ' '],
        chunk_size=200,
        chunk_overlap=0
    )
    chunks = splitter.split_documents(data)

    encoder = HuggingFaceBgeEmbeddings()
    db = Chroma.from_documents(chunks, encoder)

    chain = RetrievalQAWithSourcesChain.from_llm(llm=model, retriever=db.as_retriever())
    return chain
