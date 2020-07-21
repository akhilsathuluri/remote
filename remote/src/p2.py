from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

client = ModbusClient('127.0.0.1', port=502)
client.connect()
UNIT = 1

while True:
    # rr = client.read_holding_registers(1, 1, unit=UNIT)
    rq = client.write_registers(1, 100, unit=UNIT)
    # print(rr.registers[0])
    time.sleep(1)
