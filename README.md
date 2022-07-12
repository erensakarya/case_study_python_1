# Python Case Study - 1

### In this task, you will need to write a Python code that extracts data from an API and saves it into a database table. First, familiarize yourself with the following API:
### https://jsonplaceholder.typicode.com/

## Requirements:
- Python and SQLAlchemy or psycopg2 installed
- A database client might be useful

## Question
### Extract all posts and their comments from the server, and save the data into the database into the corresponding tables.

## My Notes:
- I used Postgres with Docker so you can find how to install Postgres via Docker in the 'docker_postgres_installation.txt' file.
- I preferred not to use Python Functions since there are only 2 api requests and 2 tables but for sure it would have been way better if used.
- I already created my tables before inserting the .csv datas to Postgres.
