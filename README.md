# Dockerfiles for Renette

## Installation

    $ cp settings/docker.py renette/renette/settings/docker.py
    $ cp settings/settings.py renette/engine/settings.py
    $ sed -e "s/<UID>/`ls -dn renette | awk '{ print $3 }'`/" celery/Dockerfile.default | sed -e "s/<GID>/`ls -dn renette | awk '{ print $4 }'`/" > celery/Dockerfile
    $ sed -e "s/<UID>/`ls -dn renette | awk '{ print $3 }'`/" django/Dockerfile.default | sed -e "s/<GID>/`ls -dn renette | awk '{ print $4 }'`/" > django/Dockerfile

## Build

    $ sudo docker build -t renette/redis redis
    $ sudo docker build -t renette/pgsql pgsql
    $ sudo docker build -t renette/celery celery
    $ sudo docker build -t renette/django django
    $ sudo docker build -t renette/nginx nginx

## Launch

    $ sudo docker run --name redis -d renette/redis
    $ sudo docker run --name pgsql -d renette/pgsql
    $ sudo docker run --link redis:redis --link pgsql:pgsql -v `pwd`/renette:/home/renette/renette -d renette/celery
    
    # first time only
    $ sudo docker run --name django --link redis:redis --link pgsql:pgsql -v `pwd`/renette:/home/renette/renette --rm=true --entrypoint='python' -i -t renette/django /home/renette/renette/manage.py syncdb
    $ sudo docker run --name django --link redis:redis --link pgsql:pgsql -v `pwd`/renette:/home/renette/renette --rm=true --entrypoint='python' -i -t renette/django /home/renette/renette/manage.py collectstatic
    
    $ sudo docker run --name django --link redis:redis --link pgsql:pgsql -v `pwd`/renette:/home/renette/renette -d renette/django
    $ sudo docker run --link django:django -v `pwd`/renette:/home/renette/renette -d renette/nginx
