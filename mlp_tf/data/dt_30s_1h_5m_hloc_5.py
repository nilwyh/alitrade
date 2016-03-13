from mlp_tf.data import common

class InputData():
    def __init__(self, p, symbol):
        self.thresh = p
        self.thresh_ = 0-p

    def get_next(self):
        pass


    def get_next_batch(self, size):
        pass


    def y_(self, data, last):
        open_price = last['close']
        close_price = data[-1]['close']
        high_price = common.max_price(data)
        low_price = common.min_price(data)
        ratio = (close_price - open_price) / (high_price - low_price)
        if ratio > self.thresh:
            return 0
        if ratio > self.thresh_:
            return 1
        return 2
