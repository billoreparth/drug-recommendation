import streamlit as st

st.set_page_config(page_title="Drug Information Guide", layout="centered")
st.title("Drug Information Guide")
st.markdown("---")

# Generic Name
st.header("Generic Name")
st.write("""
The **generic name** of a drug refers to its chemical name or the standard name of its active ingredient. 
It is **not the brand name** used for marketing.
""")

# Rx/OTC Information
st.header("Rx-to-OTC Classification")
st.write("""
- **Rx**: Prescription Needed  
- **OTC**: Over-the-counter, can be purchased without a prescription  
- **Rx/OTC**: Available as both prescription and non-prescription depending on form or dosage
""")

# Pregnancy Category
st.header("Pregnancy Risk Categories")
st.write("""
- **A**: No risk in first trimester; no evidence of risk in later trimesters.  
- **B**: Animal studies show no risk; no controlled studies in humans.  
- **C**: Adverse effects in animals; no human studies, but potential benefits may justify use.  
- **D**: Positive evidence of human fetal risk, but benefits may warrant use.  
- **X**: Fetal abnormalities proven; risks outweigh benefits.  
- **N**: Not classified by FDA.
""")

# CSA Schedule
st.header("Controlled Substances Act (CSA) Schedules")
st.write("""
- **1**: High abuse potential, no accepted medical use.  
- **2**: High abuse potential, accepted use with severe restrictions.  
- **3**: Moderate to low abuse potential, accepted medical use.  
- **4**: Low abuse potential.  
- **5**: Lowest abuse potential.  
- **M**: Multiple schedules depending on form/strength.  
- **N**: Not subject to CSA.  
- **U**: Unknown CSA schedule.
""")

# Alcohol Interaction
st.header("Alcohol Interaction")
st.write("""
- **X**: The drug **interacts with alcohol** and should not be consumed together.
""")




st.markdown("""
---
### ⚠️ Disclaimer

This web application is a **personal project** created for learning and demonstration purposes only.  
It is **not intended for professional use**, and the results or recommendations provided may not be accurate for real-world decisions.

For the full code and more information, visit my Github [Parth Billore ](https://github.com/billoreparth).  
📧 For any questions or feedback, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/parth-billore-9647332a1/).

""")




st.markdown("---")
st.info("This guide provides general classifications and definitions. Always consult healthcare professionals for individual drug risks.")
