from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timezone
import json

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
    
    