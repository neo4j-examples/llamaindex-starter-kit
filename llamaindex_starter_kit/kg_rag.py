from llama_index.core import StorageContext, KnowledgeGraphIndex
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import KnowledgeGraphRAGRetriever
from llama_index.graph_stores.neo4j import Neo4jGraphStore
from llama_index.readers.graphdb_cypher import GraphDBCypherReader
import os

# Load Neo4j Credentials from a .env file
url = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
database = os.getenv("NEO4J_DATABASE")


neo4j_graph_store = Neo4jGraphStore(username=username,password=password, url=url)

query = """
    MATCH (d)
    WHERE (d.Text) is not null
    RETURN d"""
reader = GraphDBCypherReader(url, username, password, database)
documents = reader.load_data(query)

storage_context = StorageContext.from_defaults(graph_store=neo4j_graph_store)


new_index = KnowledgeGraphIndex.from_documents(
    documents,
    max_triplets_per_chunk=2,
    storage_context=storage_context,
    include_embeddings=True,
    show_progress=True,
)

graph_rag_retriever = KnowledgeGraphRAGRetriever(
    storage_context=storage_context,
    verbose=False,
)

query_engine = RetrieverQueryEngine.from_args(
    graph_rag_retriever,
)

def get_kg_response(query: str)-> str:
    result = query_engine.query(query)
    return result.response