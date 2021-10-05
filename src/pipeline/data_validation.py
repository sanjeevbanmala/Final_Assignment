# importing required libraries
import os

# Function to validate data of video_data which takes cur and con as parameter
def check_video_data_validity(cur,con):
    # variable to store the path where validation scripts are available for video data
    the_dir = 'E:\\Final_Assignment\\src\\\sql\\validation_scripts\\video_validation'
    # variable to store all .sql file validation scripts name using lamda function
    all_validation_files = filter(lambda x: x.endswith('.sql'), os.listdir(the_dir))
    # variable to count total number of failed test cases. Initially it is 0
    count=0
    # looping through each file in all_validation_files
    for each_script in all_validation_files:
        #opening each validation_scripts
        with open('../sql/validation_scripts/video_validation/'+each_script) as file:
            # joining all lines in script
            validation_script = " ".join(file.readlines())
            # excuting the validation script
            cur.execute(validation_script)
            #storing the fetched values in result
            result=cur.fetchone()
            # does nothing if there is 0 failed cases
            if(str(result)=="(0, 'passed')"):
                print
            else:
                # adds 1 to count if there are failed cases
                count += 1
                # prints error message indicating the script where errors are
                print("Data Validation error in "+each_script)
            con.commit() # commiting in the database
    return count # returning count variable


# Function to validate data of category_data which takes cur and con as parameter
# This function works exactly as the above function.
# But takes the path for validation as category_validation folder
def check_category_data_validity(cur,con):
    the_dir = 'E:\\Final_Assignment\\src\\\sql\\validation_scripts\\category_validation'
    all_validation_files = filter(lambda x: x.endswith('.sql'), os.listdir(the_dir))
    count=0
    for each_script in all_validation_files:
        
        with open('../sql/validation_scripts/category_validation/'+each_script) as file:
            validation_script = " ".join(file.readlines())
            cur.execute(validation_script)
            result=cur.fetchone()
            if(str(result)=="(0, 'passed')"):
                print
            else:
                count += 1
                print("Data Validation error in "+each_script)
            con.commit()
    return count
