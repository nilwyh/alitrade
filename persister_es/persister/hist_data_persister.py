from common.conn import kafka_reader
from common.utils import log
from common.conn import es_conn
from persister_es.converter import hist_data_converter as converter


class HistDataPersister():
    def __init__(self):
        self.hist_data_reader = kafka_reader.KafkaReader('get_hist_data_resp')
        self.es_writer = es_conn.ESConnection('alitrade', 'mkt_data')

    def persist(self):
        resp = self.hist_data_reader.read_message()
        lists = converter.convert(resp.value)
        for data in lists:
            print data
            self.es_writer.create(data)
        log.info('persist finished!')
