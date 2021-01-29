# Django + Redis

This is a simple django project showing how to add cache layer with Redis.


## SETUP

In order to setup this project we need below services:

* MySQL
* Redis
* Django Project

### Deploy MySQL in Fandogh PaaS using below manifest

```py
fandogh service apply -f mysql_deployment.yml
```

### Deploy Redis in Fandogh PaaS using below manifest

```bash
fandogh service apply -f redis_deployment.yml 
```


### Deploy Django Project in Fandogh PaaS using Source Deployment command


#### First initialize the source project

```bash
fandogh source init
```

#### Then deploy the fandogh.yml generated manifest with below command

```bash
fandogh source run
```
