import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain import OpenAI
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
import time 

# Load environment variables from .env file
load_dotenv()

# Initialize SentenceTransformer model for embeddings
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize Chroma vector store for document embeddings
# and create retriever from the vector store
vectordb = Chroma(persist_directory="docs/chroma_db", embedding_function=embedding_function)
retriever = vectordb.as_retriever()

# Initialize OpenAI language model with temperature parameter
llm = OpenAI(temperature=0.9)

# Create a retrieval-based question-answering (QA) chain
# based on a predefined chain type "stuff"
qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type="stuff",
                                       retriever=retriever,
                                       return_source_documents=True,
                                       verbose=False)

# Function to generate output based on a query
def make_output(query):
    # Query the QA chain and extract the result
    answer = qa_chain(query)
    result = answer["result"]
    return result 

# Function to modify the output by adding spaces between each word with a delay
def modify_output(input):
    # Iterate over each word in the input string
    for text in input.split():
        # Yield the word with an added space
        yield text + " "
        # Introduce a small delay between each word
        time.sleep(0.05)
