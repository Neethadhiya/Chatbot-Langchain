import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
st.title("Ask me anything 🐦")
st.subheader("🚀")

gpt3_model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125", openai_api_key=api_key)
topic = st.text_input("Topic")

if st.button("Generate"):
    prompt = f"Give details about {topic}"
    response = gpt3_model.invoke(prompt)
    st.write(response.content)

# Display the output
