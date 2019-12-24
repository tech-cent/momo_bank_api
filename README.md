# momo_bank_api
[![Build Status](https://travis-ci.org/tech-cent/momo_bank_api.svg?branch=dev)](https://travis-ci.org/tech-cent/momo_bank_api)
[![Maintainability](https://api.codeclimate.com/v1/badges/c268c405bdc2dd61a4be/maintainability)](https://codeclimate.com/github/tech-cent/momo_bank_api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c268c405bdc2dd61a4be/test_coverage)](https://codeclimate.com/github/tech-cent/momo_bank_api/test_coverage)

#### Requirements to run application.
- Python > 3.5
- Postgres
- Postman

#### How to set up appliction.
- Clone repository.
- Create virtual venv. (You could use the command `python3 -m venv project_env`)
- Create postgres database.
- Inside the `momo_bank_api` root folder create .env file from .env_example.
- Run migrations using the command. `python manage.py migrate`.
- Run application using the command. `python manage.py runserver`.