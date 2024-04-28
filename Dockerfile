FROM python:3.12-alpine

COPY . /

RUN pip3 install -r requirements.txt

WORKDIR /src

CMD ["python3", "run.py"]
