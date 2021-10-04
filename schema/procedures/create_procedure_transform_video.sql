CREATE OR REPLACE PROCEDURE transform_video()
LANGUAGE plpgsql
AS $$
BEGIN

TRUNCATE TABLE transform_video;

INSERT INTO transform_video
SELECT 
CASE 
WHEN 
   video_id = '#NAME?'
THEN 
    LEFT(title,7)||views
ELSE 
   video_id
END AS video_id,
TO_DATE(trending_date,'yy.dd.mm'),
title,
channel_title,
category_id,
REPLACE(REPLACE(publish_time,'T',' '),'.000Z','') as publish_time,
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
description
FROM raw_video;
END;
$$;
