class OutletCollector:
    def __init__(self, collector_id, p_out=0, p_target=0):
        """
        Инициализация выходного коллектора.

        :param collector_id: Уникальный идентификатор коллектора.
        :param p_out: Давление на выходе насоса, кПа.
        :param p_target: Давление в магистральном трубопроводе, кПа.
        """
        self.collector_id = collector_id
        self.p_out = p_out      # Давление от насоса
        self.p_target = p_target  # Давление в магистрали

    def calculate_pressure_drop(self):
        """Расчет перепада давления на выходном коллекторе."""
        delta_p = self.p_out - self.p_target
        print(f"Перепад давления на выходном коллекторе {self.collector_id}: {delta_p} кПа")
        return delta_p

    def update_p_out(self, p_out):
        """Обновление давления на выходе насоса."""
        self.p_out = p_out
        print(f"Давление на выходе насоса (Pout) коллектора {self.collector_id} обновлено: {p_out} кПа.")

    def update_p_target(self, p_target):
        """Обновление целевого давления в магистрали."""
        self.p_target = p_target
        print(f"Давление в магистрали (Ptarget) коллектора {self.collector_id} обновлено: {p_target} кПа.")

    def __str__(self):
        """Возвращает строку состояния коллектора."""
        return (f"Выходной коллектор {self.collector_id}: Pout={self.p_out} кПа, "
                f"Ptarget={self.p_target} кПа, ΔPcol_out={self.calculate_pressure_drop()} кПа")