import streamlit as st
from sympy import *
import numpy as np
import PHYS_Functions01 as PH01

def Cal_Velocity_Ave(Cal_Ave_Num_Dim,Cal_Ave_Error_Str,Cal_Velocity_App_num):
    st.write("### **＜Step0：平均速度の定義と解説＞**")
    st.write("$\\quad$[こちらを参照：KIT物理ナビゲーションへ](https://w3e.kanazawa-it.ac.jp/math/physics/high-school_index/mechanics/motion/henkan-tex.cgi?target=/math/physics/high-school_index/mechanics/motion/velocity.html)")
    Error_Str=Cal_Ave_Error_Str
    Dim_Num=Cal_Ave_Num_Dim
    App_num=Cal_Velocity_App_num
    CB00_r=[]
    CB00_dr=[]
    CB00_str_r=[]
    CB00_str_r_ini={ 0:"t_i",
                     1:"t_f",
                     2:"Symbol(\"\Delta t\")",
                     3:"x_i",
                     4:"x_f",
                     5:"Symbol(\"\Delta x\")",
                     6:"y_i",
                     7:"y_f",
                     8:"Symbol(\"\Delta y\")",
                     9:"z_i",
                    10:"z_f",
                    11:"Symbol(\"\Delta z\")"
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
    CB00_Colum_T=st.columns([1,3,3,3])
    E_01=0
    if Method_Cal_dt[Radio_cal_dt]==0:        
        with CB00_Colum_T[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')        
        with CB00_Colum_T[1]:
            CB00_str_r.append(r"変化前の時刻(App%2d)"%(App_num))
            CB00_r.append(st.text_input(CB00_str_r[0],value=CB00_str_r_ini[0]))
        with CB00_Colum_T[2]:
            CB00_str_r.append(r"変化後の時刻(App%2d)"%(App_num))
            CB00_r.append(st.text_input(CB00_str_r[1],value=CB00_str_r_ini[1]))
            try:
                Tmp = sympify(CB00_r[1])- sympify(CB00_r[0])
            except:
                E_01 = 1
            else:
                CB00_dr.append(Tmp)
    else :
        with CB00_Colum_T[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')     
        with CB00_Colum_T[1]:
            CB00_str_r.append(r"時間の変化量(App%2d)"%(App_num))
            CB00_str_r.append("")
            CB00_r.append(st.text_input(CB00_str_r[0],value=CB00_str_r_ini[2]))
            CB00_r.append("")
            try :
                Tmp=sympify(CB00_r[0])
            except:
                E_01 = 1
            else:
                CB00_dr.append(Tmp)
    Num_Len_CB00_r0 = len(CB00_r)
    if E_01==1:
        ECB = st.checkbox(
                 "予想される原因(App%2d-%2d)：エラーが出ています．"%(App_num,1)
                 )
        if ECB : 
            st.markdown(Error_Str)


    st.write("### **＜Step2：位置の変化＞**")
    st.write("#### ▷ 位置の変化量（変位）の値を，変化の前後から計算するか，直接与えるか選択してください.")
    Method_Cal_dr={'１）変化の前後を入力':0,'２）変化量を直接を入力':1}
    Radio_cal_dr=st.radio(
                        "",
                        ('１）変化の前後を入力','２）変化量を直接を入力'),
                        key="App%02d-2"+str(App_num)
                        )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write("#### ▷ 変化する前・後の位置の各成分を入力してください．")
    CB00_Colum_R=st.columns([1,3,3,3])
    E_02 = 0
    for i in range(Dim_Num+1):
        if i == 0:
            with CB00_Colum_R[i]:
                st.write('$\\quad$')
                st.write('$\\quad$入力')  
        else:
            with CB00_Colum_R[i]:
                if Method_Cal_dr[Radio_cal_dr]==0:               
                   CB00_str_r.append( "変化前の位置の第"+str(i)+"成分(App%2d)"%(App_num))
                   CB00_r.append(st.text_input(CB00_str_r[2*i+0],value=CB00_str_r_ini[3*i+0]))
                   CB00_str_r.append( "変化後の位置の第"+str(i)+"成分(App%2d)"%(App_num))
                   CB00_r.append(st.text_input(CB00_str_r[2*i+1],value=CB00_str_r_ini[3*i+1]))
                   try:
                       Tmp = sympify(CB00_r[2*i+1])- sympify(CB00_r[2*i+0])
                   except:
                       E_02=1
                   else:
                        CB00_dr.append(Tmp)
                else:
                    CB00_str_r.append( "位置の変化量の第"+str(i)+"成分(App%2d)"%(App_num))
                    CB00_str_r.append( "")
                    CB00_r.append(st.text_input(CB00_str_r[2*i+0],value=CB00_str_r_ini[3*i+2]))
                    CB00_dr.append(sympify(CB00_r[i+1]))
    Num_Len_CB00_r = len(CB00_r) - Num_Len_CB00_r0
    if E_02==1:
        if st.checkbox(
                 "予想される原因(App%2d-%2d)：エラーが出ています．"%(App_num,1)
                 ) : 
                 st.markdown(Error_Str)

    st.write("### **＜Step3：平均速度の計算＞**")
    if st.checkbox("結果の表示：平均速度は，以下の通り",key="Result"):
        try:
            CB00_V_Average=PH01.Cal_Q_Average_ver01(CB00_dr[0],CB00_dr[1:4]) 
        except:
            ECB = st.checkbox("詳細表示(App%2d-%2d:エラーが出ています．)"%(App_num,3))
            if ECB : st.markdown(Error_Str)
        else : 
            Result_V_Ave1 = "\\displaystyle \\overrightarrow{v}_{\scriptscriptstyle{\\rm Ave.}} = "
            Result_V_Ave2 = PH01.List_to_vec01(CB00_V_Average)
            st.latex(Result_V_Ave1+Result_V_Ave2)

    if st.checkbox("途中の表示：各変化量は，以下の通り",key="proc"):
        Display_01 = "$\\qquad$"
        if Method_Cal_dt[Radio_cal_dt] == 0 :
            Display_01 += PH01.md("時間の変化量： $\\Delta t$ = $",CB00_dr[0],"$\n\n")
        else:
            Display_01 += PH01.md("時間の変化量： =$",CB00_dr[0],"$\n\n")
        r_index={0:"$x$",1:"$y$",2:"$z$"}
        for i in range(Dim_Num):
            if Method_Cal_dr[Radio_cal_dr] == 0 :
                Display_01 += PH01.md("$\\qquad$",r_index[i],"の変化量： ","$\\Delta$",r_index[i]," = $",CB00_dr[i+1],"$\n\n")
            else:
                Display_01 += PH01.md("$\\qquad$",r_index[i],"の変化量： =$",CB00_dr[i+1],"$\n\n") 
        st.markdown(Display_01)
