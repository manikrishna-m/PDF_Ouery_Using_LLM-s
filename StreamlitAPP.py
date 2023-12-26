import os
import json
import traceback
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from langchain.callbacks import get_openai_callback

def present_quiz(questions):
    user_responses = []
    
    for index, question in enumerate(questions, start=1):
        st.write(f"Question {index}: {question['MAQ']}")
        options = question['Choices'].split(" || ")
        
        # Include the question index in the key
        user_response = st.radio(f"Select an option for Question {index}:", options, key=f"radio_{index}")
        user_responses.append(user_response)
    
    return user_responses


with open('/Users/manikrishnamandepudi/Documents/NLP Projects/llm-pdf-query/Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQs Creator Application with LangChain")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    mcq_count = st.number_input("Enter the number of MCQs you want to generate", min_value=3, max_value=50)

    subject = st.text_input("Enter the subject you want to generate the MCQs for", max_chars=20)

    tone = st.text_input("Enter the tone you want to generate the MCQs for", max_chars=20, placeholder="Simple")

    button = st.form_submit_button("Generate MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Generating MCQs..."):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Something went wrong. Please try again.")
                st.stop()
            else:
                if isinstance(response, dict):
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)

                            # Present the quiz to the user
                            st.title("Quiz Time!")
                            user_responses = present_quiz(table_data)

                            # Evaluate user responses
                            correct_responses = [question['Correct'] for question in table_data]
                            user_score = sum([1 for user_resp, correct_resp in zip(user_responses, correct_responses) if user_resp == correct_resp])

                            st.title(f"Your Score: {user_score}/{len(table_data)}")
                            st.text_area(label="Reviews", value=response["review"])

                        else:
                            st.error("Error in the table data")
                    else:
                        st.error("Error in generating quiz questions")
                else:
                    st.write(response)