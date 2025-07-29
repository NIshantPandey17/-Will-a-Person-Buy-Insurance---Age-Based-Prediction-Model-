import pickle
import streamlit as st

model1=pickle.load(open("insurance_brought.pkl","rb"))

def mydeploy():
    st.title("Insurance Brought Predictor")
    age= st.number_input("Enter age of a person :")
    pred=st.button("Predict")

    if pred:
        x=model1.predict([[age]])

        if x == 0:
            st.success("❌ The person is **not likely** to buy insurance ")
        elif x == 1:
            st.success("✅ The person is **likely** to buy insurance.")
        


 
mydeploy()    