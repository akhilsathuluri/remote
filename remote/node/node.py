import streamlit as st
import json
from datetime import datetime
import time
from sqlalchemy import create_engine

from comm import comm

class Node(comm.Comm):
    def __init__(self):
        self.node_description = 'Insert node description by accessing node_description'
        self.node_number = 'Insert node description by accessing node_number'
        self.node_name = 'Insert node description by accessing node_name'
        comm.Comm.__init__(self)
        self.data = {}
        self.logging_status = False
        self.time_stamp = datetime.now()
        # Time in seconds
        self.log_frequency = 1

    def init_page(self):
        st.title("{}: {}".format(self.node_number, self.node_name))
        st.header(self.node_description)
        st.write('Accessed on: '+ str(self.time_stamp))

    # Add function to connect to db and save data
