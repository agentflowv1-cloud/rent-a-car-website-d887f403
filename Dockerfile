# Base image — replace with the appropriate runtime for this project.
# The AI-generated application code may update this file automatically.
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt* ./
RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
