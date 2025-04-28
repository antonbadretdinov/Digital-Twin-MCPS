from entities.pipe import Pipe
from entities.pump import Pump
from entities.valve import Valve


class DigitalTwinSystem:
    def __init__(self):
        # Инициализация компонентов NA2
        self.pump_na2 = Pump(
            pump_id="NA2",
            efficiency=0.85,
            k_expansion=0.01
        )
        self.valve_na2 = Valve(valve_id="NA2_valve")
        self.pipe_na2 = Pipe(component_id="NA2_pipe")

        # Инициализация компонентов NA4 (аналогично)
        self.pump_na4 = Pump(pump_id="NA4")
        self.valve_na4 = Valve(valve_id="NA4_valve")

        # Настройка соединений
        self._connect_components()

        # Текущие аварийные состояния
        self.alarms = {
            'oil_pressure_low': False,
            'overheating': False
        }

    def _connect_components(self):
        """Связывание компонентов в систему"""
        self.pump_na2.connect(self.pipe_na2)
        self.pipe_na2.connect(self.valve_na2)

        self.pump_na4.connect(self.pipe_na4)
        # ... другие соединения

    def emergency_stop(self):
        """Аварийная остановка всей системы"""
        self.pump_na2.turn_off()
        self.pump_na4.turn_off()
        self.valve_na2.close()
        self.valve_na4.close()
        print("!!! АВАРИЙНАЯ ОСТАНОВКА !!!")

    def update_alarms(self):
        """Проверка аварийных состояний"""
        # Проверка давления масла
        if self.pump_na2.oil_pressure < 10:
            self.alarms['oil_pressure_low'] = True

        # Проверка перегрева (макс. из 5 температурных зон)
        max_temp = max(self.pump_na2.temperature_out)
        if max_temp > 90:
            self.alarms['overheating'] = True
            self.emergency_stop()