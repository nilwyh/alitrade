import json

from kafka import KafkaConsumer

class KafkaReader():




    def __init__(self, topic):

        # To consume latest messages and auto-commit offsets
        self.consumer = KafkaConsumer(group_id='my-group',
                                 bootstrap_servers='localhost:9092',
                                 enable_auto_commit=True)
        self.consumer.subscribe(topics=[topic])
        self.buffer = []

    def read_message(self):
        # print len(self.buffer)
        # if len(self.buffer) == 0:
        #     self.get_batch()
        # if len(self.buffer) > 0:
        #     return self.buffer.pop(0)
        # else:
        #     print "11"
        #     return None
        return self.consumer.next()


    def get_batch(self):
        for message in self.consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            self.buffer.append(message)
            print self.buffer

