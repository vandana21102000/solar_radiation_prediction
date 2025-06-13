# import streamlit as st
# import pandas as pd
# import pickle
# import nbformat
# from nbconvert import HTMLExporter
# import streamlit.components.v1 as components
# from datetime import datetime

# # --- Function to render notebook as HTML ---
# def render_notebook_html(notebook_path):
#     with open(notebook_path, 'r', encoding='utf-8') as f:
#         notebook = nbformat.read(f, as_version=4)
#     html_exporter = HTMLExporter()
#     html_exporter.exclude_input_prompt = False
#     html_exporter.exclude_output_prompt = False
#     html_exporter.template_name = 'lab'
#     (body, _) = html_exporter.from_notebook_node(notebook)
#     components.html(body, height=1500, scrolling=True)

# # --- Main App ---
# def main():
#     st.set_page_config(
#         page_title="Solar Radiation Prediction",
#         layout="wide",
#         page_icon="☀️",
#         initial_sidebar_state="expanded",
#     )

#     st.markdown("""
#         <style>
#             .main {
#                 background-color: #f4f9f9;
#             }
#             .block-container {
#                 padding-top: 2rem;
#                 padding-bottom: 2rem;
#                 padding-left: 3rem;
#                 padding-right: 3rem;
#             }
#             .st-emotion-cache-1avcm0n {
#                 background-color: #e0f7fa;
#                 padding: 1rem;
#                 border-radius: 0.5rem;
#                 margin-bottom: 1rem;
#             }
#             .st-emotion-cache-1v0mbdj button {
#                 width: 100%;
#                 font-size: 1.1rem;
#             }
#             header {visibility: hidden;}
#             .css-18ni7ap.e8zbici2 {visibility: hidden;}
#         </style>
#     """, unsafe_allow_html=True)

#     st.sidebar.title("Solar Radiation Prediction")
#     page = st.sidebar.radio(" ", ["🏠 Home", "📓 Notebook", "🔮 Manual Prediction"])

#     if page == "🏠 Home":
#         col_img, col_text = st.columns([1, 2])

#         with col_img:
#             st.image("img.jpg", use_container_width=True)

#         with col_text:
#             st.title("☀️ Solar Radiation Prediction")
#             st.markdown("""
#             This application predicts **Solar Radiation Intensity** using environmental and temporal features such as temperature,
#             humidity, wind conditions, and sun movement timings. Explore data, visualize insights, and try real-time prediction!
#             """)

#             st.markdown("""
#             <div style='display: flex; gap: 20px;'>
#                 <a href='https://github.com/yourusername/solar_radiation_prediction.git' target='_blank'>
#                     <button style='background-color:#007BFF; color:white; padding:10px; border:none; border-radius:5px;'>🔗 GitHub Repo</button>
#                 </a>
#                 <a href='https://www.kaggle.com/datasets/dronio/SolarEnergy' target='_blank'>
#                     <button style='background-color:#28a745; color:white; padding:10px; border:none; border-radius:5px;'>📂 Dataset Source</button>
#                 </a>
#             </div>
#             """, unsafe_allow_html=True)

#     elif page == "📓 Notebook":
#         st.subheader("📓 Code + Output Notebook View")
#         render_notebook_html("Solar_Prediction.ipynb")

#     elif page == "🔮 Manual Prediction":
#         st.subheader("🔮 Predict Solar Radiation")

#         col1, col2 = st.columns(2)

#         with col1:
#             Temperature = st.slider('Temperature (°C)', -10.0, 50.0, 25.0)
#             Pressure = st.slider('Pressure (hPa)', 950.0, 1050.0, 1013.0)
#             Humidity = st.slider('Humidity (%)', 0.0, 100.0, 50.0)
#             WindDirection = st.slider('Wind Direction (°)', 0.0, 360.0, 180.0)
#             Speed = st.slider('Wind Speed (m/s)', 0.0, 20.0, 5.0)
#             Month = st.slider('Month', 1, 12, 6)
#             Day = st.slider('Day', 1, 31, 15)

#         with col2:
#             Hour = st.slider('Hour', 0, 23, 12)
#             Minute = st.slider('Minute', 0, 59, 30)
#             Second = st.slider('Second', 0, 59, 0)
#             RiseMinute = st.slider('Sunrise Minute', 0, 59, 6)
#             SetHour = st.slider('Sunset Hour', 0, 23, 18)
#             SetMinute = st.slider('Sunset Minute', 0, 59, 30)

#         input_data = [[
#             Temperature, Pressure, Humidity, WindDirection, Speed,
#             Month, Day, Hour, Minute, Second,
#             RiseMinute, SetHour, SetMinute
#         ]]

#         model = pickle.load(open("solar_model.sav", "rb"))
#         scaler = pickle.load(open("solar_scaler.sav", "rb"))

#         if "prediction_history" not in st.session_state:
#             st.session_state.prediction_history = pd.DataFrame(columns=["DateTime", "SolarRadiation"])

#         if st.button("📡 Predict Solar Radiation"):
#             scaled = scaler.transform(input_data)
#             result = model.predict(scaled)
#             prediction_time = datetime(2025, int(Month), int(Day), int(Hour), int(Minute), int(Second))

