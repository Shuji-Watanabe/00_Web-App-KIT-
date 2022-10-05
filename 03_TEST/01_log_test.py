import streamlit


import streamlit as st
import pandas as pd
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
d = now.strftime('%Y%m%d%H%M%S')

DF = []

cols = st.columns(3)
with cols[0] :
    username = st.text_input("ユーザー名")


score=0
tmp_num = 0 
x = 0
with cols[1] :
    x += 1
    list_ans1 = {"無回答":-1 ,"AAA":0,"BBB":1,"CCC":0,"DDD":0}
    n1 = st.radio("答え1",list_ans1.keys()) 

    if list_ans1[n1] != -1 : 
        tmp_num += 1
        score += list_ans1[n1]

with cols[2] :
    x += 1
    list_ans2 = {"無回答":-1 ,"AAA":0,"BBB":1,"CCC":0,"DDD":0}
    n2 = st.radio("答え2",list_ans2.keys())
    if list_ans2[n2] != -1 : 
        tmp_num += 1
        score += list_ans2[n2]

if tmp_num >= x and len(str(username)) != 0:
    tmp_DF = ["","",""] 
    tmp_DF[0]=username
    tmp_DF[1]=d
    tmp_DF[2]=score
    st.write(tmp_DF)
    df = pd.DataFrame([tmp_DF],columns=['id', 'time', 'score'])
    if st.button("Submit"):
        df.to_csv("./employee.csv", sep=",")

