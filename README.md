# SQL Case Study - 1

### In this task, you will need to write SQL queries against the Managers and Teams tables that you have already ingested into your database.

## Requirements:
- an SQL database (e.g. https://www.postgresql.org/download/)
### **I preferred using MySQL with Docker and Impala.**
### **You can find the Docker installation documents in the "docker_mysql_installation.txt" document.**


## Preparation:
1. Download the following database from Kaggle: https://www.kaggle.com/datasets/open-source-sports/baseball-databank
2. You will need the following files: “Managers.csv” and “Teams.csv”
3. Ingest the tables into a database of your choice
4. You will need to answer the questions based on your SQL queries. If possible, please refrain from having multiple separate queries for each answer, use CTEs.

## Questions
1. Of the teams who have won at least 70 games in the year 2010, how many of
them have changed at least their managers once during the same year, and
what is the teamID for each team?

Sample answer:
5 teams: SFN,SLN,TBA,TEX,TOR

2. What are the playerIDs for each teamID mentioned above?
Let's say there are 3 teams, and each team changes their managers 3x, then
there are 3*3. Separate the answer by ":" and ","

Sample answer:
KCA : coxbo01, trembda99, francte01
LAA : yostne01, bakerdu01, tracyji01
HOU : millsbr01, gardero01, manueje01

3. Please rank each playerID of each team mentioned above by descending
order and pick only the latest one, so that each team only has one playerID left.
