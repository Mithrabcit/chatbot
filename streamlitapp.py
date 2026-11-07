import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Application heading
st.title("🤖 My AI Chatbot")
st.write("Welcome! Ask me anything.")

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/ask"

# User input
question = st.text_input("Enter your question:")

# Send button
if st.button("Send"):

    if question.strip():

        try:
            with st.spinner("Generating your answer..."):

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=60
                )

            if response.status_code == 200:

                answer = response.json()["answer"]

                st.subheader("AI Response")
                st.write(answer)

            else:
                st.error("Backend error!")
                st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to FastAPI. Check whether the backend is running.")

        except requests.exceptions.Timeout:
            st.error("The request took too long. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.warning("Please enter a question.")