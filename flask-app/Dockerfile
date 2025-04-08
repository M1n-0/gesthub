FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install flask flask_sqlalchemy pymysql

CMD ["python", "app.py"]
