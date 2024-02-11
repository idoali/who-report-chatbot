import os
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain import OpenAI
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
import time 

os.environ["OPENAI_API_KEY"] = "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"

embedding_function = SentenceTransformerEmbeddings(model_name = "all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory = "docs/chroma_db", embedding_function = embedding_function)
retriever = vectordb.as_retriever()
llm = OpenAI(temperature = 0.9)

qa_chain = RetrievalQA.from_chain_type(llm = llm,
                                       chain_type = "stuff",
                                       retriever = retriever,
                                       return_source_documents = True,
                                       verbose = False)

def make_output(query):
    answer = qa_chain(query)
    result = answer["result"]
    return result 

def modify_output(input):
    for text in input.split():
        yield text + " "
        time.sleep(0.05)