class Motor:
    def __init__(self, motor_id, power_rating, efficiency=0.9, status="off", speed=0, temperature=25):
        """
        Инициализация двигателя.

        :param motor_id: Уникальный идентификатор двигателя.
        :param power_rating: Номинальная мощность двигателя (кВт).
        :param efficiency: КПД двигателя (от 0 до 1).
        :param status: Текущее состояние двигателя ("on"/"off").
        :param speed: Скорость вращения двигателя (об/мин).
        :param temperature: Температура двигателя (°C).
        """
        self.motor_id = motor_id
        self.power_rating = power_rating
        self.efficiency = efficiency
        self.status = status
        self.speed = speed
        self.temperature = temperature

    def turn_on(self):
        """Включение двигателя."""
        if self.status == "off":
            self.status = "on"
            self.speed = 100 #начальная скорость
            print(f"Двигатель {self.motor_id} включен.")
        else:
            print(f"Двигатель {self.motor_id} уже включен.")

    def turn_off(self):
        """Выключение двигателя."""
        if self.status == "on":
            self.status = "off"
            self.speed = 0
            print(f"Двигатель {self.motor_id} выключен.")
        else:
            print(f"Двигатель {self.motor_id} уже выключен.")

    def set_speed(self, speed):
        """Установка скорости вращения двигателя."""
        if self.status == "on":
            self.speed = speed
            print(f"Скорость двигателя {self.motor_id} установлена на {speed} об/мин.")
        else:
            print(f"Двигатель {self.motor_id} выключен. Сначала включите двигатель.")

    def update_temperature(self, temperature):
        """Обновление температуры двигателя."""
        self.temperature = temperature
        print(f"Температура двигателя {self.motor_id} обновлена до {temperature} °C.")

    def get_power_consumption(self):
        """Расчет потребляемой мощности двигателя (кВт)."""
        #  В реальной системе формула будет сложнее
        if self.status == "on":
            return self.power_rating * (self.speed / 1000) / self.efficiency  # Примерная формула
        else:
            return 0

    def __str__(self):
        """Возвращает строку состояния двигателя."""
        return (f"Двигатель {self.motor_id}: Состояние={self.status}, "
                f"Скорость={self.speed} об/мин, Температура={self.temperature} °C, "
                f"Номинальная мощность={self.power_rating} кВт, КПД={self.efficiency}")