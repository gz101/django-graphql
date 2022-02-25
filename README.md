# Django-GraphQL
A simple backend application created using `Django` and `graphene-django` frameworks to serve `GraphQL` queries. 

## Purpose
This repository contains all the code needed for a simple backend `GraphQL` API service using the `Django` and `graphene-django` Python frameworks.

All dependencies for this project are located in the `requirements.txt` file at the root of the repository.

The `GraphQL` endpoint is located at `/graphql`.

This API is able to handle a query, `person`, which returns a `Person` object. Refer to the `apps/graph_api/models.py` file for details on how this model class is defined. The `Person` object consists of the following variables:
- `email`, a string type
- `name`, a string type
- `address`, an Address type consisting of:
    - `number`, an integer type
    - `street`, a string type
    - `city`, a string type
    - `state`, a `GraphQL enum` type

Some mock data has been provided in the local `db.sqlite3` database file. This file is not usually provided, but is uploaded for test purposes.

## Usage
You will need Python and `pip` installed. Below are the versions that I use.

```
python --version   # using 3.10.2
pip --version      # using 22.0.3
```

The `requirements.txt` file describes project dependencies, and `pip` can use it
with:

```
pip install -r requirements.txt
```

Note that you may wish to set up a separate environment with `virtualenv`.

To use this API service, start the project with:

```
python manage.py runserver
```

And go to `http://127.0.0.1:8000/graphql/` in a web browser (I use Firefox. Alternatively, it is possible to use `Postman` to make the query as well, but this involves disabling `CSRF` protection in the `apps/graph_api/urls.py` file. 

The following query can be used to obtain a `Person` object from the database.

```
query {
  person {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```

As there are no arguments provided to this query, it is designed to return a random `Person` object from all the `Person` objects in the database.

For alternative ways to query the database, please refer to the [Any Other Business](#any-other-business) section below.

## Any Other Business
To allow for validation and review of this application, the `sqlite3` database is included in this repository, as mentioned above. A file named `env_secrets.py` is also included in this repository, which stores `Django`'s `SECRET_KEY`. These two files are not normally included in the GitHub repository, but has been included for review purposes.

No explicit conversion from the `state` field choice in the `Address` model is required from a `string` type to a `GraphQL enum` type, as the default behaviour of `graphene-django` is to convert it implicitly. [Reference](https://docs.graphene-python.org/projects/django/en/latest/queries/).

While in development phase, I created two other queries to assist in verifying my `models.py` file defined the database models correctly. The first is the `people` query, which returns a list of all `Person` objects in the database. The second is the `personById` query, which returns a `Person` object by its primary key in the database. These queries are shown below.

The `people` query is defined as:

```
query {
  people {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```

The `personById` query is defined as:

```
query {
  personById(personId:1) {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```

Where the `personId` value of 1 used in this example can be replaced with the primary key of any other person in the database. If the primary key does not exist, a `null` object is returned.
