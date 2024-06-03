import streamlit as st
import plotly.express as px

# User interface
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
day = st.slider("Forecast day: ", min_value=1, max_value=5,
                help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {day} days in {place}")


# Create a graph with plotly
# Define a function to get the data
def get_data (day_local):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = ["10", "11", "17"]
    temperatures = [day * i for i in temperatures]
    return dates, temperatures


# Split the return of the function so d=date and t=temperature
d, t = get_data(day)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C*)"})
st.plotly_chart(figure)


