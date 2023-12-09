import os
import logging

from openai import OpenAI
from fastapi import FastAPI

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

app = FastAPI()

@app.get("/list/assistants")
def get_assistants():
    assistants = client.beta.assistants.list()
    return assistants

@app.post("/assistants")
def create_assistants():
    return {"Hello": "World"}
