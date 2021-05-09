from fastapi import FastAPI
import trie_client

app = FastAPI()


@app.get("/suggest/")
async def suggest(query: str, count: int = 10):
    return trie_client.suggest(query, count)


@app.get("/parse/")
async def parse(query: str):
    return trie_client.parse(query)
