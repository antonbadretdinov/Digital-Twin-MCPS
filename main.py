from entities.pump import Pump

# насос
pump1 = Pump(pump_id="P001")
print(pump1)
pump1.turn_on()
pump1.set_speed(1500)
pump1.set_pressure(10)
pump1.update_temperature(30)
print(pump1)
pump1.turn_off()
print(pump1)