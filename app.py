import streamlit as st
import pandas as pd
import time # to simulate realtime data
import numpy as np
import plotly.express as px

# dataset = "my_data.csv"

# SEO 
st.set_page_config(
    page_title = 'Real-Time Dashboard',
    page_icon = '🌱',
    layout = 'wide'
)

# dashboard title
st.title("Real-Time / Plant Monitor Dashboard")

# creating a single-element container.
placeholder = st.empty()

# set and initialise variables
x_max = 0.45
x_min = 0.35
u = 0
flow_factor = 36 # ms/mL for a 100L/H pump
tube_const = 5 # tube takes 5 seconds to fill


with st.status("Setting up pump..."):
    # loop for 100 seconds
    # x measurement every 10 seconds
    # this is simulating live data, replace with real live data
    for seconds in range(100):
    #while True: 
        x_new = np.random.uniform(0.3, 0.5)
        # check x against limts and calc u time
        if x_new < x_min:
            st.info('Pump on', icon="ℹ️")
            pump_time = (x_min - x_new)*flow_factor + tube_const
            time.sleep(pump_time)   