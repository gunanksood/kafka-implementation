# from confluent_kafka import Producer
#
# p = Producer({'bootstrap.servers': 'localhost:9092'})
# p.produce('mytopic2', key='hello', value='world')
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
                  .format(random.choice('abcdefghijklmnopqrstuvwxyz')), callback=acked)


except KeyboardInterrupt:
    pass

p.flush(30)

