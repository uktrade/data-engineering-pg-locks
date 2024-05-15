# Data Engineering CoP pg_locks task
Repository for the pg_lock pair programming session on 6th June

Heavily inspired by [Michal Charemza's block or not script](https://gist.github.com/michalc/d5da003fdbc673cb6b0dfd82cd4d4c2a)

In one terminal run:
```
pip install psycopg2

make docker_start
```

## First task
In another terminal run:
```
python task_1
```

You will see this has a deadlock, something will need to be done to unblock this. A hint for the correct implementation to resolve this deadlock can be seen here:

https://www.postgresql.org/docs/9.4/sql-rollback.html

If you are still stuck, you can run:
```
python hint_for_task_1
```