import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data

# User interface
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast day: ", min_value=1, max_value=5,
                help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {day} days in {place}")


# Split the return of the function so d=date and t=temperature
d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C*)"})
st.plotly_chart(figure)


