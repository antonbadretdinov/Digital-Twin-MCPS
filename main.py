from entities.pump import Pump
from entities.motor import Motor
from entities.valve import Valve
from entities.tank import Tank

pump1 = Pump(pump_id="P001", capacity=120, efficiency=0.75)
motor1 = Motor(motor_id="M001", power_rating=20)
valve1 = Valve(valve_id="V001", valve_type="gate")
tank1 = Tank(tank_id="T001", capacity=500, initial_level=100)
# Включение насоса и двигателя
pump1.turn_on()
motor1.turn_on()
# Установка скорости насоса
pump1.set_speed(1500)
# Открытие клапана
valve1.open_valve(50)
 # Расчет расхода через клапан (условно, разница давлений 2 бара)
flow_rate = valve1.get_flow_rate(2)
print(f"Расход через клапан: {flow_rate:.2f} м3/ч")
# Добавление жидкости в резервуар
tank1.add_liquid(flow_rate)

# Вывод информации об объектах
print(pump1)
print(motor1)
print(valve1)
print(tank1)
    # Выключение насоса и двигателя
pump1.turn_off()
motor1.turn_off()

    # Закрытие клапана
valve1.close_valve()

print(pump1)
print(motor1)
print(valve1)
print(tank1)