SELECT
    COUNT(*) AS impacted_record_count,
    CASE
        WHEN COUNT(*) > 0 THEN 'failed'
        ELSE 'passed'
    END AS test_status
FROM raw_video_archive
WHERE CAST(publish_time AS TIMESTAMP)::DATE > CAST(trending_date AS DATE);