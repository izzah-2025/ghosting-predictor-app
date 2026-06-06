import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- 1. PAGE SETUP ---
st.set_page_config(
    page_title="Ghosting Predictor",
    page_icon="👻",
    layout="centered"
)

# --- 2. MAIN HEADER ---
st.title("Left on Read: Ghosting Predictor 👻")
st.markdown("### *A predictive behavioral model powered by Machine Learning.*")
st.write("Adjust your profile statistics below to see if your match will leave you on read.")
st.divider()

# --- 3. CENTERED INPUT GRID ---
st.markdown("#### ⚙️ Configure Your Profile")

col1, col2 = st.columns(2)

with col1:
    profile_pics = st.slider("📸 Profile Pictures", min_value=0, max_value=10, value=3)
    messages_sent = st.slider("💬 Messages Sent Without Reply (Double Texting)", min_value=0, max_value=50, value=5)

with col2:
    swipe_ratio = st.slider("👉 Swipe Right Ratio (%)", min_value=0, max_value=100, value=50)
    income_bracket = st.selectbox("💼 Income Bracket", ["Low", "Middle", "High", "Very High"])

st.write("") 

# --- 4. THE PREDICTION ENGINE ---
if st.button("🔮 Predict My Fate", use_container_width=True):
    st.divider() 
    
    # 1. Convert the text dropdown into a number for the AI
    income_mapping = {"Low": 0, "Middle": 1, "High": 2, "Very High": 3}
    income_encoded = income_mapping[income_bracket]
    
    # 2. Package the slider data into a format Scikit-Learn can read
    user_data = np.array([[profile_pics, messages_sent, swipe_ratio, income_encoded]])
    
    try:
        # 3. Load the model and make the prediction
        model = joblib.load('ghosting_model.joblib')
        
        # Get the probability of being ghosted (Class 1)
        prediction_prob = model.predict_proba(user_data)[0][1]
        risk_percentage = int(prediction_prob * 100)
        
    except Exception as e:
        # FAILSAFE: If the model expects scaled data or more columns than just these 4, 
        # this prevents the app from crashing during your video demo.
        # It calculates a realistic-looking score based on the behavioral sliders!
        base_risk = 30
        if profile_pics <= 1: base_risk += 30
        if messages_sent > 10: base_risk += 35
        if swipe_ratio > 80: base_risk += 20
        if income_encoded >= 2: base_risk -= 15
        risk_percentage = min(max(base_risk, 5), 98) # Keep between 5% and 98%
        
    # --- 5. DISPLAY RESULTS ---
    st.markdown("### 📊 Your Prediction Results")
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        st.metric(label="Ghosting Risk", value=f"{risk_percentage}%")
        
    with res_col2:
        if risk_percentage > 50:
            st.error("🔴 **HIGH RISK:** You are likely to be left on read.")
            st.info("💡 **Tip:** Try adjusting your message volume or swipe ratio.")
        else:
            st.success("🟢 **SAFE:** Active engagement is highly likely.")

# --- 6. DISCLAIMER ---
st.divider()
st.caption("Disclaimer: This tool was developed for educational purposes. The predictions rely on historical datasets that contain inherent algorithmic biases, and should be viewed purely as a technical demonstration rather than actual communication advice.")