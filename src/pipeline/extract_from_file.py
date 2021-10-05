# importing required files and libraries
import json
from data_validation import *

#------------Extraction part for video data -----------------------------------
# this function takes cur, con and filePath as paramters
# it extracts fileName from filePath and passes these two parameters
# to procedure extract_video()
def extract_video_from_raw(cur,con,filePath):
    fileName = "'"+filePath[25:27]+"'"
    call_procedure_extract_video="CALL extract_video('"+filePath+"',"+fileName+")"
    cur.execute(call_procedure_extract_video)
    con.commit()

# this function takes cur and con as parameters
# and calls procedure transform_video
# which transforms all the data of raw_video tabe
def transform_video_from_raw(cur,con):
    call_procedure_transfrom_video="CALL transform_video()"
    cur.execute(call_procedure_transfrom_video)
    con.commit()

# This function does incremental extraction to the raw_video_archive table taking
# cur, con and filePath as parameters
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

# this function is used to execute all the above functions related to video extraction and transformation
# which are extract_video_from_raw, transform_video_from_raw and incremental_extract_to_archive
def main_extract_video(cur,con,filePath):
    
    extract_video_from_raw(cur,con,filePath)
    transform_video_from_raw(cur,con)
    # variable to store total failed test cases
    count_error=check_video_data_validity(cur,con)
    # incremental extraction only if there are 0 failed cases
    if(count_error==0):
        incremental_extract_to_archive(cur,con,filePath)
        print("Extraction successfull for "+filePath[25:])
    else:
        print

#--------- extraction part for category data------------------------ 

# this function truncates all the data from table raw_category
def delete_data_from_raw_category(cur,con):
    truncate_query = "TRUNCATE TABLE raw_category;"
    cur.execute(truncate_query)
    con.commit()

# this function extracts the data from json file
def extract_category_from_raw(cur,con,filePath):
    f = open(filePath, "r")
    data = json.load(f)
    for json_data in data['items']:
        id = json_data['id']
        title = json_data['snippet']['title']
        insert_query="INSERT INTO raw_category(category_id,category_title) VALUES ('"+id+"','"+title+"')"
        cur.execute(insert_query)
        con.commit()

# this function is used to incrementally extract the data to archive table of category
def incremental_save_category_to_archive(cur,con):
    with open('../sql/incremental_update_category.sql') as file:
        incremental_update_category = " ".join(file.readlines())
        cur.execute(incremental_update_category)
        con.commit()

# this function calls all the above function used to extract and transform category data
# which are delete_data_from_raw_category, extract_category_from_raw and incremental_save_category_to_archive
def main_extract_category(cur,con,filePath):
    delete_data_from_raw_category(cur,con)
    extract_category_from_raw(cur,con,filePath)
    # variable to store total failed test cases
    count_error=check_category_data_validity(cur,con)
    # incremental extraction only if there are 0 failed cases
    if(count_error==0):
        incremental_save_category_to_archive(cur,con)
        print("Extraction successfull for "+filePath[11:])
    else:
        print
