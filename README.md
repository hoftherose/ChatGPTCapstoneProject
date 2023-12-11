# Wizeline Capstone Project

In this repo we will be using ChatGPT and the Openai API to create a study card creator for any textbook.

## Setup
To setup the project you can use docker-compose. That being said, there are some variables that need to be setup before. For the database you can use the following values to mirror what is already set in docker-compose.

```
DB_ADDRESS=postgres
DB_USER=user
DB_PASS=password
DB_NAME=db
```

The only thing missing is your openai key. You can get this by following [this guide.](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)

## Usage

### Create assistant
Once you have everything setup you can use the following [path](http://0.0.0.0:8000/docs) to open a swagger UI. The first set is to upload a file to post:/api/v1/assistant/ which will create an assistant that we will use later. This also creates a thread in the background.

Once the assistant is created, we can get the assistant and thread id using postgres or by querying get:/api/v1/assistant/list. 

### Create questions
Now that you have the assistant id you can create N number of questions with the post:/api/v1/queries/generate/{assistant_id} endpoint. The default number of questions is 10 but you can pass how ever many questions you would like. The questions should come back as a response. If not run again.

### Checking potential answers
Now you have everything you need, find a question you think you can answer and send it to post:/api/v1/answers/{question_id}. ChatGPT should tell you if you are correct, as well as some observations that can help if you got it wrong, or to get a more complete answer.

## What we can improve.
* Error handling: It was originally planned, but at the end I didn't have time.
* API optimization: Since assistants were used we were forced into a more expensive model. Finding ways to reduce price, most of the prices comes from the fact that the documents you upload can be quite large, but hopefully there may be ways to optimize.
* Multi-users/Multi-tenant: More users would mean not having to create as many assistants for each users.
* UI: Swagger is fine for showing the functionallity but a front end would be simple enough and can go far.
* Scalability: Did not make this async due to it being easier, but it might be more friendly due to how long some of the requests take.

## Things I feel we got right.
* Question creation: The questions are actually pretty useful for studying and chatgpt is pretty good at not repeating questions.
* Answer verification: From testing, answers are well "graded", being able to find incomplete answers, giving suitable explanations and providing more detailed solutions even when you are right.
