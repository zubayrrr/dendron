---
id: q972711fkjnov4mv6kfzb53
title: Running a Web Server in a Docker Container
desc: ''
updated: 1653665225384
created: 1653664874753
---

- Related: [[devlog.Docker]]

---

Using Ngnix for a web server

- Run `docker container run -d -p 8080:80 --name mysite ngnix`
  - `-d` for detached mode (as a bg process)
  - `-p 8080:80` will expose container's port 80 to docker host's port 8080
  - `--name` to define a name, otherwise it'll choose one from a predefined list of names(applicabale to all containers not just ngnix)
