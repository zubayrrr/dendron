---
id: p5jw4wchevr9jx8inug22qo
title: DELETE FROM
desc: ''
updated: 1653304922284
created: 20211107114041660
---

- Areas: [[devlog.sql]]

We use `DELETE FROM` statement to delete records from a table

    DELETE FROM invoices
    -- WHERE can be optionally used to search and filter out results to delete
    WHERE client_id =
    -- using subquery
    (SELECT *
    FROM clients
    WHERE name = 'Myworks')
