import ujson as json

from common.utils import time


def convert(message):
    print message
    obj = json.loads(message)
    req = obj['histDataReq']
    resp = obj['histDataResp']
    lists = []

    for data in resp:
        data['symbol'] = req['symbol']
        data['bar'] = req['barSize']
        t = time.AliTime(data['time'])
        data['date'] = t.get_date_day()
        data['id'] = data['symbol'] + '_'+data['bar']+'_'+str(data['time'])
        lists.append(data)


    return lists
