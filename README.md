# 🏥 AarogyaAssist AI
### Intelligent Symptom Risk Assessment & Hospital Navigation System (Offline Healthcare Assistant)

---

## 📌 Overview

AarogyaAssist AI is a dynamic, rule-based healthcare assistance system designed to guide users through structured symptom evaluation and provide medical guidance in an interactive, step-by-step workflow.

The system evaluates:
- Primary symptom
- Duration of illness
- Severity level

Based on these inputs, it generates:
- Risk classification (Mild / Moderate / Serious)
- Educational medicine suggestions
- General health advice
- Nearby hospital information (State → City → Hospital)

⚠ This application is built strictly for educational and demonstration purposes.

---

## 🎯 Problem Statement

Many individuals are unsure whether their symptoms require:

- Simple rest
- Over-the-counter medication
- Immediate medical consultation

AarogyaAssist AI provides a structured decision-support experience that helps users understand potential risk levels and take appropriate action.

---

## 🚀 Key Features

✔ Multi-step dynamic symptom selection  
✔ Stateful interactive UI using Streamlit  
✔ Rule-based risk scoring engine  
✔ Severity classification (Mild / Moderate / Serious)  
✔ Educational tablet & syrup suggestions  
✔ Emergency consultation alert system  
✔ Offline State → City → Hospital dropdown navigation  
✔ India-focused structured hospital dataset  
✔ No external APIs required  
✔ Fully offline system  

---

## 🧠 How It Works

### Step 1 – Symptom Selection
User selects a primary symptom:
- Fever
- Cold
- Diarrhea
- Headache
- Stomach Pain

### Step 2 – Duration Assessment
User selects how long the symptom has persisted:
- 1–2 days
- 3–5 days
- More than 5 days

### Step 3 – Severity Selection
User selects:
- Mild
- Moderate
- Severe

### Step 4 – Risk Scoring Engine
The system calculates a risk score based on:
- Duration
- Severity
- Symptom-specific logic

Example:
- Severe condition → Higher score
- Long duration → Increased risk
- Certain symptom combinations → Additional weight

### Step 5 – Result Generation
Displays:
- Possible condition
- Suggested tablet
- Suggested syrup
- Health advice
- Severity badge

### Step 6 – Emergency Handling
If risk score exceeds threshold:
- Red emergency alert displayed
- User selects State
- City dropdown updates dynamically
- Hospital list appears with contact numbers

---

## 🏗 Technical Architecture

### Frontend
- Streamlit dynamic UI
- Multi-step workflow using session state

### Backend Logic
- Rule-based scoring engine
- Conditional rendering logic
- Structured symptom-to-condition mapping

### Data Layer
- JSON-based hospital database
- State → City → Hospital hierarchy
- Fully offline data storage

---

## 📂 Project Structure

AarogyaAssist-AI/
│
├── app.py
├── hospitals.json
├── requirements.txt
└── README.md

---

## ⚙ Installation Guide

### 1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/AarogyaAssist-AI.git
cd AarogyaAssist-AI

---

### 2️⃣ Install Requirements

pip install -r requirements.txt

If needed:

pip install streamlit

---

### 3️⃣ Run Application

streamlit run app.py

Open in browser:

http://localhost:8501

---

## 📊 Sample Workflow

Example:

1. Symptom → Fever  
2. Duration → More than 5 days  
3. Severity → Severe  
4. System detects high risk  
5. Emergency alert displayed  
6. User selects Karnataka → Bengaluru  
7. Hospital list appears with phone numbers  

---

## 🔒 Offline Capability

- No external API usage  
- No internet dependency  
- Hospital dataset stored locally  
- Fully self-contained system  

---

## ⚠ Ethical Disclaimer

AarogyaAssist AI is not a medical diagnostic tool.

It is developed strictly for:
- Educational purposes
- Technical demonstration
- Portfolio showcase

Users should always consult a licensed medical professional for medical advice.

---

## 📈 Future Enhancements

- Multi-symptom combination analysis  
- Machine Learning-based severity prediction  
- Hospital specialty filtering  
- Ambulance emergency number (108) integration  
- SQLite database integration  
- User login & history tracking  
- Cloud deployment version  
- Doctor appointment booking simulation  
- Real-time map integration  

---

## 💼 Resume Description

Developed AarogyaAssist AI, a dynamic rule-based healthcare assistant featuring multi-step symptom risk evaluation, structured severity scoring engine, and offline state-city hospital navigation system using Python and Streamlit.

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- JSON Data Architecture  
- Rule-Based Logic Engine  

---

## 👨‍💻 Author

Madhu Gowda K S  
B.Tech – Artificial Intelligence & Machine Learning  

---

## 📜 License

This project is intended for educational and demonstration purposes only.
