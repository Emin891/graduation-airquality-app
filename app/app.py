import streamlit as st
st.set_page_config(page_title="Air Pollutant Prediction", page_icon=":earth_africa:", layout="wide")

# import pandas as pd
# import requests  
# import pickle
# import numpy as np
# import datetime
# import matplotlib.pyplot as plt
# import seaborn as sns
# from PIL import Image

from streamlit_option_menu import option_menu
from app_pages.tahmin_page import show as show_tahmin
from app_pages.veri_analizi_page import show as show_veri_analizi
from app_pages.ana_sayfa_page import show as show_ana_sayfa
from app_pages.info_page import show as show_info



  
# df = pd.read_csv("cleaned_final.csv")

# import requests
# import datetime

# API_KEY = "TMETWPYHK5LX45VNWZ4PSDJWF"
# LOG_FILE = "api_log.txt"

# def get_weather_by_ilce(ilce, selected_datetime):
#     location = f"{ilce} istanbul"
#     datetime_str = selected_datetime.strftime('%Y-%m-%dT%H:%M:%S')

#     url = (
#         f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/"
#         f"timeline/{location}/{datetime_str}"
#         f"?unitGroup=metric&key={API_KEY}&include=hours&contentType=json"
#     )

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()

#         query_cost = data.get("queryCost", "Bilinmiyor")
#         now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         log_entry = f"[{now_str}] İlçe: {ilce}, Tarih/Saat: {selected_datetime}, QueryCost: {query_cost}\n"
#         print(log_entry.strip())

#         with open(LOG_FILE, "a", encoding="utf-8") as f:
#             f.write(log_entry)

#         # Günün saatlik veriler
#         hours_data = data.get("days", [])[0].get("hours", [])

#         hedef_saat = selected_datetime.hour
#         en_yakin = min(hours_data, key=lambda h: abs(int(h["datetime"].split(":")[0]) - hedef_saat))

#         return {
#             "temp": en_yakin.get("temp", 15.0),
#             "feelslike": en_yakin.get("feelslike", 14.0),
#             "humidity": en_yakin.get("humidity", 50),
#             "dew": en_yakin.get("dew", 10.0),
#             "pressure": en_yakin.get("pressure", 1012.0),
#             "windspeed": en_yakin.get("windspeed", 10.0),
#             "windgust": en_yakin.get("windgust", 20.0),
#             "winddir": en_yakin.get("winddir", 180),
#             "cloudcover": en_yakin.get("cloudcover", 50),
#             "uvindex": en_yakin.get("uvindex", 5),
#             "visibility": en_yakin.get("visibility", 10.0),
#             "solarradiation": en_yakin.get("solarradiation", 200.0),
#         }

#     except Exception as e:
#         print("❌ API Hatası:", e)
#         with open(LOG_FILE, "a", encoding="utf-8") as f:
#             f.write(f"[{datetime.datetime.now()}] HATA: {e}\n")
#         return None



