class InletCollector:
    def __init__(self, collector_id, psource=0, pin=0):
        """
        Инициализация приемного коллектора.

        :param collector_id: Уникальный идентификатор коллектора.
        :param psource: Давление в магистральном трубопроводе, кПа.
        :param pin: Давление на входе насоса, кПа.
        """
        self.collector_id = collector_id
        self.psource = psource
        self.pin = pin

    def calculate_pressure_drop(self):
        """Расчет перепада давления на коллекторе."""
        pcol = self.psource - self.pin
        print(f"Перепад давления на коллекторе {self.collector_id}: {pcol} кПа")
        return pcol

    def update_psource(self, psource):
        """Обновление давления в магистральном трубопроводе."""
        self.psource = psource
        print(f"Давление в магистрали (Psource) коллектора {self.collector_id} обновлено: {psource} кПа.")

    def update_pin(self, pin):
        """Обновление давления на входе насоса."""
        self.pin = pin
        print(f"Давление на входе насоса (Pin) коллектора {self.collector_id} обновлено: {pin} кПа.")

    def __str__(self):
        """Возвращает строку состояния коллектора."""
        return (f"Приемный коллектор {self.collector_id}: Psource={self.psource} кПа, "
                f"Pin={self.pin} кПа, Pcol={self.calculate_pressure_drop()} кПа")