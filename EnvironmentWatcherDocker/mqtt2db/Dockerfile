FROM python:3.9

WORKDIR /root

RUN apt update
RUN apt install -y python3-pip
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mqtt_to_db.py .

CMD ["python3", "mqtt_to_db.py"]