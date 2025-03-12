from fastapi import FastAPI
from fastapi.responses import JSONResponse

from internal.translator import (
    TranaslationData,
    TranslationException,
    action,
    error_responder,
    responder,
)


app = FastAPI()


@app.exception_handler(TranslationException)
async def translation_exception_handler(_, exc: TranslationException):
    response_content = error_responder(exc)
    return JSONResponse(content=response_content, status_code=400)


@app.post("/translate")
async def translate(request: TranaslationData):
    response_content = responder(action(request))
    return JSONResponse(content=response_content, status_code=200)
