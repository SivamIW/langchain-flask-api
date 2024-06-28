# LangChain Flask API

This project is a simple Flask API server that uses the LangChain pipeline to answer questions. The server listens for POST requests to the `/ask` endpoint with a JSON payload containing a question. It then uses the LangChain pipeline to generate an answer to the question and returns it in the response.

## Requirements

- Python 3.7+
- Flask
- LangChain
- OPENAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/SivamIW/langchain-flask-api.git
   cd langchain-flask-api
   ```

2. Install the required packages:
   ```
   pip install flask langchain langchain-openai
   ```

## Setting up API Keys

### For OpenAI API Key

1. Obtain an API key from the [OpenAI](https://platform.openai.com/api-keys).
2. To set API Key, change the value of the OPENAI_API_KEY variable in the .env file.

## Running the Server

### Using Python

Run the following command:
```
python server.py
```

### Run Using a Batch File (Windows)

Double-click `run_server.bat` to start the server.

## Testing the Server

You can test the server using cURL:

```
curl -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is the capital of France?\"}"
```

Or using Python:

```python
import requests

response = requests.post('http://localhost:5000/ask', json={'question': 'What is the capital of France?'})
print(response.json())
```