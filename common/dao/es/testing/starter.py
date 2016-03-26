from common.dao.es import mkt_data as dao

def run():
    c = dao.MktDataEsDao()
    res = c.get_daily_mkt_data('UVXY', '2016/01/22')
    print res.text


run()