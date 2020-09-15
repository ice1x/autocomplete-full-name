from fastapi import FastAPI

from prefix_trie import client

app = FastAPI()


@app.get("/suggest/{query}&{count}")
async def suggest(query: str, count: int):
    return client.suggest(query, count)
