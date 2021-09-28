def extract_video(cur,con,filePath):
    fileName = "'"+filePath[26:28]+"'"
    call_procedure_extract_video ="call extract_video("+filePath+","+fileName+")"
    cur.execute(call_procedure_extract_video)
    con.commit()

#def transform_video(cur, con):
