FROM python:3.11

RUN pipx install poetry

WORKDIR / docker_test

COPY ./pyproject.toml .

RUN poetry install

COPY . .

CMD ['python', 'manage.py', 'runserver']
