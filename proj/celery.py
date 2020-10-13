from celery import Celery

app = Celery('proj',
             broker='amqp://rabbitmq:rabbitmq@localhost:5672//',
             backend='rpc://',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)