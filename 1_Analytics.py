import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Disease Analytics")

data = pd.DataFrame({
    'Disease': [
        'Flu','Hypertension','Cold','Hypertension','Cold','Malaria','Hypertension','Allergy','Flu','Hypertension',
        'Cold','Hypertension','Typhoid','Pneumonia','Allergy','Migraine','Hypertension','Dengue','Flu','Cold'
    ]
})

counts = data['Disease'].value_counts()

colors = plt.cm.plasma(range(len(counts)))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribution")
    fig, ax = plt.subplots()
    counts.plot(kind='bar', color=colors, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Disease Share")
    fig2, ax2 = plt.subplots()
    counts.plot(kind='pie', autopct='%1.1f%%', colors=colors, ax=ax2)
    ax2.set_ylabel('')
    st.pyplot(fig2)

st.markdown("### Insights")
st.info("Hypertension appears frequently along with Flu and Cold.")