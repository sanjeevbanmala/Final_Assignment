-- create table script for dim_channel
CREATE TABLE dim_channel(
	channel_id SERIAL PRIMARY KEY,
	channel_title VARCHAR(200)
);
