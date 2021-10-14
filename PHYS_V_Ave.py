import streamlit as st
from sympy import *
import PHYS_Functions01

def Cal_Ave(Cal_Ave_Num_Dim,Cal_Ave_Error_Str):
    st.write("### Step1:変化前・後の時刻か時間の変化量の値または式を入力してください．")
    Error_Str=Cal_Ave_Error_Str
    Num_Dim=Cal_Ave_Num_Dim
    CB0_col_Time=st.columns(3)
    with CB0_col_Time[0]:
        CB0_T_i =  st.text_input("変化前の時刻")
    with CB0_col_Time[1]:
        CB0_T_f =  st.text_input("変化後の時刻")
    with CB0_col_Time[2]:
        CB0_T_Deltat =  st.text_input("時間の変化量")
    try:
        if len(CB0_T_Deltat) == 0 :
            Delta_t = sympify(CB0_T_f) - sympify(CB0_T_i)
        else:
            Delta_t = sympify(CB0_T_Deltat)
    except:
        st.write("※ 時間の変化量の計算でエラーが出ています．")
        st.markdown(Error_Str)

    st.write("### Step2:変化前・後の速度の各成分の値または式を入力してください．")
    CB0_col_V= st.columns(Num_Dim)
    CB0_V_i=[]
    CB0_V_f=[]
    CB0_str_V_i=[]
    CB0_str_V_f=[]
    for i in range(Num_Dim):
        with CB0_col_V[i]:
            CB0_str_V_i.append( "変化前の速度の第"+str(int(i)+1)+"成分")
            CB0_str_V_f.append( "変化後の速度の第"+str(int(i)+1)+"成分")
            
            CB0_V_i.append(st.text_input(CB0_str_V_i[i]))
            CB0_V_f.append(st.text_input(CB0_str_V_f[i]))

    st.write("### Step3:平均速度が出力されます．")
    try:
        CB0_V_Average=PHYS_Functions01.Cal_V_Average_ver01(Delta_t,CB0_V_i,CB0_V_f)    
    except:
        st.write("※ 平均速度の計算でエラーが出ています．")
        st.markdown(Error_Str)
    else : 
        Result_V_Ave1 = "\\displaystyle \\overrightarrow{v}_{\\rm Ave.} = "
        Result_V_Ave2 = PHYS_Functions01.List_to_vec01(CB0_V_Average)
        st.latex(Result_V_Ave1+Result_V_Ave2)