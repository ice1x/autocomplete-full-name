from fastapi import FastAPI

from prefix_trie import client

app = FastAPI()


@app.get("/suggest/{letter}")
async def suggest(letter):
    return client.suggest(letter)
