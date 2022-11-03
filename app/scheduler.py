import schedule
from time import sleep

class Scheduler:
    def schedule_everyday(self, time, job):
        schedule.every().day.at(time).do(job)

        while True:
            schedule.run_pending()
            sleep(1)