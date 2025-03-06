from typing import TypedDict
from ollama import ChatResponse, Client
from pydantic import BaseModel, Field

from internal.infrastructre import Config, get_ollama_client

config = Config()


class TranslationException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class TranaslationData(BaseModel):
    text: str = Field(..., title="Text to translate", min_length=1)
    source: str = Field(..., title="Source language", min_length=1)
    target: str = Field(..., title="Target language", min_length=1)


def action(data: TranaslationData) -> ChatResponse:
    try:
        return chat(get_ollama_client(config), config, compose_message(data))
    except Exception as e:
        raise TranslationException("Getting translation from model failed") from e


class TranslatedResponse(TypedDict):
    message: str


def responder(response: ChatResponse) -> TranslatedResponse:
    content = response.get("message", {}).get("content", "")
    if not content:
        raise TranslationException("Translation response is empty")
    return {"message": content}


def compose_message(data: TranaslationData) -> str:
    return (
        f"translate the following text from {data.source} to {data.target}: {data.text}"
    )


def chat(client: Client, config: Config, message: str) -> ChatResponse:
    return client.chat(
        model=config.ollama_model,
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
