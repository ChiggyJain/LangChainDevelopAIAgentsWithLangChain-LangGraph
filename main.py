
import re
from unittest import result
from dotenv import load_dotenv
from langchain_core import vectorstores
from openai import embeddings
load_dotenv()
import os
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


def main():

    print(f"Hello introduction-to-vector-dbs from langchain-course!\n")

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    llm = ChatOpenAI()
    query = "What is pinecone in machine learning?"
    chain = PromptTemplate.from_template(template=query) | llm
    result = chain.invoke(input={})
    print(f"LLm-Result-1: {result.content}\n")

    vectorstores = PineconeVectorStore(embedding=embeddings, index_name=os.getenv("PINECONE_INDEX_NAME"))

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat") 
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(retriever=vectorstores.as_retriever(), combine_docs_chain=combine_docs_chain)  
    result  = retrieval_chain.invoke(input={"input":query})
    print(f"LLm-Result-2: {result}\n")



if __name__ == "__main__":
    main()
