# Celery/RabbitMQ playground

### Tutorials:
    - https://www.codeproject.com/Articles/1224515/Python-Celery-RabbitMQ-Tutorial
    - https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

### Requirements
  - Docker-compose
  - Celery   
 
### Docker-compose
```
version: '2.2'

services:
  rabbitmq:
    image: rabbitmq:3-management
    hostname: my-rabbit
    environment:
      RABBITMQ_ERLANG_COOKIE: "SWQOKODSQALRPCLNMEQG"
      RABBITMQ_DEFAULT_USER: "rabbitmq"
      RABBITMQ_DEFAULT_PASS: "rabbitmq"
      RABBITMQ_DEFAULT_VHOST: "/"
    volumes:
      # - ./rabbitmq/etc/definitions.json:/etc/rabbitmq/definitions.json
      # - ./rabbitmq/etc/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf
      # - ./rabbitmq/data:/var/lib/rabbitmq/mnesia/rabbit@my-rabbit
      - ./rabbitmq/logs:/var/log/rabbitmq/log
    ports:
      - 5672:5672
      - 15672:15672

```

### Execution
```
cd test-celery
celery -A proj worker --loglevel=INFO
python run_task
```