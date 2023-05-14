FROM python:3.11-slim

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN apt-get update \
    && apt-get -y install gcc g++ apt-transport-https \
                          ca-certificates curl gnupg \
                           --no-install-recommends
    \

RUN pip install --upgrade pip poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && rm -rf /root/.cache/pip
    \

COPY .env /app/.env
COPY ./app /app

CMD ["python", "launch.py"]
