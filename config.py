import os

host = os.environ['HOST']
redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']

export HOST="localhost:8080"
export REDIS_HOST="localhost"
export REDIS_PORT=6379

pip install redis