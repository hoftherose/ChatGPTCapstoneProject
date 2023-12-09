import logging
from fastapi import APIRouter, UploadFile

from src.utils.constants import client
from src.services.assistants import *


assistant_router = APIRouter()

@assistant_router.get("/list")
def list_assistants():
    try:
        assistants = client.beta.assistants.list()
        return assistants
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}

@assistant_router.get("/{assistant_id}")
def get_assistants(assistant_id: str):
    try:
        assistant = get_assistant(assistant_id)
        return assistant
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}

@assistant_router.post("/")
def create_assistants(file: UploadFile):
    try:
        create_assistant(file.filename)
        return {"message": "Succeeded"}
    except FileNotFoundError as e:
        logging.error(f"File \"{file.filename}\" does not exist")
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}

@assistant_router.post("/chapters")
def create_multiple_assistant(file: UploadFile, chapters: str):
    try:
        create_assistant(file.filename)
        return {"message": "Succeeded"}
    except FileNotFoundError as e:
        logging.error(f"File \"{file.filename}\" does not exist")
    except Exception as e:
        logging.error(f"{str(e)}")
    return {"message": "Failed"}
