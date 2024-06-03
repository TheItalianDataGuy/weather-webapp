import streamlit as st

# User interface
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
day = st.slider("Forecast day: ", min_value=1, max_value=5,
                help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {day} days in {place}")


