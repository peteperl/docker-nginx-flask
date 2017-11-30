# docker-nginx-flask
Dockerized Nginx Flask configuration in multiple containers

## Configuration

Web -> [Nginx]
          |
          |->[gunicorn-Flask]
          |->[legacy API]

* Breaking each component into it's own container allows for a true microservice architecture
where each component can be updated independently (including nginx).
Nginx handles the forwarding between each container.

## Setup

AWS does not allow you to build on the fly from the docker-compose.yml so we built each piece
and push to our repo. This assumes you have setup the 'aws' and 'ecs-cli' clis and configured.
  
* Build Nginx:
     sudo docker build --no-cache -t nginx:a .
     sudo docker tag nginx:a 613145902265.dkr.ecr.us-west-2.amazonaws.com/container_west:nginx-a
     sudo docker push 613145902265.dkr.ecr.us-west-2.amazonaws.com/container_west:nginx-a

* Build Flask-gunicorn:
     sudo docker build --no-cache -t gunicorn-flask:a .
     sudo docker tag gunicorn-flask:a 613145902265.dkr.ecr.us-west-2.amazonaws.com/container_west:gunicorn-flask-a
     sudo docker push 613145902265.dkr.ecr.us-west-2.amazonaws.com/container_west:gunicorn-flask-a


