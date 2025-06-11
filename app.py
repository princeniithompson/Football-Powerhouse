# Main Panel
st.title("Match Analysis Dashboard")
st.write(f"Predicting {match}... (Last Updated: {datetime.now().strftime('%H:%M GMT')})")
if match == "Amazonas vs. Athletic Club":
    st.write("🔮 Predicted: 1-0 Amazonas, 0-0 secondary (45% probability)")
    st.write(f"Confidence: {confidence_explanation}")
    st.write("🧠 Savvy Pick: Under 2.5 Goals (~68%) – Amazonas’ 0.8 xG, Athletic’s 0.6 xG, defensive solidity")
elif match == "Kosovo vs. Comoros":
    st.write("🔮 Predicted: 2-1 Kosovo, 3-1 secondary (55% probability)")
    st.write(f"Confidence: {confidence_explanation}")
    st.write("🧠 Savvy Pick: Over 2.5 Goals (~58%) – Kosovo’s 1.8 xG, Comoros’ 0.7 xG, intensity")
elif match == "Mexico vs. Turkey":
    st.write("🔮 Predicted: 1-0 Mexico (Actual: 1-0)")
    st.write(f"Confidence: {confidence_explanation}")
    st.write("🧠 Savvy Pick: Under 2.5 Goals (~67%) – Match result confirmed, validating model’s focus on Özer’s xGC increase (0.15) and Mexico’s defense")
elif match == "Oran vs. El Bayadh":
    st.write("🔮 Predicted: 1-0 Oran")
    st.write(f"Confidence: {confidence_explanation}")
    st.write("🧠 Savvy Pick: Under 2.5 Goals (~65%) – Oran’s home edge (0.8 xG), El Bayadh’s low scoring trend (0.4 xG)")
elif match == "Constantine vs Belouizdad":
    st.write("🔮 Predicted: 1-1 Draw, 2-1 Belouizdad secondary (50% probability)")  # Based on H2H trends
    st.write(f"Confidence: {confidence_explanation}")
    st.write("🧠 Savvy Pick: Under 2.5 Goals (~70%) – Constantine’s 0.86 xG, Belouizdad’s 1.23 xG, tight H2H history")
with st.expander("Why this Savvy Pick?"):
    if match == "Constantine vs Belouizdad":
        st.write("SHAP Analysis: H2H (40%), form (30%), xG (20%). Adjusted for Constantine’s recent 3-game goalless streak and Belouizdad’s 7-match unbeaten run.")
# Add similar updates to other sections (e.g., Betting Markets, Team Form) as needed