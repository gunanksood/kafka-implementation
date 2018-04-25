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
import argparse


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))


parser = argparse.ArgumentParser()
parser.add_argument("ip", help="IP address")
parser.add_argument("port", help="Port no.")
args = parser.parse_args()

address = "" + args.ip + ":" + args.port
p = Producer({'bootstrap.servers': address})


try:
    for val in xrange(1, 10000):
        p.produce('mytopic', 'myvalue #{0}'
                  .format(random.randint(1, 1000000)), callback=acked)


except KeyboardInterrupt:
    pass

p.flush(30)
