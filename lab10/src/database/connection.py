from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv("/home/user/PP2_Spring/lab10/src/.env")

class DbConnection:
    db_name : str
    db_user : str
    db_password : str
    db_host : str
    db_port : str

    def __init__(self):
        self.db_name = os.getenv("DBNAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
    def __enter__(self):
        # print("Connection started...")
        self.connection = psycopg2.connect(
            dbname = self.db_name,
            password = self.db_password,
            user = self.db_user,
            host = self.db_host,
            port = self.db_port 
        )
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        return self.cursor
    def __exit__(self, type, value, traceback):
        # print("Connection ended...")
        self.connection.commit()
        self.connection.close()