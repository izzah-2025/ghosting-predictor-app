# ghosting-predictor-app
# Left on Read: Ghosting Predictor 👻

### Live Application
**[Click here to test the live Streamlit Web App](https://ghosting-predictor-app-vpdkgrclm6ueqktnypmkvj.streamlit.app/)**

### Project Overview
The "Ghosting Predictor" is a machine learning web application designed to analyze user behavior on dating platforms and calculate the mathematical probability of a user being "ghosted" (left on read). 

### The Tech Used
* **Front-End User Interface:** Streamlit
* **Machine Learning Model:**  (Random Forest Classifier)
* **Data Manipulation:** Pandas, NumPy
* **Model Serialization:** Joblib
* **Development Environment:** Visual Studio Code

### Predictive Features
The application processes four key behavioral inputs through the machine learning model to generate a real-time risk score:
1. **Profile Pictures:** Evaluates the risk associated with unverified or inactive-looking accounts.
2. **Swipe-Right Ratio (%):** Measures user selectiveness.
3. **Double Texting (Messages Sent Without Reply):** The core indicator of communication breakdown.
4. **Income Bracket:** Categorical data reflecting socioeconomic status.


