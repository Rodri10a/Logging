import requests
import random
from datetime import datetime, timezone

TOKEN = "abc123"
SERVICE_NAME = "service_alpha"
URL = "http://localhost:5000/logs"

SEVERITIES = ["INFO", "DEBUG", "ERROR", "WARNING"]
MESSAGES = [
    "Todo bien.",
    "Algo falló.",
    "Conectando a base de datos.",
    "Timeout inesperado.",
    "Usuario no encontrado."
]