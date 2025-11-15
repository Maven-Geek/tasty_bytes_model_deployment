import streamlit as st
import pickle
import pandas as pd

# Load the complete pipeline
pipeline = pickle.load(open("pipeline.bin", "rb"))

category_order = [
    'Beverages', 'Breakfast', 'Chicken', 'Dessert',
    'Lunch/Snacks', 'Meat', 'One Dish Meal', 'Pork',
    'Potato', 'Vegetable'
]

st.title("High Traffic Recipe Prediction")

cal = st.number_input("Calories")
carb = st.number_input("Carbohydrate (g)")
sug = st.number_input("Sugar (g)")
pro = st.number_input("Protein (g)")
cat = st.selectbox("Category", category_order)
ser = st.number_input("Servings", step=1, format="%d")

if st.button("Predict Traffic"):

    input_df = pd.DataFrame([{
        'calories': cal,
        'carbohydrate': carb,
        'sugar': sug,
        'protein': pro,
        'servings': ser,
        'category': cat
    }])

    prediction = pipeline.predict(input_df)[0]
    probability = pipeline.predict_proba(input_df)[0][1]

    label = "High Traffic" if prediction == 1 else "Low Traffic"
    color = "green" if prediction == 1 else "red"

    st.markdown(
        f"<h3>Prediction: <span style='color:{color};'>{label}</span></h3>",
        unsafe_allow_html=True
    )
    st.write(f"Probability: {probability:.2%}")
