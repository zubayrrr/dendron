
Web applications can be really complex and no matter how "modular" you make the code, it will still be a single, cohesive piece of code that will be deployed to a server. This is called a "Monolithic" application/architecture. It can tedious to manage and it can be hard to debug because even a single commit(in any of the modules) needs the entire application to be rebuilt.

Soooo

Rather than having the whole application smushed into monolith and deployed into one machine; why not split them application into "mini" applications and deploy them separately on different machines. You can have them talk to each other and work together as a single application. They can talk to each other using [[devlog.REST API]] APIs. Making a single application into a collection of smaller applications is called "Microservices".
