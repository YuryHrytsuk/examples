FROM python:3.8-alpine

ARG ENV=production

RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN if [[ "$ENV" == "production" ]] ; then \
        pipenv install --system --deploy --ignore-pipfile; \
    else \
        pipenv install --dev --system --deploy --ignore-pipfile; \
    fi

COPY ./examples ./examples

CMD ["python", "-m", "examples.cli", "start-server"]