import requests
import datetime

API_KEY = "TMETWPYHK5LX45VNWZ4PSDJWF"
LOG_FILE = "api_log.txt"

def get_weather_by_ilce(ilce, selected_datetime):
    location = f"{ilce} istanbul"
    datetime_str = selected_datetime.strftime('%Y-%m-%dT%H:%M:%S')

    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/"
        f"timeline/{location}/{datetime_str}"
        f"?unitGroup=metric&key={API_KEY}&include=hours&contentType=json"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        query_cost = data.get("queryCost", "Bilinmiyor")
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"[{now_str}] İlçe: {ilce}, Tarih/Saat: {selected_datetime}, QueryCost: {query_cost}\n"
        print(log_entry.strip())

        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)

        # Saatlik verilerden en yakını seç
        hours_data = data.get("days", [])[0].get("hours", [])
        hedef_saat = selected_datetime.hour
        en_yakin = min(hours_data, key=lambda h: abs(int(h["datetime"].split(":")[0]) - hedef_saat))

        return {
            "temp": en_yakin.get("temp", 15.0),
            "feelslike": en_yakin.get("feelslike", 14.0),
            "humidity": en_yakin.get("humidity", 50),
            "dew": en_yakin.get("dew", 10.0),
            "pressure": en_yakin.get("pressure", 1012.0),
            "windspeed": en_yakin.get("windspeed", 10.0),
            "windgust": en_yakin.get("windgust", 20.0),
            "winddir": en_yakin.get("winddir", 180),
            "cloudcover": en_yakin.get("cloudcover", 50),
            "uvindex": en_yakin.get("uvindex", 5),
            "visibility": en_yakin.get("visibility", 10.0),
            "solarradiation": en_yakin.get("solarradiation", 200.0),
        }

    except Exception as e:
        print("❌ API Hatası:", e)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] HATA: {e}\n")
        return None
