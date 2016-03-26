from common.conn import es_conn
from common.utils import log
import ujson as json

test_id = 'UVXY_10m_1451923200000'
test_symbol = 'UVXY'
test_date = '2016/01/22'

class MktDataEsDao():
    def __init__(self):
        self.es_reader = es_conn.ESConnection('alitrade', 'mkt_data')

    def get_mkt_data_by_id(self, id):
        id =test_id
        resp = self.es_reader.get_message_by_id(id)
        if resp.status_code != 200:
            log.debug("Error, can't get mkt data from es!")
        source = json.loads(resp.text)
        if not source['found']:
            log.debug("Error, can't get mkt data from es!")
        source = source['_source']
        return source

    def get_daily_mkt_data(self, symbol, date, bar='10m'):
        term = {'term': {'date': date}}
        filter = {'filter': term}
        query = {'query': {'filtered': filter}}
        resp = self.es_reader.get_messages(query)
        return resp

