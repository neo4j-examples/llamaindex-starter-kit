from __future__ import annotations
from typing import Union
from fastapi import FastAPI
from .models import ApiChatPostRequest, ApiChatPostResponse
from .vector_index import get_vector_response
from .agent import get_agent_response
from .kg_rag import get_kg_response

app = FastAPI(
    title='Chat API',
    description='API for sending and receiving chat messages',
    version='0.1.0',
    servers=[{'url': 'http://localhost:3000'}],
)

@app.post(
    '/api/chat',
    response_model=None,
    responses={'201': {'model': ApiChatPostResponse}},
    tags=['chat'],
)
def send_chat_message(body: ApiChatPostRequest) -> Union[None, ApiChatPostResponse]:
    """
    Send a chat message
    """

    mode = body.mode.lower()
    if mode == "vector":
        print(f'Running vector index')
        response = get_vector_response(body.message)
    elif mode == "kg":
        print(f'Running KG Rag Retreiver')
        response = get_kg_response(body.message)
    else:
        print(f'Running agent')
        response = get_agent_response(body.message)

    return ApiChatPostResponse(message=response)
