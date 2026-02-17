from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timezone
import json

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
    
# Cargar tokens válidos desde archivo externo
with open("tokens.json") as f:
    VALID_TOKENS = json.load(f)

def is_token_valid(token):
    """Verifica si el token recibido está en la lista de tokens válidos"""
    return token in VALID_TOKENS.values()


# Conexión SQLite y creación de tabla
conn = sqlite3.connect("logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    service TEXT,
    severity TEXT,
    message TEXT,
    received_at TEXT
)
""")
conn.commit()