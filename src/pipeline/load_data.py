# this function is used to load the extracted data in fact and dimension table
# all the sql scripts related to loading the data are availble in procedure load_dim_fact_tables()
# This function just calls that procedure to load data
def load_data_into_warehouse(cur,con):
    call_procedure="CALL load_dim_fact_tables()"
    cur.execute(call_procedure)
    con.commit()
    print("Data Successfully loaded in Fact and Dimension tables!!!")