from entities.pump import Pump

# насос
pump_example = Pump(pump_id="P001")
print(pump_example)
pump_example.turn_on()
pump_example.set_power(15)
print(f"Текущая мощность насоса: {pump_example.get_power()} кВт")
pump_example.set_speed(1500)
pump_example.set_pressure(10)
pump_example.update_temperature(30)
print(pump_example)
pump_example.turn_off()
pump_example.set_power(10)
print(pump_example)

#типа алгоритм вот