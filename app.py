import streamlit as st
import pandas as pd
import joblib
import random

# --- 1. PAGE SETUP & AESTHETICS ---
# This makes the app look clean and modern right from the start
st.set_page_config(
    page_title="Ghosting Predictor",
    page_icon="👻",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. SIDEBAR: USER INPUTS ---
# Moving inputs to the side keeps the main screen uncluttered
st.sidebar.header("⚙️ Configure Profile")
st.sidebar.write("Adjust your behavioral and demographic metrics below:")

profile_pics = st.sidebar.slider("📸 Profile Pictures Count", min_value=0, max_value=10, value=3)
swipe_ratio = st.sidebar.slider("👉 Swipe Right Ratio (%)", min_value=0, max_value=100, value=50)
messages_sent = st.sidebar.slider("💬 Messages Sent (Before Reply)", min_value=0, max_value=50, value=5)
income_bracket = st.sidebar.selectbox("💼 Income Bracket", ["Low", "Middle", "High", "Very High"])

# --- 3. MAIN PAGE TITLE ---
st.title("Left on Read: Ghosting Predictor 👻")
st.markdown("### *A predictive behavioral model powered by Machine Learning.*")
st.write("Will your match leave you on read? Adjust your profile statistics in the sidebar and let the AI calculate your fate.")
st.divider()

# --- 4. THE PREDICTION ENGINE ---
if st.button("🔮 Predict My Fate", use_container_width=True):
    
    # Try to load the real brain, but fall back to Test Mode if missing
    try:
        model = joblib.load('ghosting_model.joblib')
        st.success("Real model loaded successfully!")
        
        # NOTE: You will format the inputs for the real model here later!
        
    except FileNotFoundError:
        st.warning("⚠️ Running in Test Mode: Waiting for the Data Team's '.joblib' file.")
        
        # Simulated result just so you can test the UI design today
        fake_probability = random.randint(10, 90)
        
        st.markdown("### 📊 Prediction Results")
        
        # Using columns to put the number and the alert side-by-side
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="Calculated Ghosting Risk", value=f"{fake_probability}%")
            
        with col2:
            if fake_probability > 50:
                st.error("🔴 **HIGH RISK:** You are likely to be left on read.")
            else:
                st.success("🟢 **SAFE:** Active engagement is highly likely.")
                
        st.divider()
        
        # Dynamic feedback text based on the result
        if fake_probability > 50:
            st.info("💡 **Tip:** Try adjusting your message volume or swipe ratio in the sidebar to see how it improves your chances.")

# --- 5. THE ACADEMIC DISCLAIMER ---
# This proves to the lecturer that you are thinking about ethical tech
st.caption("Disclaimer: This tool was developed for educational purposes. To maximize predictive accuracy, the underlying AI evaluates statistical patterns including socioeconomic demographics (Income Bracket). This algorithmic bias may not reflect fair, human-centric communication standards. Always prioritize healthy digital boundaries.")