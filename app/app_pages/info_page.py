import streamlit as st
import pandas as pd
from PIL import Image
from app_pages.map import show_station_map

def show():
    st.title("ℹ️ Info")

    st.subheader("🏭 Air Pollutants ")

    pollutant_descriptions = {
        "PM10": "PM10 refers to particulate matter with a diameter of less than 10 micrometers. These particles can reach the lungs through inhalation, and long-term exposure may lead to health problems.",
        "SO2": "Sulfur dioxide (SO₂) is produced by the combustion of fossil fuels. It can irritate the eyes, nose, and throat, and may worsen respiratory diseases such as asthma.",
        "CO": "Carbon monoxide (CO) is a colorless and odorless gas. Inhalation at high levels reduces the blood’s ability to carry oxygen, potentially causing headaches and loss of consciousness.",
        "NO2": "Nitrogen dioxide (NO₂) is emitted from sources like diesel-powered vehicles. It can cause inflammation in the respiratory tract, trigger asthma attacks, and impair lung function.",
        "NOX": "NOx is a general term for nitrogen oxides (NO and NO₂). It contributes to the formation of ozone and fine particulates, thus deteriorating air quality.",
        "NO": "Nitric oxide (NO) is produced during high-temperature combustion processes. While not directly harmful, it can convert into NO₂, leading to indirect health risks.",
        "O3": "Ozone (O₃) is harmful at ground level. It irritates the respiratory system, causes eye burning and coughing, and poses a risk especially for individuals with asthma."
}


    for pollutant, description in pollutant_descriptions.items():
        st.markdown(f"**{pollutant}**: {description}")


    st.markdown("### 🌡️ Weather Inputs ")

    html_inputs_table = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            font-size: 15px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
            font-weight: bold;
        }
    </style>

    <table>
        <tr>
            <th>Variable</th>
            <th>Description</th>
            <th>Unit</th>
        </tr>
        <tr><td>temp</td><td>Average temperature</td><td>°C</td></tr>
        <tr><td>feelslike</td><td>Feels-like temperature</td><td>°C</td></tr>
        <tr><td>humidity</td><td>Relative humidity</td><td>%</td></tr>
        <tr><td>dew</td><td>Dew point</td><td>°C</td></tr>
        <tr><td>windgust</td><td>Wind gust speed</td><td>km/h</td></tr>
        <tr><td>windspeed</td><td>Average wind speed</td><td>km/h</td></tr>
        <tr><td>winddir</td><td>Wind direction (0–360°)</td><td>Degrees (°)</td></tr>
        <tr><td>pressure</td><td>Atmospheric pressure</td><td>hPa</td></tr>
        <tr><td>cloudcover</td><td>Cloud cover percentage</td><td>%</td></tr>
        <tr><td>solarradiation</td><td>Amount of solar radiation</td><td>W/m²</td></tr>
        <tr><td>visibility</td><td>Visibility distance</td><td>km</td></tr>
        <tr><td>weather_group_code</td><td>General weather condition code (Clear, Cloudy, Rainy, Snowy, etc.)</td><td>-</td></tr>
    </table>

    """

    st.markdown(html_inputs_table, unsafe_allow_html=True)

    st.markdown("### 📊 Data Sources", unsafe_allow_html=True)

    st.markdown("""
                 The air pollutant data used in the application has been obtained from the fixed and mobile air quality monitoring stations in Istanbul operated by the <b>Republic of Türkiye Ministry of Environment, Urbanization and Climate Change</b>.
                 These stations measure pollutants such as PM10, SO₂, CO, NO₂, NOx, NO, and O₃ on an hourly and daily basis and regularly provide data through environmental sensors.
                 While fixed stations conduct continuous measurements at specific locations, mobile stations offer the ability to perform temporary measurements in different areas. The data covers the years 2022–2025.
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
     image = Image.open("images/image12.png")
     resized_image = image.resize((400, 300))  
     st.image(resized_image)

    with col2:
     image = Image.open("images/image13.png")
     resized_image = image.resize((400, 300))  
     st.image(resized_image)

    

    st.markdown("""
                The hourly weather data used during the model training process was obtained from the Visual Crossing Weather API and corresponds to the Atatürk Airport meteorological station in Istanbul, covering the years 2022–2025.
                This dataset includes meteorological variables such as temperature, feels-like temperature, humidity, dew point, wind direction and speed, pressure, cloud cover, visibility, and solar radiation.
                This long-term and consistent dataset from a fixed location was chosen to ensure stability and uniformity during model training.

                When a user requests a prediction in the application, real-time and forecasted weather data is retrieved via the Visual Crossing API based on the selected district.
                This data is calculated as a distance-weighted average of measurements from meteorological stations closest to the chosen location.
                In this way, more realistic and district-specific input values are provided, allowing the application to generate air quality predictions that are most relevant to the user’s actual location.
    """, unsafe_allow_html=True)

    
    image = Image.open("images/image14.png")  
    resized_image = image.resize((800, 280))  
    st.image(resized_image)

    st.markdown("""
    <sub>🔗 Weather data [Visual Crossing](https://www.visualcrossing.com/) were obtained using the Visual Crossing service.</sub>
    """, unsafe_allow_html=True)

    show_station_map()
   


