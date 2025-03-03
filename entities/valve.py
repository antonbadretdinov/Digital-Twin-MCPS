class Valve:
    def __init__(self, valve_id, valve_type="gate", position=0):
        """
        Инициализация клапана.

        :param valve_id: Уникальный идентификатор клапана.
        :param valve_type: Тип клапана (например, "gate", "ball", "butterfly").
        :param position: Положение клапана (от 0 до 100, где 0 - закрыт, 100 - открыт).
        """
        self.valve_id = valve_id
        self.valve_type = valve_type
        self.position = position

    def open_valve(self, percentage):
        """Открытие клапана на заданный процент."""
        if 0 <= percentage <= 100:
            self.position = percentage
            print(f"Клапан {self.valve_id} открыт на {percentage}%.")
        else:
            print("Недопустимое значение процента открытия клапана (0-100).")

    def close_valve(self):
        """Закрытие клапана."""
        self.position = 0
        print(f"Клапан {self.valve_id} закрыт.")

    def get_flow_rate(self, pressure_difference, flow_coefficient=0.5):
        """
        Расчет расхода через клапан.

        :param pressure_difference: Разница давлений на клапане (бар).
        :param flow_coefficient: Коэффициент расхода клапана.
        :return: Расход через клапан (м3/ч).
        """
        #  Это очень упрощенная модель
        if self.position > 0:
            flow_rate = flow_coefficient * self.position / 100 * (pressure_difference**0.5)
            return flow_rate
        else:
            return 0

    def __str__(self):
        """Возвращает строку состояния клапана."""
        return f"Клапан {self.valve_id}: Тип={self.valve_type}, Положение={self.position}%"