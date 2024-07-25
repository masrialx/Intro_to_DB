-- Use the specified database (you will provide the database name when running the script)
USE alx_book_store;

-- Query the information_schema to get the full description of the Books table
SELECT 
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Column Type',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_KEY AS 'Key',
    EXTRA AS 'Extra Info'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store' AND
    TABLE_NAME = 'Books';
