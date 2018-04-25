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
    for val in xrange(1, 10000):
        items = [1, 2, 3, 4, 5, 6, 7]
        random.shuffle(items)
        p.produce('mytopic2', 'myvalue #{0}'
                  .format(items), callback=acked)


except KeyboardInterrupt:
    pass

p.flush(30)