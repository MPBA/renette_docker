FROM fedora

MAINTAINER hiromu

ENV RABBITMQ_PID_FILE /var/run/rabbitmq/rabbitmq.pid

RUN yum install -y rabbitmq-server
RUN (rabbitmq-server &) && rabbitmqctl wait $RABBITMQ_PID_FILE && rabbitmqctl add_user renette renette && rabbitmqctl add_vhost renette && rabbitmqctl set_permissions -p renette renette '.*' '.*' '.*' && rabbitmqctl stop

EXPOSE 5672

ENTRYPOINT ["/usr/sbin/rabbitmq-server"]
