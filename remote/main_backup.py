import pandas as pd
from node import node
import streamlit as st
from datetime import datetime
from streamlit.ReportThread import add_report_ctx
import time
from sqlalchemy import create_engine
import threading
import multiprocessing as mp
import numpy as np

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems
from collections import OrderedDict

# Replacing node with pin
@st.cache(allow_output_mutation=True)
def create_node():
    # Instantiate node
    pin = node.Node()
    # Set node params
    pin.node_name = 'Current monitoring dashboard'
    pin.node_description = 'Current trend monitoring system'
    pin.node_number = 'N1_1507'

    pin.host_ip = '127.0.0.1'
    # pin.host_ip = '192.168.3.250'
    pin.host_port = '502'
    # Load register map
    # map = pin.load_register_map()
    # Connect with slave
    pin.connect()
    # Create and connect to db
    engine = create_engine('sqlite:///database/current_data.db', echo=False)
    # Initiate the basic page

    return pin, map, engine

# Globally initiate variables and load page
pin, map, engine = create_node()
pin.init_page()

# @st.cache(allow_output_mutation=True)
# def data_storage():
#     # current = pin.read_holding_registers(address, count,  unit=pin.unit)
#     # distance = pin.read_holding_registers(address, count,  unit=pin.unit)
#     # Decode data
#     # Add tag corresponding to cycle
#     # Save to database
#     pass

# def live_monitor():
#     # Update page with latest data
#     # Read from database latest 50 points which will be one cycle for sure
#     # save it in a dataframe
#     st.line_chart(df[['Current', 'Distance']])
#     pass

# current = []
# distance = []
# i = 1
# while i<=99:
#     # Reading current registers
#     result = pin.client.read_holding_registers(i,2,unit = pin.unit)
#     decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
#     current.append(decoder.decode_16bit_float())
#     # Reading distance registers
#     result = pin.client.read_holding_registers(200+i,2,unit = pin.unit)
#     decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
#     distance.append(decoder.decode_16bit_float())
#     # Increment register
#     i = i + 2
#
# current = np.array(current)
# distance = np.array(distance)
#
# print(current)
# print(' ')
# print(distance)
distance = np.random.uniform(low=0, high=10, size=(50,))
current = np.random.uniform(low=0, high=10, size=(50,))

cycle_number = st.sidebar.selectbox(
    "Select cycle number",
    ("1", "2", "3")
)

df = pd.DataFrame({'distance': distance, 'current': current})
df = df.rename(columns={'distance':'index'}).set_index('index')
# print(df)
st.line_chart(df)
