import streamlit as st
from sympy import *
import numpy as np
import PHYS_Functions01 as PH01

def Cal_Acceleration_Ave(Cal_Ave_Num_Dim,Cal_Ave_Error_Str,Cal_Acceleration_App_num):
    st.write("### **＜Step0：平均加速度の定義と解説＞**")
    st.write("$\\quad$[こちらを参照：KIT物理ナビゲーションへ](https://w3e.kanazawa-it.ac.jp/math/physics/high-school_index/mechanics/motion/henkan-tex.cgi?target=/math/physics/high-school_index/mechanics/motion/acceleration.html)")
    Error_Str=Cal_Ave_Error_Str
    Dim_Num=Cal_Ave_Num_Dim
    App_num=Cal_Acceleration_App_num
    CB01_v=[]
    CB01_dv=[]
    CB01_str_v=[]
    CB01_str_v_ini={ 0:"t_i",
                     1:"t_f",
                     2:"Symbol(\"\Delta t\")",
                     3:"v_ix",
                     4:"v_fx",
                     5:"Symbol(\"\Delta v_x\")",
                     6:"v_iy",
                     7:"v_fy",
                     8:"Symbol(\"\Delta v_y\")",
                     9:"v_iz",
                    10:"v_fz",
                    11:"Symbol(\"\Delta v_z\")"
                    }
    
    st.write("### **＜Step1：時間の変化＞**")
    st.write("#### ▷ 時間の変化量の値を，変化の前後から計算するか，直接与えるか選択してください.")
    Method_Cal_dt={'１）変化の前後を入力':0,'２）変化量を直接を入力':1}
    Radio_cal_dt=st.radio(
        "",
        ('１）変化の前後を入力', '２）変化量を直接を入力')
        ,key="App%02d-1"+str(App_num)
        )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write('#### ▷ 変化前・後の時刻を入力してください．')
    CB01_Colum_T=st.columns([1,3,3,3])
    E_01=0
    if Method_Cal_dt[Radio_cal_dt]==0:        
        with CB01_Colum_T[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')        
        with CB01_Colum_T[1]:
            CB01_str_v.append(r"変化前の時刻(App%2d)"%(App_num))
            CB01_v.append(st.text_input(CB01_str_v[0],value=CB01_str_v_ini[0]))
        with CB01_Colum_T[2]:
            CB01_str_v.append(r"変化後の時刻(App%2d)"%(App_num))
            CB01_v.append(st.text_input(CB01_str_v[1],value=CB01_str_v_ini[1]))
            try:
                Tmp = sympify(CB01_v[1])- sympify(CB01_v[0])
            except:
                E_01 = 1
            else:
                CB01_dv.append(Tmp)
    else :
        with CB01_Colum_T[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')     
        with CB01_Colum_T[1]:
            CB01_str_v.append(r"時間の変化量(App%2d)"%(App_num))
            CB01_str_v.append("")
            CB01_v.append(st.text_input(CB01_str_v[0],value=CB01_str_v_ini[2]))
            CB01_v.append("")
            try :
                Tmp=sympify(CB01_v[0])
            except:
                E_01 = 1
            else:
                CB01_dv.append(Tmp)
    Num_Len_CB01_v0 = len(CB01_v)
    if E_01==1:
        ECB = st.checkbox(
                 "予想される原因(App%2d-%2d)：エラーが出ています．"%(App_num,1)
                 )
        if ECB : 
            st.markdown(Error_Str)


    st.write("### **＜Step2：速度の変化＞**")
    st.write("#### ▷ 速度の変化量の値を，変化の前後から計算するか，直接与えるか選択してください.")
    Method_Cal_dv={'１）変化の前後を入力':0,'２）変化量を直接を入力':1}
    Radio_cal_dv=st.radio(
                        "",
                        ('１）変化の前後を入力','２）変化量を直接を入力'),
                        key="App%02d-2"+str(App_num)
                        )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write("#### ▷ 変化する前・後の速度の各成分を入力してください．")
    CB01_Colum_R=st.columns([1,3,3,3])
    E_02 = 0
    for i in range(Dim_Num+1):
        if i == 0:
            with CB01_Colum_R[i]:
                st.write('$\\quad$')
                st.write('$\\quad$入力')  
        else:
            with CB01_Colum_R[i]:
                if Method_Cal_dv[Radio_cal_dv]==0:               
                   CB01_str_v.append( "変化前の速度の第"+str(i)+"成分(App%2d)"%(App_num))
                   CB01_v.append(st.text_input(CB01_str_v[2*i+0],value=CB01_str_v_ini[3*i+0]))
                   CB01_str_v.append( "変化後の速度の第"+str(i)+"成分(App%2d)"%(App_num))
                   CB01_v.append(st.text_input(CB01_str_v[2*i+1],value=CB01_str_v_ini[3*i+1]))
                   try:
                       Tmp = sympify(CB01_v[2*i+1])- sympify(CB01_v[2*i+0])
                   except:
                       E_02=1
                   else:
                        CB01_dv.append(Tmp)
                else:
                    CB01_str_v.append( "速度の変化量の第"+str(i)+"成分(App%2d)"%(App_num))
                    CB01_str_v.append( "")
                    CB01_v.append(st.text_input(CB01_str_v[2*i+0],value=CB01_str_v_ini[3*i+2]))
                    CB01_dv.append(sympify(CB01_v[i+1]))
    Num_Len_CB01_v = len(CB01_v) - Num_Len_CB01_v0
    if E_02==1:
        if st.checkbox(
                 "予想される原因(App%2d-%2d)：エラーが出ています．"%(App_num,1)
                 ) : 
                 st.markdown(Error_Str)

    st.write("### **＜Step3：平均加速度の計算＞**")
    if st.checkbox("結果の表示：平均加速度は，以下の通り",key="CB01_Result"):
        try:
            CB00_V_Average=PH01.Cal_Q_Average_ver01(CB01_dv[0],CB01_dv[1:4]) 
        except:
            ECB = st.checkbox("詳細表示(App%2d-%2d:エラーが出ています．)"%(App_num,3))
            if ECB : st.markdown(Error_Str)
        else : 
            Result_V_Ave1 = "\\displaystyle \\overrightarrow{a}_{\scriptscriptstyle{\\rm Ave.}} = "
            Result_V_Ave2 = PH01.List_to_vec01(CB00_V_Average)
            st.latex(Result_V_Ave1+Result_V_Ave2)

    if st.checkbox("途中の表示：各変化量は，以下の通り",key="CB01_proc"):
        Display_01 = "$\\qquad$"
        if Method_Cal_dt[Radio_cal_dt] == 0 :
            Display_01 += PH01.md("時間の変化量： $\\Delta t$ = $",CB01_dv[0],"$\n\n")
        else:
            Display_01 += PH01.md("時間の変化量： =$",CB01_dv[0],"$\n\n")
        r_index={0:"$v_x$",1:"$v_y$",2:"$v_z$"}
        for i in range(Dim_Num):
            if Method_Cal_dv[Radio_cal_dv] == 0 :
                Display_01 += PH01.md("$\\qquad$",r_index[i],"の変化量： ","$\\Delta$",r_index[i]," = $",CB01_dv[i+1],"$\n\n")
            else:
                Display_01 += PH01.md("$\\qquad$",r_index[i],"の変化量： =$",CB01_dv[i+1],"$\n\n") 
        st.markdown(Display_01)
