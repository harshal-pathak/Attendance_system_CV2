# Import necessary libraries
import streamlit as st
import pandas as pd
from datetime import datetime
import time
import os

# Get the current timestamp and format it for date and timestamp
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
exist = os.path.isfile(r"C:\Users\HARSHAL\Downloads\Attendance_"+ date + ".csv")
# Corrected file name concatenation
filename = f"C:\Users\HARSHAL\Downloads\Attendance_" + date + ".csv"  # Using the formatted date in the file name
if not exist:
    print("Please take attendence first")
    # Assuming the file is generated with this name
else:
    df = pd.read_csv(filename)
    # Use Streamlit to display the DataFrame in an interactive web app
    st.dataframe(df)