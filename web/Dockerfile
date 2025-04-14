FROM python:3.11

WORKDIR /web
COPY . /web

RUN pip install flask flask_sqlalchemy pymysql

CMD ["python", "app.py"]
