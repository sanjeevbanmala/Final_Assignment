# Folder Structure

The folder structure of this project is given below:
* data - contains data files to be extracted
* docs - contains documentation file for datawarehouse deisgn and ETL pipeline
* schema - contains SQL create script for required tables and procedures
* src - contains three folders which are
    - pipeline - python scripts for pipeline
    - sql - data validation scripts and other scripts
    - utils - database connection scripts and other utilities

The data for this project can be downloaded from here [click here](https://www.kaggle.com/datasnaek/youtube-new)

Note: Maintain the data files in data folder as mentioned in above folder structure.

Also, create a `.env` file inside `src` folder to store credentials to the postgresql database like below:
The port number is by default `5432` or you can set your own port if you have set another port number.
```
HOST = 'your host name'
USER = 'your username'
PASSWORD = 'your password'
PORT = 'your port number'
DATABASE='your database name'
```
Then, in your database create the tables and procedures using the scripts provided in schema folder.

Finally, run the `main.py` file in `src/pipeline` folder to run the ETL process.

To learn more about the data warehouse model design and ETL pipeline process, look at the docs folder.