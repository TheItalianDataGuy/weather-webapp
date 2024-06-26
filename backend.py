import requests
import os

API_key = os.getenv("api_key")


# Define the function to get the weather data
def get_data(place, days=None):

    # use the url to get the json data.
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()

    # Filter the data so that we get only the data needed
    filtered_data = data["list"]

    # There are 40 dictionaries because for each day there are
    # 8 endpoints. So for two days we need 16 endpoints and so on.
    user_input_day = 8 * days
    filtered_data = filtered_data[:user_input_day]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Madrid", days=3))
