import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.pkl')

numerical_features = [
    'Age','Education_Level', 'Time_of_service', 'Time_since_promotion', 'growth_rate', 
    'Travel_Rate', 'Post_Level', 'Pay_Scale', 'Work_Life_balance', 
    'VAR1', 'VAR2', 'VAR3', 'VAR4', 'VAR5', 'VAR6', 'VAR7'
]

categorical_features = {
    'Gender': ['F', 'M'],
    'Relationship_Status': ['Married', 'Single'],
    'Hometown': ['Lebanon', 'Springfield', 'Franklin', 'Washington', 'Clinton'],
    'Unit': [
        'IT', 'Logistics', 'Sales', 'Operations', 'R&D', 'Purchasing', 
        'Accounting and Finance', 'Human Resource Management', 'Marketing', 
        'Production', 'Quality', 'Security'
    ],
    'Decision_skill_possess': ['Conceptual', 'Analytical', 'Directive', 'Behavioral'],
    'Compensation_and_Benefits': ['type0', 'type1', 'type2', 'type3', 'type4']
}

st.title('Analyze Retention Rate')

input_data = {}

for feature, categories in categorical_features.items():
    input_data[feature] = st.selectbox(f'Select {feature}', options=categories)
for feature in numerical_features:
    input_data[feature] = st.number_input(f'Enter {feature}', value=0.0)
input_df = pd.DataFrame([input_data])
if st.button('Analyze'):
    prediction = model.predict(input_df)
    attrition = prediction[0] * 100
    retention = (1 - prediction[0])*100 
    st.write(f'Prediksi attrition rate: {attrition:.2f}%')
    st.write(f'Analisa retention rate menjadi: {retention:.2f}%')