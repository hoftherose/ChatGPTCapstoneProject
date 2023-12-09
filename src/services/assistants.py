import datetime

from src.utils.constants import client, logging

def upload_file(path):
    file = client.files.create(
        file=open(path, mode="rb"),
        purpose="assistants",
    )
    return file

def get_assistant(path):
    assistant = client.beta.assistants.retrieve("asst_QHYOXsAQ96vbf3JpmGcoc28D")
    return assistant

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

def create_assistant(path):
    file = upload_file(path)
    if file is None:
        logging.error("Assistant could not be created")
        return None
    assistant = client.beta.assistants.create(
        name="Study Quizzer Assistant",
        instructions="You're a helpful assistant that creates questions to help study from a specific document.",
        tools=[{"type": "retrieval"}],
        model="gpt-4-1106-preview",
        file_ids=[file.id],
    )
    return assistant
