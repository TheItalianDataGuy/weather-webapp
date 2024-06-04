import streamlit as st
import plotly.express as px
from backend import get_data

# User interface
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast day: ", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Give the condition to avoid the error when the Place box is empty
if place:
    # Use try except to fix the error in case of typo
    try:
        # Split the return of the function so d=date and t=temperature
        filtered_data = get_data(place, days)

        # Create the plot for temperature
        if option == "Temperature":
            # Use the list comprehension to select all the temperature/date
            # in all the dictionaries of list.
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        # Create a rendered image of the sky
        if option == "Sky":
            # Create a dictionary to contain the key that matches with the image
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}

            # Use the list comprehension to select all the sky
            # in all the dictionaries of list.
            sky = [dict["weather"][0]["main"] for dict in filtered_data]

            # Create the list comprehension so that the sky's weather matches with the picture
            image_paths = [images[weather] for weather in sky]
            print(sky)
            st.image(image_paths, width=115, caption=[dict["dt_txt"] for dict in filtered_data])
    except KeyError:
        st.write("The typed place does exist in the database.")
