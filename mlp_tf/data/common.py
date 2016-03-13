

def max_price(data):
    max_p=-1
    for row in data:
        max_p = max(max_p, row['high'])
    return max_p


def min_price(data):
    min_p=9999999
    for row in data:
        min_p=min(min_p,row['low'])
    return min_p

