FROM python:3.9.7

RUN pip install fastapi uvicorn sqlalchemy

COPY . /welleat-data/api

ENV PYTHONPATH=/api
WORKDIR /welleat-data

EXPOSE 443

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0"]