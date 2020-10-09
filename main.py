# -*- coding: utf-8 -*-
from fastapi import FastAPI

from prefix_trie import client

app = FastAPI()


@app.get("/suggest/{query}&{count}")
async def suggest(query: str, count: int):
    return client.suggest(query, count)


@app.get("/parse/{query}")
async def parse(query: str):
    return client.parse(query)
