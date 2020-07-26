import pandas as pd
from node import node
from camutils import *
from cycleutils2 import *
import streamlit as st
from datetime import datetime
from streamlit.ReportThread import add_report_ctx
import time
from sqlalchemy import create_engine
import threading
import multiprocessing as mp

def create_node(node):
    # Instantiate node
    node = node.Node()
    # Set node params
    node.node_description = 'Pad printing machine for Husqvarna rims'
    node.node_number = 'N1_1507'
    node.node_name = 'Pad printing machine'

#    node.host_ip = '127.0.0.1'
    node.host_ip = '192.168.0.109'
    node.host_port = '502'

    # Load register map
    map = node.load_register_map()
    # Connect with slave
    node.connect()
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

def display(node, engine):
    # Initialise page
    node.init_page()
    show_data = st.empty()
    while True:
        # publish(node, map, temp, engine)
        df = pd.read_sql('register_data', con=engine)
        show_data.dataframe(df)

def main_funcs(node, map, engine):
    t1 = threading.Thread(target=health, args=(node,map, ))
    t2 = threading.Thread(target=cycle, args=(node,map, ))
    t3 = threading.Thread(target=write_to_db, args=(node,map,engine ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__=="__main__":
    node, map = create_node(node)
    # Connect to db
    engine = create_engine('sqlite:///database/register_data.db', echo=False)

    p = mp.Process(target=main_funcs, args=(node, map, engine, ))
    p.start()

    time.sleep(1)

    t3 = threading.Thread(target=display, args=(node, engine,))
    add_report_ctx(t3)
    t3.start()

    t3.join()
    p.join()
