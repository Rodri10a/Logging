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