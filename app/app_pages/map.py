import streamlit as st
import folium
from streamlit_folium import st_folium

def show_station_map():
    st.markdown("### 🗺️ Monitoring Stations")

    
    m = folium.Map(location=[41.0, 28.8], zoom_start=11)

    
    stations = [
        {"name": "ATATÜRK Airport (Data Source 1)", "lat": 40.977, "lon": 28.821, "type": "weather"},
        {"name": "ATATÜRK Airport (Data Source 2)", "lat": 40.97, "lon": 28.82, "type": "weather"},
        {"name": "Yenibosna Air Quality Station", "lat": 40.9973, "lon": 28.8270, "type": "air"},
        {"name": "Şirinevler Air Quality Station", "lat": 41.0024, "lon": 28.8386, "type": "air"},
        {"name": "Bağcılar Air Quality Station", "lat": 41.0327, "lon": 28.8429, "type": "air"},
        {"name": "Sultangazi Air Quality Station", "lat": 41.1019, "lon": 28.8720, "type": "air"},
        {"name": "Esenyurt Air Quality Station", "lat": 41.0202, "lon": 28.6695, "type": "air"},
    ]


  
    for s in stations:
        color = "red" if s["type"] == "weather" else "blue"
        folium.Marker(
            location=[s["lat"], s["lon"]],
            popup=s["name"],
            tooltip=s["name"],
            icon=folium.Icon(color=color, icon="cloud" if s["type"] == "weather" else "cloud", prefix="fa")
        ).add_to(m)

    
    latlngs = [[s["lat"], s["lon"]] for s in stations]
    m.fit_bounds(latlngs)

   
    st_folium(m, width=1000, height=400)


