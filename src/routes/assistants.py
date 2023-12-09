import logging

from fastapi import APIRouter, UploadFile

from src.utils.constants import client
from src.services.assistants import create_assistant


assistant_router = APIRouter()

@assistant_router.get("/list")
def get_assistants():
    assistants = client.beta.assistants.list()
    return assistants

@assistant_router.post("/")
def create_assistants(file: UploadFile):
    try:
        create_assistant(file.filename)
    except FileNotFoundError as e:
        logging.error(f"File \"{file.filename}\" does not exist")
    except Exception as e:
        logging.error(f"{str(e)}")
