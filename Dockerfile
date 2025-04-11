FROM python:3.13
WORKDIR /app
COPY . /app
COPY requirements.txt /app/
RUN python3 -m ensurepip && pip install --upgrade pip
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
