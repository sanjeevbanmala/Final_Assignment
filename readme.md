# Trending YouTube Video Statistics

## Context

YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform. According to Variety magazine, “To determine the year’s top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes). Note that they’re not the most-viewed videos overall for the calendar year”. Top performers on the YouTube trending list are music videos (such as the famously virile “Gangam Style”), celebrity and/or reality TV performances, and the random dude-with-a-camera viral videos that YouTube is well-known for.

This dataset is a daily record of the top trending YouTube videos.

Note that this dataset is a structurally improved version of this dataset.

## Content

The dataset includes 20 files: 10 csv files for 10 different countries and 10 json files as the supportive file for csv files. The json file includes the details of the category of the items in the csv file. Each CSV file consists of 10 columns (video_id, trending_date, title, channel_title, category_id, publish_time, tags, views, likes, dislikes).  As the supportive file, each CSV file has an individual JSON file containing the details of the category.

## Acknowledgement

The data for this project can be downloaded from here [click here](https://www.kaggle.com/datasnaek/youtube-new)

# What this project is actually for?

* Designing and developing a data warehouse for the youtube dataset.

* Developing an ETL pipeline for the data loading in data warehouse.

* Making use of POWER BI to analyze the trending video data like:
   - To find the category having highest trending videos.
   - Do trending videos have comments disabled, ratings disabled or video error or removed?
   - Do comments increase with increase in like?
   - For more you can look to docs/data_visualization.md

# The data can also be used for othe rpurpose than this project like:

* Sentiment Analysis
* Training ML algorithms like RNNs to generate their own YouTube comments.
* Statistical analysis over time.

Note: This readme file only consists of project description and folder structure. To learn more about documentation, Please visit docs folder.

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