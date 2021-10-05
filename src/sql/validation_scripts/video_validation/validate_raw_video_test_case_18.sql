SELECT
    COUNT(*) AS impacted_record_count,
    CASE
        WHEN COUNT(*) > 0 THEN 'failed'
        ELSE 'passed'
    END AS test_status
FROM transform_video
WHERE CAST(ratings_disabled AS BOOL) NOT IN(FALSE,TRUE);
