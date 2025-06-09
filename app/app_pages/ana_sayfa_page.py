import streamlit as st
from PIL import Image


def show():
    st.title("🏠 Home Page")
    st.header("🌫️ What is air pollution?")

    st.markdown("""
    <div style='text-align: left ; font-size: 18px;'>
        <p>
          Air pollution occurs when harmful gases, particles, and chemical compounds accumulate in the atmosphere at levels that can negatively affect human health and environmental balance.
          Human-induced factors such as fossil fuel consumption, industrial activities, motor vehicle emissions, energy production, and heating play a major role in the deterioration of air quality.
          In this process, various air pollutants such as PM10, SO₂, CO, NO₂, NO, NOₓ, and O₃ are released into the atmosphere directly or indirectly, and as they become more concentrated, they can reach levels that pose a threat to human health.    
       </p> 
          
       <p>    
         Air pollution can lead to serious health problems such as respiratory diseases, cardiovascular disorders, allergic reactions, and even premature deaths.
          The World Health Organization (WHO) defines air pollution as one of the greatest environmental risk factors threatening human health today.     
       </p>       
    </div>           
    """,unsafe_allow_html=True)

    st.markdown("<div style='padding-top: 10px;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
     image = Image.open("images/image1.png")
     resized_image = image.resize((400, 400))  
     st.image(resized_image)

    with col2:
     image = Image.open("images/image2.png")
     resized_image = image.resize((400, 400))  
     st.image(resized_image)


    st.header("Air Pollution in Istanbul")
    st.markdown("""
    <div style='padding-bottom: 20px; text-align: left ; font-size: 18px;'>            
       <p>
          Due to its geographical and demographic characteristics, Istanbul is one of the most at-risk cities in Turkey in terms of air pollution.
          Its population of approximately 16 million, heavy vehicle traffic, industrial facilities, individual heating methods, and dense urbanization make Istanbul environmentally vulnerable.
          Especially during morning and evening hours, the intense traffic on the Bosphorus bridges results in significant motor vehicle emissions, releasing harmful pollutants such as
          exhaust gases, particulate matter (PM10), nitrogen dioxide (NO₂), and carbon monoxide (CO) into the city’s atmosphere.
          In areas with high-rise buildings and narrow streets, the dispersion of these emissions becomes more difficult, leading to accumulation at ground level.      
       </p> 
          
       <p>    
         During the winter months, individual heating based on fossil fuel use significantly degrades air quality, especially when combined with the use of low-quality fuels in low-income neighborhoods.
         Smoke emitted from chimneys spreads across densely populated residential areas, while meteorological conditions such as windless weather and temperature inversions cause pollutants to remain in the atmosphere for extended periods.
         Istanbul’s topography further exacerbates this issue; in certain areas, layers of polluted air become trapped at ground level, severely reducing the quality of the air people breathe.      
       </p> 
                
       <p>    
          Industrial facilities also play a significant role in air pollution. Located on the outskirts and in some inner parts of the city, these facilities often release large amounts of gas and smoke,
          especially during evening hours, threatening not only air quality but also overall quality of life and ecological balance.
          These pollutants can also have negative impacts on agricultural lands, water resources, and natural habitats.      
       </p>
                
       <p>    
          According to the World Health Organization (WHO) threshold values, PM10 and SO₂ levels in certain areas of Istanbul exceed critical limits throughout the year, triggering numerous respiratory diseases, particularly asthma and COPD.
          In order to enhance the city's sustainability, improve quality of life, and protect public health, it is crucial to modernize transportation systems, promote clean energy sources, strictly regulate industrial emissions,
          and expand public awareness initiatives.
       </p>
                                                  
    </div>            
    """,unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
     image = Image.open("images/image11.png")
     resized_image = image.resize((700, 400))  
     st.image(resized_image)

    with col2:
     image = Image.open("images/image7.png")
     resized_image = image.resize((700, 400)) 
     st.image(resized_image)

    col1, col2 = st.columns(2)

    with col1:
     image = Image.open("images/image9.png")
     resized_image = image.resize((700, 400)) 
     st.image(resized_image)

    with col2:
     image = Image.open("images/image10.png")
     resized_image = image.resize((700, 400))  
     st.image(resized_image)




    st.header("🤖 What Does This App Offer?")
    st.markdown("""
    <div style='padding-bottom: 20px; text-align: left ; font-size: 18px;'>                     
              This application aims to inform users in advance about potential air pollution levels by predicting air pollutants (PM10, SO₂, CO, NO₂, NOX, NO, and O₃) based on meteorological data.
              Through the use of developed machine learning models, users can input weather parameters such as temperature, humidity, and wind to forecast future pollutant levels.
              In this way, individuals can make their daily plans—such as sports, transportation, and outdoor activities—with greater environmental awareness and health consideration.
              The application also provides in-depth insights through tools that visualize model performance, time-dependent analyses, and feature importance graphs.
              The goal is not only to offer predictions but also to raise awareness and support users in making informed decisions.            
    </div>             
    """,unsafe_allow_html=True)

    st.markdown("""
   <div style='
        background-color: #fff3cd;
        padding: 15px 20px;
        margin-top: 45px;
        border-radius: 8px;
        font-size: 16px;'
    >
    <b>📌 Informing:</b><br>
      This application provides estimated information on air pollutants using machine learning models based on weather data.
      The results obtained are <b>not exact values</b> and are intended solely for <i>informational and awareness</i> purposes.
      For decisions related to air quality, <b>official air quality monitoring systems</b> and up-to-date data provided by <b>authorized institutions</b> should be taken as the primary reference.
    </div>
    """, unsafe_allow_html=True)