st.markdown("""
    <style>
    .stNumberInput, .stSelectbox, .stSlider, .stRadio, .stTextInput {
        max-width: 1000px;
        margin: auto;
    }
    .stButton, .stSuccess {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .block-container {
        max-width: 1000px;
        margin: auto;
    }
    h1, h2, h3 {
        text-align: center;
    }
    p {
        text-align: left;
    }        
    .stButton > button {
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        transition: 0.2s ease;
    }
    .stButton > button:hover {
        box-shadow: 0px 0px 6px rgba(0,0,0,0.08);
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)


# Nav Menü
selected = option_menu(
    menu_title="Air Pollutant Prediction Application",
    options=["Home Page", "Prediction", "Data Analysis", "Info"],
    icons=["house", "cloud", "bar-chart", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if 'pollutant_selected' not in st.session_state:
    st.session_state.pollutant_selected = "PM10"

if 'weather_group_code' not in st.session_state:
    st.session_state.weather_group_code = 0

if selected == "Prediction":
    show_tahmin() 
if selected == "Data Analysis":
    show_veri_analizi() 
if selected == "Home Page":
    show_ana_sayfa()   
if selected == "Info":
    show_info()              

# # Tahmin Sayfası
# if selected == "Tahmin":
#     st.title(":foggy: İstanbul Hava Kalitesi Tahmini")
    

#     st.markdown("#### Kirletici Seçiniz:")
#     cols = st.columns(7)
#     pollutants = ["PM10", "SO2", "CO", "NO2", "NOX", "NO", "O3"]

#     for i, pol in enumerate(pollutants):
#         if st.session_state.pollutant_selected == pol:
#             button_style = f"background-color:#ffe6e6;border:2px solid red;border-radius:10px;font-weight:bold;"
#         else:
#             button_style = f"background-color:#f9f9f9;border:2px solid #ccc;border-radius:10px;"

#         if cols[i].button(pol, key=f"pollutant_{pol}", use_container_width=True):
#             st.session_state.pollutant_selected = pol
    

#     selected_features = [
#     'temp', 'feelslike', 'humidity', 'dew', 'windgust',
#     'windspeed', 'pressure', 'cloudcover', 'visibility',
#     'solarradiation', 'uvindex', 'weather_group_code',
#     'hour', 'day', 'month', 'dayofweek', 'season',
#     'wind_dir_rad', 'wind_dir_sin', 'wind_dir_cos',
#     'humidity_level', 'feelslike_diff', 'is_rainy',
#     'is_weekend', 'is_nighttime', 'is_rush_hour',
#     'humid_heat_index', 'uv_level'
# ]

#     selected_pollutant = st.session_state.pollutant_selected

#     now = datetime.datetime.now()
#     today = now.date()
#     next_full_hour = (now + datetime.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)

#     ilceler = [
#     "Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler",
#     "Bakırköy", "Başakşehir", "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü",
#     "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy", "Esenler", "Esenyurt",
#     "Eyüpsultan", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane",
#     "Kartal", "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer",
#     "Silivri", "Sultanbeyli", "Sultangazi", "Şile", "Şişli", "Tuzla",
#     "Ümraniye", "Üsküdar", "Zeytinburnu"
# ]

#     ilce = st.selectbox("İlçe Seçiniz", ilceler)


#     st.markdown("#### 🗓️ Tahmin Edilecek Tarih ve Saat")
#     col_date, col_time = st.columns(2)
#     with col_date:
#         selected_date = st.date_input("Tarih", value=today, min_value=today, label_visibility="collapsed")
#     with col_time:
#         selected_time = st.time_input("Saat", value=next_full_hour, step=datetime.timedelta(hours=1), label_visibility="collapsed")

#     selected_datetime = datetime.datetime.combine(selected_date, selected_time)
#     if selected_datetime < now:
#         st.warning("⚠️ Lütfen şimdiki zamandan daha ileri bir saat seçin!")

#     button_disabled = selected_datetime < datetime.datetime.now()
    


#     if st.button("📥 Hava Durumu Verilerini Otomatik Doldur", disabled=button_disabled):
#         weather_data = get_weather_by_ilce(ilce, selected_datetime)
#         if weather_data:
#             st.success("✅ Veriler başarıyla alındı!")
#             st.session_state["auto_weather"] = weather_data
#         else:
#             st.warning("⚠️ API'den veri alınamadı.")


#     day = selected_date.day
#     month = selected_date.month
#     dayofweek = selected_date.weekday()
#     hour = selected_time.hour
#     season = (month % 12) // 3 + 1


#     weather = st.session_state.get("auto_weather", {})

#     temp = st.number_input("Sıcaklık (°C)", value=weather.get("temp", 15.0))
#     feelslike = st.number_input("Hissedilen Sıcaklık (°C)", value=weather.get("feelslike", 14.0))
#     humidity = st.slider("Nem (%)", 0, 100, int(weather.get("humidity", 50)))
#     dew = st.number_input("Çiy Noktası (°C)", value=weather.get("dew", 10.0))
#     windgust = st.number_input("Rüzgar Ani Hızı (km/h)", value=weather.get("windgust", 20.0))
#     windspeed = st.number_input("Rüzgar Hızı (km/h)", value=weather.get("windspeed", 10.0))
#     winddir = st.slider("Rüzgar Yönü (0°-360°)", 0, 360, int(weather.get("winddir", 180)))
#     pressure = st.number_input("Basınç (hPa)", value=weather.get("pressure", 1012.0))
#     cloudcover = st.slider("Bulutluluk (%)", 0, 100, int(weather.get("cloudcover", 50)))
#     solarradiation = st.number_input("Güneş Radyasyonu (W/m²)", value=weather.get("solarradiation", 200.0))
#     visibility = st.number_input("Görünürlülük (km)", value=weather.get("visibility", 10.0))


#     #else:
#         #solarenergy = st.number_input("Solar Enerji", value=weather.get("solarenergy", 10.0))
#         #uvindex = st.slider("UV Index", 0, 11, int(weather.get("uvindex", 5)))
        

#     st.markdown("#### Genel Hava Durumunu Seçiniz:")
#     weather_options = [
#         ("Partly Cloudy", 0, ":partly_sunny:"),
#         ("Clear", 1, ":sunny:"),
#         ("Overcast", 2, ":cloud:"),
#         ("Rainy", 3, ":sun_behind_rain_cloud:"),
#         ("Snowy", 4, ":snowflake:")
#     ]
#     cols = st.columns(len(weather_options))
#     for i, (label, code, icon) in enumerate(weather_options):
#         button_label = f"{icon} {label}"
#         if cols[i].button(button_label, key=f"weather_btn_{code}"):
#             st.session_state.weather_group_code = code

#     st.markdown("<br>", unsafe_allow_html=True)

#     weather_group_code = st.session_state.weather_group_code

#     wind_rad = np.deg2rad(winddir)
#     wind_dir_sin = np.sin(wind_rad)
#     wind_dir_cos = np.cos(wind_rad)
#     wind_dir_rad = wind_rad

#     # Ortak tüm değişkenler
#     input_dict = {
#         'temp': temp,
#         'feelslike': feelslike,
#         'humidity': humidity,
#         'dew': dew,
#         'windgust': windgust,
#         'windspeed': windspeed,
#         'pressure': pressure,
#         'cloudcover': cloudcover,
#         'visibility': visibility,
#         'solarradiation': solarradiation,
#         'uvindex': weather.get("uvindex", 5),
#         'weather_group_code': weather_group_code,
#         'hour': hour,
#         'day': day,
#         'month': month,
#         'dayofweek': dayofweek,
#         'season': season,
#         'wind_dir_rad': wind_rad,
#         'wind_dir_sin': wind_dir_sin,
#         'wind_dir_cos': wind_dir_cos,
#         'humidity_level': humidity / 100,
#         'feelslike_diff': abs(temp - feelslike),
#         'is_rainy': 1 if weather_group_code == 3 else 0,
#         'is_weekend': 1 if dayofweek >= 5 else 0,
#         'is_nighttime': 1 if (hour < 6 or hour > 22) else 0,
#         'is_rush_hour': 1 if (7 <= hour <= 9 or 17 <= hour <= 19) else 0,
#         'humid_heat_index': (humidity / 100) * feelslike,
#         'uv_level': 0 if weather.get("uvindex", 5) <= 2 else (1 if weather.get("uvindex", 5) <= 5 else 2)
#     }

# # Ortak input verisi
#     input_data = pd.DataFrame([[input_dict[feat] for feat in selected_features]], columns=selected_features)


    

#     if st.button(f" 🎯 {selected_pollutant} Tahminini Hesapla 🎯"):
#          if selected_datetime < now:
#             st.error("⚠️ Geçmiş saat ile tahmin yapılamaz!")
#          else:
            
#             model_paths = {
#                 "PM10": "pm10_model.pkl",
#                 "SO2": "so2_model.pkl",
#                 "CO": "co_model.pkl",
#                 "NO2": "no2_model.pkl",
#                 "NO": "no_model.pkl",
#                 "NOX": "nox_model.pkl",
#                 "O3": "o3_model.pkl"
#             }
#             model_path = model_paths[selected_pollutant]

           
#             with open(model_path, "rb") as f:
#                 data = pickle.load(f)
#             model = data["model"]
#             mae = data["mae"]

#             prediction = model.predict(input_data)[0]
#             lower = max(0, prediction - mae)
#             upper = prediction + mae


            # thresholds = {
            #     "PM10":    [31.16, 36.43, 41.16],
            #     "SO2":     [1.83, 2.30, 2.97],
            #     "CO":      [617.96, 751.70, 927.96],
            #     "NO2":     [27.04, 36.85, 49.93],
            #     "NO":      [6.20, 11.84, 20.92],
            #     "NOX":     [38.72, 56.03, 81.46],
            #     "O3":      [23.58, 37.75, 52.00]
            # }

            # explanations = {
            #     "PM10": [
            #     "Hava kalitesi mükemmel. PM10 seviyeleri çok düşük ve sağlığa herhangi bir olumsuz etkisi beklenmez. Her yaş grubundaki bireyler için dış ortam aktiviteleri güvenlidir. Açık havada uzun süre kalınabilir, spor yapılabilir.",
            #     "Hava kalitesi genel halk için hâlâ kabul edilebilir düzeydedir. Ancak solunum yolları hassas olan bireylerde (astım, KOAH, yaşlılar, çocuklar) hafif etkiler ortaya çıkabilir. Açık hava aktivitelerinde dikkatli olunmalı, belirtiler takip edilmelidir.",
            #     "PM10 seviyeleri sağlıksız düzeydedir. Özellikle solunum sıkıntısı yaşayan bireyler açık havada kalmaktan kaçınmalıdır. Maske kullanımı ve kapalı ortamda bulunma tercih edilmelidir. Dış mekânda fiziksel aktiviteler sınırlandırılmalıdır.",
            #     "Hava ciddi düzeyde kirli. PM10 maruziyeti özellikle kronik hastalığı olanlar için tehlikelidir. Dışarı çıkılmamalı, pencereler kapalı tutulmalı ve mümkünse hava temizleyici kullanılmalıdır. Gerekiyorsa tıbbi destek alınmalıdır."
            #     ],


            #     "SO2": [
            #     "SO2 seviyesi oldukça düşüktür. Hava solunum açısından güvenli kabul edilir. Herkes rahatlıkla dış mekânda zaman geçirebilir. Özellikle hassas bireyler için endişe verici bir durum yoktur.",
            #     "SO2 seviyeleri orta düzeydedir. Hassas gruplarda (astım, bronşit hastaları) gözlerde sulanma veya boğazda tahriş oluşabilir. Açık havada uzun süreli kalınacaksa dikkatli olunmalıdır. Belirti görülürse iç ortama geçilmesi önerilir.",
            #     "SO2 değerleri sağlıksız seviyelere ulaşmıştır. Solunum yollarında tahriş, öksürük ve gözlerde yanma gibi etkiler olabilir. Hassas bireyler mümkünse dış ortama çıkmamalıdır. İç mekânlar tercih edilmeli, havalandırma iyi yapılmalıdır.",
            #     "SO2 seviyesi tehlikeli düzeyde yüksektir. Açık havada bulunmak ciddi solunum problemlerine yol açabilir. Özellikle çocuklar, yaşlılar ve kronik hastalığı olanlar kapalı alanlarda kalmalıdır. Gerekiyorsa tıbbi yardım alınmalıdır."
            #    ],

            #     "CO": [
            #     "Karbonmonoksit seviyesi çok düşüktür. Hava kalitesi açısından herhangi bir risk oluşturmaz. Açık ve kapalı alanlarda herkes güvenle bulunabilir. Egzersiz yapmak veya dış ortamda uzun süre kalmak sakıncalı değildir.",
            #     "CO seviyeleri orta düzeydedir. Uzun süreli maruziyet bazı bireylerde baş ağrısı, halsizlik gibi belirtilere neden olabilir. Özellikle kapalı ve havasız alanlarda dikkatli olunmalıdır. Egzersiz yaparken ortamın havalandırıldığından emin olun.",
            #     "CO konsantrasyonu sağlıksız seviyeye ulaşmıştır. Baş dönmesi, mide bulantısı ve yorgunluk gibi etkiler görülebilir. Kapalı alanlar sıkça havalandırılmalı ve uzun süre kalmaktan kaçınılmalıdır. Belirti hissedildiğinde ortam terk edilmelidir.",
            #     "CO seviyesi tehlikeli boyuttadır. Bilinç kaybı ve bayılma riski ciddi şekilde artar. Kapalı ortamlarda durulmamalı, hemen temiz havaya çıkılmalıdır. Gerekirse acil tıbbi yardım alınmalıdır."
            #    ],

            #     "NO2": [
            #     "NO2 seviyesi çok düşüktür. Hava kalitesi oldukça iyidir ve dış ortam aktiviteleri herkes için güvenlidir. Solunum yolu üzerinde olumsuz bir etki beklenmez. Açık havada egzersiz ve yürüyüş yapılabilir.",
            #     "NO2 seviyeleri orta düzeydedir. Hassas bireylerde (özellikle astım ve bronşit hastaları) hafif semptomlar gelişebilir. Açık havada uzun süreli bulunma halinde dikkatli olunmalı, belirtiler takip edilmelidir.",
            #     "NO2 seviyesi sağlıksız aralığa ulaşmıştır. Boğazda yanma, gözlerde sulanma ve nefes darlığı gibi etkiler görülebilir. Özellikle çocuklar ve yaşlılar açık havada bulunmaktan kaçınmalıdır.",
            #     "NO2 düzeyi ciddi sağlık riski taşır. Akciğer fonksiyonlarını olumsuz etkileyebilir ve mevcut solunum hastalıklarını ağırlaştırabilir. Kapalı ortamlarda kalınmalı, dışarı çıkılması gerekiyorsa maske kullanılmalıdır."
            #    ],

            #     "NO": [
            #     "NO seviyesi oldukça düşüktür ve sağlık açısından herhangi bir risk teşkil etmez. Dış mekân aktiviteleri güvenle yapılabilir. Solunum yollarında olumsuz bir etki beklenmez. Hava kalitesi genel olarak iyidir.",
            #     "NO seviyesi orta düzeydedir. Özellikle hassas bireylerde (astım, KOAH hastaları) hafif solunum semptomları oluşabilir. Açık havada uzun süreli fiziksel aktivite yapılacaksa dikkatli olunmalıdır.",
            #     "NO seviyesi sağlıksız düzeydedir. Solunum yollarında tahriş, öksürük veya nefes darlığına neden olabilir. Kapalı ortamlarda kalmak ve gerekiyorsa maske takmak faydalı olacaktır.",
            #     "NO seviyesi yüksek ve tehlikelidir. Solunum sistemi üzerindeki etkileri ciddi olabilir. Özellikle hassas bireyler dışarı çıkmamalı, kapalı ortamlarda kalmalı ve tıbbi destek gerekebilir."
            #    ],

            #     "NOX": [
            #     "NOX seviyeleri oldukça düşüktür. Hava kalitesi sağlıklı ve güvenlidir. Herkes rahatlıkla dış ortamda vakit geçirebilir. Solunum yolu problemleri beklenmez.",
            #     "NOX seviyeleri orta düzeydedir. Özellikle hassas gruplar için (çocuklar, yaşlılar, astım hastaları) dikkatli olunmalıdır. Uzun süreli açık hava temasından kaçınmak faydalı olabilir.",
            #     "NOX seviyesi sağlıksız düzeydedir. Astım, bronşit gibi solunum hastalıklarını tetikleyebilir. Açık hava aktiviteleri azaltılmalı, kapalı ortamlarda kalınmalıdır.",
            #     "NOX konsantrasyonu tehlikeli düzeye ulaşmıştır. Solunum yolları üzerinde ciddi etkilere yol açabilir. Dışarı çıkılmamalı, pencere ve kapılar kapalı tutulmalıdır. Gerekiyorsa tıbbi destek alınmalıdır."
            #    ],

            #     "O3": [
            #     "Ozon seviyesi çok düşüktür ve hava kalitesi mükemmeldir. Açık havada kalmak herkes için güvenlidir. Spor ve yürüyüş gibi fiziksel aktiviteler gönül rahatlığıyla yapılabilir.",
            #     "Ozon seviyesi orta düzeydedir. Özellikle güneşli saatlerde hassas bireylerde gözlerde yanma veya hafif nefes darlığı oluşabilir. Uzun süreli dış ortam maruziyetinden kaçınılmalıdır.",
            #     "Ozon seviyesi sağlıksız seviyeye ulaşmıştır. Boğaz tahrişi, baş ağrısı ve nefes alma güçlüğü gibi belirtiler görülebilir. Öğle saatlerinde dışarıda bulunmak önerilmez.",
            #     "Ozon seviyesi çok yüksektir ve ciddi sağlık riskleri oluşturabilir. Güneşli saatlerde dış ortamdan uzak durulmalı, pencereler kapalı tutulmalıdır. Hassas bireyler kapalı, filtreli ortamlarda kalmalıdır."
            #    ]

            # }

            # if selected_pollutant in thresholds:
            #     p25, p50, p75 = thresholds[selected_pollutant]
            #     if prediction <= p25:
            #         bg_color = "#d4edda"
            #         border_color = "#28a745"
            #         explanation = explanations[selected_pollutant][0]
            #     elif prediction <= p50:
            #         bg_color = "#fff3cd"
            #         border_color = "#ffc107"
            #         explanation = explanations[selected_pollutant][1]
            #     elif prediction <= p75:
            #         bg_color = "#ffe0b2"
            #         border_color = "#f57c00"
            #         explanation = explanations[selected_pollutant][2]
            #     else:
            #         bg_color = "#f8d7da"
            #         border_color = "#dc3545"
            #         explanation = explanations[selected_pollutant][3]
            # else:
            #     bg_color = "#f0f9ff"
            #     border_color = "#2a9df4"
            #     explanation = ""

            # st.markdown(f"""
            # <div style='
            #     padding: 20px;
            #     margin-top: 20px;
            #     border-radius: 10px;
            #     background-color: {bg_color};
            #     border-left: 6px solid {border_color};
            #     text-align: center;'>
            #     <h3 style='color:{border_color}; margin-bottom: 10px;'>🌫️ {selected_pollutant} Tahmini</h3>
            #     <h2 style='font-size: 28px; font-weight: bold; margin: 0;'>{prediction:.2f} µg/m³</h2>
            #     <h style='font-size: 16px; color: #333;'>( Beklenen aralık: {lower:.2f} – {upper:.2f} µg/m³ )</h>
            #     <p style='margin-top: 15px; font-size: 18px; font-weight: 600; color: #333;'>{explanation}</p>
            # </div>
            # """, unsafe_allow_html=True)


# elif selected == "Genel HKİ Tahmini":
#     st.title("🌍 Genel Hava Kalitesi (HKİ) Tahmini")

#     now = datetime.datetime.now()
#     today = now.date()
#     next_full_hour = (now + datetime.timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)

#     ilceler = [
#         "Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler",
#         "Bakırköy", "Başakşehir", "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü",
#         "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy", "Esenler", "Esenyurt",
#         "Eyüpsultan", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane",
#         "Kartal", "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer",
#         "Silivri", "Sultanbeyli", "Sultangazi", "Şile", "Şişli", "Tuzla",
#         "Ümraniye", "Üsküdar", "Zeytinburnu"
#     ]

#     ilce = st.selectbox("İlçe Seçiniz", ilceler)

#     st.markdown("#### 🗓️ Tahmin Edilecek Tarih ve Saat")
#     col_date, col_time = st.columns(2)
#     with col_date:
#         selected_date = st.date_input("Tarih", value=today, min_value=today, label_visibility="collapsed")
#     with col_time:
#         selected_time = st.time_input("Saat", value=next_full_hour, step=datetime.timedelta(hours=1), label_visibility="collapsed")

#     selected_datetime = datetime.datetime.combine(selected_date, selected_time)
#     button_disabled = selected_datetime < now

#     if st.button("📥 Hava Durumu Verilerini Otomatik Doldur", disabled=button_disabled):
#         weather_data = get_weather_by_ilce(ilce, selected_datetime)
#         if weather_data:
#             st.success("✅ Veriler başarıyla alındı!")
#             st.session_state["auto_weather_hki"] = weather_data
#         else:
#             st.warning("⚠️ API'den veri alınamadı.")

#     weather = st.session_state.get("auto_weather_hki", {})

#     # 📂 Detaylı veri gösterme kutusu
#     show_inputs = st.checkbox("📂 Detaylı Hava Durumu Verilerini Göster", value=False)

#     if show_inputs:
#     # Kullanıcının doldurduğu inputlardan veri topla
#         temp = st.number_input("Sıcaklık (°C)", value=weather.get("temp", 15.0))
#         feelslike = st.number_input("Hissedilen Sıcaklık (°C)", value=weather.get("feelslike", 14.0))
#         humidity = st.slider("Nem (%)", 0, 100, int(weather.get("humidity", 50)))
#         dew = st.number_input("Çiy Noktası (°C)", value=weather.get("dew", 10.0))
#         windgust = st.number_input("Rüzgar Ani Hızı (km/h)", value=weather.get("windgust", 20.0))
#         windspeed = st.number_input("Rüzgar Hızı (km/h)", value=weather.get("windspeed", 10.0))
#         winddir = st.slider("Rüzgar Yönü (0°-360°)", 0, 360, int(weather.get("winddir", 180)))
#         pressure = st.number_input("Basınç (hPa)", value=weather.get("pressure", 1012.0))
#         cloudcover = st.slider("Bulutluluk (%)", 0, 100, int(weather.get("cloudcover", 50)))
#         solarradiation = st.number_input("Güneş Radyasyonu (W/m²)", value=weather.get("solarradiation", 200.0))
#         visibility = st.number_input("Görünürlülük (km)", value=weather.get("visibility", 10.0))

#     else:
#     # Otomatik API'den gelen verilerle doldur
#         temp = weather.get("temp", 15.0)
#         feelslike = weather.get("feelslike", 14.0)
#         humidity = weather.get("humidity", 50)
#         dew = weather.get("dew", 10.0)
#         windgust = weather.get("windgust", 20.0)
#         windspeed = weather.get("windspeed", 10.0)
#         winddir = weather.get("winddir", 180)
#         pressure = weather.get("pressure", 1012.0)
#         cloudcover = weather.get("cloudcover", 50)
#         solarradiation = weather.get("solarradiation", 200.0)
#         visibility = weather.get("visibility", 10.0)

# # 🧠 Burada ortak olarak input_data her zaman tanımlanacak:
#     weather_group_code = st.session_state.weather_group_code

#     input_dict = {
#         'temp': temp,
#         'feelslike': feelslike,
#         'humidity': humidity,
#         'dew': dew,
#         'windgust': windgust,
#         'windspeed': windspeed,
#         'pressure': pressure,
#         'cloudcover': cloudcover,
#         'visibility': visibility,
#         'solarradiation': solarradiation,
#         'uvindex': weather.get("uvindex", 5),
#         'weather_group_code': weather_group_code,
#         'hour': selected_time.hour,
#         'day': selected_date.day,
#         'month': selected_date.month,
#         'dayofweek': selected_date.weekday(),
#         'season': (selected_date.month % 12) // 3 + 1,
#         'wind_dir_rad': np.deg2rad(winddir),
#         'wind_dir_sin': np.sin(np.deg2rad(winddir)),
#         'wind_dir_cos': np.cos(np.deg2rad(winddir)),
#         'humidity_level': humidity / 100,
#         'feelslike_diff': abs(temp - feelslike),
#         'is_rainy': 1 if weather_group_code == 3 else 0,
#         'is_weekend': 1 if selected_date.weekday() >= 5 else 0,
#         'is_nighttime': 1 if selected_time.hour < 6 or selected_time.hour > 22 else 0,
#         'is_rush_hour': 1 if (7 <= selected_time.hour <= 9 or 17 <= selected_time.hour <= 19) else 0,
#         'humid_heat_index': (humidity / 100) * feelslike,
#         'uv_level': 0 if weather.get("uvindex", 5) <= 2 else (1 if weather.get("uvindex", 5) <= 5 else 2)
#     }

#     input_data = pd.DataFrame([input_dict])


#  # Tahmin butonu
#     if st.button("🌍 Genel HKİ Tahminini Hesapla"):
#             if selected_datetime < now:
#                  st.error("⚠️ Geçmiş saat ile tahmin yapılamaz!")
#             else:
#                 pollutant_models = {
#                     "PM10": "pm10_model.pkl",
#                     "SO2": "so2_model.pkl",
#                     "CO": "co_model.pkl",
#                     "NO2": "no2_model.pkl",
#                     "O3": "o3_model.pkl"
#                 }

#                 thresholds = {
#                     "PM10": [23.8, 35.1, 47.1],
#                     "SO2": [1.6, 2.3, 3.2],
#                     "CO": [521.3, 724.6, 1007.2],
#                     "NO2": [24.9, 35.7, 51.2],
#                     "O3": [19.8, 37.8, 55.0]
#                 }

#                 class_names = ["İyi", "Fena Değil", "Hassas Gruplar için Riskli", "Kötü"]
#                 results = {}

#                 for pol, model_path in pollutant_models.items():
#                     with open(model_path, "rb") as f:
#                         data = pickle.load(f)
#                     model = data["model"]
#                     features = data["features"]
#                     pred = model.predict(input_data[features])[0]

#                     p25, p50, p75 = thresholds[pol]
#                     if pred <= p25:
#                         pol_class = 1
#                     elif pred <= p50:
#                         pol_class = 2
#                     elif pred <= p75:
#                         pol_class = 3
#                     else:
#                         pol_class = 4
#                     results[pol] = {"prediction": pred, "class": pol_class}

#                 # En kötü (en yüksek) sınıfı bul
#                 worst_pollutant = max(results, key=lambda x: results[x]["class"])
#                 genel_sinif = results[worst_pollutant]["class"]

#                 # Renk ayarları
#                 color_codes = {1: "#d4edda", 2: "#fff3cd", 3: "#ffe0b2", 4: "#f8d7da"}
#                 border_codes = {1: "#28a745", 2: "#ffc107", 3: "#f57c00", 4: "#dc3545"}

#                 explanations = {
#                     1: "Hava kalitesi iyi. Dışarıda zaman geçirebilirsiniz.",
#                     2: "Hava kalitesi fena değil. Hassas gruplar dikkatli olmalı.",
#                     3: "Hava hassas gruplar için riskli. Dikkatli olunmalı.",
#                     4: "Hava kalitesi kötü. Dışarı çıkmaktan kaçının."
#                 }

#                 st.markdown(f"""
#                 <div style='padding: 20px; margin-top: 20px; border-radius: 10px;
#                     background-color: {color_codes[genel_sinif]};
#                     border-left: 6px solid {border_codes[genel_sinif]};
#                     text-align: center;'>
#                     <h3 style='color:{border_codes[genel_sinif]};'>🌍 Genel Hava Kalitesi Durumu:</h3>
#                     <h2>{class_names[genel_sinif-1]}</h2>
#                     <p style='font-size:18px;'>En etkili kirletici: <strong>{worst_pollutant}</strong> ({results[worst_pollutant]["prediction"]:.2f} µg/m³)</p>
#                     <p>{explanations[genel_sinif]}</p>
#                 </div>
#                 """, unsafe_allow_html=True)


# elif selected == "Ana Sayfa":
#     st.title("🏠 Ana Sayfa")
#     st.header("🌫️ Hava Kirliliği Nedir?")

#     st.markdown("""
#     <div style='text-align: left ; font-size: 18px;'>
#         <p>
#           Hava kirliliği, atmosferde insan sağlığı ve çevresel denge üzerinde olumsuz etkilere yol açabilecek düzeyde zararlı gazların, partiküllerin ve 
#           kimyasal bileşiklerin birikmesiyle oluşur. Başta fosil yakıt tüketimi olmak üzere sanayi faaliyetleri, motorlu taşıt emisyonları, 
#           enerji üretimi ve ısınma gibi insan kaynaklı etkenler, hava kalitesinin bozulmasında büyük rol oynamaktadır. Bu süreçte PM10, SO₂, CO, NO₂, NO, NOₓ ve O₃ 
#           gibi çeşitli hava kirleticileri doğrudan veya dolaylı yollarla atmosfere yayılmakta ve yoğunlaştıkça insan sağlığını tehdit edici seviyelere ulaşabilmektedir.     
#        </p> 
          
#        <p>    
#          Hava kirliliği; solunum yolu hastalıkları, kalp-damar rahatsızlıkları, alerjik reaksiyonlar ve hatta erken ölümler gibi ciddi sağlık sorunlarına yol açabilmektedir.
#          Dünya Sağlık Örgütü (WHO), hava kirliliğini günümüzde insan sağlığını tehdit eden en büyük çevresel risk faktörlerinden biri olarak tanımlamaktadır.     
#        </p>       
#     </div>           
#     """,unsafe_allow_html=True)

#     st.markdown("<div style='padding-top: 10px;'></div>", unsafe_allow_html=True)
#     col1, col2 = st.columns(2)

#     with col1:
#      image = Image.open("images/image1.png")
#      resized_image = image.resize((400, 400))  # (genişlik, yükseklik)
#      st.image(resized_image)

#     with col2:
#      image = Image.open("images/image2.png")
#      resized_image = image.resize((400, 400))  # (genişlik, yükseklik)
#      st.image(resized_image)


#     st.header(" İstanbul’da Hava Kirliliği")
#     st.markdown("""
#     <div style='padding-bottom: 20px; text-align: left ; font-size: 18px;'>            
#        <p>
#           İstanbul, coğrafi ve demografik özellikleri itibarıyla Türkiye'nin hava kirliliği açısından en riskli kentlerinden biridir.
#           Yaklaşık 16 milyonluk nüfusu, yoğun araç trafiği, sanayi tesisleri, bireysel ısınma yöntemleri ve kentsel yapılaşma yoğunluğu İstanbul’u çevresel 
#           açıdan kırılgan hale getirmektedir. Özellikle sabah ve akşam saatlerinde Boğaz köprülerinde yaşanan trafik yoğunluğu ciddi miktarda motorlu taşıt emisyonuna yol açmakta,
#           egzoz gazları ile partikül madde (PM10), azot dioksit (NO₂) ve karbon monoksit (CO) gibi zararlı kirleticiler şehir atmosferine karışmaktadır. 
#           Yüksek yapılaşmanın ve dar sokakların olduğu bölgelerde bu emisyonların dağılması güçleşmekte ve yer seviyesinde birikime neden olmaktadır.      
#        </p> 
          
#        <p>    
#          Kış aylarında fosil yakıt kullanımına dayalı bireysel ısınma, özellikle düşük gelirli semtlerde kalitesiz yakıt kullanımıyla birleştiğinde hava kalitesini ciddi biçimde
#          bozmaktadır. Bacalardan çıkan dumanlar yoğun konut bölgelerine yayılırken, rüzgarsız ve ters sıcaklık tabakası (inversiyon) gibi meteorolojik koşullar kirleticilerin
#          uzun süre atmosferde kalmasına sebep olur. İstanbul’un topografyası da bu sorunu derinleştiren bir faktördür; belirli bölgelerde kirli hava tabakası yer
#          seviyesinde hapsolmakta ve solunan havanın kalitesini ciddi biçimde düşürmektedir.      
#        </p> 
                
#        <p>    
#           Sanayi tesisleri de hava kirliliğinde önemli bir yer tutmaktadır. Şehrin çeperlerinde ve bazı iç bölgelerde konumlanan bu tesisler, 
#           özellikle akşam saatlerinde yoğun gaz ve duman salımı yaparak sadece havayı değil, aynı zamanda genel yaşam kalitesini ve ekolojik dengeleri tehdit etmektedir.
#           Bu kirleticiler tarım arazileri, su kaynakları ve doğal yaşam alanları üzerinde de olumsuz etkilere yol açabilir.      
#        </p>
                
#        <p>    
#           Dünya Sağlık Örgütü (WHO) sınır değerlerine göre İstanbul’un bazı bölgelerinde yıl boyunca PM10 ve NO₂ seviyeleri kritik eşikleri aşmakta, 
#           bu da başta astım ve KOAH olmak üzere pek çok solunum yolu hastalığını tetiklemektedir. Kentin sürdürülebilirliği, yaşam kalitesinin artırılması ve halk sağlığının 
#           korunması için ulaşım sistemlerinin modernleştirilmesi, temiz enerji kaynaklarının teşvik edilmesi, sanayi emisyonlarının sıkı biçimde
#           denetlenmesi ve bireysel farkındalık çalışmalarının yaygınlaştırılması büyük önem taşımaktadır.
#        </p>
                                                  
#     </div>            
#     """,unsafe_allow_html=True)

#     col1, col2 = st.columns(2)

#     with col1:
#      image = Image.open("images/image11.png")
#      resized_image = image.resize((700, 400))  # (genişlik, yükseklik)
#      st.image(resized_image)

#     with col2:
#      image = Image.open("images/image7.png")
#      resized_image = image.resize((700, 400))  # (genişlik, yükseklik)
#      st.image(resized_image)

#     col1, col2 = st.columns(2)

#     with col1:
#      image = Image.open("images/image9.png")
#      resized_image = image.resize((700, 400))  # (genişlik, yükseklik)
#      st.image(resized_image)

#     with col2:
#      image = Image.open("images/image10.png")
#      resized_image = image.resize((700, 400))  # (genişlik, yükseklik)
#      st.image(resized_image)




#     st.header("🤖 Bu Uygulama Ne Sunar?")
#     st.markdown("""
#     <div style='padding-bottom: 20px; text-align: left ; font-size: 18px;'>                     
#               Bu uygulama, meteorolojik veriler doğrultusunda hava kirleticilerinin (PM10, SO₂, CO, NO₂, NOX, NO ve O₃) tahminini yaparak kullanıcıları olası hava kirliliği düzeyleri
#               hakkında önceden bilgilendirmeyi hedeflemektedir. Geliştirilen makine öğrenmesi modelleri sayesinde kullanıcı, sıcaklık, nem, rüzgar gibi hava durumu parametrelerini
#               girerek geleceğe yönelik kirletici seviyelerini tahmin edebilir. Bu sayede bireyler; spor, ulaşım, dış mekân etkinlikleri gibi günlük planlarını daha sağlıklı bir 
#               çevresel farkındalıkla yapabileceklerdir.
#               Uygulama aynı zamanda model performanslarını görselleştiren araçlar, zamana bağlı analizler ve özellik önem grafikleriyle kullanıcıya derinlemesine bilgi sunmaktadır.
#               Amaç yalnızca tahmin sunmak değil; aynı zamanda farkındalık yaratmak ve kullanıcıyı bilinçli kararlar alma yönünde desteklemektir.            
#     </div>             
#     """,unsafe_allow_html=True)

#     st.markdown("""
#    <div style='
#         background-color: #fff3cd;
#         padding: 15px 20px;
#         margin-top: 45px;
#         border-radius: 8px;
#         font-size: 16px;'
#     >
#     <b>📌 Bilgilendirme:</b><br>
#     Bu uygulama, hava durumu verilerine dayalı olarak makine öğrenmesi modelleriyle hava kirleticilerine ilişkin tahmini bilgiler sunar. 
#     Elde edilen sonuçlar, <b>kesin değerler</b> olmayıp yalnızca <i>bilgilendirme ve farkındalık</i> amacı taşımaktadır. 
#     Hava kalitesiyle ilgili alınacak kararlar için <b>resmî hava kalitesi ölçüm sistemleri</b> ve <b>yetkili kurumlar</b> tarafından sağlanan güncel veriler esas alınmalıdır.
#     </div>
#     """, unsafe_allow_html=True)


    

    







# elif selected == "Veri Analizi":
#     st.title("📊 Veri Analizi ve Görselleştirme")

#     pollutant_options = ['PM10', 'SO2', 'CO', 'NO2', 'NOX', 'NO', 'O3']
#     selected_pollutant = st.selectbox("🔬 İncelenecek Kirletici:", pollutant_options)

#     viz_option = st.radio("📈 Görselleştirme Türü Seçin", [
#         "📊 Dağılım Grafiği",
#         "⏱️ Zaman Bazlı Değişim",
#         "📉 Özellik Önemi (Model)",
#         "🎯 Gerçek vs Tahmin",
#         "🧩 Tahmin Hatası Dağılımı"
#     ])

#     # 1. Dağılım Grafiği
#     if viz_option == "📊 Dağılım Grafiği":
#         st.subheader(f"{selected_pollutant} - Dağılım Grafiği")
#         fig, ax = plt.subplots()
#         sns.histplot(df[selected_pollutant], bins=30, kde=True, ax=ax, color="skyblue")
#         ax.set_xlabel(f"{selected_pollutant} Seviyesi µg/m³")
#         ax.set_ylabel("Frekans")
#         st.pyplot(fig)

#     # 2. Zaman Bazlı Değişim
#     elif viz_option == "⏱️ Zaman Bazlı Değişim":
#         st.subheader(f"{selected_pollutant} - Zamana Bağlı Ortalama")

#         time_granularity = st.radio("Zaman Türü Seçin:", ["Saatlik Ortalama", "Aylık Ortalama"], horizontal=True)

#         if time_granularity == "Saatlik Ortalama":
#             if 'hour' in df.columns:
#                 hourly_avg = df.groupby("hour")[selected_pollutant].mean()
#                 fig, ax = plt.subplots()
#                 hourly_avg.plot(kind="line", marker="o", color="tomato", ax=ax)
#                 ax.set_xlabel("Saat")
#                 ax.set_ylabel(f"{selected_pollutant} Ortalaması µg/m³")
#                 st.pyplot(fig)

#                 # Saatlik yorumlar
#                 if selected_pollutant == "O3":
#                     st.info("☀️ **O3 (Ozon):** Öğleden sonra güneş ışığı ile NOx tepkimeleri sonucunda artar. 14:00–16:00 arası zirve yapması tipiktir. Gece seviyeleri düşer.")
#                 elif selected_pollutant == "PM10":
#                     st.info("🌫️ **PM10:** Gece saatlerinde (22:00–01:00) artış gözlenir. Bu durum, ısınma ve düşük hava sirkülasyonuna bağlı olabilir. Gün içinde ise daha stabil seyreder.")
#                 elif selected_pollutant == "SO2":
#                     st.info("🔥 **SO2:** Öğleden sonra 15:00 civarında zirve yapması sanayi kaynaklı olabilir. Gece ve sabah saatlerinde düşüş gözlenmiştir.")
#                 elif selected_pollutant == "CO":
#                     st.info("🚗 **CO:** Sabah saatlerinde ani artış trafik etkisini gösterebilir. 14:00 civarındaki ikinci zirve sanayi veya yoğun kent içi etkileşimle açıklanabilir.")
#                 elif selected_pollutant == "NO2":
#                     st.info("🛣 **NO2:** Gece ve akşam saatlerinde yüksek, öğlen düşük. Bu durum güneşli havalarda NO2'nin fotokimyasal parçalanmasıyla açıklanabilir.")
#                 elif selected_pollutant == "NOX":
#                     st.info("🏭 **NOX:** Sabah ve gece zirveleri trafiğe ve ısınma kaynaklı emisyonlara işaret eder. Öğle saatlerinde düşüş tipiktir.")
#                 elif selected_pollutant == "NO":
#                     st.info("🚦 **NO:** Sabah saatlerinde 08–10 arası yoğunluk gösterir. Bu durum doğrudan egzoz emisyonlarıyla ilişkilidir.")
            
#         elif time_granularity == "Aylık Ortalama":
#             if 'month' in df.columns:
#                 monthly_avg = df.groupby("month")[selected_pollutant].mean()
#                 fig, ax = plt.subplots()
#                 monthly_avg.plot(kind="line", marker="o", color="seagreen", ax=ax)
#                 ax.set_xlabel("Ay (1=Ocak, 12=Aralık)")
#                 ax.set_ylabel(f"{selected_pollutant} Ortalaması")
#                 st.pyplot(fig)

#                 # Aylık yorumlar
#                 if selected_pollutant == "O3":
#                     st.info("☀️ **O3 (Ozon):** Yaz aylarında (Haziran–Ağustos) artar çünkü güneş ışığı fotokimyasal reaksiyonları tetikler. Kışın düşük seviyelerde seyreder.")
#                 elif selected_pollutant == "PM10":
#                     st.info("🌫️ **PM10:** Kış aylarında ve sonbaharda artış eğilimi gösterir. Isıtma kaynaklı emisyonlar ve düşük hava sirkülasyonu etkili olabilir.")
#                 elif selected_pollutant == "SO2":
#                     st.info("🔥 **SO2:** Kış aylarında (Ocak–Mart) zirve yapar. Fosil yakıtla ısınma etkisi belirgindir. Yaz aylarında düşer.")
#                 elif selected_pollutant == "CO":
#                     st.info("🚗 **CO:** Kış aylarında ısınma ve trafik etkisiyle artış olabilir. Yaz döneminde değerler dalgalı olabilir, bazı yerel etkiler gözlenebilir.")
#                 elif selected_pollutant == "NO2":
#                     st.info("🛣 **NO2:** Kış aylarında daha yüksek seviyelere ulaşır. Bu durum düşük hava sirkülasyonu ve güneş eksikliği ile açıklanabilir.")
#                 elif selected_pollutant == "NOX":
#                     st.info("🏭 **NOX:** Kış ve ilkbahar aylarında yüksek, yazın düşüş gösterir. Trafik ve ısınma kaynaklı emisyonların etkisi büyüktür.")
#                 elif selected_pollutant == "NO":
#                     st.info("🚦 **NO:** Kış aylarında zirve yapar. Trafik ve ısınma etkisiyle oluşan doğrudan emisyonları yansıtır. Yaz aylarında düşer.")
      

#     # 3. Özellik Önemi
#     elif viz_option == "📉 Özellik Önemi (Model)":
#         st.subheader(f"{selected_pollutant} - Özellik Önem Grafiği")
#         with open(f"{selected_pollutant.lower()}_model.pkl", "rb") as f:
#             model_data = pickle.load(f)
#         model = model_data["model"]
#         features = model_data["features"]
#         importances = model.feature_importances_

#         importance_df = pd.DataFrame({
#             "Feature": features,
#             "Importance": importances
#         }).sort_values(by="Importance", ascending=False)

#         fig, ax = plt.subplots()
#         sns.barplot(x="Importance", y="Feature", data=importance_df.head(10), ax=ax, palette="viridis")
#         ax.set_title("En Önemli Özellikler")
#         st.pyplot(fig)

#     # 4. Gerçek vs Tahmin
#     elif viz_option == "🎯 Gerçek vs Tahmin":
#         st.subheader(f"{selected_pollutant} - Gerçek vs Tahmin")
#         with open(f"{selected_pollutant.lower()}_model.pkl", "rb") as f:
#             model_data = pickle.load(f)
#         model = model_data["model"]
#         features = model_data["features"]

#         X = df[features]
#         y_true = df[selected_pollutant]
#         y_pred = model.predict(X)

#         fig, ax = plt.subplots()
#         ax.scatter(y_true, y_pred, alpha=0.3, color="mediumseagreen")
#         ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
#         ax.set_xlabel("Gerçek Değer")
#         ax.set_ylabel("Tahmin Edilen")
#         ax.set_title("Gerçek vs Tahmin Grafiği")
#         st.pyplot(fig)

#     elif viz_option == "🧩 Tahmin Hatası Dağılımı":
#         st.subheader(f"{selected_pollutant} - Tahmin Hatası Dağılımı")
#         with open(f"{selected_pollutant.lower()}_model.pkl", "rb") as f:
#             model_data = pickle.load(f)
#         model = model_data["model"]
#         features = model_data["features"]

#         X = df[features]
#         y_true = df[selected_pollutant]
#         y_pred = model.predict(X)

#         residuals = y_true - y_pred

#         fig, ax = plt.subplots()
#         sns.histplot(residuals, bins=50, kde=True, color="salmon", ax=ax)
#         ax.set_xlabel("Tahmin Hatası (Gerçek - Tahmin)")
#         ax.set_ylabel("Frekans")
#         ax.set_title("Hata Dağılımı")
#         st.pyplot(fig)

#         st.info("ℹ️ Hataların sıfıra yakın ve simetrik dağılması modelin iyi genelleştirdiğini gösterir.")
    
    






# elif selected == "Dokümantasyon":
#     st.title("ℹ️ Dokümantasyon")
  

