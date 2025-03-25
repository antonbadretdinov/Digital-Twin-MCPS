from entities.pipe import Pipe
from entities.pump import Pump
from entities.valve import Valve

# Создание и подключение компонентов
pump = Pump(pump_id="P001", efficiency=0.85)
pipe = Pipe(component_id="Pipe1")
valve = Valve(valve_id="V001")

pump.connect(pipe)  # Насос -> Труба
pipe.connect(valve)  # Труба -> Задвижка

# Работа системы
pump.turn_on()
pump.set_flow_rate(10)      # Автоматически рассчитает power/pressure_out
pump.pressure_in = 100      # Давление на входе
pump.calculate_pressure_out()  # Обновит давление в подключенной трубе