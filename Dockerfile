FROM python:3.12-alpine
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add --no-cache git gcc musl-dev
# the repo is bind-mounted and owned by the host user, so let git (used by the auto-updater) operate on it
RUN git config --global --add safe.directory /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "ootBot.py"]
