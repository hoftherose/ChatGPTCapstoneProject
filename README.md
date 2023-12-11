# Wizeline Capstone Project

In this repo we will be using ChatGPT and the Openai API to create a study card creator for any textbook.

## Setup

## Usage

### Create assistant
Once you have everything setup you can use the following [path](http://0.0.0.0:8000/docs) to open a swagger UI. The first set is to upload a file to post:/api/v1/assistant/ which will create an assistant that we will use later. This also creates a thread in the background.

Once the assistant is created, we can get the assistant and thread id using postgres or by querying get:/api/v1/assistant/list. 

### Create questions
Now that you have the assistant id you can create N number of questions with the post:/api/v1/queries/generate/{assistant_id} endpoint. The default number of questions is 10 but you can pass how ever many questions you would like. The questions should come back as a response. If not run again.

### Checking potential answers
Now you have everything you need, find a question you think you can answer and send it to post:/api/v1/answers/{question_id}. ChatGPT should tell you if you are correct, as well as some observations that can help if you got it wrong, or to get a more complete answer.

