import asyncio
import logging
from asyncua import Client, ua

logging.basicConfig(level=logging.WARNING)
_logger = logging.getLogger('asyncua')


async def main():
    client = Client(
        url="opc.tcp://192.168.56.1:4840/Objects/DeviceSet/CODESYS Control Win V3/Resources/Application/Programs",
        timeout=4)

    try:
        await client.connect()
        print("connected")
        testNode = client.get_node("ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.iVar")
        value = testNode.get_value
        print("Node value:", value)
    except Exception as e:
        print(e)
        return

    '''
    clientcode!

    '''

    try:
        await client.disconnect()
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    asyncio.run(main())

# # насос
# pump_example = Pump(pump_id="P001")
# print(pump_example)
# pump_example.turn_on()
# pump_example.set_power(15)
# print(f"Текущая мощность насоса: {pump_example.get_power()} кВт")
# pump_example.set_speed(1500)
# pump_example.set_pressure(10)
# pump_example.update_temperature(30)
# print(pump_example)
# pump_example.turn_off()
# pump_example.set_power(10)
# print(pump_example)
