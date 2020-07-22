import streamlit as st
import json
from datetime import datetime
import time

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
        st.header('Accessed at: '+ str(self.time_stamp))
        # st.header('Connection status: '+str(self.connection_status))
        # st.header('Logging status: {}'.format(self.logging_status))

    # def start_logging(log_frequency):
    #     self.logging_status = True
    #     st.header('Logging status: {}'.format(self.logging_status))
        # Instead of initiating the log file every time. Load one from the memory
        # so that we dont rewrite it every time we restart it
