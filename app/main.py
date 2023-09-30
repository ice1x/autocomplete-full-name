from typing import Text

from fastapi import FastAPI
from starlette.responses import PlainTextResponse

from app import trie_client

app = FastAPI()


@app.get("/suggest/")
async def suggest(query: Text, count: int = 10) -> PlainTextResponse:
    return trie_client.suggest(query, count)


@app.get("/parse/")
async def parse(query: Text) -> PlainTextResponse:
    return trie_client.parse(query)
