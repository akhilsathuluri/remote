import streamlit as st

# from remote.dashboard import dashboard
from dashboard import dashboard
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

class Node(dashboard.Dashboard):
    def __init__(self):
        self.node_description = 'Pad printing machine for Husqvarna rim printing'
        self.node_number = 'N1_1507'
        self.node_name = 'Pad printing machine'
        dashboard.Dashboard.__init__(self)

    def initiate(self):
        st.title("{}: {}".format(self.node_number, self.node_name))
        st.header(self.node_description)
        st.header('Accessed at: '+ str(self.time_stamp))
        st.header('Connection status: '+str(self.connection))


    # def log_data()

node = Node()
node.initiate()
node.connect()
map = node.load_register_map()

# while node.connection_status:
#     rq = node.client.read_holding_registers(map['Registers'][0], 2, unit = node.unit)
#     st.header(str(rq.registers))

# while self.connection_status:
#     rq = client.read_holding_registers()
