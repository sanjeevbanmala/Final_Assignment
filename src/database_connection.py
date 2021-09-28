import psycopg2
try:
    def connect():
        return psycopg2.connect( 
            host = "localhost", 
            database = "final_assignment", 
            user ="postgres", 
            password ="password", 
            port =5432
        )

except Exception as e:
    print('AN error has occured', e)
