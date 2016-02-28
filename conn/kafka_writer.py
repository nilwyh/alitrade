from kafka import KafkaProducer
import time


class KafkaWriter():


    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def write_message(self, topic, key, value):
        # produce keyed messages to enable hashed partitioning
        a = self.producer.send(topic, key =key, value=value)
        b=a.get(timeout=10)

        #
        # # Asynchronous by default
        # future = producer.send('get_hist_data_req', b'raw_bytes')
        #
        # # Block for 'synchronous' sends
        # try:
        #     record_metadata = future.get(timeout=10)
        # except KafkaError:
        #     # Decide what to do if produce request failed...
        #     log.exception()
        #     pass
        #
        # # Successful result returns assigned partition and offset
        # print (record_metadata.topic)
        # print (record_metadata.partition)
        # print (record_metadata.offset)
        #
        # # produce keyed messages to enable hashed partitioning
        # producer.send('my-topic', key=b'foo', value=b'bar')
        #
        # # encode objects via msgpack
        # producer = KafkaProducer(value_serializer=msgpack.dumps)
        # producer.send('msgpack-topic', {'key': 'value'})
        #
        # # produce json messages
        # producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
        # producer.send('json-topic', {'key': 'value'})
        #
        # # configure multiple retries
        # producer = KafkaProducer()