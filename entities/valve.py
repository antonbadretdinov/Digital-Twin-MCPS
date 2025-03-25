from entities.component import Component


class Valve(Component):

    def __init__(self, valve_id, status="closed"):
        """
        Инициализация задвижки.

        :param valve_id: Уникальный идентификатор задвижки.
        :param status: Состояние ("open"/"closed").
        pressure_in: Давление на входе, кПа.
        pressure_out: Давление на выходе, кПа.
        """
        super().__init__(valve_id)
        self.status = status
        self.pressure_in = 0
        self.pressure_out = 0

    def open(self):
        """Открыть задвижку."""
        self.status = "open"
        self.pressure_out = self.pressure_in
        self.update_connected("pressure_in", self.pressure_out)


    def close(self):
        """Закрыть задвижку."""
        self.status = "closed"
        self.pressure_out = 0
        self.update_connected("pressure_in", self.pressure_out)