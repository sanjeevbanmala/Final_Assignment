-- create table script for dim_date
CREATE TABLE dim_date(
	date_id SERIAL PRIMARY KEY,
	trending_date DATE,
	publish_time TIMESTAMP
);
