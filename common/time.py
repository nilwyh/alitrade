import datetime

class ali_time():
    def __init__(self, date):
        self.date = datetime.datetime.strptime(date, "%Y%m%d %H:%M:%S")

    def get_date(self):
        return self.date.strftime("%Y%m%d %H:%M:%S")

    def increase_day(self):
        self.date = self.date + datetime.timedelta(days=1)

    def before(self, end_date):
        end = datetime.datetime.strptime(end_date, "%Y%m%d %H:%M:%S")
        return self.date <= end

