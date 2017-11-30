# docker-nginx-flask
Dockerized Nginx Flask configuration in multiple containers

## Configuration

[Nginx]  
 |  
 |->[gunicorn-Flask]  
 |->[legacy API]  

* Breaking each component into it's own container allows for a true microservice architecture
where each component can be updated independently (including nginx).
Nginx handles the forwarding between each container.

## Setup

AWS does not allow you to build on the fly from the docker-compose.yml so we built each piece
and push to our repo. This assumes you have setup the 'aws' and 'ecs-cli' clis and configured.  

The 'aws' cli setup to use docker can be thorny. More comments to come.  
...  
  
Get your aws docker login:  

     ~/.local/bin/aws ecr get-login

Paste what the above command returns, removing the '-e none' (this has been depreciated and won't work if you leave it in).  
  
cd into the directory of each component. Use a reasonable versioning. I used 'a' as an example.    
  
Build Nginx: (I used nginx:alpine)  

     sudo docker build --no-cache -t nginx:a .
     sudo docker tag nginx:a RepositoryURI:nginx-a
     sudo docker push RepositoryURI:nginx-a

Build Flask-gunicorn:  

     sudo docker build --no-cache -t gunicorn-flask:a .
     sudo docker tag gunicorn-flask:a RepositoryURI:gunicorn-flask-a
     sudo docker push RepositoryURI:gunicorn-flask-a
  
Make sure you have installed and configured the 'ecs-cli'

     ecs-cli configure profile --profile-name container-west-small --access-key XXXXXXXXX --secret-key XXXXXXXXXXXXXXXX
     ecs-cli configure -r REGION -c CLUSTER

cd to the 'docker-nginx-flask' directory:  

     ecs-cli compose up
  
## Todo

I appreciate any comments.  
