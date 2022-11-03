from .time_manager import TimeManager

class StatusCreator:
    def __init__(self):
        self.time_manager = TimeManager()

    def create_status_message(self):
        date = self.time_manager.convert_to_datetime("1/1/2023")
        days = self.time_manager.how_many_days_until(date)

        return f"Faltam {days} para a posse do @LulaOficial"