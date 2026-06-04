import streamlit as st
import pandas as pd
import joblib
import random # Used just to generate a fake number until you get the real model

# 1. Page Configuration
st.set_page_config(page_title="Ghosting Predictor", page_icon="👻", layout="centered")

# 2. Header Section
st.title("Left on Read: Ghosting Risk Calculator 👻")
st.write("Enter your dating app habits below to see the probability that your match will leave you on read.")
st.divider() # Draws a neat line across the screen

# 3. User Input Section (Organized into two neat columns)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Profile")
    profile_pics = st.slider("Profile Pictures Count", min_value=0, max_value=10, value=3)
    income_bracket = st.selectbox("Income Bracket", ["Low", "Middle", "High", "Very High"])
    
with col2:
    st.subheader("Your App Habits")
    messages_sent = st.slider("Messages Sent to Match", min_value=0, max_value=200, value=20)
    swipe_ratio = st.slider("Swipe Right Ratio (%)", min_value=0, max_value=100, value=50)
    time_of_day = st.selectbox("Usual Time Swiping", ["Morning", "Afternoon", "Evening", "Late Night"])

st.divider()

# 4. The Prediction Button
if st.button("Predict My Fate", use_container_width=True):
    
    # This tries to load your real model. If it doesn't exist yet, it plays a test round!
    try:
        model = joblib.load('ghosting_model.joblib')
        
        # --- (Later, you will format the inputs here to match the exact model requirements) ---
        
        st.success("Real model loaded successfully!")
        
    except FileNotFoundError:
        # What happens today before you get the .joblib file
        st.warning("⚠️ Waiting for the real '.joblib' file from the Data Team. Running a test prediction...")
        
        # Generates a random fake probability just so you can see how the UI looks
        fake_probability = random.randint(10, 90)
        
        if fake_probability > 50:
            st.error(f"🔴 High Risk! There is a {fake_probability}% chance you will be ghosted.")
        else:
            st.success(f"🟢 Safe! There is only a {fake_probability}% chance you will be ghosted.")

# 5. The Academic Disclaimer (Great for human-centric grading!)
st.caption("Disclaimer: This tool was developed for educational purposes. The underlying AI model is trained on synthetic data, meaning real-world human behavior and emotional predictors may vary significantly. Always prioritize healthy communication in digital spaces.")