import os
from dotenv import load_dotenv
load_dotenv()

from neo4j import GraphDatabase


# Connect to Neo4j database
driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"), 
    auth=(
        os.getenv("NEO4J_USERNAME"), 
        os.getenv("NEO4J_PASSWORD")
    )
)


# Create embedder
from neo4j_graphrag.embeddings.openai import OpenAIEmbeddings

embedder = OpenAIEmbeddings(model="text-embedding-ada-002")


# Create retriever
from neo4j_graphrag.retrievers import VectorRetriever

retriever = VectorRetriever(
    driver,
    index_name="moviePlots",
    embedder=embedder,
    return_properties=["title", "plot"],
)

# Search for similar items

# Parse results

# CLose the database connection
driver.close()
