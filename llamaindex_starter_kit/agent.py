import os
import logging
import sys

from llama_index.llms.openai import OpenAI
from llama_index.core import Settings, StorageContext
from llama_index.tools.neo4j import Neo4jQueryToolSpec
from llama_index.agent.openai import OpenAIAgent
from llama_index.graph_stores.neo4j import Neo4jGraphStore
from llama_index.readers.graphdb_cypher import GraphDBCypherReader

logging.basicConfig(
    stream=sys.stdout, level=logging.INFO
) 

Settings.llm = OpenAI(temperature=0, model="gpt-4", api_key=os.environ["OPENAI_API_KEY"])
Settings.chunk_size = 512
embed_dim = 1536

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

llm = OpenAI(model="gpt-4", openai_api_key=os.environ["OPENAI_API_KEY"] , temperature=0)

gds_db = Neo4jQueryToolSpec(
    url=url,
    user=username,
    password=password,
    llm=llm,
    database=database,
)

tools = gds_db.to_tool_list()
agent = OpenAIAgent.from_tools(tools, verbose=True)


def get_agent_response(query: str)-> str:
    output = agent.chat(query)
    return output.response