
from common import time
import ujson as json
from conn import kafka_writer

def run():
    writer = kafka_writer.KafkaWriter()
    start = '20150101 00:00:00'
    end = '20150301 00:00:00'
    cur = time.AliTime(start)
    cur.increase_day()
    while cur.before(end):
        print cur.get_date()
        send_req(writer, cur.get_date())
        cur.increase_day()

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
    data['whatToShow']='trades'

    writer.write_message('get_hist_data_req', 'null', json.dumps(req))






if __name__ == "__main__":
    run()
