from flask import Flask, render_template, request, redirect, url_for, session
from data_preprocessing import DataPreProcessing
from data_ingestion import DataIngestion
from chat_pipeline import ChatPipeline
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
load_dotenv()

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def answer_question():
    # Get the JSON data from the request body
    data = request.get_json()

    # Check if 'question' key is in the request data
    if 'question' not in data:
        return jsonify({"error": "Invalid request, 'question' key missing"}), 400

    question = data['question']
    pdf = "E:/Projects/nepatronix_chatbot/chatbot/pdfs/Nepatronix_syllabus.pdf"
    data_preprocess = DataPreProcessing()
    
    
    text = data_preprocess.read_pdf()
    print(text)
    splits = data_preprocess.extract_chunk(text)
    print(len(splits))
    
    data_ingestion = DataIngestion(store_name="nepatronix")
    vector_store = data_ingestion.create_vectorstore(splits)
    chat_pipeline  = ChatPipeline(vectorstore=vector_store)
    response = chat_pipeline.process_query(question)
    return jsonify({"response": response})


    # # Process the question (here we're using a simple predefined answer)
    # if question.lower() == "what is my name":
    #     answer = "My name is Bikam"
    # else:
    #     answer = "I don't know the answer to that question"

    # # Respond with JSON
    # response = {
    #     "response": answer
    # }

    # return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
