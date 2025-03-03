

class Pump:
    def __init__(self, pump_id, status="off", speed=0, pressure=0, temperature=25):
        """
        Инициализация насоса.

        :param pump_id: Уникальный идентификатор насоса.
        :param status: Текущее состояние насоса ("on"/"off").
        :param speed: Скорость работы насоса (об/мин).
        :param pressure: Давление, создаваемое насосом (бар).
        :param temperature: Температура насоса (°C).
        """
        self.pump_id = pump_id
        self.status = status
        self.speed = speed
        self.pressure = pressure
        self.temperature = temperature

    def turn_on(self):
        """Включение насоса."""
        if self.status == "off":
            self.status = "on"
            print(f"Насос {self.pump_id} включен.")
        else:
            print(f"Насос {self.pump_id} уже включен.")

    def turn_off(self):
        """Выключение насоса."""
        if self.status == "on":
            self.status = "off"
            self.speed = 0
            self.pressure = 0
            print(f"Насос {self.pump_id} выключен.")
        else:
            print(f"Насос {self.pump_id} уже выключен.")

    def set_speed(self, speed):
        """Установка скорости насоса."""
        if self.status == "on":
            self.speed = speed
            print(f"Скорость насоса {self.pump_id} установлена на {speed} об/мин.")
        else:
            print(f"Насос {self.pump_id} выключен. Сначала включите насос.")

    def set_pressure(self, pressure):
        """Установка давления насоса."""
        if self.status == "on":
            self.pressure = pressure
            print(f"Давление насоса {self.pump_id} установлено на {pressure} бар.")
        else:
            print(f"Насос {self.pump_id} выключен. Сначала включите насос.")

    def update_temperature(self, temperature):
        """Обновление температуры насоса."""
        self.temperature = temperature
        print(f"Температура насоса {self.pump_id} обновлена до {temperature} °C.")

    def __str__(self):
        """Возвращает строку состояния насоса."""
        return (f"Насос {self.pump_id}: Состояние={self.status}, "
                f"Скорость={self.speed} об/мин, Давление={self.pressure} бар, "
                f"Температура={self.temperature} °C")

# Пример использования
# pump1 = Pump(pump_id="P001")
# print(pump1)
# pump1.turn_on()
# pump1.set_speed(1500)
# pump1.set_pressure(10)
# pump1.update_temperature(30)
# print(pump1)
# pump1.turn_off()
# print(pump1)