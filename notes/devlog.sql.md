---
id: 93cp838qc8pnou1we4cbdjb
title: SQL
desc: ''
updated: 1653437762210
created: 20211105134756444
tags:
  - areas
---

### SQL stands for Structured Query Language, MySQL is a relational database, every(column, row) is related to each other.

SQL is not case sensitive but as an industry standard practice, use uppercase for SQL keywords and lowercase for all the other things when writing queries.

Order of the clauses matter

1.  [[SELECT]]
2.  [[FROM]]
3.  [[WHERE]]
4.  [[ORDER BY]]

Line breaks, whitespaces, tabs are ignored when executing SQL code, each clause are written on a new line for better readability.

- Composite primary key contains more than one column

## Getting started

To get started, install:

- `sudo apt-get install mysql-server mysql-client libmysqlclient-dev`
- Also install [Mysql Workbench](https://www.mysql.com/products/workbench/)
- See [[Access denied for user 'root'@'localhost']]

## Retrieving Data From a Single Table

- [[SELECT]] clause

### Combine multiple multiple search conditions when filtering data

- The AND, OR and NOT operators
- [[IN]] operator
- [[BETWEEN]] operator
- [[devlog.LIKE]]command
- [[REGEXP]] command
- [[devlog.NULL]] value
- [[ORDER BY]] clause
- [[LIMIT]] clause

---

## Retrieving Data From Multiple Tables

- [[JOIN]] operator
- [[USING]] clause
- [[NATURAL JOIN]] - not recommend, can produce unexpected results
- [[CROSS JOIN]]
- [[UNION]] - combine rows from multiple tables and queries

---

## Inserting, Updating, and Deleting Data

### Column attributes

- Column name
- Datatype:
  - `INT` (whole numbers, no decimals)
  - `VARCHAR` (variable-characters used for strings, textual values, max length can be assigned inside paranthesis)
  - `DATE`
  - `CHAR` (unlike VARCHAR, max length assigned to CHAR is not variable and will be assigned indefinitely no matter the input size of the string)
- Primary Key
- [[NOT NULL]]
- `AUTO_INCREMENT` (often used with primary key columns, mysql or other engines will auto assign a value)
- Default values/Expression (can be specified in this column)

## Inserting

- [[INSERT INTO]]

## Creating

- [[CREATE TABLE]]

The SELECT clause on the above query is known as a `Subquery`, another example of Subquery:

    -- right click on orders_archived table and truncate to delete all records
    INSERT INTO orders_archived
    SELECT *
    FROM orders
    WHERE order_date < '2019-01-01'

## Updating

- [[UPDATE]]

## Deleting Rows

- [[DELETE FROM]]

---

## Summarizing Data

- [[Aggregate Functions]]
- [[GROUP BY]] clause
- [[HAVING]] clause
- [[ROLLUP]] operator
