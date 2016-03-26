from common.dao.es import mkt_data as dao
from common.utils import time

def run():
    c = dao.MktDataEsDao()
    res = c.get_daily_mkt_data_by_time_order('UVXY', '2016/01/22', bar='10m')
    for data in res:
        t=time.AliTime(data['time'])
        print t.get_date()


run()