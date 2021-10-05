/*
  This procedure is used for loading data in fact and dimension tables.
  At first, it truncates all the data in fact and dimension table with cascade.
  Then, it inserts in all the dimension tables.
  Then, it loads data in act table.
*/
CREATE OR REPLACE PROCEDURE load_dim_fact_tables()
LANGUAGE plpgsql
AS $$
BEGIN
TRUNCATE TABLE fact_video RESTART IDENTITY CASCADE;
TRUNCATE TABLE dim_date RESTART IDENTITY CASCADE;
TRUNCATE TABLE dim_channel RESTART IDENTITY CASCADE;
TRUNCATE TABLE dim_country RESTART IDENTITY CASCADE;
TRUNCATE TABLE dim_category RESTART IDENTITY CASCADE;

INSERT INTO dim_date(trending_date, publish_time)
SELECT
   DISTINCT 
   CAST(trending_date AS DATE), 
   CAST(publish_time AS TIMESTAMP) 
FROM raw_video_archive;

INSERT INTO dim_channel(channel_title)
  SELECT DISTINCT channel_title 
  FROM raw_video_archive;

INSERT INTO dim_country
SELECT DISTINCT country_code,
CASE 
  WHEN country_code = 'RU'
    THEN 'Russia'
  WHEN country_code = 'MX'
    THEN 'Mexico'
  WHEN country_code = 'CA'
    THEN 'Canada'
  WHEN country_code = 'IN'
    THEN 'India'
  WHEN country_code = 'US'
    THEN 'United States'
  WHEN country_code = 'KR'
    THEN 'Korea'
  WHEN country_code = 'FR'
    THEN 'France'
  WHEN country_code = 'JP'
    THEN 'Japan'
  WHEN country_code = 'GB'
    THEN 'Great Britain'
  WHEN country_code = 'DE'
    THEN 'Denmark'
  ELSE ''
   END
     AS country
FROM raw_video_archive;

INSERT INTO dim_category
SELECT DISTINCT
   CAST(category_id AS INT),
   category_title
FROM raw_category_archive;

INSERT INTO fact_video(
	date_id,
	channel_id,
	category_id,
	country_code,
	title,
	views,
	likes,
	dislikes,
	comment_count,
	comments_disabled,
	ratings_disabled,
	video_error_or_removed,
	description
    )
SELECT d.date_id, 
       c.channel_id, 
	   CAST(r.category_id AS INT), 
	   co.country_code,r.title,
	   CAST(r.views AS INT),
	   CAST(r.likes AS INT),
	   CAST(r.dislikes AS INT),
	   CAST(r.comment_count AS INT),
	   CAST(r.comments_disabled AS BOOL),
	   CAST(r.ratings_disabled AS BOOL),
	   CAST(r.video_error_or_removed AS BOOL),
	   r.description
FROM raw_video_archive r
INNER JOIN 
     dim_date d 
     ON CAST(r.trending_date AS DATE) = d.trending_date 
       AND CAST(r.publish_time AS TIMESTAMP) = d.publish_time
INNER JOIN 
    dim_channel c 
	ON r.channel_title= c.channel_title
INNER JOIN dim_country co 
    ON r.country_code = co.country_code;
	
END;
$$;
