import streamlit as st
import requests
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Fitness Data Analysis", layout="wide")

# Custom CSS that works for both Light and Dark mode
st.markdown("""
    <style>
    /* Style the metric cards with a border instead of a forced white background */
    [data-testid="stMetric"] {
        border: 1px solid #464b5d;
        padding: 15px;
        border-radius: 10px;
    }
    /* Style the advice box to have a nice accent border */
    .advice-container {
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        background-color: rgba(0, 123, 255, 0.05); /* Very light blue tint */
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Fitness Data Analysis with AI")
st.markdown("---")

# Sidebar for user inputs
with st.sidebar:
    st.header("👤 User Profile")
    age = st.number_input("Age", 18, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (kg)", 40.0, 200.0, 80.0)
    height = st.number_input("Height (cm)", 100, 250, 175)
    activity = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
    
    st.header("🎯 Target Goals")
    goals_input = st.text_area("What are your fitness goals?", "Lose 5kg of fat and build lean muscle.")
    
  # Main Area: Question & Execution
st.subheader("💬 Ask your AI Expert")
user_question = st.text_input("e.g., What should I eat after a workout?", "Give me a general overview of my fitness plan.")

if st.button("🚀 Analyze & Generate Plan"):
    # Prepare data for FastAPI
    profile_str = f"Age: {age}, Gender: {gender}, Weight: {weight}kg, Height: {height}cm, Activity: {activity}"
    
    payload = {
        "profile": profile_str,
        "question": user_question,
        "goals": goals_input
    }

    with st.spinner("Talking to Langflow Agents..."):
        try:
            # Call your FastAPI endpoint
            response = requests.post("http://127.0.0.1:8000/process-fitness-data", json=payload)
            response.raise_for_status()
            result = response.json()
            
            data = result.get("data", {})
            macros = data.get("macros", {})
            advice = data.get("advice", "")

            # Layout for Macros
            st.subheader("📊 Recommended Daily Macros")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Calories", f"{macros.get('calories', 0)} kcal")
            with col2:
                st.metric("Protein", f"{macros.get('protein', 0)}g")
            with col3:
                st.metric("Carbs", f"{macros.get('carbs', 0)}g")
            with col4:
                st.metric("Fat", f"{macros.get('fat', 0)}g")

            # --- Updated Visualization Section ---
            st.markdown("---")
            col_left, col_right = st.columns([2, 1])
            
            with col_left:
                st.subheader("📜 AI Professional Advice")
                # Using a standard st.info or st.markdown ensures the text color flips 
                # correctly between white (dark mode) and black (light mode).
                with st.container():
                    st.markdown(f'<div class="advice-container">{advice}</div>', unsafe_allow_html=True)
            
            with col_right:
                st.subheader("🥧 Macro Split")
                macro_df = pd.DataFrame({
                    "Nutrient": ["Protein", "Carbs", "Fat"],
                    "Grams": [macros.get('protein', 0), macros.get('carbs', 0), macros.get('fat', 0)]
                })
                st.bar_chart(macro_df.set_index("Nutrient"))

        except Exception as e:
            st.error(f"Failed to connect to Backend: {e}")

else:
    st.info("Fill in your profile on the left and click 'Generate Plan' to begin.")