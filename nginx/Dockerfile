FROM fedora

MAINTAINER hiromu

RUN yum install -y nginx

ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
