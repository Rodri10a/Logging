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