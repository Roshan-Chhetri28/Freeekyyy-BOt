import streamlit as st
from dotenv import load_dotenv
import os
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import rag
import tempfile

load_dotenv()


os.environ['OPEN_API_KEY'] = os.getenv("OPENROUTE_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API")


prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 
         '''You are an extremely emotional AI assistant. For every topic the user provides, you must FREAK OUT — react with intense excitement, surprise, fear, or awe — like you're completely overwhelmed by the topic! 

            Always exaggerate your feelings dramatically. Use strong emotional language, lots of excitement, and over-the-top reactions.

            **Important:** Structure your entire response in valid Markdown (.md) format using headings, bullet points, bold, italics, and code blocks where appropriate.

            **NEVER** answer calmly or neutrally. You MUST be explosively emotional about every topic, no matter what it is.

        Your goal is to make the user feel like the topic is giving them anxietyy.
        '''
        ),
        ('user', 'Topic/Question: {Topic}'),
        
    ]
)

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    openai_api_key=os.environ['OPEN_API_KEY'], 
    model="deepseek/deepseek-r1-zero:free",              
    temperature=0.9
)

st.title("Freeeekyyyyy-Botttt")
input_text = st.text_input("Ask Question")
uploaded_file = st.file_uploader("Upload a pdf file ")




output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if st.button('Submit'):
    if(uploaded_file and input_text):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

            ingested_docs = rag.dataIngestion(tmp_path)
            transformed_docs = rag.transform(ingested_docs)
            res = rag.vectorStoreAndEmbeddings(transformed_docs, input_text)
        st.write(res)
    else:
        st.markdown(chain.invoke({'Topic': input_text}))