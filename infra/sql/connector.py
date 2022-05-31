import os

from mysql import connector

conn = connector.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("HOST"),
    database=os.getenv("DB_NAME"),
)

cursor = conn.cursor()
