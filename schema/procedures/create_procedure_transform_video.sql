CREATE OR REPLACE PROCEDURE transform_video()
LANGUAGE plpgsql
AS $$
BEGIN

TRUNCATE TABLE transform_video;

INSERT INTO transform_video
SELECT * FROM raw_video;

UPDATE transform_video
SET tags = NULL
WHERE tags = '[none]';

UPDATE transform_video 
SET trending_date = TO_DATE(trending_date,'yy.dd.mm');

UPDATE transform_video 
SET publish_time= REPLACE(publish_time,'T',' ');

UPDATE transform_video 
SET publish_time= REPLACE(publish_time,'.000Z','');

UPDATE transform_video
SET video_id = LEFT(title,7)||views
WHERE video_id = '#NAME?';

END;
$$;


