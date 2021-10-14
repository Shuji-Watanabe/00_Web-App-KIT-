import streamlit as st
from sympy import *
import PHYS_Functions01

def Cal_Velocity_Ave(Cal_Ave_Num_Dim,Cal_Ave_Error_Str,Cal_Velocity_App_num):
    st.write("### **Step0:平均速度の定義と解説**")
    st.write("$\\quad$[こちらを参照：KIT物理ナビゲーションへ](https://w3e.kanazawa-it.ac.jp/math/physics/high-school_index/mechanics/motion/henkan-tex.cgi?target=/math/physics/high-school_index/mechanics/motion/velocity.html)")
    Error_Str=Cal_Ave_Error_Str
    Num_Dim=Cal_Ave_Num_Dim
    App_num=Cal_Velocity_App_num
    E_01=0
    st.write("### **Step1:時間の変化量**")

    Cal_V_select_str_dt="▷ 時間の変化量の値を，変化の前後から計算するか，直接与えるか選択してください."
    Radio_cal_dt=st.radio(
        Cal_V_select_str_dt,
        ('１）変化の前後', '２）直接')
        ,key="App%02d-1"+str(App_num)
        )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Method_Cal_dt={'１）変化の前後':0,'２）直接':1}
    if Method_Cal_dt[Radio_cal_dt]==0:
        st.write('#### ▷ 変化前・後の時刻を入力してください．')
        CB0_col_Time=st.columns([1,3,3])
        with CB0_col_Time[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')        
        with CB0_col_Time[1]:
            CB0_T_i =  st.text_input(r"変化前の時刻(App%2d)"%(App_num),value="t_i")
        with CB0_col_Time[2]:
            CB0_T_f =  st.text_input(r"変化後の時刻(App%2d)"%(App_num),value="t_f")
        try:
            Delta_t = sympify(CB0_T_f) - sympify(CB0_T_i)
        except:
            E_01 = 1
    else :
        CB0_col_Time=st.columns([1,3])
        with CB0_col_Time[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')     
        with CB0_col_Time[1]:
            
            CB0_T_d =  st.text_input(r"時間の変化量(App%2d)"%(App_num),value="Symbol(\"\Delta t\")")
        try:
            Delta_t = sympify(CB0_T_d)
        except:
            E_01 = 1
    if E_01==1 :
        ECB = st.checkbox(
                "予想される原因(App%2d-%2d)：エラーが出ています．"%(App_num,1)
                )
        if ECB : st.markdown(Error_Str)


    st.write("### **Step2:位置の変化量**")

    Cal_V_select_str_dr="▷ 位置の変化量の値を，変化の前後から計算するか，直接与えるか選択してください."
    Radio_cal_dr=st.radio(
                                Cal_V_select_str_dr,
                                ('１）変化の前後', '２）直接'),
                                key="App%02d-2"+str(App_num)
                                )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    Method_Cal_dr={'１）変化の前後':0,'２）直接':1}
    if Method_Cal_dr[Radio_cal_dr]==0:
        st.write("##### ▷ 変化する前・後の位置の各成分を入力してください．")
        E_02=0
        Nnn0=[1]
        for i in range(Num_Dim):
            Nnn0.append(3)
        CB0_col_V= st.columns(Nnn0)
        CB0_r_i=[]
        CB0_r_f=[]
        CB0_str_r_i=[]
        CB0_str_r_f=[]
        CB0_str_r_i_ini={0:"x_i",1:"y_i",2:"z_i"}
        CB0_str_r_i_final={0:"x_f",1:"y_f",2:"z_f"}
        with CB0_col_V[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')  
        for i in range(Num_Dim):
            with CB0_col_V[i+1]:
                CB0_str_r_i.append( "変化前の位置の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                CB0_r_i.append(st.text_input(CB0_str_r_i[i],value=CB0_str_r_i_ini[i]))
                CB0_str_r_f.append( "変化後の位置の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                CB0_r_f.append(st.text_input(CB0_str_r_f[i],value=CB0_str_r_i_final[i]))
        try:
            Delta_r = []
            for i in range(len(CB0_r_i)):
                Delta_r.append(
                     sympify( CB0_r_f[i]) - sympify(CB0_r_i[i]) 
                 )
        except:
            E_02 = 1

    else:
        st.write("##### ▷ 位置の変化量の各成分を入力してください．")
        E_02=0
        Delta_r=[]
        CB0_str_r_d=[]
        Nnn0=[1]
        for i in range(Num_Dim):
            Nnn0.append(3)
        CB0_col_V= st.columns(Nnn0)
        CB0_str_r_d_ini={0:"Symbol(\"\Delta x\")",1:"Symbol(\"\Delta y\")",2:"Symbol(\"\Delta z\")"}
        with CB0_col_V[0]:
            st.write('$\\quad$')
            st.write('$\\quad$入力')  
        for i in range(Num_Dim):
            with CB0_col_V[i+1]:
                CB0_str_r_d.append( "位置の変化量の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                try:
                    Delta_r.append(sympify(st.text_input(CB0_str_r_d[i],value=CB0_str_r_d_ini[i])))
                except:
                    E_02 = 1
    
    if E_02==1 :
            ECB = st.checkbox("詳細表示(App%2d-%2d):エラーが出ています．"%(App_num,2))
            if ECB : st.markdown(Error_Str)
    
    st.write("### **Step3:平均速度が出力されます．**")
    try:
        CB0_V_Average=PHYS_Functions01.Cal_Q_Average_ver01(Delta_t,Delta_r) 
    except:
        ECB = st.checkbox("詳細表示(App%2d-%2d:エラーが出ています．)"%(App_num,3))
        if ECB : st.markdown(Error_Str)
    else : 
        Result_V_Ave1 = "\\displaystyle \\overrightarrow{v}_{\scriptscriptstyle{\\rm Ave.}} = "
        Result_V_Ave2 = PHYS_Functions01.List_to_vec01(CB0_V_Average)
        st.latex(Result_V_Ave1+Result_V_Ave2)