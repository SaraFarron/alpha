# alpha
First project on fast api

### Description
An API, that stores information about employees in a company and their performance. Employees can access a limited 
amount of endpoint to tell about their performance and receive new tasks. Managers can make tasks for employees to do
and look at their performance (with plots!), they have access to some endpoints, that employees have no access to. At 
last there are directors, who have access to all endpoints and can fire and hire people.

### Endpoints

#### Access levels:

0 - Not authorized,
1 - Employee,
2 - Manager,
3 - Director

#### Tasks:
+ get_task 1
+ get_tasks 1
+ update_task 1 (only is_completed field) 2 (all fields)
+ create_task 2
+ delete_task 2

#### Employees:
+ get_employee 1
+ get_employees 1
+ create_employee 3
+ delete_employee 3

### Lookup:

[crudrouter](https://fastapi-crudrouter.awtkns.com/routing)

[crudrouter tutorial](https://www.youtube.com/watch?v=0xIe2qGZdiM)

[alembic tutorial](https://www.youtube.com/watch?v=SdcH6IEi6nE)

[testing](https://fastapi.tiangolo.com/tutorial/testing/)

### Alembic commands:

Init

`docker exec -it alpha_web_1 alembic init alembic`

Make migrations

`docker exec -it alpha_web_1 alembic revision --autogenerate -m 'commit message'`

Migrate to latest

`docker exec -it alpha_web_1 alembic upgrade head`

Migrate to previous

`docker exec -it alpha_web_1 alembic downgrade -1`

### Testing

`docker exec -it alpha_web_1 pytest`
