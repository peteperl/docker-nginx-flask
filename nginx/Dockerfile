FROM nginx:alpine

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY flask.conf /etc/nginx/conf.d/

# VOLUME /var/log/nginx/log
