# Weather Forecast Application

This project is a weather forecasting web application built with Streamlit and Plotly. It provides weather forecasts for the next few days for any specified location. Users can view temperature trends or sky conditions (e.g., clear, cloudy, rainy, snowy) over the selected number of days.

## Features

- **Location Input:** Users can input the name of a place to get the weather forecast.
- **Day Selection:** Users can choose the number of days (from 1 to 5) for which they want to see the weather forecast.
- **Data Visualization:** 
  - Temperature trends are visualized using a line graph.
  - Sky conditions are displayed using corresponding images.
  
## Prerequisites

- Python 3.x
- Required Python libraries:
  - `streamlit`
  - `plotly`
  - A backend function `get_data` for retrieving weather data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather-forecast-app.git

2. Navigate to the project directory:

  ```bash
  cd weather-forecast-app
```

3. Install the required Python packages:

  ```bash
  pip install -r requirements.txt
  ```

4. Run the Streamlit app:

  ```bash
  streamlit run app.py
  ```

## Usage
1. Place Input: Enter the name of the place you want the weather forecast for.
2. Days Selection: Use the slider to choose the number of days (1-5) for the forecast.
3. Data View Option: Select either "Temperature" or "Sky" from the dropdown menu to view the corresponding forecast.
4. Output: The app displays either a temperature line chart or sky condition images for the selected days.

## Error Handling
The app includes error handling to manage cases where the place entered does not exist in the weather data database. An appropriate message is displayed to the user in such cases.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Weather data is retrieved from an external API (assumed to be handled in the backend.py file).
- Images used for sky conditions are assumed to be stored in the images/ directory.

This `README.md` provides a comprehensive overview of your weather forecast application, including instructions for installation, usage, and the project structure. Make sure to adjust any file paths or project-specific details as needed.
