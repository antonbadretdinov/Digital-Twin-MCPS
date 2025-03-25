from entities.component import Component


class Pump(Component):
    def __init__(self, pump_id, status="off", speed=0, pressure_in=0, pressure_out=0,
                 temperature_in=25, temperature_out=30, power=0, efficiency=0.8,
                 flow_rate=0, k_expansion=0.01, f_vib=0):
        """
        Инициализация насоса с поддержкой подключений к другим компонентам.

        :param pump_id: Уникальный идентификатор насоса.
        :param status: Состояние ("on"/"off").
        :param speed: Скорость вращения (об/мин).
        :param pressure_in: Давление на входе (кПа).
        :param pressure_out: Давление на выходе (кПа).
        :param temperature_in: Температура на входе (°C).
        :param temperature_out: Температура на выходе (°C).
        :param power: Мощность (кВт).
        :param efficiency: КПД насоса (0..1).
        :param flow_rate: Расход (м³/ч).
        :param k_expansion: Коэф. теплового расширения вала (мм/°C).
        :param f_vib: Влияние вибраций (мм).
        """
        super().__init__(pump_id)
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
        """Включение насоса с оповещением системы."""
        if self.status == "off":
            self.status = "on"
            print(f"Насос {self.component_id} включен.")
            # При включении обновляем давление на выходе
            self.calculate_pressure_out()
        else:
            print(f"Насос {self.component_id} уже включен.")

    def turn_off(self):
        """Выключение насоса с обнулением параметров."""
        if self.status == "on":
            self.status = "off"
            self.speed = 0
            self.pressure_out = 0
            self.power = 0
            self.flow_rate = 0
            print(f"Насос {self.component_id} выключен.")
            # Оповещаем подключенные компоненты об обнулении давления
            self.update_connected("pressure_in", 0)
        else:
            print(f"Насос {self.component_id} уже выключен.")

    def calculate_pressure_out(self):
        """Расчет давления на выходе с автоматическим обновлением системы."""
        if self.status == "on":
            self.pressure_out = self.pressure_in + (self.efficiency * self.power) / max(self.flow_rate, 0.001)
            print(f"Давление на выходе насоса {self.component_id}: {self.pressure_out} кПа")
            # Автоматическое обновление подключенных компонентов
            self.update_connected("pressure_in", self.pressure_out)
            return self.pressure_out
        else:
            print(f"Насос {self.component_id} выключен. Невозможно рассчитать давление.")
            return 0

    def calculate_power(self):
        """Расчет мощности насоса."""
        if self.status == "on":
            delta_p = self.pressure_out - self.pressure_in
            self.power = delta_p * self.flow_rate
            print(f"Мощность насоса {self.component_id}: {self.power} кВт")
            return self.power
        else:
            print(f"Насос {self.component_id} выключен. Невозможно рассчитать мощность.")
            return 0

    def calculate_shaft_shift(self):
        """Расчет осевого сдвига вала."""
        if self.status == "on":
            delta_t = self.temperature_out - self.temperature_in
            shaft_shift = self.k_expansion * delta_t + self.f_vib
            print(f"Сдвиг вала насоса {self.component_id}: {shaft_shift} мм")
            return shaft_shift
        else:
            print(f"Насос {self.component_id} выключен. Невозможно рассчитать сдвиг вала.")
            return 0

    def set_flow_rate(self, flow_rate):
        """Установка расхода с пересчетом параметров."""
        self.flow_rate = flow_rate
        if self.status == "on":
            self.calculate_power()
            self.calculate_pressure_out()
        print(f"Расход насоса {self.component_id} установлен: {flow_rate} м³/ч")

    def update_temperature(self, temp_in, temp_out):
        """Обновление температурных параметров."""
        self.temperature_in = temp_in
        self.temperature_out = temp_out
        print(f"Температуры насоса {self.component_id} обновлены: вход={temp_in}°C, выход={temp_out}°C")
        self.calculate_shaft_shift()

    def __str__(self):
        """Строковое представление состояния насоса."""
        return (f"Насос {self.component_id}: [Статус: {self.status}, "
                f"Давление: вход={self.pressure_in} кПа, выход={self.pressure_out} кПа, "
                f"Мощность: {self.power} кВт, Расход: {self.flow_rate} м³/ч, "
                f"Температура: вход={self.temperature_in}°C, выход={self.temperature_out}°C]")