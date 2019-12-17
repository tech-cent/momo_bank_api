# momo_bank_api

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