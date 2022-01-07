import streamlit as st
from sympy import *
import PHYS_Functions01

def Cal_Acceleration_Ave(Cal_Ave_Num_Dim,Cal_Ave_Error_Str,Cal_Acceleration_App_num):
    st.write("### **＜Step0:平均加速度の定義と解説＞**")
    st.write("$\\quad$[こちらを参照：KIT物理ナビゲーションへ](https://w3e.kanazawa-it.ac.jp/math/physics/high-school_index/mechanics/motion/henkan-tex.cgi?target=/math/physics/high-school_index/mechanics/motion/acceleration.html)")
    Error_Str=Cal_Ave_Error_Str
    Num_Dim=Cal_Ave_Num_Dim
    App_num=Cal_Acceleration_App_num
    E_01=0
    st.write("### **＜Step1:時間の変化量＞**")

    Cal_A_radio_str_dt="▷ 時間の変化量の値を，変化の前後から計算するか，直接与えるか選択してください."
    Radio_cal_dt=st.radio(
        Cal_A_radio_str_dt,
        ('１）変化の前後', '２）直接')
        ,key="App%02d-1"+str(App_num)
        )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Method_Cal_dt={'１）変化の前後':0,'２）直接':1}
    if Method_Cal_dt[Radio_cal_dt]==0:
        st.write('#### ▷ 変化前・後の時刻を入力してください．')
        CB01_col_Time=st.columns([1,3,3])
        with CB01_col_Time[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')        
        with CB01_col_Time[1]:
            CB01_T_i =  st.text_input(r"変化前の時刻(App%2d)"%(App_num),value="t_i")
        with CB01_col_Time[2]:
            CB01_T_f =  st.text_input(r"変化後の時刻(App%2d)"%(App_num),value="t_f")
        try:
            Delta_t = sympify(CB01_T_f) - sympify(CB01_T_i)
        except:
            E_01 = 1
    else :
        CB01_col_Time=st.columns([1,3])
        with CB01_col_Time[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')     
        with CB01_col_Time[1]:
            
            CB01_T_d =  st.text_input(r"時間の変化量(App%2d)"%(App_num),value="Symbol(\"\Delta t\")")
        try:
            Delta_t = sympify(CB01_T_d)
        except:
            E_01 = 1
    if E_01==1 :
        ECB = st.checkbox(
                "予想される原因(App%2d-%2d)：エラーが出ています．"%(App_num,1)
                )
        if ECB : st.markdown(Error_Str)


    st.write("### **＜Step2:速度の変化量＞**")

    Cal_A_select_str_dr="▷ 位置の変化量の値を，変化の前後から計算するか，直接与えるか選択してください."
    Radio_cal_dr=st.radio(
                                Cal_A_select_str_dr,
                                ('１）変化の前後', '２）直接'),
                                key="App%02d-2"+str(App_num)
                                )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Method_Cal_dr={'１）変化の前後':0,'２）直接':1}
    if Method_Cal_dr[Radio_cal_dr]==0:
        st.write("##### ▷ 変化する前・後の速度の各成分を入力してください．")
        E_02=0
        Nnn0=[1]
        for i in range(Num_Dim):
            Nnn0.append(3)
        CB01_col_A= st.columns(Nnn0)
        CB01_v_i=[]
        CB01_v_f=[]
        CB01_str_v_i=[]
        CB01_str_v_f=[]
        CB01_str_v_i_ini={0:"v_ix",1:"v_iy",2:"v_iz"}
        CB01_str_v_i_final={0:"v_fx",1:"v_fy",2:"v_fz"}
        with CB01_col_A[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')  
        for i in range(Num_Dim):
            with CB01_col_A[i+1]:
                CB01_str_v_i.append( "変化前の速度の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                CB01_v_i.append(st.text_input(CB01_str_v_i[i],value=CB01_str_v_i_ini[i]))
                CB01_str_v_f.append( "変化後の速度の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                CB01_v_f.append(st.text_input(CB01_str_v_f[i],value=CB01_str_v_i_final[i]))
        try:
            Delta_v = []
            for i in range(len(CB01_v_i)):
                Delta_v.append(
                     sympify( CB01_v_f[i]) - sympify(CB01_v_i[i]) 
                 )
        except:
            E_02 = 1

    else:
        st.write("##### ▷ 速度の変化量の各成分を入力してください．")
        E_02=0
        Delta_v=[]
        CB01_str_v_d=[]
        Nnn0=[1]
        for i in range(Num_Dim):
            Nnn0.append(3)
        CB01_col_A= st.columns(Nnn0)
        CB01_str_v_d_ini={0:"Symbol(\"\Delta v_x\")",1:"Symbol(\"\Delta v_y\")",2:"Symbol(\"\Delta v_z\")"}
        with CB01_col_A[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')  
        for i in range(Num_Dim):
            with CB01_col_A[i+1]:
                CB01_str_v_d.append( "速度の変化量の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                try:
                    Delta_v.append(sympify(st.text_input(CB01_str_v_d[i],value=CB01_str_v_d_ini[i])))
                except:
                    E_02 = 1
    
    if E_02==1 :
            ECB = st.checkbox("詳細表示(App%2d-%2d):エラーが出ています．"%(App_num,2))
            if ECB : st.markdown(Error_Str)
    
    st.write("### **＜Step3:平均加速度が出力されます．＞**")
    try:
        CB01_A_Average=PHYS_Functions01.Cal_Q_Average_ver01(Delta_t,Delta_v) 
    except:
        ECB = st.checkbox("詳細表示(App%2d-%2d:エラーが出ています．)"%(App_num,3))
        if ECB : st.markdown(Error_Str)
    else : 
        Result_A_Ave1 = "\\displaystyle \\overrightarrow{a}_{\scriptscriptstyle{\\rm Ave.}} = "
        Result_A_Ave2 = PHYS_Functions01.List_to_vec01(CB01_A_Average)
        st.latex(Result_A_Ave1+Result_A_Ave2)