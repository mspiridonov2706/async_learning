"""Приложение Flask для выборки торговых марок"""

from flask import Flask, jsonify
import psycopg

from src.settings import settings

app = Flask(__name__)
conn_info = f"dbname={settings.postgres.db} user={settings.postgres.user} password={settings.postgres.password} host={settings.postgres.host}"
db = psycopg.connect(conn_info)


@app.route("/brands")
def brands():
    cur = db.cursor()
    cur.execute("SELECT brand_id, brand_name FROM brand")
    rows = cur.fetchall()
    cur.close()
    return jsonify([{"brand_id": row[0], "brand_name": row[1]} for row in rows])
