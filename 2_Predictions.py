import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

st.title("🧠 Disease Prediction")

data = pd.DataFrame({
    'Age': [25,40,30,50,23,60,45,35,28,55,33,48,22,65,38,29,41,52,47,36],
    'Gender': ['Male','Female']*10,
    'Fever': [1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0],
    'Cough': [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1],
    'Fatigue': [1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0],
    'Headache': [1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0],
    'Disease': [
        'Flu','Hypertension','Cold','Hypertension','Cold','Malaria','Hypertension','Allergy','Flu','Hypertension',
        'Cold','Hypertension','Typhoid','Pneumonia','Allergy','Migraine','Hypertension','Dengue','Flu','Cold'
    ]
})

data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

X = data[['Age','Gender','Fever','Cough','Fatigue','Headache']]
y = data['Disease']

model = DecisionTreeClassifier()
model.fit(X, y)

age = st.slider("Age", 1, 100, 25)
gender = st.selectbox("Gender", ["Male", "Female"])
fever = st.selectbox("Fever", ["No", "Yes"])
cough = st.selectbox("Cough", ["No", "Yes"])
fatigue = st.selectbox("Fatigue", ["No", "Yes"])
headache = st.selectbox("Headache", ["No", "Yes"])

vals = [
    age,
    0 if gender=="Male" else 1,
    1 if fever=="Yes" else 0,
    1 if cough=="Yes" else 0,
    1 if fatigue=="Yes" else 0,
    1 if headache=="Yes" else 0
]

if st.button("🚀 Predict"):
    result = model.predict([vals])
    st.session_state['result'] = result[0]

    # Auto redirect
    st.switch_page("pages/3_Result.py")