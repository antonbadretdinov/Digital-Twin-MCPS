from entities.component import Component


class Pipe(Component):

    def __init__(self, component_id, pressure_in=0, pressure_out=0, flow_rate=0):
        """
        Инициализация трубы.

        :param component_id: Уникальный идентификатор трубы.
        :param pressure_in: Давление на входе трубы, кПа.
        :param pressure_out: Давление на выходе трубы, кПа.
        :param flow_rate: Расход жидкости через трубу, м³/ч.
        """
        super().__init__(component_id)  # Передаем component_id в родительский класс
        self.pressure_in = pressure_in
        self.pressure_out = pressure_out
        self.flow_rate = flow_rate


    def update_pressure(self, pressure_in):
        """Обновление давления на входе и выходе трубы (без потерь)."""
        self.pressure_in = pressure_in
        self.pressure_out = pressure_in  # Упрощенная модель без потерь
        self.update_connected("pressure_in", self.pressure_out)


    def set_flow_rate(self, flow_rate):
        """Установка расхода жидкости через трубу."""
        self.flow_rate = flow_rate
        print(f"Расход жидкости через трубу установлен на {flow_rate} м³/ч.")

    def __str__(self):
        """Возвращает строку состояния трубы."""
        return (f"Труба: Давление на входе={self.pressure_in} кПа, "
                f"Давление на выходе={self.pressure_out} кПа, Расход={self.flow_rate} м³/ч")