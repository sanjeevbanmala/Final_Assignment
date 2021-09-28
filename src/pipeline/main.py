from database_connection import connect
from extract_from_file import *

def extract_raw_data():
    extract_video(cur,con,"'E:/final_assignment/data/CAvideos.csv'")

if __name__ == "__main__":
    con = connect()
    cur = con.cursor()
    extract_raw_data()
    
    cur.close()
    con.close()
    