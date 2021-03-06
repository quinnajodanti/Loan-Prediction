# -*- coding: utf-8 -*-
"""
Created on Sun May  1 22:06:40 2022

@author: Hp
"""
import numpy as np
import pickle
import streamlit as st
from PIL import Image

model =  pickle.load(open('loan.pkl', 'rb'))

img1 = Image.open('loan.jpg')
st.image(img1)
st.title('Loan Prediction Using Machine Learning')

def run():
    col1 = st.columns(1)
    col1_expander = st.expander("More Info")
    with col1_expander :
        st.subheader('About')
        st.write('This Loan prediction streamlit web app takes full name, gender, marital status, dependents, \
                 education, employment status, applicant’s income, co-applicant’s income, loan amount, loan duration, \
                 credit history and property area, after receiving input, the web app is using Support vector machine \
                 model to predict whether the bank should give the applicant loan based on the information.')
        st.write('这个贷款预测流线型网络应用程序接受全名、性别、婚姻状况、家属、教育、就业状况、\
                 申请人收入、共同申请人收入、贷款金额、贷款期限、信用记录和财产区域，在收到输入后，\
                 网络应用程序正在使用支持向量机模型来预测银行是否应该根据信息给申请人贷款。')
        
    ## Full name
    name = st.text_input('Full Name')
    
    ## for gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options,format_func=lambda x: gen_display[x])
    
    ## for marital status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status",mar_options,format_func=lambda x: mar_display[x])
    
    ## no of dependents
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",dep_options,format_func=lambda x: dep_display[x])
    
    
    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])
   
   ## For self_employed
    emp_display = ('No','Yes')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])
    
    
    ## for applicant income
    income = st.number_input('Applicant Income($)',value=0)
    
    ## Co-Applicant Monthly Income
    co_income = st.number_input('Co-Applicant Income($)',value=0)
    
    ## Loan amount
    loan_amt = st.number_input("Loan Amount",value=0)
    
    ## loan duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])
    
   ## credit history
    credit_display = ('No','Yes')
    cred_options = list(range(len(credit_display)))
    cred = st.selectbox("Credit History",cred_options,format_func=lambda x: credit_display[x])
    
    ##For property area
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])
    
    if st.button('Submit'):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, income, co_income, loan_amt, duration , cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Hello: " + name +" || "
                'According to our Calculations, you will not get the loan from Bank'
            )
        else:
            st.success(
                "Hello: " + name +" || "
                'Congratulations!! you will get the loan from Bank'
            )
            
run()
    
    


