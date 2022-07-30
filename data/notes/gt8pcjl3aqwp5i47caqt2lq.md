
- Areas: [[devlog.sql]]

The `IS NULL` operator is used to test for empty values ([[devlog.NULL]] values).

    SELECT *
    FROM customers
    WHERE phone IS NULL

using with NOT operator

    SELECT *
    FROM customers
    WHERE phone IS NOT NULL
