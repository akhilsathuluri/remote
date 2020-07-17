import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

from SessionState import get
# from remote.comm import Comm
# from remote.node import Node

# class Dashboard(Comm, Node):
class Dashboard():
    def __init__(self):
        self.time_stamp = datetime.now()
        # Define any description for the active node

    def main():
        st.title("{}: {}".format(node_number, node_name))
        st.header(node_description)

# main()
