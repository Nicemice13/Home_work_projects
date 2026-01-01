class Television:
    def __init__(self, work=False, canal=1, volume_level=50):
        self.work = work
        self.canal = max(1, min(999, canal))
        self.volume_level = max(0, min(100, volume_level))

    def turn_on(self):
        """Переключает состояние телевизора между включенным и выключенным."""

        self.work = not self.work
        return f'Телевизор включен' if self.work else f'Телевизор выключен'

    def change_canal(self, new_canal):
        """Переключает каналы в случае если телевизор включен."""

        if self.work:
            if 1 <= new_canal <= 999:
                self.canal = new_canal
                return self.canal
            else:
                return f"Указан неправильный номер канала.\nВедите новый номер канала."
        else:
            return f"Телевизор выключен, для выбора канала включите телевизор."

    def change_volume(self, volume_level_new):
        """Изменяет режим громкости в случае если телевизор включен."""

        if self.work:
            if volume_level_new < 0:
                return 0
            elif volume_level_new > 100:
                return 100
            else:
                self.volume_level = volume_level_new
                return self.volume_level
        else:
            return f"Телевизор выключен. Для регулирования громкости включите телевизор."

    def check_in_status(self):
        """
        Выводит информацию о том, включен ли телевизор или нет,
        текущий канал, и уровень громкости.
        """
        status = "Телевизор включен" if self.work else "Телевизор выключен."

        if self.work:
                return f"{status}, канал: {self.canal}, громкость: {self.volume_level}"
        else:
            return f"{status}"

tv_1 = Television(canal=23, volume_level=200)
print(tv_1.check_in_status())
tv_1.turn_on()
print(tv_1.check_in_status())
tv_2 = Television(True, 12, 64)
print(tv_2.check_in_status())
tv_2.turn_on()
print(tv_2.check_in_status())
tv_3 = Television(True, 1000, 101)
print(tv_3.check_in_status())
tv_3.turn_on()
print(tv_3.check_in_status())
