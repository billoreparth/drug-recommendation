import streamlit as st

# Define the pages
Recomendation_by_drug = st.Page("src/Resources/Recomendation_by_drug.py", title="Recommendation_by_Drug", icon="🎈")
Recomendation_by_condition = st.Page("src/Resources/Recomendation_by_condition.py", title="Recommendation_by_Symptoms", icon="❄️")
Providing_Data = st.Page("src/Resources/Providing_Data.py", title="More Details", icon="🎉")

# Set up navigation
pg = st.navigation([Recomendation_by_drug, Recomendation_by_condition, Providing_Data])

# Run the selected page
pg.run()



