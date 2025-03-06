from dataclasses import dataclass
import os

from ollama import Client


@dataclass(frozen=True)
class Config:
    ollama_host: str = os.getenv("OLLAMA_HOST", "localhost")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "")


def get_ollama_client(config: Config) -> Client:
    return Client(host=config.ollama_host)
