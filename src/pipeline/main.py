import sys
sys.path.append("/final_assignment/src/")
import utils
import utils.database_connection
from extract_from_file import *
from data_validation import *
from load_data import *
import os


def extract_raw_data():
    the_dir = 'E:\Final_Assignment\data'
    all_csv_files = filter(lambda x: x.endswith('.csv'), os.listdir(the_dir))
    all_json_files = filter(lambda x: x.endswith('.json'), os.listdir(the_dir))

    for each_csv_file in all_csv_files:
        main_extract_video(cur,con,"E:/Final_Assignment/data/"+each_csv_file)

    for each_json_file in all_json_files:
        main_extract_category(cur,con,"../../data/"+each_json_file)

if __name__ == "__main__":
    con = utils.database_connection.connect()
    cur = con.cursor()
    extract_raw_data()
    count_error_in_video_validation=check_video_data_validity(cur,con)
    count_error_in_category_validation=check_category_data_validity(cur,con)
    if(count_error_in_video_validation==0):
        if(count_error_in_category_validation==0):
            load_data_into_warehouse(cur,con)
    cur.close()
    con.close()
    