def load_data_into_warehouse(cur,con):
    call_procedure="CALL load_dim_fact_tables()"
    cur.execute(call_procedure)
    con.commit()