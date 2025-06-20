# utils/dbcheck.py

from django.db import connection

class DBCheck:
    @staticmethod
    def is_connected():
        try:
            connection.ensure_connection()
            return True
        except Exception as e:
            print("Database connection failed:", e)
            return False