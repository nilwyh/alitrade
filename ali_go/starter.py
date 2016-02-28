
from common import time
import ujson as json
from conn import kafka_writer

def run():
    writer = kafka_writer.KafkaWriter()
    start = '20160101 00:00:00'
    end = '20160201 00:00:00'
    cur = time.ali_time(start)
    cur.increase_day()
    while cur.before(end):
        print cur.get_date()
        send_req(writer, cur.get_date())

def send_req(writer, date):
    data = {}
    req = {}
    req['histDataReq'] = data
    data['rth'] = False
    data['symbol'] = 'UVXY'
    data['duration'] = 1
    data['durationUnit'] = 'day'
    data['barSize'] = '10m'
    data['endDate'] =date

    writer.write_message('get_hist_data_req', 'null', json.dumps(req))






if __name__ == "__main__":
    run()
