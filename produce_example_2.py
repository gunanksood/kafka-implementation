# from confluent_kafka import Producer
#
#
# def acked(err, msg):
#     if err is not None:
#         print("Failed to deliver message: {0}: {1}"
#               .format(msg.value(), err.str()))
#     else:
#         print("Message produced: {0}".format(msg.value()))
#
# p = Producer({'bootstrap.servers': 'localhost:9092'})
#
# try:
#     # for val in xrange(1, 1000):
#     #     p.produce('mytopic', 'myvalue #{0}'
#     #               .format(val), callback=acked)
#     #     p.poll(0.5)
#     text = raw_input("Enter message to send ")
#     while text != 'exit':
#         p.produce('mytopic', text, callback=acked)
#         p.poll(0.5)
#         text = raw_input("enter a message to send and exit to end ")
#
#
#
# except KeyboardInterrupt:
#     pass
#
# p.flush(30)
from confluent_kafka import Producer
import random


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))


p = Producer({'bootstrap.servers': 'localhost:29092'})

try:
    for val in xrange(1, 10000):
        p.produce('mytopic', 'myvalue #{0}'
                  .format(random.randint(1, 1000000)), callback=acked)


except KeyboardInterrupt:
    pass

p.flush(30)
