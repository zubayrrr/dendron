---
id: 1io9ap5pqqnrhlpl7o31giw
title: NATURAL JOIN
desc: ''
updated: 1653304922221
created: 20211106113055600
modified: 20211106113237244
---

- Areas: [[devlog.sql]]

We don't need to explicity define what column names to compare, the engine will look at the tables and join them based on the common columns

    SELECT
            o.order_id,
            c.first_name
    FROM orders o
    NATURAL JOIN customers c
