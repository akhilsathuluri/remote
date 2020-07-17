import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

# from remote.comm import comm
from comm import comm

class Dashboard(comm.Comm):
    def __init__(self):
        comm.Comm.__init__(self)
        self.time_stamp = datetime.now()
        # self.logger_status = False

    # def access_logger(self):
        # self.logger_status = True
