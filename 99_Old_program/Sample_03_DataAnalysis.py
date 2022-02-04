import streamlit as st
import pandas as pd
import math

st.write("## 2021年度学期末総合評価の自動採点アプリ")
Data_file00= st.file_uploader("**データファイルをアップロードしてください**", type={"csv"})

if Data_file00:
    df = pd.read_csv(Data_file00, header=0,sep=",",encoding="cp932")
    #set parameter
    LIST01 = ["氏名","回答","回答.1","回答.2","回答.3","回答.4","回答.5","回答.6","回答.7"]
    LIST02 = ["氏名","回答.8","回答.9","回答.10","回答.11","回答.12","回答.13","回答.14"]
    LIST03 = ["氏名","回答.15","回答.16","回答.17","回答.18","回答.19","回答.20"]
    LIST04 = ["氏名","回答.21","回答.22","回答.23","回答.24","回答.25","回答.26"]
    LIST05 = ["氏名","回答.27","回答.28","回答.29","回答.30","回答.31","回答.32"]
    LIST06 = ["氏名","回答.33","回答.34","回答.35","回答.36","回答.37"]
    LIST07 = ["氏名","回答.38","回答.39","回答.40","回答.41","回答.42","回答.43"]

    Cond01 = ["両方","理解","技能"]

    # def functions
    def discriminantF1(a):
        if a > 3:
            x = 3
        elif a == 3:
            x = 2
        elif a < 3 :
            x = 1
        return x

    def discriminantF2(a):
        if a > 4:
            x = 3
        elif a == 4:
            x = 2
        elif a < 4:
            x = 1
        return x

    def discriminantF3(a):
        if  a > 2:
            x = 3
        elif a == 2:
            x = 2
        elif a < 2:
            x = 1
        return x

    def discriminantF4(a):
        if  a > 4:
            x = 6
        elif a == 4:
            x = 4
        elif a == 3:
            x = 2        
        elif a < 3:
            x = 1
        return x

    Nrange = len(df)

    SCORE=[[0]* 17 for i in range(Nrange)]
    SCORE=pd.DataFrame(SCORE)

    for i in range(Nrange):
        #条件に合う要素のカウント
        SCORE.iloc[i,0]=df[LIST01].iloc[i,0]
        SCORE.iloc[i,1]=df[LIST01].iloc[i,1:].str.contains(Cond01[0]).sum()
        SCORE.iloc[i,2]=df[LIST02].iloc[i,1:].str.contains(Cond01[0]).sum()
        SCORE.iloc[i,3]=df[LIST03].iloc[i,1:].str.contains(Cond01[1]).sum()
        SCORE.iloc[i,4]=df[LIST04].iloc[i,1:].str.contains(Cond01[0]).sum()
        SCORE.iloc[i,5]=df[LIST05].iloc[i,1:].str.contains(Cond01[0]).sum()
        SCORE.iloc[i,6]=df[LIST06].iloc[i,1:].str.contains(Cond01[0]).sum()
        SCORE.iloc[i,7]=df[LIST07].iloc[i,1:].str.contains(Cond01[2]).sum()

        SCORE.iloc[i,8]=df["提出状況"].iloc[i]

        #採点
        SCORE.iloc[i,9] =discriminantF2(SCORE.iloc[i,1])
        SCORE.iloc[i,10]=discriminantF1(SCORE.iloc[i,2])
        SCORE.iloc[i,11]=discriminantF1(SCORE.iloc[i,3])
        SCORE.iloc[i,12]=discriminantF1(SCORE.iloc[i,4])
        SCORE.iloc[i,13]=discriminantF1(SCORE.iloc[i,5])
        SCORE.iloc[i,14]=discriminantF3(SCORE.iloc[i,6])
        SCORE.iloc[i,15]=discriminantF4(SCORE.iloc[i,7])

        for j in range(7):
            SCORE.iloc[i,16]=SCORE.iloc[i,16]+SCORE.iloc[i,j+9]
            
        SCORE.iloc[i,16]=SCORE.iloc[i,8]*SCORE.iloc[i,16]
        
    ColumNs= ["学生氏名"]
    ColumNs+=["カウント1","カウント2","カウント3","カウント4","カウント5","カウント6","カウント7"]
    ColumNs+=["提出状況"]
    ColumNs+=["採点１","採点２","採点３","採点４","採点５","採点６","採点７"]
    ColumNs+=["合計"]

    SCORE.columns=ColumNs
    st.dataframe(SCORE)
    OUTPUT = SCORE.to_csv().encode("cp932")
    st.download_button(label="Download data as CSV",data=OUTPUT,file_name='output.csv',mime='text/csv',key='download-csv')
else:
    st.write("ファイルがアップロードされていないか，アップロードしたファイルに誤りがあるようです")
