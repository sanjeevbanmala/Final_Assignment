/*
 This procedure transfoms the extracted raw_video and stores the transformed
 data into transform_video table.
 
*/

-- defining procedure transform_video()
CREATE OR REPLACE PROCEDURE transform_video()
-- language to be used in procedure
LANGUAGE plpgsql
AS $$
--start of begin/end block
BEGIN
-- truncating all data in transform_video at first
TRUNCATE TABLE transform_video;
-- inserting data in transform_video using insert into command
INSERT INTO transform_video
SELECT 
  -- replacing the data in raw_video having video id as '#NAME?'
  CASE 
  WHEN 
     video_id = '#NAME?'
  THEN 
     LEFT(title,7)||views
  ELSE 
     video_id
  END AS video_id,
  -- changing the format of date to postgres date format
  TO_DATE(trending_date,'yy.dd.mm'),
  title,
  channel_title,
  category_id,
  -- removing unnecessary words from publish time
  REPLACE(REPLACE(publish_time,'T',' '),'.000Z','') as publish_time,
  -- replacing tags as '[none]' to null
  CASE 
  WHEN 
     tags='[none]'
  THEN
     NULL
  ELSE
     tags
  END AS tags,
  views,
  likes,
  dislikes,
  comment_count,
  thumbnail_link,
  comments_disabled,
  ratings_disabled,
  video_error_or_removed,
  description,
  country_code
FROM raw_video;

END;
$$;
