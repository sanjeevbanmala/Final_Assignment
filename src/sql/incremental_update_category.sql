INSERT INTO raw_category_archive
SELECT * FROM raw_category
WHERE category_id NOT IN(
    SELECT category_id FROM raw_category_archive
)
AND
category_title NOT IN(
    SELECT category_title FROM raw_category_archive
);
