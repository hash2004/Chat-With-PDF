import streamlit as st
import cassio
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
import spacy
from pdfminer.high_level import extract_text


Astra_DB_ID = "XYZ"
Astra_DB_Application_Token = "XYZ"
OPENAI_API_KEY = "XYZ"

nlp = spacy.load("en_core_web_sm")

cassio.init(database_id=Astra_DB_ID, token=Astra_DB_Application_Token)

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

st.title('Chat with your PDF! Developed By: Hashim Muhammad Nadeem')
vector_table_name = st.text_input("Enter your name")

def read_pdf(file):
    text = extract_text(file)
    return text

def process_text(raw_text):
    doc = nlp(raw_text)
    return [sent.text.strip() for sent in doc.sents]

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    try:
        raw_text = read_pdf(uploaded_file)
        if raw_text:
            sentences = process_text(raw_text)
            astra_vector_store = Cassandra(embedding=embedding, table_name=vector_table_name, session=None, keyspace=None)
            astra_vector_store.add_texts(sentences)
            astra_vector_index = VectorStoreIndexWrapper(vectorstore=astra_vector_store)

            query_text = st.text_input("Enter your question:")
            if query_text:
                answer = astra_vector_index.query(query_text, llm=llm).strip()
                st.write(answer)
        else:
            st.write("No text could be extracted from the uploaded PDF.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
