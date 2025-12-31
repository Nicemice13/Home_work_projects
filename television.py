class Television:
    def __init__(self, work = False, canal=1, volume_level=50):
        self.work = work
        self.canal = canal
        self.volume_level = volume_level

    def turn_on(self):
        """Переключает состояние телевизора между включенным и выключенным."""

        self.work = not self.work
        if self.work:
            return f"Телевизор включен"
        else:
            return f"Телевизор выключен"

    def change_canal(self,canal_new):
        """Переключает каналы в случае если телевизор включен."""

        if self.work:
            if 1 <= canal_new <= 999:
                self.canal = canal_new
                return self.canal
            else:
                print("Указан неправильный номер канала.\nВедите новый номер канала.")
        else:
            print("Телевизор выключен, для выбора канала включите телевизор.")

    def change_volme(self, volume_new):
        """Изменяет режим громкости в случае если телевизор включен."""

        if self.work:
            if 0 <= self.volume <= 100:
                self.volume += volume_new
                return self.volume
            elif self.volume < 0:
                self.volume = 0
                return self.volume
            else:
                self.volume = 100
                return self.volume
        else:
            print("Телевизор выключен. Для регулирования громкости включите телевизор.")

    def check_in_status(self):
        """
        Выводит информацию о том, включен ли телевизор или нет,
        текущий канал, и уровень громкости.
        """
        return f"{self.turn_on()}, канал: {self.canal}, громкость: {self.volume_level}"

tv_1 = Television(canal=23, volume_level=100)
print(tv_1.check_in_status())
tv_1.turn_on()
print(tv_1.check_in_status())
tv_2 = Television(1, 12, 64)
print(tv_2.check_in_status())
tv_2.turn_on()
print(tv_2.check_in_status())
