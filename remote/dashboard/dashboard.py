# import streamlit as st
# import numpy as np
# import pandas as pd
# from datetime import datetime
#
# import datetime as dt
# import matplotlib.pyplot as plt
# from matplotlib import style
#
# # from remote.comm import comm
# from comm import comm
# from node import node
#
# class Dashboard(comm.Comm, node.Node):
#     def __init__(self):
#         comm.Comm.__init__(self)
#         node.Node.__init__(self)
#         self.time_stamp = datetime.now()
#
#     def initiate(self):
#         st.title("{}: {}".format(self.node_number, self.node_name))
#         st.header(self.node_description)
#         st.header('Accessed at: '+ str(self.time_stamp))
#         # st.header('Connection status: '+str(self.connection_status))
