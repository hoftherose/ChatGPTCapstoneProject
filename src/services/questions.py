import time

from src.repositories.assistants import AssistantsTable
from src.repositories.questions import QuestionsTable
from src.utils import get_numbered_list
from src.utils.constants import client


def generate_questions(assistant_id: str, num_questions: int):
    assistant = AssistantsTable.select_assistant(assistant_id).all()[0]
    thread_id = assistant[3]
    
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=f"Can you give me {num_questions} questions to quiz me on the contents of the file? If asked before, try not to repeat if possible.",
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
    questions = get_numbered_list(messages.data[0].content[0].text.value)
    for q in questions:
        QuestionsTable.insert_question(thread_id, q)
    return { "questions":
            [{ "question": q} for q in questions]
        }
