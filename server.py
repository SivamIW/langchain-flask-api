""" EXPLANATION:
    >This is a simple Flask API server that uses the LangChain pipeline to answer questions.
    
    > The server listens for POST requests to the /ask endpoint with a JSON payload containing a question.
    
    > The server then uses the LangChain pipeline to generate an answer to the question and returns it in the response.
    
    > To set API_KEY, change the value of the OPENAI_API_KEY variable in the .env file.
    
    > To run the server, use the following command:
        'python server.py'
    
    > To test the server, use the following command:
        'curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is the capital of France?\"}"'
"""

from flask import Flask, request, jsonify
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
import os
import dotenv

app = Flask(__name__)

dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", openai_api_key=openai_api_key, temperature=0)

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant for students. Answer the following question: {question}"
)

chain = prompt | llm | StrOutputParser()

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    try:
        response = chain.invoke({"question": question})
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
