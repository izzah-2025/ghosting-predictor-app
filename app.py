import streamlit as st
import pandas as pd
import joblib
import random

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

# Creating two columns side-by-side to make the layout compact and clean
col1, col2 = st.columns(2)

with col1:
    profile_pics = st.slider("📸 Profile Pictures", min_value=0, max_value=10, value=3)
    messages_sent = st.slider("💬 Messages Sent Before Reply (Double Texting)", min_value=0, max_value=50, value=5)

with col2:
    swipe_ratio = st.slider("👉 Swipe Right Ratio (%)", min_value=0, max_value=100, value=50)
    income_bracket = st.selectbox("💼 Income Bracket", ["Low", "Middle", "High", "Very High"])

st.write("") # Adds a tiny bit of blank space before the button

# --- 4. THE PREDICTION ENGINE ---
# Make the button span the whole width of the center column
if st.button("🔮 Predict My Fate", use_container_width=True):
    
    st.divider() # Add a line to separate inputs from results
    
    try:
        model = joblib.load('ghosting_model.joblib')
        st.success("Real model loaded successfully!")
        
    except FileNotFoundError:
        st.warning("⚠️ Running in Test Mode: Waiting for the Data Team's '.joblib' file.")
        
        fake_probability = random.randint(10, 90)
        
        st.markdown("### 📊 Your Prediction Results")
        
        # Display the result and the message side-by-side
        res_col1, res_col2 = st.columns([1, 2])
        
        with res_col1:
            st.metric(label="Ghosting Risk", value=f"{fake_probability}%")
            
        with res_col2:
            if fake_probability > 50:
                st.error("🔴 **HIGH RISK:** You are likely to be left on read.")
                st.info("💡 **Tip:** Try adjusting your message volume or swipe ratio.")
            else:
                st.success("🟢 **SAFE:** Active engagement is highly likely.")

# --- 5. THE ACADEMIC DISCLAIMER ---
st.divider()
st.caption("Disclaimer: This tool was developed for educational purposes. The AI’s predictions rely on historical datasets that contain inherent algorithmic biases, and should be viewed purely as a technical demonstration rather than actual communication advice.")