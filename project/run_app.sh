#!/bin/bash

#sudo systemclt start docker

sudo docker build --tag img_api_events .
sudo docker run --name mysql_api_events -p 127.0.0.1:3306:3306 -e MYSQL_ROOT_PASSWORD=teste123 -e MYSQL_DATABASE=desafio_elo7 -d mysql:5.7
sudo docker run --name api_events --link mysql_api_events:mysql_api_events -p 127.0.0.1:5000:5000 -d img_api_events
