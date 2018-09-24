#!/bin/bash

sudo docker stop mysql_api_events api_events
sudo docker rm mysql_api_events api_events
sudo docker image rm img_api_events