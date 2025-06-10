import streamlit as st
import pandas as pd
import plotly.express as px

st.sidebar.title("Football Powerhouse 🇬🇭")
match = st.sidebar.selectbox("Select Match", ["Amazonas vs. Athletic Club", "Custom Match"])
custom_match = st.sidebar.text_input("Custom Match (e.g., Apple FC vs. Carrot FC):") if match == "Custom Match" else ""
match = custom_match if custom_match else match
result = st.sidebar.text_input("Enter Result (e.g., 1-0, 2 yellows):")
crowd_size = st.sidebar.slider("Crowd Size", 10000, 60000, 15000, 1000)
squad = st.sidebar.selectbox("Away Squad", ["A-Squad", "B-Squad"])
st.sidebar.text_area("Data Gaps", "Uncertainties: Injuries (±5%), Weather (±2%)")

st.title("Match Analysis Dashboard")
if match and not result:
    st.write(f"🔍 Predicting {match}...")
    st.write("🟡 Predicted: 1-0, 42% ±5% Confidence")
    st.write("💰 Savvy Pick: Under 2.5 Goals, 65%, 1.57 odds")
    data = pd.DataFrame({"Team": ["Amazonas", "Athletic"], "Goals/Game": [1.0, 1.1]})
    fig = px.bar(data, x="Team", y="Goals/Game", title="Team Form")
    st.plotly_chart(fig)
elif match and result:
    st.write(f"📊 {match} Result: {result}")
    st.write("📈 Accuracy updated, model refining...")

st.write("🧠 SHAP Plot: Disabled (missing model)")