import streamlit as st

# from remote.dashboard import dashboard
from dashboard import dashboard
from node import node
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time
import json

node = node.Node()
node.initiate()

self.node_description = 'Pad printing machine for Husqvarna rim printing'
self.node_number = 'N1_1507'
self.node_name = 'Pad printing machine'

node.log_frequency = 1

node.host_ip = '127.0.0.1'
node.host_port = '502'

node.connect()
map = node.load_register_map()

node.logging_status = True

st.header('Connection status: '+str(node.connection_status))
st.header('Logging status: {}'.format(node.logging_status))

# log = open('log.json', 'a')
message = {}
while node.logging_status:
    # Reads every 1 second
    for r in map['Registers']:
        rq = node.client.read_holding_registers(r, 1, unit = node.unit)
        # message = map['Components'][r-1]+' : '+str(rq.registers[0])
        message['Components'] = map['Components'][r-1]
        message['Value'] = rq.registers[0]
        with open('log.json', "a") as log:
            json.dump([comp, val], log)
    time.sleep(node.log_frequency)



node.client.close()
