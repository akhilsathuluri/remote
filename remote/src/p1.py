from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

client = ModbusClient('127.0.0.1', port=502)
client.connect()
UNIT = 1
i = 0
while True:
    # i = i+1
    rq = client.write_registers(1, 0, unit=UNIT)
    time.sleep(1)
