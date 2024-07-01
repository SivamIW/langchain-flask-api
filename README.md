# LangChain Flask API with Memory

This project is a Flask API server that uses the LangChain pipeline to answer questions with memory for different students. The server maintains conversation history for each student, providing a more personalized experience.

## Requirements

- Python 3.7+
- Flask
- LangChain
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/SivamIW/langchain-flask-api.git
   cd langchain-flask-api
   ```

2. Install the required packages:
   ```
   pip install flask langchain langchain-openai langchain-community
   ```

## Setting up API Keys

### For OpenAI API Key

1. Obtain an API key from [OpenAI](https://platform.openai.com/api-keys).
2. Set the API Key by changing the value of the OPENAI_API_KEY variable in the .env file.

## Running the Server

### Using Python

Run the following command:
```
python server.py
```

### Using a Batch File (Windows)

Double-click `run_server.bat` to start the server.

## Testing the Server

You can test the server using cURL:

```
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "Hi I am Ram.", "student_id": "IW_STUDENT1"}'
```

Then, to test the memory feature:

```
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{"question": "What is my name?", "student_id": "IW_STUDENT1"}'
```

Or using Python:

```python
import requests

response = requests.post('http://localhost:5000/ask', json={'question': 'Hi I am Ram.', 'student_id': 'IW_STUDENT1'})
print(response.json())

response = requests.post('http://localhost:5000/ask', json={'question': 'What is my name?', 'student_id': 'IW_STUDENT1'})
print(response.json())
```

## Features

- Maintains separate conversation histories for different students
- Uses LangChain's ChatOpenAI model for generating responses
- Implements a system message to set the context for the AI assistant
- Utilizes Flask for easy API setup and handling

## Note

The server stores the conversation history in memory. If the server is restarted, the conversation history will be lost. For production use, consider implementing a persistent storage solution.

## Contributing

This is the memory feature branch of the Langchain Flask API Project. Once tested and verified, it will be merged into the main branch.