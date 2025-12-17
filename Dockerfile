FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001 8501

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

ENTRYPOINT ["/app/start.sh"]
