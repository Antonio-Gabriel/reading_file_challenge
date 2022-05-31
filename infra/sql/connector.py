from mysql import connector

conn = connector.connect(
    user="root", password="12345", host="db", database="recicla"
)

cursor = conn.cursor()