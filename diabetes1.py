import numpy as np
import pandas as pd
import pickle
import streamlit as st

from PIL import Image

pickle_in = open('C:\\Users\\user\\Desktop\\Naheemah\\Personal Projects\\diabetes indication\\logistic_regression_model_for_diabetes.pkl', 'rb')
logistic_regression_model_for_diabetes = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_diabetes(HighBP, HighChol, CholCheck, BMI, Smoker,
       Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
       HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
       MentHlth, PhysHlth, DiffWalk, Sex, Age):
    
    # Check if input values are not empty
    if not HighBP or not HighChol or not CholCheck or not BMI or not Smoker \
        or not Stroke or not HeartDiseaseorAttack or not PhysActivity \
        or not Fruits or not Veggies or not HvyAlcoholConsump \
        or not AnyHealthcare or not NoDocbcCost or not GenHlth \
        or not MentHlth or not PhysHlth or not DiffWalk or not Sex or not Age:
        
        return "Please enter values for all features."

    # Convert input features to float
    HighBP = float(HighBP)
    HighChol = float(HighChol)
    CholCheck = float(CholCheck)
    BMI = float(BMI)
    Smoker = float(Smoker)
    Stroke = float(Stroke)
    HeartDiseaseorAttack = float(HeartDiseaseorAttack)
    PhysActivity = float(PhysActivity)
    Fruits = float(Fruits)
    Veggies = float(Veggies)
    HvyAlcoholConsump = float(HvyAlcoholConsump)
    AnyHealthcare = float(AnyHealthcare)
    NoDocbcCost = float(NoDocbcCost)
    GenHlth = float(GenHlth)
    MentHlth = float(MentHlth)
    PhysHlth = float(PhysHlth)
    DiffWalk = float(DiffWalk)
    Sex = float(Sex)
    Age = float(Age)
    # Education = float(Education)
    # Income = float(Income)

    prediction = logistic_regression_model_for_diabetes.predict([[HighBP, HighChol, CholCheck, BMI, Smoker,
    Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
    HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
    MentHlth, PhysHlth, DiffWalk, Sex, Age]])

    print(prediction)
    return prediction

def main():
    st.title ('Welcome...')
    html_temp = """

    <div style="background-color: blue; padding:10px">
    <h1 style="color:white;text-align:center;">DIABETES HEALTH INDICATOR ML APP </h1>
    </div>
    <br>
    <p style="color: cyan;text-align:center;">Instruction : HighChol: Cholesterol levels, CholCheck: Cholesterol Check history, BMI: Body Mass Index, 
       Smoker: Smoking habits, Stroke: Stroke history, HeartDiseaseorAttack: History of heart-related issues, 
        PhysActivity: Physical Activity levels, Fruits: Fruit consumption, Veggies: Vegetable consumption, 
        HvyAlcoholConsump: Heavy Alcohol Consumption, AnyHealthcare: Access to healthcare, 
        NoDocbcCost: Healthcare costs coverage, DiffWalk: Difficulty in walking, Sex: Gender, 
        Age: Age of individuals. <b>THE INPUT FOR ALL THESE SHOULD BE 0 (no) OR 1(yes) except BMI, Age and Sex 0 for female, 1 for male)</b></p>
    <p style="color:cyan;text-align:center;"> GenHlth: General health perception can take input from 1 - 5. <b>(1: Very Sick, 2: Sick, 3: Neutral, 4: Healthy,5: Very Healthy)</b></p>
    <p style="color:cyan;text-align:center;"> The 'MentHlth' (Mental Health Perception) and 'PhysHlth' (Physical Health Perception) features represent the patient's self-perceived health status in the context of mental and physical well-being, respectively. The specific values assigned to these features can vary. THE INPUT SHOULD BE BETWEEN 0 - 30. Higher values indicate a more positive perception of health, while lower values suggest a less favorable perception.</P>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    HighBP = st.text_input("HighBP")
    HighChol = st.text_input("HighChol")
    CholCheck = st.text_input("CholCheck")
    BMI = st.text_input("BMI")
    Smoker = st.text_input("Smoker")
    Stroke = st.text_input("Stroke")
    HeartDiseaseorAttack = st.text_input("HeartDiseaseAttack" )
    PhysActivity = st.text_input("PhysActivity")
    Fruits = st.text_input("Fruits", )
    Veggies = st.text_input("Veggies", )
    HvyAlcoholConsump = st.text_input("HvyAlcoholConsump")
    AnyHealthcare = st.text_input("AnyHealthcare")
    NoDocbcCost = st.text_input("NoDocbcCost")
    GenHlth = st.text_input("GenHlth")
    MentHlth =st.text_input("MenHlth")
    PhysHlth = st.text_input("PhysHlth")
    DiffWalk = st.text_input("DiffWalk")
    Sex = st.text_input("Sex")
    Age = st.text_input("Age")
    # Education = st.text_input("Education")
    # Income = st.text_input("Income")

    result=""
    prediction = ''

    if st.button("Predict"):
        prediction=predict_diabetes(HighBP, HighChol, CholCheck, BMI, Smoker,
       Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
       HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
       MentHlth, PhysHlth, DiffWalk, Sex, Age)
        
        
    st.success(f'The raw prediction value is {prediction}')
    # Check if the prediction is greater than 0.5
    if prediction and prediction[0] > 0.5:
        result = "Healthy"
    else:
        result = "At risk of having diabetes"

    # Print the risk assessment
    st.success(f'The patient is {result}')

    if st.button("About"):
        st.text("""
            Diabetes, a global epidemic affecting millions, encompasses various types—Type 1, Type 2, and gestational diabetes—each with distinct causes and risk factors. 
            In Type 1 diabetes, the immune system mistakenly attacks insulin-producing cells, while Type 2 results from ineffective insulin use. 
            Lifestyle choices, such as diet and physical activity, significantly impact Type 2 diabetes.
            Gestational diabetes, occurring during pregnancy, heightens the risk for both mother and baby to develop Type 2 diabetes later. 
            Regular blood sugar monitoring, typically using a blood glucose meter, is crucial for effective diabetes management. 
            Diabetes can lead to complications like heart disease, kidney issues, vision problems, and nerve damage.
            Despite ongoing research, there is currently no cure for diabetes. However, proper management through medication, lifestyle adjustments, and sometimes insulin therapy empowers individuals to lead healthy lives. 
            Technological advances, including insulin pumps and continuous glucose monitoring, have revolutionized diabetes care.
            Community support and awareness initiatives are pivotal in providing education, resources, and emotional support to those affected by diabetes. 
            As we delve into the complexities of this condition, let's appreciate the strides in technology and the resilience of individuals managing diabetes worldwide.
        """)

        # st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    