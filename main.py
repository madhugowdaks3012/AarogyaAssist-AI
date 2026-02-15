import streamlit as st
import json

st.set_page_config(page_title="HealthGuard AI", layout="centered")

# Load hospital data
with open("hospitals.json", "r") as file:
    hospital_data = json.load(file)

st.title("🏥 HealthGuard AI")
st.markdown("⚠️ *This tool is for educational purposes only. Not a substitute for medical advice.*")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------------------
# STEP 1 – Select Symptom
# ---------------------------
if st.session_state.step == 1:
    st.subheader("Step 1: Select Your Main Symptom")

    symptom = st.radio(
        "Choose symptom:",
        ["Fever", "Cold", "Diarrhea", "Headache", "Stomach Pain"]
    )

    if st.button("Next"):
        st.session_state.symptom = symptom
        st.session_state.step = 2

# ---------------------------
# STEP 2 – Duration
# ---------------------------
elif st.session_state.step == 2:
    st.subheader("Step 2: How many days have you had this?")

    duration = st.radio(
        "Duration:",
        ["1-2 days", "3-5 days", "More than 5 days"]
    )

    if st.button("Next"):
        st.session_state.duration = duration
        st.session_state.step = 3

# ---------------------------
# STEP 3 – Severity
# ---------------------------
elif st.session_state.step == 3:
    st.subheader("Step 3: Select Severity Level")

    severity = st.radio(
        "Severity:",
        ["Mild", "Moderate", "Severe"]
    )

    if st.button("Analyze"):
        st.session_state.severity = severity
        st.session_state.step = 4

# ---------------------------
# STEP 4 – Analysis & Result
# ---------------------------
elif st.session_state.step == 4:
    st.subheader("🩺 Analysis Result")

    symptom = st.session_state.symptom
    duration = st.session_state.duration
    severity = st.session_state.severity

    # Risk scoring logic
    score = 0

    if duration == "More than 5 days":
        score += 2
    if severity == "Severe":
        score += 3
    if symptom == "Diarrhea" and duration == "More than 5 days":
        score += 2

    # Determine seriousness
    serious = score >= 4

    # Condition mapping
    condition_info = {
        "Fever": {
            "condition": "Possible Viral Fever",
            "tablet": "Paracetamol",
            "syrup": "Crocin Syrup",
            "advice": "Stay hydrated and rest well."
        },
        "Cold": {
            "condition": "Common Cold",
            "tablet": "Cetirizine",
            "syrup": "Benadryl",
            "advice": "Steam inhalation and warm fluids recommended."
        },
        "Diarrhea": {
            "condition": "Gastroenteritis",
            "tablet": "Loperamide",
            "syrup": "ORS Solution",
            "advice": "Drink plenty of fluids to avoid dehydration."
        },
        "Headache": {
            "condition": "Tension Headache",
            "tablet": "Ibuprofen",
            "syrup": "Calpol",
            "advice": "Take rest and reduce screen exposure."
        },
        "Stomach Pain": {
            "condition": "Acidity or Indigestion",
            "tablet": "Antacid",
            "syrup": "Digene",
            "advice": "Avoid spicy foods and eat light meals."
        }
    }

    info = condition_info[symptom]

    st.success(f"**Condition:** {info['condition']}")
    st.write(f"💊 **Tablet Suggestion:** {info['tablet']}")
    st.write(f"🧴 **Syrup Suggestion:** {info['syrup']}")
    st.write(f"📝 **Advice:** {info['advice']}")

    if serious:
        st.error("🚨 This appears serious. Please consult a medical professional immediately.")

        st.subheader("Find Nearby Hospitals")

        state = st.selectbox("Select State", list(hospital_data.keys()))

        if state:
            city = st.selectbox("Select City", list(hospital_data[state].keys()))

            if city:
                hospitals = hospital_data[state][city]
                st.markdown("### 🏥 Available Hospitals")
                for h in hospitals:
                    st.write(f"**{h['name']}** — 📞 {h['phone']}")

    if st.button("Reset"):
        st.session_state.step = 1
