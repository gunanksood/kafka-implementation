from confluent_kafka import Producer
import random


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))


p = Producer({'bootstrap.servers': 'localhost:9092'})

try:
    for val in xrange(1, 100000):
        p.produce('mytopic1', 'myvalue #{0}'
                  .format(random.random()), callback=acked)


except KeyboardInterrupt:
    pass

p.flush(30)