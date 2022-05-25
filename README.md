# FastAPI Example - Domain driven design & Clean architecture

## Tech Stack
 - [Python 3.10](https://www.python.org/downloads/release/python-3100/)
 - [FastAPI](https://fastapi.tiangolo.com)
 - [SQLAlchemy](https://www.sqlalchemy.org)
   - [Postgres](https://www.postgresql.org)
 - [Docker](https://www.docker.com)
   - [Docker Compose](https://docs.docker.com/compose/)
 - [Poetry](https://python-poetry.org)

## Environment's variables
.env file
   - POSTGRES_USER - database root name
   - POSTGRES_PASSWORD - database root password
   - DB_HOST - database's hostname
   - DB_PORT - database's port
   - DB_NAME - database's name
   - DB_USER - database's username
   - DB_PASS - database user's password
   - PORT - port which will be listening for incoming connections

## Code Architecture
Directory structure based on [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

```tree
├── core
├── app
│   ├── main.py
│   ├── dependencies.py
│   ├── config.py
│   └── features
│       └── users
│           ├── data
│           │   ├── repositories
│           │   │   ├── user_unit_of_work_impl.py
│           │   │   └── user_repository_impl.py
│           │   ├── services
│           │   │   └── user_query_service_impl.py
│           │   └── models
│           │       ├── user.py
│           │       └── database.py
│           ├── domain
│           │   ├── entities
│           │   │   ├── user_command_model.py
│           │   │   ├── user_common_model.py
│           │   │   ├── user_entity.py
│           │   │   └── user_query_model.py
│           │   ├── repositories
│           │   │   ├── user_repository.py
│           │   │   └── user_unit_of_work.py
│           │   ├── services
│           │   │   └── user_query_service.py
│           │   └── usecases
│           │       ├── create_user.py
│           │       ├── delete_user.py
│           │       ├── get_user.py
│           │       ├── get_users.py
│           │       └── update_user.py
│           ├── presentation
│           │   ├── routes
│           │   │   ├── __init__.py
│           │   │   ├── create_user_route.py
│           │   │   ├── delete_user_route.py
│           │   │   ├── get_user_route.py
│           │   │   ├── get_users_route.py
│           │   │   └── update_user_route.py
│           │   └── schema
│           │       └── routes
│           └── dependencies.py
└── tests
```
# Domain-driven design Glossary
There is a number of high-level concepts that are used in conjunction with one another to create and modify domain models:
- **Model**: A system of abstractions that describes aspects of a ``domain`` 
and can be used to solve problems related to that domain.
- **Value Object**: An immutable object that has attributes and validation logic, but no distinct identity.
- **Entity**: An object that is identified by its consistent thread of continuity, as opposed to traditional ``objects``,
which are defined by their attributes.
- **Aggregate**: A cluster of ``entities`` and ``value objects`` with defined boundaries around the group.
Rather than allowing every single entity ``entity`` or ``value object`` to perform all actions on its own,
the collective aggregate of items is assigned a singular aggregate root item. 
External objects no longer have direct access to every individual ``entity`` or ``value object`` within the aggregate,
 and use that to pass along instructions to the group as a whole.
- **Service**: Service is an operation or form of business logic that doesn't naturally fit within real of objects.
That means if functionality must exist, but doesn't relate to an ``entity`` or ``value object``.
- **Repository**: the DDD meaning of a repository is a service that uses a global interface to provide access to all ``entities``.
 and ``value objects`` that are withing a particular ``aggregate`` collection. Methods should be defined to allow for creation,
modification, and deletion of objects within the aggregate.
- **Factory**: Factory is a creational design pattern that provides an interface for creating ``objects``.
DDD highly suggests use such pattern. Factory pattern encapsulates the logic of creating complex ``objects`` and ``aggregates``,
ensuring that the client has no knowledge of the inner-workings of ``object`` manipulation (creation).


# Setup
1. Clone repository
2. Create .env file and setup env variables
3. Run `docker-compose up`
4. Access the API document `http://localhost:<specified_opened_port>`
