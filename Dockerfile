FROM python:3.10-slim-buster

COPY . .

RUN pip3 install pipenv

RUN pipenv install --system

EXPOSE 5000

ENTRYPOINT ["python3", "main.py"]




