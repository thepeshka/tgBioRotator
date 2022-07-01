FROM python:3.7

EXPOSE 8000
WORKDIR /app
ENV PYTHONPATH /app
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY src /app

COPY deploy/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]