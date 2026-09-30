FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY channel_sinuosity_classifier.py app.py ./

EXPOSE 7860

CMD ["python", "app.py"]
