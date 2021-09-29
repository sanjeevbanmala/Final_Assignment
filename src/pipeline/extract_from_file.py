def extract_video(cur,con,filePath):
    fileName = "'"+filePath[26:28]+"'"
    call_procedure_extract_video ="CALL extract_video("+filePath+","+fileName+")"
    cur.execute(call_procedure_extract_video)
    con.commit()
