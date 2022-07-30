
- The LIMIT clause is used to set an upper limit on the number of [[tuple]]s or results returned by SQL.
- It is important to note that this clause is not supported by all SQL versions.
- The LIMIT clause can also be specified using the SQL 2008 [[OFFSET]]/[[FETCH]], [[FIRST]] clauses.
- The limit/offset expressions must be a non-negative integer.

  SELECT \*
  FROM customers
  LIMIT 3
  --will output only first 3 customers(rows?)

  LIMIT 300
  --if there are 300 customers in the table that will be returned, otherwise only the existing columns will be returned

To use offset (in case of building pagination etc)

    SELECT *
    FROM customers
    LIMIT 6, 3
    --will output columns after 6 rows and then return 3 columns

### Example

    SELECT *
    FROM customers
    ORDER BY points DESC
    LIMIT 3

The order of clauses written matters.