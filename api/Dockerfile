FROM python:3.6
EXPOSE 3000

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app/
WORKDIR /app/
VOLUME /app

CMD ["python", "app.py"]
