TRUNCATE TABLE raw_video;

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
FROM 'E:\archive\CAvideos.csv' 
WITH CSV HEADER;
