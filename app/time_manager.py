from datetime import datetime

class TimeManager:
    def convert_to_datetime(self, time):
        return datetime.strptime(time, "%d/%m/%Y")

    def how_many_days_until(self, date):
        today = datetime.today()
        delta = date - today
        return delta.days
