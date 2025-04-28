from entities.opc_mapping import OPCMapping
from entities.pump import Pump
from entities.valve import Valve

# Инициализация системы
pump_na2 = Pump(pump_id="NA2")
valve_na2 = Valve(valve_id="NA2_valve")
opc_mapping = OPCMapping(pump_na2, valve_na2)

# Эмуляция данных от OPC сервера
opc_data = {
    'NA2_AI_P_Oil_Nas_n': 15.2,
    'NA2_AI_Qmom_n': 10.5,
    'na2_pressure_in': 150,
    'NA2_CMD_Zadv_Open': True,
    'na2_on': True
}

# Обновление цифрового двойника
opc_mapping.update_from_opc(opc_data)

# Проверка состояния
print(f"Насос NA2: {'Вкл' if pump_na2.status == 'on' else 'Выкл'}")
print(f"Задвижка: {valve_na2.status}")
print(f"Давление масла: {pump_na2.pressure_out} бар")
