import json
from data_validation import *

def extract_video_from_raw(cur,con,filePath):
    fileName = "'"+filePath[25:27]+"'"
    call_procedure_extract_video="CALL extract_video('"+filePath+"',"+fileName+")"
    cur.execute(call_procedure_extract_video)
    con.commit()

def transform_video_from_raw(cur,con):
    call_procedure_transfrom_video="CALL transform_video()"
    cur.execute(call_procedure_transfrom_video)
    con.commit()

def incremental_extract_to_archive(cur,con,filePath):
    fileName = "'"+filePath[25:27]+"'"
    incremental_update="""
    INSERT INTO raw_video_archive 
    SELECT * 
    FROM transform_video 
    WHERE video_id 
    NOT IN( SELECT video_id FROM raw_video_archive WHERE country_code = """+fileName+""")
    AND trending_date
    NOT IN( SELECT trending_date FROM raw_video_archive WHERE country_code = """+fileName+""")"""
    cur.execute(incremental_update)
    con.commit()

def main_extract_video(cur,con,filePath):
    
    extract_video_from_raw(cur,con,filePath)
    transform_video_from_raw(cur,con)
    count_error=check_video_data_validity(cur,con)
    if(count_error==0):
        incremental_extract_to_archive(cur,con,filePath)
        print("Extraction successfull for "+filePath[25:])
    else:
        print
    

def delete_data_from_raw_category(cur,con):
    truncate_query = "TRUNCATE TABLE raw_category;"
    cur.execute(truncate_query)
    con.commit()

def extract_category_from_raw(cur,con,filePath):
    f = open(filePath, "r")
    data = json.load(f)
    for json_data in data['items']:
        id = json_data['id']
        title = json_data['snippet']['title']
        insert_query="INSERT INTO raw_category(category_id,category_title) VALUES ('"+id+"','"+title+"')"
        cur.execute(insert_query)
        con.commit()

def incremental_save_category_to_archive(cur,con):
    with open('../sql/incremental_update_category.sql') as file:
        incremental_update_category = " ".join(file.readlines())
        cur.execute(incremental_update_category)
        con.commit()



def main_extract_category(cur,con,filePath):
    delete_data_from_raw_category(cur,con)
    extract_category_from_raw(cur,con,filePath)
    count_error=check_category_data_validity(cur,con)
    if(count_error==0):
        incremental_save_category_to_archive(cur,con)
        print("Extraction successfull for "+filePath[11:])
    else:
        print
