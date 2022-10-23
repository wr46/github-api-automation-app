FROM python:3.10-slim as build

RUN pip install --user pipenv

ENV PIPENV_VENV_IN_PROJECT=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY Pipfile Pipfile.lock setup.py /app/
COPY ./github_automation ./github_automation

RUN /root/.local/bin/pipenv sync


FROM python:3.10-slim

RUN apt-get update && apt-get install -y git
    
RUN groupadd -g 1000 python && \
    useradd -m -r -u 1000 -g python python

COPY --chown=python:python --from=build /app /app

WORKDIR /app
USER python

ENTRYPOINT [ "./.venv/bin/python", "github_automation/main.py" ]
CMD [ "--help" ]
