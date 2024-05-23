# Neo4j LlamaIndex Starter Kit

This repository contains a Python notebook and a FastAPI application that demonstrate how to use the `llama-index` library to interact with a Neo4j graph database for storing, indexing, and querying documents.

## Prerequisites

- Python 3.8+
- Neo4j database
- OpenAI API key
- FastAPI
- Uvicorn (or any other ASGI server)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/llama-index-neo4j-starter-kit.git
cd llama-index-neo4j-starter-kit
```

2. Install the required Python packages using Poetry:

```bash
poetry install
```

Alternatively, if you prefer to use `pip`, you can install the dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Set up your Neo4j credentials:

Update your Neo4j credentials in the `credentials.json` file in the project directory. If you already have a graphdatabase set up you will update with your current Neo4j DB Credentials and OpenAI api key. If you are looking to test out a sample dataset, the following Neo4j credentials allow for read-only access to a hosted sample dataset. Your own OpenAI key will be needed to run this server.

```json
NEO4J_URI=neo4j+ssc://9fcf58c6.databases.neo4j.io 
NEO4J_DATABASE=neo4j 
NEO4J_USERNAME=public 
NEO4J_PASSWORD=read_only 
OPENAI_API_KEY=<add_your_openai_key_here>
```
NOTE: the `NEO4J_URI` value can use either the neo4j or [bolt](https://neo4j.com/docs/bolt/current/bolt/) uri scheme. For more details on which to use, see this example.

## Usage

### Jupyter Notebook

1. Open the `starter_kit_notebook.ipynb` notebook in Jupyter Notebook or Google Colab.

2. Run the notebook cells sequentially to:
   - Install necessary libraries
   - Import required modules and classes
   - Load Neo4j credentials
   - Set up the OpenAI API key and other settings
   - Create graph and vector stores
   - Retrieve documents from Neo4j nodes with text properties
   - Create a KnowledgeGraphIndex from the retrieved documents and store it back in the Neo4j database with embeddings
   - Query the KnowledgeGraphIndex using a query engine
   - Create a GPTVectorStoreIndex from the documents and query it
   - Use a KnowledgeGraphRAGRetriever to query the graph database
   - Query the Neo4j database directly using Cypher queries with the help of the Neo4jQueryToolSpec and OpenAIAgent classes
   - Create a VectorStoreIndex from the documents and query it

### FastAPI Application

The starter kit also includes a FastAPI application that provides an API endpoint for sending and receiving chat messages. The application is defined in the `app.py` file.

To run the FastAPI application using Poetry, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the FastAPI server:

```bash
poetry run uvicorn llamaindex_starter_kit.main:app --reload
```

The default local address will be: `http://127.0.0.1:8000`

To change the port, append the command with `--port=<port>`. For example:

```bash
poetry run uvicorn llamaindex_starter_kit.main:app --reload --port=9000
```

3. The FastAPI application will be available at the specified address and port. You can interact with the API using tools like cURL, Postman, or by making HTTP requests from your code.

4. To send a chat message, make a POST request to the `/api/chat` endpoint with a JSON payload containing the message. For example:

```json
{
  "message": "Hello, how can I assist you today?"
}
```

Note: The current implementation of the `send_chat_message` function is a placeholder that echoes the received message. You need to replace it with the actual implementation that calls the underlying language model (LLM) using the target framework.

## Pydantic Models

The FastAPI application uses Pydantic models to define the structure and validation of the request and response data. These models are defined in the `models.py` file.

The following models are used:

1. `ApiChatPostRequest`: Represents the request data for sending a chat message. It has the following field:
   - `message` (str): The chat message to send.

2. `ApiChatPostResponse`: Represents the response data for a chat message. It has the following field:
   - `message` (Optional[str]): The chat message response, which can be None.

The Pydantic models ensure that the incoming request data and outgoing response data conform to the specified structure and types. They also provide automatic validation and serialization/deserialization of the data.

## Contributing

Feel free to submit issues or pull requests to improve this starter kit or add new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This starter kit is built using the [llama-index](https://github.com/jerryjliu/llama_index) library by Jerry Liu and the [Neo4j](https://neo4j.com/) graph database.
