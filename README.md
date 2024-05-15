# Data Engineering CoP pg_locks task
Repository for the pg_lock pair programming session on 6th June

Heavily inspired by [Michal Charemza's block or not script](https://gist.github.com/michalc/d5da003fdbc673cb6b0dfd82cd4d4c2a)

## Getting Started

In order to begin, please follow these steps:

1. Open one terminal and install the required dependencies/launch docker env by running:
```
pip install psycopg2

make docker_start
```

2. In another terminal, proceed with the tasks outlined below.

## Task 1 - Resolving Deadlock
To begin task 1, execute the following in terminal:
```
python task_1
```

This demonstrates a deadlock scenario. Your objective is to identify and implement a solution to resolve this deadlock. If you require assistance, refere to the [documentation](https://www.postgresql.org/docs/9.4/sql-rollback.html).


If you are still stuck, you can run:
```
python hint_for_task_1
```

## Second task - Resolving Block
For task 2, execute the following:
```
python task_2
```

This task is showing a block scenario. Your goal is to implement a solution to resolve this blockage. For guidance, this is the [documentation](https://www.postgresql.org/docs/current/sql-commit.html)


If you are still stuck, you can run:
```
python hint_for_task_2
```