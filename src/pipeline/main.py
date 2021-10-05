# importing necessary modules and files
import sys
sys.path.append("/final_assignment/src/")
import utils
import utils.database_connection
from extract_from_file import *
from data_validation import *
from load_data import *
import os

# function to exract raw video and category data
def extract_raw_data():
    # variable to store the path of data to be extracted
    the_dir = 'E:\Final_Assignment\data'
    # variable to store filenames with .csv extensions only
    all_csv_files = filter(lambda x: x.endswith('.csv'), os.listdir(the_dir))
    # variable to store filenames with .json extensions only
    all_json_files = filter(lambda x: x.endswith('.json'), os.listdir(the_dir))
    
    # extracting data from all csv files by calling main_extract_video function
    for each_csv_file in all_csv_files:
        main_extract_video(cur,con,"E:/Final_Assignment/data/"+each_csv_file)

    # extracting data from all json files by calling main_extract_category function
    for each_json_file in all_json_files:
        main_extract_category(cur,con,"../../data/"+each_json_file)

if __name__ == "__main__":
    # creating connection object for database
    con = utils.database_connection.connect()
    # creating cursor object for connecton
    cur = con.cursor()
    # calling extract_raw_data function
    extract_raw_data()
    # variable to store count of total failed validation scripts for video data
    count_error_in_video_validation=check_video_data_validity(cur,con)
    # variable to store count of total failed validation scripts for category data
    count_error_in_category_validation=check_category_data_validity(cur,con)
    # loads the data in the fact and dimension tables if all the validation cases are passed
    if(count_error_in_video_validation==0):
        if(count_error_in_category_validation==0):
            load_data_into_warehouse(cur,con)
    # finally closing the cursor and connection object
    cur.close()
    con.close()
    