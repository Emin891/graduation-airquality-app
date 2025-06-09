import streamlit as st
import datetime
import numpy as np
import pandas as pd
import pickle
import os
from utils import get_weather_by_ilce
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo



def show():
    st.title(":foggy: Istanbul Air Pollutant Prediction")

    st.markdown("#### Select Pollutant:")
    cols = st.columns(7)
    pollutants = ["PM10", "SO2", "CO", "NO2", "NOX", "NO", "O3"]

    for i, pol in enumerate(pollutants):
        if st.session_state.pollutant_selected == pol:
            button_style = f"background-color:#ffe6e6;border:2px solid red;border-radius:10px;font-weight:bold;"
        else:
            button_style = f"background-color:#f9f9f9;border:2px solid #ccc;border-radius:10px;"

        if cols[i].button(pol, key=f"pollutant_{pol}", use_container_width=True):
            st.session_state.pollutant_selected = pol

    selected_pollutant = st.session_state.pollutant_selected

    selected_features = [
        'temp', 'humidity', 'dew', 'windgust',
        'windspeed', 'pressure', 'cloudcover', 'visibility',
        'solarradiation', 'weather_group_code',
        'hour', 'day', 'month', 'dayofweek', 'season',
        'wind_dir_rad', 'wind_dir_sin', 'wind_dir_cos',
        'is_weekend', 'is_nighttime', 'is_rush_hour',
    ]

    now = datetime.now(ZoneInfo("Europe/Istanbul"))
    today = now.date()
    next_full_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)


    ilceler = ["Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler",
        "Bakırköy", "Başakşehir", "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü",
        "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy", "Esenler", "Esenyurt",
        "Eyüpsultan", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane",
        "Kartal", "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer",
        "Silivri", "Sultanbeyli", "Sultangazi", "Şile", "Şişli", "Tuzla",
        "Ümraniye", "Üsküdar", "Zeytinburnu"]

    ilce = st.selectbox("Select County", ilceler)

    st.markdown("#### 🗓️ Estimated Date and Time information")
    col_date, col_time = st.columns(2)
    with col_date:
      selected_date = st.date_input("Date", value=today, min_value=today, label_visibility="collapsed")
    with col_time:
      selected_time = st.time_input("Hour", value=next_full_hour.time(), step=timedelta(hours=1), label_visibility="collapsed")

    selected_datetime = datetime.combine(selected_date, selected_time)
    if selected_datetime < now:
      st.warning("⚠️ Please choose a time later than the current time!")

    if st.button("📥 Autofill Weather Data", disabled=(selected_datetime < now)):
      weather_data = get_weather_by_ilce(ilce, selected_datetime)
    if weather_data:
        st.success("✅ Data received successfully!")
        st.session_state["auto_weather"] = weather_data
    else:
        st.warning("⚠️ Failed to retrieve data from API.")

    weather = st.session_state.get("auto_weather", {})

    temp = st.number_input("Temperature (°C)", value=weather.get("temp", 15.0))
    humidity = st.slider("Humidity (%)", 0, 100, int(weather.get("humidity", 50)))
    dew = st.number_input("Dew Point (°C)", value=weather.get("dew", 10.0))
    windgust = st.number_input("Wind Gust Speed (km/h)", value=weather.get("windgust", 20.0))
    windspeed = st.number_input("Wind Speed (km/h)", value=weather.get("windspeed", 10.0))
    winddir = st.slider("Wind Direction (0°–360°)", 0, 360, int(weather.get("winddir", 180)))
    pressure = st.number_input("Pressure (hPa)", value=weather.get("pressure", 1012.0))
    cloudcover = st.slider("Cloud Cover (%)", 0, 100, int(weather.get("cloudcover", 50)))
    solarradiation = st.number_input("Solar Radiation (W/m²)", value=weather.get("solarradiation", 200.0))
    visibility = st.number_input("Visibility (km)", value=weather.get("visibility", 10.0))


    st.markdown("#### Select General Weather Situation: ")
    weather_options = [
        ("Partly Cloudy", 0, ":partly_sunny:"), ("Clear", 1, ":sunny:"),
        ("Overcast", 2, ":cloud:"), ("Rainy", 3, ":sun_behind_rain_cloud:"),
        ("Snowy", 4, ":snowflake:")
    ]
    cols = st.columns(len(weather_options))
    for i, (label, code, icon) in enumerate(weather_options):
        button_label = f"{icon} {label}"
        if cols[i].button(button_label, key=f"weather_btn_{code}"):
            st.session_state.weather_group_code = code

    weather_group_code = st.session_state.weather_group_code

    wind_rad = np.deg2rad(winddir)

    input_dict = {
        'temp': temp,
        'humidity': humidity, 
        'dew': dew,
        'windgust': windgust, 
        'windspeed': windspeed, 
        'pressure': pressure,
        'cloudcover': cloudcover, 
        'visibility': visibility, 
        'solarradiation': solarradiation,
        'weather_group_code': weather_group_code,
        'hour': selected_time.hour, 
        'day': selected_date.day, 
        'month': selected_date.month,
        'dayofweek': selected_date.weekday(), 
        'season': (selected_date.month % 12) // 3 + 1,
        'wind_dir_rad': wind_rad, 
        'wind_dir_sin': np.sin(wind_rad), 
        'wind_dir_cos': np.cos(wind_rad),
        'is_weekend': 1 if selected_date.weekday() >= 5 else 0,
        'is_nighttime': 1 if selected_time.hour < 6 or selected_time.hour > 22 else 0,
        'is_rush_hour': 1 if (7 <= selected_time.hour <= 9 or 17 <= selected_time.hour <= 19) else 0,
       
    }

    input_data = pd.DataFrame([[input_dict[feat] for feat in selected_features]], columns=selected_features)

    if st.button(f" 🎯 {selected_pollutant} Predict 🎯"):
        if selected_datetime < now:
            st.error("⚠️ You can't predict with the past hour!")
        else:
            model_paths = {
                "PM10": os.path.join("models", "pm10_model.pkl"),
                "SO2": os.path.join("models", "so2_model.pkl"),
                "CO": os.path.join("models", "co_model.pkl"),
                "NO2": os.path.join("models", "no2_model.pkl"),
                "NO": os.path.join("models", "no_model.pkl"),
                "NOX": os.path.join("models", "nox_model.pkl"),
                "O3": os.path.join("models", "o3_model.pkl"),
            }
            model_path = model_paths[selected_pollutant]
            with open(os.path.join(os.path.dirname(__file__), "..", model_path), "rb") as f:
                data = pickle.load(f)
            model = data["model"]
            mae = data["mae"]
            prediction = model.predict(input_data)[0]
            lower = max(0, prediction - mae)
            upper = prediction + mae
            

            thresholds = {
                "PM10":    [30.40, 38.21, 46.31],
                "SO2":     [2.32, 2.74, 3.39],
                "CO":      [345.06, 402.07, 480.25],
                "NO2":     [33.70, 46.21, 64.52],
                "NO":      [25.42, 31.28, 37.83],
                "NOX":     [29.06, 42.55, 61.42],
                "O3":      [21.74, 36.84, 52.50]
            }

            explanations = {
                "PM10": [
                    "PM10 levels are low and no adverse health effects are expected. Outdoor activities are safe for all age groups. Long periods outdoors and physical exercise are safe.",
                    "PM10 levels may still be within acceptable limits. However, individuals with respiratory sensitivity (asthma, COPD, the elderly, children) may experience mild effects. Caution is advised during outdoor activities, and symptoms should be monitored.",
                    "PM10 levels may be at unhealthy levels. Individuals with respiratory conditions should avoid staying outdoors. Mask use and remaining indoors are recommended. Outdoor physical activities should be limited.",
                    "Air pollution may be severe. PM10 exposure is particularly dangerous for those with chronic illnesses. People should stay indoors, keep windows closed, and use air purifiers if possible."
                ],

                "SO2": [
                    "SO₂ levels may be low. The air is considered safe for breathing. Everyone can comfortably spend time outdoors. There is no concern for sensitive individuals.",
                    "SO₂ levels may be moderate. Sensitive groups (asthma, bronchitis patients) may experience eye irritation or throat discomfort. Caution should be exercised during prolonged outdoor exposure. If symptoms appear, moving indoors is advised.",
                    "SO₂ levels may be unhealthy. Effects may include respiratory irritation, coughing, and eye burning. Sensitive individuals should avoid going outside. Indoor areas should be preferred and well ventilated.",
                    "SO₂ levels may be at hazardous levels. Being outdoors can cause serious respiratory problems. Children, the elderly, and people with chronic illnesses should remain indoors."
                ],

                "CO": [
                    "Carbon monoxide levels may be very low. There is no air quality risk. Everyone can safely be in both indoor and outdoor spaces. Exercising or spending long periods outside poses no concern.",
                    "CO levels may be moderate. Prolonged exposure may cause symptoms such as headaches or fatigue in some individuals. Caution is advised especially in enclosed and poorly ventilated areas. Ensure proper ventilation during physical activity.",
                    "CO concentrations may be at unhealthy levels. Symptoms such as dizziness, nausea, and fatigue may occur. Enclosed spaces should be frequently ventilated and prolonged stays avoided. If symptoms arise, leave the area immediately.",
                    "CO levels may be dangerously high. The risk of unconsciousness or fainting increases significantly. Do not remain in enclosed spaces; move to fresh air immediately."
                ],

                "NO2": [
                    "NO₂ levels may be low. Air quality is very good and outdoor activities are safe for everyone. No adverse effects on the respiratory system are expected. Outdoor exercise and walks are encouraged.",
                    "NO₂ levels may be moderate. Mild symptoms may appear in sensitive individuals (especially those with asthma or bronchitis). Caution is advised during long stays outdoors, and symptoms should be monitored.",
                    "NO₂ levels may be in the unhealthy range. Effects such as throat irritation, eye watering, and shortness of breath may occur. Children and the elderly should avoid being outdoors.",
                    "NO₂ levels may pose serious health risks. It may impair lung function and worsen existing respiratory illnesses. Stay indoors and wear a mask if going outside is necessary."
                ],

                "NO": [
                    "NO levels may be low and pose no health risks. Outdoor activities can be carried out safely. No negative effects on the respiratory system are expected. Air quality is generally good.",
                    "NO levels may be moderate. Mild respiratory symptoms may occur in sensitive individuals (e.g., those with asthma or COPD). Caution is advised for prolonged physical activity outdoors.",
                    "NO levels may be unhealthy. They may cause respiratory irritation, coughing, or shortness of breath. It is advisable to stay indoors and wear a mask if needed.",
                    "NO levels may be high and hazardous. The effects on the respiratory system may be serious. Sensitive individuals should not go outside and should remain indoors."
                ],

                "NOX": [
                    "NOx levels may be low. Air quality is healthy and safe. Everyone can spend time outdoors comfortably. No respiratory issues are expected.",
                    "NOx levels may be moderate. Caution is advised especially for sensitive groups (children, the elderly, asthma patients). Avoiding prolonged outdoor exposure may be beneficial.",
                    "NOx levels may be unhealthy. They can trigger respiratory illnesses such as asthma or bronchitis. Outdoor activities should be reduced, and staying indoors is recommended.",
                    "NOx concentrations may be dangerously high. They can have serious effects on the respiratory system. Avoid going outside, and keep windows and doors closed."
                ],

                "O3": [
                    "Ozone levels may be low and air quality is excellent. Staying outdoors is safe for everyone. Physical activities like exercise and walking can be done comfortably.",
                    "Ozone levels may be moderate. Sensitive individuals may experience eye irritation or mild shortness of breath, especially during sunny hours. Prolonged outdoor exposure should be avoided.",
                    "Ozone levels may be unhealthy. Symptoms such as throat irritation, headaches, and difficulty breathing may occur. Being outside during midday is not recommended.",
                    "Ozone levels may be very high and pose serious health risks. Avoid being outdoors during sunny hours and keep windows closed. Sensitive individuals should stay in filtered indoor environments."
                ]
            }


            if selected_pollutant in thresholds:
                p25, p50, p75 = thresholds[selected_pollutant]
                if prediction - mae <= p25:
                    bg_color = "#d4edda"
                    border_color = "#28a745"
                    explanation = explanations[selected_pollutant][0]
                elif prediction - mae <= p50:
                    bg_color = "#fff3cd"
                    border_color = "#ffc107"
                    explanation = explanations[selected_pollutant][1]
                elif prediction - mae  <= p75:
                    bg_color = "#ffe0b2"
                    border_color = "#f57c00"
                    explanation = explanations[selected_pollutant][2]
                else:
                    bg_color = "#f8d7da"
                    border_color = "#dc3545"
                    explanation = explanations[selected_pollutant][3]
            else:
                bg_color = "#f0f9ff"
                border_color = "#2a9df4"
                explanation = ""

            st.markdown(f"""
            <div style='
                padding: 20px;
                margin-top: 20px;
                border-radius: 10px;
                background-color: {bg_color};
                border-left: 6px solid {border_color};
                text-align: center;'>
                <h3 style='color:{border_color}; margin-bottom: 10px;'>🌫️ {selected_pollutant} Prediction</h3>
                <h2 style='font-size: 28px; font-weight: bold; margin: 0;'>{prediction:.2f} µg/m³</h2>
                <h style='font-size: 16px; color: #333;'>( Expected estimated range: {lower:.2f} – {upper:.2f} µg/m³ )</h>
                <p style='margin-top: 15px; font-size: 18px; font-weight: 600; color: #333;'>{explanation}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div style='
                        background-color: #add8e6;
                        padding: 15px 20px;
                        margin-top: 45px;
                        border-radius: 8px;
                        font-size: 16px;'
                    >
                    <b>📌 Informing:</b><br>
                    This application provides estimated information on air pollutants using machine learning models based on weather data.
                    The results obtained are <b>not exact values</b> and are intended solely for <i>informational and awareness</i> purposes.
                    For any decisions regarding air quality, the most up-to-date data from <b>official air quality monitoring systems</b> and <b>authorized institutions</b> should be used as the primary reference.
                    </div>
                    """, unsafe_allow_html=True)
