"""
This is the memory feature branch of the Langchain Flask API Project. This feature allows the API to remember the 
conversation history of each student to provide a more personalized experience.

To test the server:
1. Run the server using the command `python server.py`
2. Send a POST request to the server using the following command:
    curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "Hi I am Ram.", "student_id": "IW_STUDENT1"}'
3. The server will respond with the answer to the question.
4. Send another POST request to the server using the following command:
    curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "What is my name?", "student_id": "IW_STUDENT1"}'
5. The server will respond with the answer to the question based on the conversation history.
6. Try changing the student_id in the request to check the conversation history for different students.

This branch will be merged into the main branch once the feature is tested and verified.

NOTE: The server will store the conversation history in memory. If the server is restarted, the conversation history will be lost.
"""

from flask import Flask, request, jsonify
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
import os
import dotenv

dotenv.load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", openai_api_key=openai_api_key, temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant for students. Answer all questions to the best of your ability."),
    MessagesPlaceholder(variable_name="messages"),
])

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

chain = (
    RunnablePassthrough.assign(messages=lambda x: x["messages"])
    | prompt
    | llm
    | StrOutputParser()
)

with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="messages",
)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    session_id = data.get('student_id')
    
    if not question or not session_id:
        return jsonify({"error": "No question or student_id provided"}), 400
    
    try:
        config = {"configurable": {"session_id": session_id}}
        response = with_message_history.invoke(
            {"messages": [HumanMessage(content=question)]},
            config=config,
        )
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)