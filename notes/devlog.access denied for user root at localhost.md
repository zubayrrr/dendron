---
id: z6st1cdnl60ecoyrkrw06ng
title: Access denied for user 'root'@'localhost'
desc: ''
updated: 1653304922224
created: 20211104223035710
tags:
  - tidbits
---

- Areas: [[devlog.sql]]

`sudo mysql`

or

Add switch -p for password based login:

`mysql -u root -p`

`SELECT user,authentication_string,plugin,host FROM mysql.user;`

`ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Current-Root-Password';FLUSH PRIVILEGES;`

## OR

`INSERT INTO mysql.user (Host, User, Password) VALUES ('%', 'root', password('YOURPASSWORD')); GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION;`

`sudo mysql -u root -p`
