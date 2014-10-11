FROM fedora

MAINTAINER hiromu

RUN yum install -y redis

EXPOSE 6379

ENTRYPOINT ["/usr/sbin/redis-server"]