#             new_result = pd.DataFrame({
#                 "DateTime": [prediction_time],
#                 "SolarRadiation": [result[0]]
#             })

#             st.session_state.prediction_history = pd.concat([
#                 st.session_state.prediction_history,
#                 new_result
#             ], ignore_index=True)

#             st.success(f"🔆 Estimated Solar Radiation: **{result[0]:.2f} W/m²**")

#         if not st.session_state.prediction_history.empty:
#             csv = st.session_state.prediction_history.to_csv(index=False).encode('utf-8')
#             st.download_button(
#                 label="📄 Download Prediction History as CSV",
#                 data=csv,
#                 file_name='solar_radiation_predictions.csv',
#                 mime='text/csv',
#             )

# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd
import pickle
import nbformat
from nbconvert import HTMLExporter
import streamlit.components.v1 as components
import plotly.express as px
from datetime import datetime

# --- Function to render notebook as HTML ---
def render_notebook_html(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.exclude_input_prompt = False
    html_exporter.exclude_output_prompt = False
    html_exporter.template_name = 'lab'
    (body, _) = html_exporter.from_notebook_node(notebook)
    components.html(body, height=1500, scrolling=True)

# --- Main App ---
def main():
    st.set_page_config(
        page_title="Solar Radiation Prediction",
        layout="wide",
        page_icon="☀️",
        initial_sidebar_state="expanded",
    )

    st.markdown("""
        <style>
            .main {
                background-color: #f4f9f9;
            }
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
                padding-left: 3rem;
                padding-right: 3rem;
            }
            .st-emotion-cache-1avcm0n {
                background-color: #e0f7fa;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
            }
            .st-emotion-cache-1v0mbdj button {
                width: 100%;
                font-size: 1.1rem;
            }
            header {visibility: hidden;}
            .css-18ni7ap.e8zbici2 {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Solar Radiation Prediction")
    page = st.sidebar.radio(" ", ["🏠 Home", "📓 Notebook", "🔮 Manual Prediction"])

    if page == "🏠 Home":
        st.title("☀️ Solar Radiation Prediction")
        st.image("img.jpg", use_container_width=True)

        st.markdown("""
        This application predicts **Solar Radiation Intensity** using environmental and temporal features such as temperature,
        humidity, wind conditions, and sun movement timings. Explore data, visualize insights, and try real-time prediction!
        """)

        st.markdown("""
        <div style='display: flex; gap: 20px;'>
            <a href='https://github.com/vandana21102000/solar_radiation_prediction.git' target='_blank'>
                <button style='background-color:#007BFF; color:white; padding:10px; border:none; border-radius:5px;'>🔗 GitHub Repo</button>
            </a>
            <a href='https://www.kaggle.com/datasets/dronio/SolarEnergy' target='_blank'>
                <button style='background-color:#28a745; color:white; padding:10px; border:none; border-radius:5px;'>📂 Dataset Source</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    elif page == "📓 Notebook":
        st.subheader("📓 Code + Output Notebook View")
        render_notebook_html("Solar_Prediction.ipynb")

    elif page == "🔮 Manual Prediction":
        st.subheader("🔮 Predict Solar Radiation")

        col1, col2 = st.columns(2)

        with col1:
            Temperature = st.slider('Temperature (°C)', -10.0, 50.0, 25.0)
            Pressure = st.slider('Pressure (hPa)', 950.0, 1050.0, 1013.0)
            Humidity = st.slider('Humidity (%)', 0.0, 100.0, 50.0)
            WindDirection = st.slider('Wind Direction (°)', 0.0, 360.0, 180.0)
            Speed = st.slider('Wind Speed (m/s)', 0.0, 20.0, 5.0)
            Month = st.slider('Month', 1, 12, 6)
            Day = st.slider('Day', 1, 31, 15)

        with col2:
            Hour = st.slider('Hour', 0, 23, 12)
            Minute = st.slider('Minute', 0, 59, 30)
            Second = st.slider('Second', 0, 59, 0)
            RiseMinute = st.slider('Sunrise Minute', 0, 59, 6)
            SetHour = st.slider('Sunset Hour', 0, 23, 18)
            SetMinute = st.slider('Sunset Minute', 0, 59, 30)

        input_data = [[
            Temperature, Pressure, Humidity, WindDirection, Speed,
            Month, Day, Hour, Minute, Second,
            RiseMinute, SetHour, SetMinute
        ]]

        model = pickle.load(open("solar_model.sav", "rb"))
        scaler = pickle.load(open("solar_scaler.sav", "rb"))

        if "prediction_history" not in st.session_state:
            st.session_state.prediction_history = pd.DataFrame(columns=["DateTime", "SolarRadiation"])

        if st.button("📡 Predict Solar Radiation"):
            scaled = scaler.transform(input_data)
            result = model.predict(scaled)
            prediction_time = datetime(2025, int(Month), int(Day), int(Hour), int(Minute), int(Second))

            new_result = pd.DataFrame({
                "DateTime": [prediction_time],
                "SolarRadiation": [result[0]]
            })

            st.session_state.prediction_history = pd.concat([
                st.session_state.prediction_history,
                new_result
            ], ignore_index=True)

            st.success(f"🔆 Estimated Solar Radiation: **{result[0]:.2f} W/m²**")


if __name__ == "__main__":
    main()
