import pandas as pd
from node import node
from camutils import *
from cycleutils import *
import threading
import signal
import streamlit as st
from datetime import datetime
from streamlit.ReportThread import add_report_ctx
import time
from sqlalchemy import create_engine

def create_node(node):
    # Instantiate node
    node = node.Node()
    # Set node params
    node.node_description = 'Pad printing machine for Husqvarna rims'
    node.node_number = 'N1_1507'
    node.node_name = 'Pad printing machine'

    node.host_ip = '127.0.0.1'
    node.host_port = '502'

    # Load register map
    map = node.load_register_map()
    # Connect with slave
    node.connect()
    # Initialise page
    node.init_page()
    # Reset the entire memory block under pi's control
    start_register = 50
    block_length = 15
    rq = node.client.write_registers(start_register, [0]*block_length, unit=node.unit)

    return node, map

def publish(node, map, temp, engine):
    # Read data from all the tagged registers
    for reg in map:
        temp_reg = node.client.read_holding_registers(map[reg], 1, unit=node.unit)
        temp[reg] = temp_reg.registers[0]
    temp.to_sql('register_data', con=engine, if_exists='append')

node, map = create_node(node)
# Connect to db
engine = create_engine('sqlite:///database/register_data.db', echo=False)
temp = map.copy()
temp = pd.DataFrame([temp], columns=temp.keys())

bla = st.empty()

while True:
    cycle(node, map)
    health(node, map)
    publish(node, map, temp, engine)
    df = pd.read_sql('register_data', con=engine)
    bla.dataframe(df)
    # time.sleep(1)
