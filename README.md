# API Count Application

```
In front of the gate under the bridge there are ducks. Come on count them, one two three, quack quack - (Chinese child song)
```

## Description 

This application provides a REST API with a front end that enables counting of ducks. The backend is built in python flask, frontend in Jquery, with a mongodb database layer.

In order to interact with the application, deploy the application and use the frontend. Otherwise, perform manual API requests by using CURL commands after deployment.

## Prerequisites

Installation of docker and docker-compose required before running the application:
1.) Installation of docker
Refer to Docker documentation:
https://docs.docker.com/install/linux/docker-ce/debian/

2.) Installation of docker-compose:
```
sudo curl -L \ 
https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) \
-o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

## Deployment

Deployment is done via docker-compose from the root directory of the app (duckcount).
Due to docker-compose linking a mongodb container with one or more web app instances in a container, the app is deployable using the minimum possible downtime.

```
cd /duck-count/
docker-compose up 
```

Then browse to http://localhost:8080/ to access the frontend or use CURL for interaction with REST API on localhost:8080/duck/ (see description below).


## Using the application

The application is deployed to localhost using port 8080. The rest interface is available via URI /duck/ 
You can either count some ducks using the front end or interact directly with the API using these CURL commands:

```

#Increase duck count:
curl -XPUT http://localhost:8080/duck/

#Decrease duck count:
curl -XDELETE http://localhost:8080/duck/

#Get duck count:
curl -XGET http://localhost:8080/duck/

#Reset duck count:
curl -XPOST http://localhost:8080/duck/

```

## Authors

* **Skjallargrimmur**

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
