SELECT
    COUNT(*) AS impacted_record_count,
    CASE
        WHEN COUNT(*) > 0 THEN 'failed'
        ELSE 'passed'
    END AS test_status
FROM (
	SELECT country_code FROM raw_video
	EXCEPT
	SELECT country_code FROM transform_video
)result;
