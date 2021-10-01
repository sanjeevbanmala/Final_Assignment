import json
import sys
sys.path.append("/final_assignment/src/")
import utils
import utils.database_connection

 
f = open('../../data/CA_category_id.json', "r")
data = json.load(f)
 
con=utils.database_connection.connect()
cur=con.cursor()

for json_data in data['items']:
    id = json_data['id']
    title = json_data['snippet']['title']
    insert_query="INSERT INTO raw_category(category_id,category_title) VALUES ('"+id+"','"+title+"')"
    cur.execute(insert_query)
    con.commit()
    


# Closing file
f.close()