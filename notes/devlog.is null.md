---
id: gt8pcjl3aqwp5i47caqt2lq
title: IS NULL
desc: ''
updated: 1653437762206
created: 20211105172925504
---

- Areas: [[devlog.sql]]

The `IS NULL` operator is used to test for empty values ([[devlog.NULL]] values).

    SELECT *
    FROM customers
    WHERE phone IS NULL

using with NOT operator

    SELECT *
    FROM customers
    WHERE phone IS NOT NULL
