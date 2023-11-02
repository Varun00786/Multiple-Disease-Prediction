import streamlit as st
from streamlit_option_menu import option_menu
import joblib
model=joblib.load("d1")
model1=joblib.load("heart_model")
model2=joblib.load("pakinson_model")


with st.sidebar:
    
    selected=option_menu(options=["Diabetes Disease Prediction","Heart Disease Prediction","Parkinson's Disease Prediction"],
                         menu_title="Multiple Disease Prediction Using ML",
                         default_index=0,menu_icon="list",icons=["activity","heart-pulse-fill","hospital"])
    
if selected=="Diabetes Disease Prediction":

    st.title("Diabetes Disease Prediction")
    st.header("fill your Symptoms")
    
    with st.form(key="form",clear_on_submit=True):
    
        col1,col2=st.columns([2,2])
        pregnancies=col1.text_input("Enter the no. of Pregnancies")
        glucose=col2.text_input("Enter the value of Glucose")
        bp=col1.text_input("Enter the value of BloodPressure")
        skt=col2.text_input("Enter the value of SkinThickness")
        insulin=col1.text_input("Enter the value of Insulin")
        bmi=col2.text_input("Enter the value of BMI")
        dpf=col1.text_input("Enter DiabetesPedigreeFunction value (in Decimal)")
        age=col2.text_input("Enter the value of Age")
        submit_button=st.form_submit_button("Check Prediction")
        h=pregnancies+glucose+bp+skt+insulin+bmi+dpf+age
    if submit_button:
        if pregnancies and glucose and bp and skt and insulin and bmi and dpf and age !="":
            if any(i.isalpha() for i in h):
                st.error("Please fill the correct Details")
            else:
                p=model.predict([[int(pregnancies),int(glucose),int(bp),int(skt),int(insulin),float(bmi),float(dpf),int(age)]])[0]
                print(p)
                if p==0:
                    st.subheader("The person is not diabetic")
                else:
                    st.subheader("The person is diabetic")
        else:
            st.error("Please fill all the detalis")
    

    
if selected=="Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    st.header("fill following Details")
    with st.form(key="formht",clear_on_submit=True):
        col1,col2=st.columns([1,1])
        age=col1.text_input("Enter the age",key="1")
        gender=col2.selectbox("Enter the gender",options=["Male","Female"])
        imp=col1.text_input("Enter the value of Heart rate",key="2")
        prh=col2.text_input("Enter the Highest value of  blood pressure",key="3")
        prl=col1.text_input("Enter the Lowest value of  blood pressure",key="4")
        glucose=col2.text_input("Enter the value of Glucose level (in  Decimal)",key="5")
        kcm=col1.text_input("Enter the value of Creatine kinase-MB (in Decimal) ",key="6")
        trn=col2.text_input("Enter the value of Troponin level (in Decimal)",key="7")
        sub_button=st.form_submit_button("Check Prediction")
    g=age+glucose+imp+prh+prl+kcm+trn
    if gender=="Male":
        gender=1
    else:
        gender=0
    if sub_button:
                if age and glucose  and imp and prh and prl and kcm and trn !="":
                    if any(i.isalpha() for i in g):
                        st.error("Please fill the correct Details")
                    else:
                        p=model1.predict([[int(age),int(gender),int(imp),
                                        int(prh),int(prl),float(glucose),float(kcm),float(trn)]])[0]
                        print(p)
                        if p=="negative":
                            st.subheader('The person does not have any heart disease')
                        else:
                            st.subheader('The person is having heart disease')
                    
                else:
                    st.error("Please fill all the detalis")

