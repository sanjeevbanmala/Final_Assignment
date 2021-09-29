def transform_video(cur,con):
    call_procedure_transform_video ="CALL transform_video()"
    cur.execute(call_procedure_transform_video)
    con.commit()
