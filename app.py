import streamlit as st

st.set_page_config(page_title="Healthcare AI", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
}
.subtitle {
    text-align: center;
    color: #dcdcdc;
}
.card {
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🏥 Healthcare AI System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart Disease Prediction & Analytics</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>📊 Analytics</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>🧠 Prediction</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'>🎯 Results</div>", unsafe_allow_html=True)

st.markdown("### 👉 Use sidebar to navigate")