import requests
import random
from datetime import datetime, timezone
import time

TOKEN = "def456"
SERVICE_NAME = "service_beta"
URL = "http://localhost:5000/logs"

SEVERITIES = ["INFO", "DEBUG", "ERROR", "WARNING"]
MESSAGES = [
    "Stress test: operación completada.",
    "Stress test: error de conexión.",
    "Stress test: usuario no válido.",
    "Stress test: timeout.",
    "Stress test: log de diagnóstico."
]

def generate_log():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": SERVICE_NAME,
        "severity": random.choice(SEVERITIES),
        "message": random.choice(MESSAGES)
    }

logs = [generate_log() for _ in range(1000)]
headers = {"Authorization": f"Token {TOKEN}"}

start = time.time()
response = requests.post(URL, json=logs, headers=headers)
end = time.time()

print("Status:", response.status_code)
print("Response:", response.json())
print(f"Tiempo total: {end - start:.2f} segundos")
