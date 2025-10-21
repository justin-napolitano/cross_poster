# Dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN pip install feedparser atproto mastodon.py requests
COPY app/ /app/
CMD ["python", "run.py"]
