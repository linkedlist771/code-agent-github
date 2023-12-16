import os
import time
import uvicorn
from fastapi import FastAPI
from loguru import logger
from fastapi.middleware.cors import CORSMiddleware

from main import get_code
from uuid import uuid4
from typing import Optional, List

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/{prompt}")
async def get(prompt: str):
    logger.info(f"get {prompt}")
    code = get_code(prompt)
    return {"code": code}


def init_logger():
    os.makedirs("logs/", exist_ok=True)
    logger.add("logs/log_{time}.log", rotation="12:00")


def start_server(host, port):
    config = uvicorn.Config(app, host=host, port=port)
    server = uvicorn.Server(config=config)
    server.run()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0", help="host")
    parser.add_argument("--port", default=20004, help="port")
    args = parser.parse_args()
    start_server(args.host, args.port)
