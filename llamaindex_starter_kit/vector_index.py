from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core import Settings, StorageContext
from llama_index.llms.openai import OpenAI
from llama_index.readers.graphdb_cypher import GraphDBCypherReader
from llama_index.vector_stores.neo4jvector import Neo4jVectorStore
import os

# Load Neo4j Credentials
URL = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE= os.getenv("NEO4J_DATABASE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure LLM
Settings.llm = OpenAI(temperature=0, model="gpt-4", api_key=OPENAI_API_KEY)
Settings.chunk_size = 512
embed_dim = 1536

neo4j_vector = Neo4jVectorStore(USERNAME, PASSWORD, URL, embed_dim)

index_name = "existing_index"
text_node_property = "text"
try:
    existing_vector = Neo4jVectorStore(
        USERNAME,
        PASSWORD,
        URL,
        embed_dim,
        index_name=index_name,
        text_node_property=text_node_property,
    )
    index = VectorStoreIndex.from_vector_store(existing_vector)
except Exception as e:
    print(f'No existing index found. Creating a new vector index...')
    query = """
        MATCH (d)
        WHERE (d.Text) is not null
        RETURN d"""
    reader = GraphDBCypherReader(URL, USERNAME, PASSWORD, DATABASE)
    documents = reader.load_data(query)
    storage_context = StorageContext.from_defaults(vector_store=neo4j_vector)

    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )

def get_vector_response(query: str)-> str:
    query_engine = index.as_query_engine()
    result = query_engine.query(query)
    return result.response

