import os

REDIS_ADDR = os.environ['REDIS_PORT_6379_TCP_ADDR']
REDIS_PORT = os.environ['REDIS_PORT_6379_TCP_PORT']
BROKER_URL = 'redis://%s:%s/0' % (REDIS_ADDR, REDIS_PORT)
BACKEND_URL = 'redis://%s:%s/0' % (REDIS_ADDR, REDIS_PORT)

DBNAME = 'renette'
DBUSER = 'renette'
DBPASSWORD = 'renette'
DBHOST = os.environ['PGSQL_PORT_5432_TCP_ADDR']
DBPORT = os.environ['PGSQL_PORT_5432_TCP_PORT']
