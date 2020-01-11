# momo_bank_api
[![Build Status](https://travis-ci.org/tech-cent/momo_bank_api.svg?branch=dev)](https://travis-ci.org/tech-cent/momo_bank_api)
[![Maintainability](https://api.codeclimate.com/v1/badges/c268c405bdc2dd61a4be/maintainability)](https://codeclimate.com/github/tech-cent/momo_bank_api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c268c405bdc2dd61a4be/test_coverage)](https://codeclimate.com/github/tech-cent/momo_bank_api/test_coverage)

#### Demo links
- Backend hosted on heroku. - `https://momobank.herokuapp.com/`

#### Requirements to run application.
- Python >= 3.5
- Postgres
- Postman

#### How to set up appliction.
- Clone repository.
- Create virtual venv. (You could use the command `python3 -m venv project_env`)
- Create postgres database.
- Inside the `momo_bank_api` root folder create .env file from .env_example.
- Run migrations using the command. `python manage.py migrate`.
- Run application using the command. `python manage.py runserver`.

#### Project Overview
--------------------------------
|Endpoint |Functionality |Note |
|---------|:------------:|:---:|
|`POST` /signup/ |Register a new user| Successfully signing up a user creates a new account for them. |
|`POST` /login/ |Login a user | Logs in an existing user. Returns JWT token and user's name. |
| `POST` /bank/ | Create a new bank. | Creates a new bank to which accounts can belong.
| `GET` /bank/ | Get all banks in system. | Returns a list of all banks.
|`GET` /account/ | Returns accounts.| Returns all accounts belonging to logged in user.|
|`POST` /account/ | Creates accounts.| Creates an account for logged in user.|
| `GET` /account/[accountId] | Fetch single account. | Returns account of specified id. |
| `GET` /account/[accountId]/transactions/ | Transactions on account. | List of transactions on particular account.
|`POST` /transactions/| Create new transaction. | A transaction changes the balance of an acoount.
|`GET` /transactions/| Return all transactions.| Returns all transactions in the db.|
|`GET` /transactions/[transaction_id]/| View a single transaction. | Detail view of a single transaction. |
|`PUT` /transactions/[transaction_id]/| Update a single transaction. | Update a transaction status to successful. |
Link to Swagger docs. `https://momobank.herokuapp.com/swagger/`

## Built With

* `Django` : [Django](https://www.djangoproject.com/) is a python web framework.
* `Django Rest-framework` : [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
* `momoapi-python` : [Repo](https://github.com/sparkplug/momoapi-python) MTN MoMo API Client Library for Python.

## Authors

* **Nangai Arthur** - [Linkedin](www.linkedin.com/in/arthur-nangai)
