import streamlit as st
import time

header = st.empty()
header.text('This is a test')
time.sleep(3)

i = 0
while i<10:
    header.text("Now the number is: {}".format(i))
    i = i+1
    time.sleep(1)
