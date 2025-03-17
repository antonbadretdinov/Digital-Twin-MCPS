

class Pump:
    def __init__(self, pump_id, status="off", speed=0, pressure_in=0, pressure_out=0, temperature_in=25, temperature_out=30, power=0, efficiency=0.8, flow_rate=0, k_expansion=0.01, f_vib=0):
        """
        Инициализация насоса.

        :param pump_id: Уникальный идентификатор насоса.
        :param status: Текущее состояние насоса ("on"/"off").
        :param speed: Скорость работы насоса (об/мин).
        :param pressure_in: Давление на входе насоса, кПа.
        :param pressure_out: Давление на выходе насоса, кПа.
        :param temperature_in: Температура воды на входе насоса, °C.
        :param temperature_out: Температура воды на выходе насоса, °C.
        :param power: Мощность насоса, кВт.
        :param efficiency: КПД насоса (безразмерная величина, 0–1).
        :param flow_rate: Расход жидкости через насос, м³/ч.
        :param k_expansion: Коэффициент теплового расширения вала, мм/°C.
        :param f_vib: Влияние вибраций на сдвиг вала, мм.
        """
        self.pump_id = pump_id
        self.status = status
        self.speed = speed
        self.pressure_in = pressure_in
        self.pressure_out = pressure_out
        self.temperature_in = temperature_in
        self.temperature_out = temperature_out
        self.power = power
        self.efficiency = efficiency
        self.flow_rate = flow_rate
        self.k_expansion = k_expansion
        self.f_vib = f_vib

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
            self.pressure_out = 0
            self.power = 0
            self.flow_rate = 0
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

    def set_flow_rate(self, flow_rate):
        """Установка расхода жидкости через насос."""
        if self.status == "on":
            self.flow_rate = flow_rate
            print(f"Расход жидкости через насос {self.pump_id} установлен на {flow_rate} м³/ч.")
        else:
            print(f"Насос {self.pump_id} выключен. Сначала включите насос.")

    def calculate_pressure_out(self):
        """Расчет давления на выходе насоса."""
        if self.status == "on":
            self.pressure_out = self.pressure_in + (self.efficiency * self.power) / self.flow_rate
            print(f"Давление на выходе насоса {self.pump_id} рассчитано: {self.pressure_out} кПа.")
        else:
            print(f"Насос {self.pump_id} выключен. Невозможно рассчитать давление.")

    def calculate_power(self):
        """Расчет мощности насоса."""
        if self.status == "on":
            delta_p = self.pressure_out - self.pressure_in
            self.power = delta_p * self.flow_rate
            print(f"Мощность насоса {self.pump_id} рассчитана: {self.power} кВт.")
        else:
            print(f"Насос {self.pump_id} выключен. Невозможно рассчитать мощность.")

    def calculate_shaft_shift(self):
        """Расчет осевого сдвига вала."""
        if self.status == "on":
            delta_t = self.temperature_out - self.temperature_in
            shaft_shift = self.k_expansion * delta_t + self.f_vib
            print(f"Осевой сдвиг вала насоса {self.pump_id} рассчитан: {shaft_shift} мм.")
            return shaft_shift
        else:
            print(f"Насос {self.pump_id} выключен. Невозможно рассчитать сдвиг вала.")
            return 0

    def update_temperature_in(self, temperature_in):
        """Обновление температуры на входе насоса."""
        self.temperature_in = temperature_in
        print(f"Температура на входе насоса {self.pump_id} обновлена до {temperature_in} °C.")

    def update_temperature_out(self, temperature_out):
        """Обновление температуры на выходе насоса."""
        self.temperature_out = temperature_out
        print(f"Температура на выходе насоса {self.pump_id} обновлена до {temperature_out} °C.")

    def __str__(self):
        """Возвращает строку состояния насоса."""
        return (f"Насос {self.pump_id}: Состояние={self.status}, "
                f"Скорость={self.speed} об/мин, Давление на входе={self.pressure_in} кПа, "
                f"Давление на выходе={self.pressure_out} кПа, Температура на входе={self.temperature_in} °C, "
                f"Температура на выходе={self.temperature_out} °C, Мощность={self.power} кВт, "
                f"Расход={self.flow_rate} м³/ч, КПД={self.efficiency}")


# Пример использования
# pump = Pump(pump_id="P001", efficiency=0.85, k_expansion=0.01, f_vib=0.1)
# pump.turn_on()
# pump.set_flow_rate(10)  # Установка расхода жидкости
# pump.pressure_in = 100  # Давление на входе
# pump.calculate_power()  # Расчет мощности
# pump.calculate_pressure_out()  # Расчет давления на выходе
# shaft_shift = pump.calculate_shaft_shift()  # Расчет осевого сдвига вала
# print(pump)
# pump.turn_off()