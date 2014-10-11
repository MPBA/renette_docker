FROM fedora

MAINTAINER hiromu

RUN yum install -y postgresql-server
RUN sed -i -e '2,2ialias system=echo' -e '2,2ifunction systemctl() { echo "Environment=PGPORT=5432 PGDATA=/var/lib/pgsql/data"; }' /usr/bin/postgresql-setup
RUN postgresql-setup initdb

USER postgres
RUN (postgres -D /var/lib/pgsql/data &) && while [ -z "`pg_isready | grep 'accepting connections'`" ]; do echo -n ''; done && psql --command "CREATE USER renette WITH SUPERUSER PASSWORD 'renette';" && createdb -O renette renette
RUN echo "host all  all    0.0.0.0/0  md5" >> /var/lib/pgsql/data/pg_hba.conf
RUN echo "listen_addresses='*'" >> /var/lib/pgsql/data/postgresql.conf


EXPOSE 5432

VOLUME ["/var/lib/pgsql"]

ENTRYPOINT ["/usr/bin/postgres", "-D", "/var/lib/pgsql/data"]
