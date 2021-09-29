CREATE OR REPLACE PROCEDURE transform_video()
LANGUAGE plpgsql
AS $$
BEGIN
UPDATE raw_video
SET tags = NULL
WHERE tags = '[none]';

UPDATE raw_video 
SET trending_date = TO_DATE(trending_date,'yy.dd.mm');

UPDATE raw_video 
SET publish_time= REPLACE(publish_time,'T',' ');

UPDATE raw_video 
SET publish_time= REPLACE(publish_time,'.000Z','.000S');


INSERT INTO video_archive
SELECT * from  raw_video 
EXCEPT
SELECT * FROM video_archive;


END;
$$;


