import shutil
import datetime

from src.repositories.assistants import AssistantsTable
from src.utils.constants import client, logging

def upload_file(path):
    file = client.files.create(
        file=open(path, mode="rb"),
        purpose="assistants",
    )
    return file

def get_assistant(assistant_id):
    assistant = client.beta.assistants.retrieve(assistant_id)
    return {"assistant": {
        "id": assistant.id,
        "created_at": datetime.datetime.fromtimestamp(int(assistant.created_at)),
        "description": assistant.description,
        "file_ids": assistant.file_ids,
        "instructions": assistant.instructions,
        "metadata": assistant.metadata,
        "model": assistant.model,
        "name": assistant.name,
        "object": assistant.object,
        "tools": [{"type": tool.type} for tool in assistant.tools],
    }}

def get_assistant_list():
    assistants = client.beta.assistants.list().model_dump()["data"]
    return {
        "num_assistants": len(assistants),
        "assistants": [{
            "id": assistant["id"],
            "created_at": datetime.datetime.fromtimestamp(int(assistant["created_at"])),
            "description": assistant["description"],
            "file_ids": assistant["file_ids"],
            "instructions": assistant["instructions"],
            "metadata": assistant["metadata"],
            "model": assistant["model"],
            "name": assistant["name"],
            "object": assistant["object"],
            "tools": [{"type": tool["type"]} for tool in assistant["tools"]],
        } for assistant in assistants],
    }

def store_file(file):
    path = f"./textbooks/{file.filename}"
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object) 
    return path

def create_assistant(file):
    path = store_file(file)
    file = upload_file(path)
    if file is None:
        logging.error("Assistant could not be created")
        return {"assistant": []}
    assistant = client.beta.assistants.create(
        name=f"{file.filename} Study Assistant",
        instructions="You're a helpful assistant that creates questions to help study from a specific document.",
        tools=[{"type": "retrieval"}],
        model="gpt-4-1106-preview",
        file_ids=[file.id],
    )
    AssistantsTable.insert_assistant(assistant.name, assistant.id, path, assistant.model)
    return {"assistant": [
        {
            "id": assistant.id,
            "name": assistant.name,
            "instructions": assistant.instructions,
            "model": assistant.model,
            "file_ids": assistant.file_ids,
            "created_at": assistant.created_at,
        }
    ]}
