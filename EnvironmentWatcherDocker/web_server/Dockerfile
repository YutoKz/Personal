FROM python:3.9

WORKDIR /root

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "web_server.py"]
