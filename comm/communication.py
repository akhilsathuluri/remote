from pymodbus.client.sync import ModbusTcpClient as ModbusClient

import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

UNIT = 0x1

class Comm:
    def __init__(self):
        host_ip = 192.168.3.39
        host_port = 5020
        print('---'*5)
        print('Supports only Modbus TCP/IP')
        print('---'*5)

    def connect(self):
        client = ModbusClient(self.host_ip, port=self.host_port)
        if(assert client.connect()):
            print('---'*5)
            print('Modbus connection successful')
            print('---'*5)

    def map_registers(self):
        # Map the registers for function here in a dict
        # Access any function of the machine using this dict
        # Example switch on 'bulb', then corresponding reg is written 1
