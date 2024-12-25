Steps to test:

1. fix postgresql username/password config in app.py
2. login in `psql`
2. `create database myadmin;`
3. `alter database myadmin set idle_in_transaction_session_timeout=3000;`
4. run app `uv run app.py`
5. open http://127.0.0.1:5000/admin/user/
6. wait 3 seconds
7. refresh http://127.0.0.1:5000/admin/user/ and get error
```
sqlalchemy.exc.OperationalError: (psycopg.OperationalError) consuming input failed: terminating connection due to idle-in-transaction timeout
SSL connection has been closed unexpectedly
```