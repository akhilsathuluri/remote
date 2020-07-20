from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
import os
import pandas as pd

FORMAT = ('%(asctime)-15s %(threadName)-15s'
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

class Comm:
    def __init__(self):
        # self.host_ip = '192.168.3.39'
        self.host_ip = '127.0.0.1'
        self.host_port = '502'
        self.unit = 0x1
        self.connection_status = False
        print('---'*5)
        print('Supports only Modbus TCP/IP for now')
        print('---'*5)

    def connect(self):
        self.client = ModbusClient(self.host_ip, port=self.host_port)
        self.connection_status = self.client.connect()
        if self.connection_status != True:
                raise AssertionError("Failed to connect with the host, ip = {}, port = {} due to error logged above"\
                .format(self.host_ip, self.host_port))
        print('---'*5)
        print('Modbus connection successful')
        print('---'*5)

    def load_register_map(self):
        # Map the registers for function here in a dict
        # Access any function of the machine using this dict
        # Example switch on 'bulb', then corresponding reg is written 1
        register_map = 'comm\mapping.xlsx'
        assert os.path.isfile(register_map), \
        "The mapping data should be present in {},\n in .xlsx file format"\
        .format('.\comm\mapping.xlsx')
        map = pd.read_excel(register_map)
        print('---'*5)
        print('Loaded register map successfully')
        print('---'*5)
        return map