if selected=="Parkinson's Disease Prediction":
    st.title("Parkinson's Disease Prediction")
    st.header("fill your Symptoms")


    s=  """ MDVP:Fo(Hz) - Average vocal fundamental frequency
MDVP:Fhi(Hz) - Maximum vocal fundamental frequency
MDVP:Flo(Hz) - Minimum vocal fundamental frequency
MDVP:Jitter(%)and MDVP:Jitter(Abs) and MDVP:RAP and MDVP:PPQ and Jitter:DDP 
- Several measures of variation in fundamental frequency
MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA 
- Several measures of variation in amplitude
NHR,HNR - Two measures of ratio of noise to tonal components in the voice
RPDE,D2 - Two nonlinear dynamical complexity measures
DFA - Signal fractal scaling exponent
spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation"""


    with st.form(key="form",clear_on_submit=True):

        col1,col2=st.columns([2,2])
        mdvpfo=col1.text_input("Enter the Average vocal fundamental frequency",key="1")
        mdvpfhi=col2.text_input("Enter the Maximum vocal fundamental frequency",key="2")
        mdvpflo=col1.text_input("Enter the Minimum vocal fundamental frequency",key="3")
        mdvpjit=col2.text_input("Enter the Value of MDVP Jitter (%)",key="4")
        mdvpabs=col1.text_input("Enter the Value of MDVP Jitter (in abs)",key="5")
        jitddp=col2.text_input("Enter the Value of Jitter DDP",key="6")
        mdvprap=col1.text_input("Enter the Value of MDVP RAP",key="7")
        mdvpppq=col2.text_input("Enter the Value of MDVP PPQ",key="8")
        mdvpsh=col1.text_input("Enter the Value of MDVP Shimmer",key="9")
        mdvpshdb=col2.text_input("""Enter the Value of MDVP Shimmer (dB)""",key="10")
        shi3=col1.text_input("Enter the Value of Shimmer APQ3",key="11")
        shi5=col2.text_input("Enter the Value of Shimmer APQ5",key="12")
        mdvpaq=col1.text_input("Enter the Value of MDVP APQ",key="13")
        shidda=col2.text_input("Enter the Value of Shimmer DDA",key="14")
        nhr=col1.text_input("Enter the value of NHR",key="15")
        hnr=col2.text_input("Enter the value of HNR",key="16")
        rpde=col1.text_input("Enter the value of RPDE",key="17")
        d2=col2.text_input("Enter the value of D2",key="18")
        dfa=col1.text_input("Enter the value of DFA",key="19")
        spread1=col2.text_input("Enter the value of Spread1",key="20")
        spread2=col1.text_input("Enter the value of Spread2",key="21")
        ppe=col2.text_input("Enter the value of PPE",key="22")
        submit_button=st.form_submit_button("Check Prediction")

    h=mdvpfo+mdvpfhi+mdvpflo+mdvpjit+mdvpabs+jitddp+mdvprap+mdvpppq+mdvpsh+mdvpshdb+shi3+shi5+mdvpaq+shidda+nhr+hnr+rpde+d2+dfa+spread1+spread2+ppe
    if submit_button:
        if mdvpfo and mdvpfhi and mdvpflo and mdvpjit and mdvpabs and jitddp and mdvprap and mdvpppq and mdvpsh and mdvpshdb and shi3 and shi5 and mdvpaq and shidda and nhr and hnr and rpde and d2 and dfa and spread1 and spread2 and ppe!="":
            if any(i.isalpha() for i in h):
                st.error("Please fill the correct Details")
            else:
                p=model2.predict([[float(mdvpfo),float(mdvpfhi),float(mdvpflo),float(mdvpjit),float(mdvpabs),float(jitddp),float(mdvprap),float(mdvpppq),float(mdvpsh),float(mdvpshdb),float(shi3),float(shi5),float(mdvpaq),float(shidda),float(nhr),float(hnr),float(rpde),float(d2),float(dfa),float(spread1),float(spread2),float(ppe)]])[0]
                print(p)
                if p==0:
                    st.subheader("The person does not have Parkinson's disease")
                else:
                    st.success("The person has Parkinson's disease")
        else:
            st.error("Please fill all the detalis")
    f=st.button("Symptoms Details")
    if f :
        st.text(s)