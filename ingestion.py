
from cgitb import text
from dotenv import load_dotenv
from openai import embeddings
load_dotenv()
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os


def main():

    print(f"Ingesting...\n")

    loader = TextLoader("mediumblog1.txt")
    document = loader.load()
    print(f"Document loaded: {document}\n")
    print(f"Splitting document...\n")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"Document split into {len(texts)} chunks\n")
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    print(f"Creating vector store...\n")
    vectorstore = PineconeVectorStore.from_documents(texts, embeddings, index_name=os.getenv("PINECONE_INDEX_NAME"))
    print(f"Vector store created!\n")
    print(f"Total vectors in the store: {vectorstore.index.describe_index_stats()['total_vector_count']}\n")
    print(f"Ingestion complete!\n")






if __name__ == "__main__":
    main()
