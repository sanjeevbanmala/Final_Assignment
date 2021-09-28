CREATE OR REPLACE PROCEDURE extract_video(filePath VARCHAR, country_code VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
TRUNCATE TABLE raw_video;
EXECUTE'
COPY raw_video(
      video_id,
      trending_date,
      title,
      channel_title,
      category_id,
      publish_time,
      tags,
      views,
      likes,
      dislikes,
      comment_count,
      thumbnail_link,
      comments_disabled,
      ratings_disabled,
      video_error_or_removed,
      description
     ) 
    FROM '''||$1||'''
    WITH CSV HEADER'; 
UPDATE raw_video 
SET country_code = ''||$2||'';
END;
$$;
