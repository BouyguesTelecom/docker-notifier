FROM python:3.9

RUN mkdir /app
ADD src/requirements.txt /app/
RUN pip3 install -r  /app/requirements.txt

ADD src/*.py /app

CMD ["python3", "/app/main.py"]