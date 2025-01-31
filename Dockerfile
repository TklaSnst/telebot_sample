FROM python:3.12 as python-base

WORKDIR /telebot_sample

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
