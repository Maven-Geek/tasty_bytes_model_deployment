import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Transformation Pipeline
yeo_cols = ['calories', 'carbohydrate', 'sugar', 'protein']
category_order = [
    'Beverages', 'Breakfast', 'Chicken', 'Dessert',
    'Lunch/Snacks', 'Meat', 'One Dish Meal', 'Pork', 'Potato', 'Vegetable'
]

yeo_scaler = Pipeline([
    ('yeo', PowerTransformer(method='yeo-johnson')),
    ('minmax', MinMaxScaler())
])

servings_scaler = Pipeline([
    ('minmax', MinMaxScaler())
])
categorical_encoder = OneHotEncoder(
    handle_unknown='ignore',
    categories=[category_order]
)

preprocessor = ColumnTransformer(transformers=[
    ('yeo-num', yeo_scaler, yeo_cols),
    ('servings', servings_scaler, ['servings']),
    ('cat', categorical_encoder, ['category'])
])

preprocessing_pipeline = Pipeline([
    
])


# Streamlit UI
st.title('High Traffic Recipe Prediction')
st.subheader('Model Inputs')

recipe_id = st.number_input('Recipe no. (Optional)', step=1, format="%d")
cal = st.number_input('Calories')
carb = st.number_input('Carbohydrate')
sug = st.number_input('Sugar')
pro = st.number_input('Protein')
# cat = st.text_input('Category')
cat = st.selectbox('Pick a category', ['Lunch/Snacks','Beverages', 'Potato','Vegetable', 'Meat', 
                                       'Chicken', 'Pork', 'Dessert', 'Breakfast', 'One Dish Meal'])
ser = st.number_input('Servings', step=1, format="%d")

if st.button('Predict Traffic'):
    # Create a DataFrame from user inputs
    input_df = pd.DataFrame([{
        'calories': cal,
        'carbohydrate': carb,
        'sugar': sug,
        'protein': pro,
        'servings': ser,
        'category': cat
    }])

    with open('svm_model.bin', 'rb') as f:
        model = pickle.load(f)
    
    # Preprocess input   
    X_processed = preprocessor.fit_transform(input_df)

    # Get feature names and rename to match training (remove 'cat__category_' prefix)
    feature_names = preprocessor.get_feature_names_out()
    clean_feature_names = [name.replace("cat__category_", "") for name in feature_names]
    clean_feature_names = [name.replace("yeo-num__", "") for name in clean_feature_names]
    clean_feature_names = [name.replace("servings__", "") for name in clean_feature_names]

    # Convert to DataFrame with matching column names
    X_processed_df = pd.DataFrame(X_processed, columns=clean_feature_names)
    #X_processed_df.to_csv('check.csv')

    # Predict using DataFrame so feature names match training
    prediction = model.predict(X_processed_df)[0]
    probability = model.predict_proba(X_processed_df)[0][1]
    
    # Make preditions
    #st.write(f"Probability of High Traffic: {prediction}")
    label = "High Traffic" if prediction == 1 else "Low Traffic"
    #st.write(f"Prediction: {label}") 
    #st.write(f"Probability of High Traffic: {probability:.2%}")
    color = "green" if prediction == 1 else "red"
    
    # Styled prediction text
    st.markdown(''
        f"<h3>Prediction: <span style='color: {color};'>{label}</span></h3>", 
        unsafe_allow_html=True
    )

    # Probability text (keep default style or match color)
    st.markdown(
        f"<p>Probability of High Traffic: {probability:.2%}</p>", 
        unsafe_allow_html=True
    )

# TODO  - Ability to upload CSVs for predictions
