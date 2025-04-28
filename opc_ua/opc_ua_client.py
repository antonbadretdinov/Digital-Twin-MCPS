from opcua import Client
import time
from threading import Thread

from digital_twin_system import DigitalTwinSystem


class OPCUAClient:
    def __init__(self, endpoint, digital_twin_system):
        """
        :param endpoint: URL OPC UA сервера (opc.tcp://host:port)
        :param digital_twin_system: Объект цифрового двойника
        """
        self.client = Client(endpoint)
        self.dt = digital_twin_system
        self._running = False
        self.subscriptions = {}

    def connect(self):
        try:
            self.client.connect()
            print("Успешное подключение к OPC UA серверу")
            self._running = True
            self._setup_subscriptions()
        except Exception as e:
            print(f"Ошибка подключения: {str(e)}")

    def _setup_subscriptions(self):
        """Настройка подписок на важные узлы"""
        self.subscription = self.client.create_subscription(500, self._data_change_handler)

        # Подписки для насосной станции NA2
        nodes = {
            'NA2_Pressure_In': 'ns=2;s=na2_pressure_in',
            'NA2_Pressure_Out': 'ns=2;s=na2_pressure_out',
            'NA2_Flow_Rate': 'ns=2;s=NA2_AI_Qmom_n',
            'NA2_Valve_Cmd_Open': 'ns=2;s=NA2_CMD_Zadv_Open',
            'NA2_Valve_Cmd_Close': 'ns=2;s=NA2_CMD_Zadv_Close',
            'NA2_Pump_On': 'ns=2;s=na2_on',
            'NA2_Pump_Off': 'ns=2;s=na2_off'
        }

        for name, node_id in nodes.items():
            try:
                node = self.client.get_node(node_id)
                handle = self.subscription.subscribe_data_change(node)
                self.subscriptions[name] = handle
                print(f"Подписка на {name} ({node_id})")
            except Exception as e:
                print(f"Ошибка подписки на {node_id}: {str(e)}")

    def _data_change_handler(self, node, val, data):
        """Обработчик изменений данных"""
        node_id = node.nodeid.to_string()
        print(f"Обновление: {node_id} = {val}")

        # Обработка критических команд в первую очередь
        if 'NA2_CMD_Zadv_Open' in node_id and val:
            self.dt.valve_na2.open()
        elif 'NA2_CMD_Zadv_Close' in node_id and val:
            self.dt.valve_na2.close()
        elif 'na2_on' in node_id and val:
            self.dt.pump_na2.turn_on()
        elif 'na2_off' in node_id and val:
            self.dt.pump_na2.turn_off()

        # Обновление аналоговых значений
        elif 'na2_pressure_in' in node_id:
            self.dt.pump_na2.pressure_in = float(val)
        elif 'na2_pressure_out' in node_id:
            self.dt.pump_na2.pressure_out = float(val)
        elif 'NA2_AI_Qmom_n' in node_id:
            self.dt.pump_na2.flow_rate = float(val)

    def start_background_monitoring(self):
        """Запуск мониторинга в фоновом потоке"""
        self.monitor_thread = Thread(target=self._monitor_loop)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def _monitor_loop(self):
        """Цикл мониторинга"""
        while self._running:
            try:
                # Чтение дополнительных параметров по таймеру
                self._read_temperatures()
                time.sleep(1)
            except Exception as e:
                print(f"Ошибка мониторинга: {str(e)}")
                time.sleep(5)

    def _read_temperatures(self):
        """Ручное чтение температурных зон"""
        for i in range(1, 6):
            try:
                node = self.client.get_node(f'ns=2;s=NA2_AI_T_{i}_n')
                temp = node.get_value()
                self.dt.pump_na2.temperature_zones[i - 1] = float(temp)
            except Exception as e:
                print(f"Ошибка чтения температуры T_{i}: {str(e)}")

    def disconnect(self):
        """Корректное отключение"""
        self._running = False
        if hasattr(self, 'monitor_thread'):
            self.monitor_thread.join()
        self.client.disconnect()
        print("Отключение от OPC UA сервера")


# Пример использования
if __name__ == "__main__":

    # Инициализация цифрового двойника
    dt_system = DigitalTwinSystem()

    # Подключение к OPC UA серверу
    opc_client = OPCUAClient("opc.tcp://10.0.0.100:4840", dt_system)
    opc_client.connect()
    opc_client.start_background_monitoring()

    try:
        while True:
            # Основной цикл может выполнять другие задачи
            time.sleep(1)
    except KeyboardInterrupt:
        opc_client.disconnect()