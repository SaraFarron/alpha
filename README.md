# alpha
First attempt at fast api

### Description
An API, that stores information about employees in a company and their performance. Employees can access a limited 
amount of endpoint to tell about their performance and receive new tasks. Managers can make tasks for employees to do
and look at their performance (with plots!), they have access to some endpoints, that employees have no access to. At 
last there are directors, who have access to all endpoints and can fire and hire people.

Lookup:

[crudrouter](https://fastapi-crudrouter.awtkns.com/routing)

[crudrouter tutorial](https://www.youtube.com/watch?v=0xIe2qGZdiM)

[alembic tutorial](https://www.youtube.com/watch?v=SdcH6IEi6nE)

### Alembic commands:

Init

`docker exec -it alpha_web_1 alembic init alembic`

Make migrations

`docker exec -it alpha_web_1 alembic revision --autogenerate -m 'commit message'`

Migrate to latest

`docker exec -it alpha_web_1 alembic upgrade head`

Migrate to previous

`docker exec -it alpha_web_1 alembic downgrade -1`
