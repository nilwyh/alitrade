import ujson as json
def convert(message):
    obj = json.loads(message)
    req = obj['histDataReq']
    resp = obj['histDataResp']
    lists = []

    for data in resp:
        data['symbol'] = req['symbol']
        data['bar'] = req['barSize']
        lists.append(data)

    return lists
