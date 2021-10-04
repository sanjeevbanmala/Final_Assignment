import os

def check_data_validity(cur,con):
    the_dir = 'E:\\Final_Assignment\\src\\sql\\validation_scripts'
    all_validation_files = filter(lambda x: x.endswith('.sql'), os.listdir(the_dir))
    count=0
    for each_script in all_validation_files:
        
        with open('../sql/validation_scripts/'+each_script) as file:
            validation_script = " ".join(file.readlines())
            cur.execute(validation_script)
            result=cur.fetchone()
            if(str(result)=="(0, 'passed')"):
                print
            else:
                count += 1
                print(count)
                print("Data Validation error in "+each_script)
            con.commit()
    if(count==0):
        print("All data are valid according to validation tests!!!!")

