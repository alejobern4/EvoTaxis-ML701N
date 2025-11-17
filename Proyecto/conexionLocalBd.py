import mysql.connector

def get_local_connection():
    try:
        return mysql.connector.connect(
        host="localhost",
        user="LAPTOP-CO6REOH4\alejo",
        password="", 
        database="DataW_IoT"
    )
    except Exception as e:
        return f"Error: {e}"
