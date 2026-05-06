import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.title("🎯 AI Prediction Result")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Better animation
anim = load_lottie("https://assets9.lottiefiles.com/packages/lf20_qp1q7mct.json")

if anim:
    st_lottie(anim, height=250)

# Result Card
if 'result' in st.session_state:
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #00F5FF, #9B59B6);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            font-size: 25px;
            color: white;
            font-weight: bold;
        ">
            🩺 Predicted Disease: {st.session_state['result']}
        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("No prediction yet!")