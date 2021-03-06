-- create table script for fact_video
CREATE TABLE fact_video(
	id SERIAL PRIMARY KEY,
	date_id INT,
	channel_id INT,
	category_id INT,
	country_code VARCHAR(5),
	title VARCHAR(300),
	views INT,
	likes INT,
	dislikes INT,
	comment_count INT,
	comments_disabled BOOL,
	ratings_disabled BOOL,
	video_error_or_removed BOOL,
	description VARCHAR(15000),
	FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
	FOREIGN KEY (channel_id) REFERENCES dim_channel(channel_id),
	FOREIGN KEY (category_id) REFERENCES dim_category(category_id),
	FOREIGN KEY (country_code) REFERENCES dim_country(country_code)	
);
