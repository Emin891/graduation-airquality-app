import streamlit as st
import pandas as pd
import pickle
import os
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("cleaned_final.csv")


def show():
    st.title("📊 Data Analysis and Visualization")

    pollutant_options = ['PM10', 'SO2', 'CO', 'NO2', 'NOX', 'NO', 'O3']
    selected_pollutant = st.selectbox("🔬 Pollutant to be Analyzed:", pollutant_options)

    viz_option = st.radio("📈 Select Visualization Type", [
        "📊 Scatter Plot",
        "⏱️ Time Based Change",
        "📉 Feature Importance (Model)",
        "🎯 Actual vs Predicted",
        "🧩 Prediction Error Distribution"
    ])

    # 1. Dağılım Grafiği
    if viz_option == "📊 Scatter Plot":
        st.subheader(f"{selected_pollutant} - Scatter Plot")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_pollutant], bins=30, kde=True, ax=ax, color="skyblue")
        ax.set_xlabel(f"{selected_pollutant} Level µg/m³")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # 2. Zaman Bazlı Değişim
    elif viz_option == "⏱️ Time Based Change":
        st.subheader(f"{selected_pollutant} - Time Based Change")

        time_granularity = st.radio("Select Time Type:", ["Hourly Average", "Monthly Average"], horizontal=True)

        if time_granularity == "Hourly Average":
            if 'hour' in df.columns:
                hourly_avg = df.groupby("hour")[selected_pollutant].mean()
                fig, ax = plt.subplots()
                hourly_avg.plot(kind="line", marker="o", color="tomato", ax=ax)
                ax.set_xlabel("Hour")
                ax.set_ylabel(f"{selected_pollutant} Average µg/m³")
                st.pyplot(fig)

                if selected_pollutant == "O3":
                    st.info("☀️ **O₃ (Ozone):** Increases in the afternoon due to photochemical reactions with NOx under sunlight. Typically peaks between 14:00–16:00. Levels drop at night.")
                elif selected_pollutant == "PM10":
                    st.info("🌫️ **PM₁₀:** Shows an increase during late evening hours (22:00–01:00), possibly due to heating and low air circulation. It tends to remain more stable during the day.")
                elif selected_pollutant == "SO2":
                    st.info("🔥 **SO₂:** Peaks around 15:00 in the afternoon, possibly due to industrial sources. A decrease is observed during night and morning hours.")
                elif selected_pollutant == "CO":
                    st.info("🚗 **CO:** Sudden spikes in the morning may indicate traffic influence. A second peak around 14:00 may be due to industrial activity or intense urban interaction.")
                elif selected_pollutant == "NO2":
                    st.info("🛣 **NO₂:** Higher at night and in the evening, lower at noon. This is likely due to photochemical breakdown of NO₂ in sunny conditions.")
                elif selected_pollutant == "NOX":
                    st.info("🏭 **NOx:** Morning and night peaks suggest emissions from traffic and heating. A drop around midday is typical.")
                elif selected_pollutant == "NO":
                    st.info("🚦 **NO:** Shows peak levels between 08:00–10:00 in the morning. This is directly associated with vehicle exhaust emissions.")
            
        elif time_granularity == "Monthly Average":
            if 'month' in df.columns:
                monthly_avg = df.groupby("month")[selected_pollutant].mean()
                fig, ax = plt.subplots()
                monthly_avg.plot(kind="line", marker="o", color="seagreen", ax=ax)
                ax.set_xlabel("Ay (1=January, 12=December)")
                ax.set_ylabel(f"{selected_pollutant} Avarage")
                st.pyplot(fig)

                if selected_pollutant == "O3":
                    st.info("☀️ **O₃ (Ozone):** Increases during summer months (June–August) as sunlight triggers photochemical reactions. Levels are lower in winter.")
                elif selected_pollutant == "PM10":
                    st.info("🌫️ **PM₁₀:** Tends to rise in winter and autumn. This may be due to emissions from heating and reduced air circulation.")
                elif selected_pollutant == "SO2":
                    st.info("🔥 **SO₂:** Peaks in winter (January–March) due to fossil fuel-based heating. Drops during the summer months.")
                elif selected_pollutant == "CO":
                    st.info("🚗 **CO:** Increases in winter due to heating and traffic. In summer, levels may fluctuate due to local effects.")
                elif selected_pollutant == "NO2":
                    st.info("🛣 **NO₂:** Reaches higher levels in winter, likely due to low air circulation and lack of sunlight.")
                elif selected_pollutant == "NOX":
                    st.info("🏭 **NOx:** Higher in winter and spring, drops in summer. Traffic and heating emissions are major contributors.")
                elif selected_pollutant == "NO":
                    st.info("🚦 **NO:** Peaks in winter, reflecting direct emissions from traffic and heating. Declines in the summer months.")

      

        # 3. Feature Importance
    elif viz_option == "📉 Feature Importance (Model)":
        st.subheader(f"{selected_pollutant} - Feature Importance Plot")
        model_path = os.path.join(os.path.dirname(__file__), "..", "models", f"{selected_pollutant.lower()}_model.pkl")
        with open(model_path, "rb") as f:
            model_data = pickle.load(f)
        model = model_data["model"]
        features = model_data["features"]
        importances = model.feature_importances_

        importance_df = pd.DataFrame({
            "Feature": features,
            "Importance": importances
        }).sort_values(by="Importance", ascending=False)

        fig, ax = plt.subplots()
        sns.barplot(x="Importance", y="Feature", data=importance_df.head(10), ax=ax, palette="viridis")
        ax.set_title("Top Important Features")
        st.pyplot(fig)

    # 4. Actual vs Predicted
    elif viz_option == "🎯 Actual vs Predicted":
        st.subheader(f"{selected_pollutant} - Actual vs Predicted")
        model_path = os.path.join(os.path.dirname(__file__), "..", "models", f"{selected_pollutant.lower()}_model.pkl")
        with open(model_path, "rb") as f:
            model_data = pickle.load(f)
        model = model_data["model"]
        features = model_data["features"]

        X = df[features]
        y_true = df[selected_pollutant]
        y_pred = model.predict(X)

        fig, ax = plt.subplots()
        ax.scatter(y_true, y_pred, alpha=0.3, color="mediumseagreen")
        ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
        ax.set_xlabel("Actual Value")
        ax.set_ylabel("Predicted Value")
        ax.set_title("Actual vs Predicted Plot")
        st.pyplot(fig)

    # 5. Residual Error Distribution
    elif viz_option == "🧩 Prediction Error Distribution":
        st.subheader(f"{selected_pollutant} - Prediction Error Distribution")
        model_path = os.path.join(os.path.dirname(__file__), "..", "models", f"{selected_pollutant.lower()}_model.pkl")
        with open(model_path, "rb") as f:
            model_data = pickle.load(f)
        model = model_data["model"]
        features = model_data["features"]

        X = df[features]
        y_true = df[selected_pollutant]
        y_pred = model.predict(X)

        residuals = y_true - y_pred

        fig, ax = plt.subplots()
        sns.histplot(residuals, bins=50, kde=True, color="salmon", ax=ax)
        ax.set_xlabel("Prediction Error (Actual - Predicted)")
        ax.set_ylabel("Frequency")
        ax.set_title("Residual Error Distribution")
        st.pyplot(fig)

        st.info("ℹ️ A residual distribution centered around zero and shaped symmetrically indicates good model generalization.")
