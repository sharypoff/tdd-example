import time
from fastapi import FastAPI, Request, Response
from .scheme import MyInfoResponse, User
from .signature import generate_signature

app = FastAPI()


@app.middleware("http")
async def add_signature_header(request: Request, call_next):
    response = await call_next(request)
    body = b""
    async for chunk in response.body_iterator:
        body += chunk
    response.headers["X-Signature"] = generate_signature(body)
    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
    )


@app.get("/my-info", response_model=MyInfoResponse)
async def my_info():
    my_info_response = MyInfoResponse(
        user=User(
            id=1,
            firstname="John",
            lastname="Smith",
            phone="+995000000000",
        ),
        timestamp=int(time.time()),
    )
    return my_info_response
