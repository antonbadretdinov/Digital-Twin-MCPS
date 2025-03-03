class Tank:
    def __init__(self, tank_id, capacity, initial_level=0):
        """
        Инициализация резервуара.

        :param tank_id: Уникальный идентификатор резервуара.
        :param capacity: Объем резервуара (м3).
        :param initial_level: Начальный уровень жидкости в резервуаре (м3).
        """
        self.tank_id = tank_id
        self.capacity = capacity
        self.level = initial_level

    def add_liquid(self, volume):
        """Добавление жидкости в резервуар."""
        if self.level + volume <= self.capacity:
            self.level += volume
            print(f"В резервуар {self.tank_id} добавлено {volume} м3 жидкости. Текущий уровень: {self.level} м3.")
        else:
            print(f"Невозможно добавить {volume} м3 в резервуар {self.tank_id}. Превышен максимальный объем.")
            self.level = self.capacity

    def remove_liquid(self, volume):
        """Удаление жидкости из резервуара."""
        if self.level - volume >= 0:
            self.level -= volume
            print(f"Из резервуара {self.tank_id} удалено {volume} м3 жидкости. Текущий уровень: {self.level} м3.")
        else:
            print(f"Невозможно удалить {volume} м3 из резервуара {self.tank_id}. Недостаточно жидкости.")
            self.level = 0

    def get_level(self):
        """Получение текущего уровня жидкости в резервуаре."""
        return self.level

    def __str__(self):
        """Возвращает строку состояния резервуара."""
        return f"Резервуар {self.tank_id}: Объем={self.capacity} м3, Текущий уровень={self.level} м3"