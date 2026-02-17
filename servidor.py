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

# Endpoint POST /logs (recibir y guardar logs)
@app.route("/logs", methods=["POST"])
def receive_logs():
    auth = request.headers.get("Authorization", "")
    token = auth.replace("Token ", "")
    
    if not is_token_valid(token):
        return jsonify({"error": "Quién sos, bro?"}), 401

    logs = request.get_json()
    if not isinstance(logs, list):
        logs = [logs]

    now = datetime.now(timezone.utc).isoformat()

    cursor.executemany("""
        INSERT INTO logs (timestamp, service, severity, message, received_at)
        VALUES (?, ?, ?, ?, ?)
    """, [
        (log.get("timestamp"), log.get("service"),
        log.get("severity"), log.get("message"), now)
        for log in logs
    ])
    conn.commit()

    return jsonify({"status": "Logs recibidos"}), 201

# Endpoint GET /logs (consulta con filtros)
@app.route("/logs", methods=["GET"])
def get_logs():
    args = request.args
    query = "SELECT * FROM logs WHERE 1=1"
    params = []

    if args.get("timestamp_start"):
        query += " AND timestamp >= ?"
        params.append(args["timestamp_start"])
    if args.get("timestamp_end"):
        query += " AND timestamp <= ?"
        params.append(args["timestamp_end"])
    if args.get("severity"):
        query += " AND severity = ?"
        params.append(args["severity"])
    if args.get("received_at_start"):
        query += " AND received_at >= ?"
        params.append(args["received_at_start"])
    if args.get("received_at_end"):
        query += " AND received_at <= ?"
        params.append(args["received_at_end"])

    cursor.execute(query, params)
    rows = cursor.fetchall()

    logs = [{
        "id": r[0], "timestamp": r[1], "service": r[2],
        "severity": r[3], "message": r[4], "received_at": r[5]
    } for r in rows]

    return jsonify(logs), 200

