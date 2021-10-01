import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() 
try:
    def connect():
        return psycopg2.connect(
            
            host = os.getenv('HOST'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            port = os.getenv('PORT'),
            database = os.getenv('DATABASE')
        )  

except Exception as e:
    print('AN error has occured', e)
