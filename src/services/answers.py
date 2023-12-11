import time
import json

from src.utils.constants import client
from src.repositories.questions import QuestionsTable
from src.repositories.assistants import AssistantsTable

def review_answer(question_id: int, answer: str):
    question_object = QuestionsTable.select_question(question_id).all()[0]
    thread_id = question_object[1]
    question = question_object[2]
    assistant_object = AssistantsTable.select_assistant_by_thread(thread_id).all()[0]
    assistant_id = assistant_object[1]

    prompt = "Given the following question: "+question+"\nWould the following be a correct answer: "+answer+"\nPlease answer the questoin in the json format: {\"correct\": true/false, \"observations\": \"Observations as to why it is correct or not, or more complete information\"}"
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt,
    )

    run = client.beta.threads.runs.create(
        assistant_id=assistant_id,
        thread_id=thread_id,
    )

    while run.status != "completed":
        time.sleep(0.25)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )

    messages = client.beta.threads.messages.list(thread_id=thread_id)
    message = messages.data[0].content[0].text.value
    json_message = json.loads(message)
    return json_message
