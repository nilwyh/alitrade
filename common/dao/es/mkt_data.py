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

    def get_daily_mkt_data_by_time_order(self, symbol, date, bar='10m'):
        term1 = {'term': {'date': date}}
        term2 = {'term': {'bar': bar}}
        must = [term1, term2]
        filter = {'filter': {'bool': {'must': must}}}
        query = {'query': {'filtered': filter}, 'size' : 1000}
        query["sort"] = { "time": { "order": "asc" }}

        resp = self.es_reader.get_messages(query)
        if resp.status_code != 200:
            log.debug("Error, can't get mkt data from es!")
        hit = json.loads(resp.text)

        if hit['timed_out']:
            log.debug("Error, time out in get mkt data from es!")
        hits = hit['hits']['hits']

        sources= []
        for hit in hits:
            sources.append(hit['_source'])

        return sources

