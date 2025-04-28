class OPCMapping:
    def __init__(self, pump, valve):
        self.pump = pump
        self.valve = valve
        self.temperature_zones = [0.0] * 5  # Для T_1_n - T_5_n

    def update_from_opc(self, data):
        """Обновление состояния из OPC-данных"""
        # Насос NA2
        if 'NA2_AI_P_Oil_Nas_n' in data:
            self.pump.oil_pressure = data['NA2_AI_P_Oil_Nas_n']

        if 'NA2_AI_Qmom_n' in data:
            self.pump.flow_rate = data['NA2_AI_Qmom_n']

        if 'na2_pressure_in' in data:
            self.pump.pressure_in = data['na2_pressure_in']

        if 'na2_pressure_out' in data:
            self.pump.pressure_out = data['na2_pressure_out']

        # Задвижки
        if data.get('NA2_CMD_Zadv_Open'):
            self.valve.open()
        elif data.get('NA2_CMD_Zadv_Close'):
            self.valve.close()

        # Температуры
        for i in range(1, 6):
            if f'NA2_AI_T_{i}_n' in data:
                self.temperature_zones[i - 1] = data[f'NA2_AI_T_{i}_n']

        # Состояния
        if data.get('na2_on'):
            self.pump.turn_on()
        elif data.get('na2_off'):
            self.pump.turn_off()