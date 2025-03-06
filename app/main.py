import traceback
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from internal.translator import (
    TranaslationData,
    TranslationException,
    action,
    responder,
)


app = FastAPI()


@app.exception_handler(TranslationException)
async def translation_exception_handler(_, exc: TranslationException):
    error_trace = traceback.format_exc()
    return JSONResponse(
        status_code=400,
        content={
            "error": "Translation Error",
            "message": exc.message,
            "trace": error_trace,
        },
    )


@app.post("/translate")
async def translate(request: TranaslationData):
    return responder(action(request))
