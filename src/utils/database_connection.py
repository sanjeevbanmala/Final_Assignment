# importing required libraries
import psycopg2
import os
from dotenv import load_dotenv

# loading all the varibles stored in .env
load_dotenv() 

# using try to handle exception
try:
    # defining function connect() which returns connection object with database
    # all credentials are passed through .env variables 
    def connect():
        return psycopg2.connect(
            
            host = os.getenv('HOST'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            port = os.getenv('PORT'),
            database = os.getenv('DATABASE')
        )  

# throwing exception if there are any
except Exception as e:
    print('AN error has occured', e)
