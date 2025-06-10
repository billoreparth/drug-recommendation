import streamlit as st

st.title("Drug Effect Classifier")

st.markdown("""
###  How to Enter Symptoms or Effects

Please follow these guidelines when entering symptoms or side effects:

1. ✅ **Use plain English**, separating each symptom with a **space**:
   - Example: `difficult breathing swelling face lips tongue throat`

2. 🚫 **Do NOT use commas or punctuation**:
   - ❌ `fever, rash, nausea`
   - ✅ `fever rash nausea`

3. ✅ You can enter full phrases or partial phrases:
   - Example: `birth control pills stop using`

4. ⚠️ **Avoid very long paragraphs** (limit to ~200 words for best results)

---

### 💡 Example Inputs:

- `severe headache blurred vision high blood pressure`
- `nausea vomiting dizziness fatigue`
- `rash swelling of face or throat difficulty breathing`

Once entered, click **"Predict"** to see the result.
""")


st.title('some other example')
st.markdown(""" 
->difficult breathing swelling face lips tongue throat topical\n
->severe stomach pain diarrhea watery bloody even occurs months last dose fever chills body aches flu symptoms pale skin easy bruising unusual bleeding seizure fever weakness confusion dark colored urine jaundice yellowing skin \n
->slow heart rate weak pulse slow breathing breathing may stop pain numbness tingling burning feeling cold pale mottled skin blue colored lips fingers toes severe pain swelling lower leg weakness arms legs \n
            
""")

st.markdown("---")
st.info("This guide provides general classifications and definitions. Always consult healthcare professionals for individual drug risks.")