from mysql import connector

conn = connector.connect(
    user="root", password="", host="localhost", database="recicla"
)

cursor = conn.cursor()