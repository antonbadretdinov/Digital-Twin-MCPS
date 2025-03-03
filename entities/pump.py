

class Pump:
    def __init__(self, pump_id, status="off", speed=0, pressure=0, temperature=25, power=0):
        """
        Инициализация насоса.

        :param pump_id: Уникальный идентификатор насоса.
        :param status: Текущее состояние насоса ("on"/"off").
        :param speed: Скорость работы насоса (об/мин).
        :param pressure: Давление, создаваемое насосом (бар).
        :param temperature: Температура насоса (°C).
        :param power: Мощность насоса (кВт).
        """
        self.pump_id = pump_id
        self.status = status
        self.speed = speed
        self.pressure = pressure
        self.temperature = temperature
        self.power = power  # Мощность насоса

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
            self.power = 0  # При выключении мощность сбрасывается
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

    def set_power(self, power):
        """Установка мощности насоса."""
        if self.status == "on":
            self.power = power
            print(f"Мощность насоса {self.pump_id} установлена на {power} кВт.")
        else:
            print(f"Насос {self.pump_id} выключен. Сначала включите насос.")

    def get_power(self):
        """Получение текущей мощности насоса."""
        return self.power

    def __str__(self):
        """Возвращает строку состояния насоса."""
        return (f"Насос {self.pump_id}: Состояние={self.status}, "
                f"Скорость={self.speed} об/мин, Давление={self.pressure} бар, "
                f"Температура={self.temperature} °C")

# Пример использования
# pump = Pump(pump_id="P001")
# pump.turn_on()
# pump.set_power(15)
# print(f"Текущая мощность насоса: {pump.get_power()} кВт")
# print(pump)
# pump.turn_off()
# pump.set_power(10)
# print(pump)