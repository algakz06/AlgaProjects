FROM python:3.11

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.0

RUN pip install "poetry==1.3.2"

# Install dependencies

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

RUN mkdir logs/
# Run your app
COPY . .

CMD ["alembic", "revision", "--autogenerate", "-m", "smth"]
CMD ["alembic", "upgrade", "head"]
CMD [ "poetry", "run", "python", "-m", "app" ]
