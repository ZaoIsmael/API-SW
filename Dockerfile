FROM python:3.7

RUN mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["python"]

CMD ["app.py"]
