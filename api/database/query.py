import os
import pymysql.cursors
from pymysql import converters

def init_connection():
    connection = pymysql.connect(   
        host= os.getenv("DATABASE_HOST"),
        port=3306,
        user=os.environ.get("DATABASE_USERNAME"),
        password=os.environ.get("DATABASE_PASSWORD"),
        database=os.environ.get("DATABASE"),
        cursorclass=pymysql.cursors.DictCursor,
    )   
    return connection

def query_get(sql,param):
    connection = init_connection()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql,param)
            return cursor.fetchall()
