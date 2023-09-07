FROM python:3.9-slim

WORKDIR /app

COPY . .

# Install dependencies
RUN apt-get update \
    && apt-get install -y curl \
    && pip install -r requirements.txt

EXPOSE 8050

CMD ["python", "illinois.py"]