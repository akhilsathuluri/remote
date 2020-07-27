import streamlit as st
import multiprocessing as mp
import threading
from streamlit.ReportThread import add_report_ctx

st.title('Title')
box = st.empty()
box.text('Yo')

def printer():
    print('yolo')

def hello():
    print('in write')
    box.text('Hello')

y = mp.Process(target=printer)
p = threading.Thread(target=hello)
add_report_ctx(p)

y.start()
p.start()

y.join()
p.join()
