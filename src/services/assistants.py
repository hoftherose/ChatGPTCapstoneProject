import logging

from src.utils.constants import client

def upload_file(path):
    file = client.files.create(
        file=open(path, mode="rb"),
        purpose="assistants",
    )
    return file

def get_assistant(path):
    return {}

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
