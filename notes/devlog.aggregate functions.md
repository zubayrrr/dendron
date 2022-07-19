---
id: 054q9b0xp93e3vftctft14r
title: Aggregate Functions
desc: ''
updated: 1653304922290
created: 20211107132521270
---

- Areas: [[devlog.sql]]

## Aggregate Functions

Function is a piece of code that we can reuse, [[devlog.MySQL]] comes with a bunch of functions, some of these functions are called as Aggregate Functions, because they take a series of values and aggregate them to produce a single value.

They only operate on non-NULL values, NULL values will not be included when passed through a function.

### Examples

- MAX()
- MIN()
- AVG()
- SUM()
- COUNT()

```sql
SELECT
        MAX(invoice_total) AS highest,
    -- MAX(payment_date) AS latest_payment,
        MIN(invoice_total) AS lowest,
        AVG(invoice_total) AS average,
    -- SUM(invoice_total) AS total,
        COUNT(invoice_total) AS number_of_invoices,
        COUNT(payment_date) AS count_of_payments,
        COUNT(*) AS total_records
    -- COUNT(DISTINCT client_id) AS total_records
    -- the above statement will get all values regardless NULL or not
    -- you can also write expressions
        SUM(invoice_total * 1.1) AS total,
    FROM invoices
    WHERE invoice_date > '2019-07-01'
```
