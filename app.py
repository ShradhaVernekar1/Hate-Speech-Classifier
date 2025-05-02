import streamlit as st
import joblib

# Load the saved model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Streamlit UI
st.title("Hate Speech Classification")

# Text input
user_input = st.text_area("Enter text here:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform input text
        transformed_input = vectorizer.transform([user_input])

        # Predict
        prediction = model.predict(transformed_input)

        st.success(f"Prediction: {prediction[0]}")
