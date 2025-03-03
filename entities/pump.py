
class Pump:
    def __init__(self, pump_id, capacity=100, efficiency=0.8, status="off", speed=0, pressure=0, temperature=25, power=0):
        """
        Инициализация насоса.

        :param pump_id: Уникальный идентификатор насоса.
        :param capacity: Номинальная производительность насоса (например, м3/ч).
        :param efficiency: КПД насоса (от 0 до 1).
        :param status: Текущее состояние насоса ("on"/"off").
        :param speed: Скорость работы насоса (об/мин).
        :param pressure: Давление, создаваемое насосом (бар).
        :param temperature: Температура насоса (°C).
        :param power: Мощность насоса (кВт).
        """
        self.pump_id = pump_id
        self.capacity = capacity
        self.efficiency = efficiency
        self.status = status
        self.speed = speed
        self.pressure = pressure
        self.temperature = temperature
        self.power = power  # Мощность насоса

    def turn_on(self):
        """Включение насоса."""
        if self.status == "off":
            self.status = "on"
            #  При включении можно предусмотреть плавный пуск, 
            # например, постепенное увеличение скорости
            self.speed = 10  # Начальная скорость при включении
            self.update_power()
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
            self.update_pressure() #обновляем давление при изменении скорости
            self.update_power()    #и мощность
            print(f"Скорость насоса {self.pump_id} установлена на {speed} об/мин.")
        else:
            print(f"Насос {self.pump_id} выключен. Сначала включите насос.")

    def set_pressure(self, pressure):
        """Установка давления насоса."""
        if self.status == "on":
            self.pressure = pressure
            # При изменении давления, возможно потребуется корректировка скорости и мощности.
            # В реальной системе они взаимосвязаны.
            self.update_speed()   #обновляем скорость если изменили давление (может быть и нет)
            self.update_power()    #и мощность
            print(f"Давление насоса {self.pump_id} установлено на {pressure} бар.")
        else:
            print(f"Насос {self.pump_id} выключен. Сначала включите насос.")

    def update_temperature(self, temperature):
        """Обновление температуры насоса."""
        self.temperature = temperature
        print(f"Температура насоса {self.pump_id} обновлена до {temperature} °C.")

    def update_power(self):
        """Обновление мощности насоса на основе скорости и давления."""
        #  В реальной системе мощность зависит от множества факторов.
        #  Это упрощенная модель
        self.power = (self.pressure * self.speed / 1000) / self.efficiency  # Примерная формула
        print(f"Мощность насоса {self.pump_id} обновлена до {self.power:.2f} кВт.")

    def update_speed(self):
        '''Обновляет скорость, в зависимости от давления.
        В данной модели скорость меняется линейно, в реальности, конечно же, это будет не так'''
        self.speed = self.pressure * 10
        print(f"Скорость насоса {self.pump_id} обновлена до {self.speed:.2f} об/мин.")
    
    def update_pressure(self):
        '''Обновляет давление, в зависимости от скорости.
        В данной модели скорость меняется линейно, в реальности, конечно же, это будет не так'''
        self.pressure = self.speed / 10
        print(f"Давление насоса {self.pump_id} обновлена до {self.pressure:.2f} бар.")


    def get_power(self):
        """Получение текущей мощности насоса."""
        return self.power

    def __str__(self):
        """Возвращает строку состояния насоса."""
        return (f"Насос {self.pump_id}: Состояние={self.status}, "
                f"Скорость={self.speed} об/мин, Давление={self.pressure} бар, "
                f"Температура={self.temperature} °C, Мощность={self.power:.2f} кВт, "
                f"Производительность={self.capacity} м3/ч, КПД={self.efficiency}")