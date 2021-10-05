SELECT
    COUNT(*) AS impacted_record_count,
    CASE
        WHEN COUNT(*) > 0 THEN 'failed'
        ELSE 'passed'
    END AS test_status
FROM (
	SELECT category_id FROM raw_video
	EXCEPT
	SELECT category_id FROM transform_video
)result;