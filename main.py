from fastapi import FastAPI
from prefix_trie import client

app = FastAPI()


@app.get("/suggest/")
async def suggest(query: str, count: int = 10):
    return client.suggest(query, count)


@app.get("/parse/")
async def parse(query: str):
    return client.parse(query)
