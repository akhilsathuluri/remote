from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
import os
import pandas as pd

# FORMAT = ('%(asctime)-15s %(threadName)-15s'
#           '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
# logging.basicConfig(format=FORMAT)
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)

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
                raise AssertionError("Failed to connect with the host, ip = {}, port = {}"\
                .format(self.host_ip, self.host_port))
        print('---'*5)
        print('Modbus connection successful')
        print('---'*5)

    def load_register_map(self):
        register_map = 'comm\mapping.xlsx'
        assert os.path.isfile(register_map), \
        "The mapping data should be present in {},\n in .xlsx file format"\
        .format('.\comm\mapping.xlsx')
        df = pd.read_excel(register_map)
        # Access map only and convert to dict
        data = df[['Register_tag', 'Modbus Address']]
        # Remove all nan values
        data = data[data['Register_tag'].notna()]
        map = dict(data.values.tolist())
        # Convert floats to int for addresses
        for a in map:
            map[a] = int(map[a])
        print('---'*5)
        print('Loaded register map successfully')
        print('---'*5)
        return map
