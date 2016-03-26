import datetime

class AliTime():
    def __init__(self, date):
        try:
            self.date = datetime.datetime.strptime(date, "%Y%m%d %H:%M:%S")
        except:
            self.date = datetime.datetime.fromtimestamp(date/1000.0)


    def get_date(self):
        return self.date.strftime("%Y%m%d %H:%M:%S")

    def get_date_day(self):
        return self.date.strftime("%Y/%m/%d")

    def increase_day(self):
        self.date = self.date + datetime.timedelta(days=1)

    def before(self, end_date):
        end = datetime.datetime.strptime(end_date, "%Y%m%d %H:%M:%S")

