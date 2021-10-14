import streamlit as st
from sympy import *
import PHYS_Functions01

def Cal_Acceleration_Ave(Cal_Ave_Num_Dim,Cal_Ave_Error_Str,Cal_Acceleration_App_num):
    Error_Str=Cal_Ave_Error_Str
    Num_Dim=Cal_Ave_Num_Dim
    App_num=Cal_Acceleration_App_num
    E_01=0
    st.write("### Step1:時間の変化量")

    Cal_A_select_str_dt="時間の変化量の値を，変化の前後から計算するか，直接与えるか選択してください.("+str(App_num)+")"
    Select_cal_dt=st.selectbox(
        Cal_A_select_str_dt,
        ('１）変化の前後', '２）直接'))
    Method_Cal_dt={'１）変化の前後':0,'２）直接':1}

    if Method_Cal_dt[Select_cal_dt]==0:
        st.write('#### 変化前・後の時刻を入力してください．')
        CB01_col_Time=st.columns([1,3,3])
        with CB01_col_Time[0]:
            st.write("入力：")        
        with CB01_col_Time[1]:
            CB01_T_i =  st.text_input(r"変化前の時刻(App%2d)"%(App_num))
        with CB01_col_Time[2]:
            CB01_T_f =  st.text_input(r"変化後の時刻(App%2d)"%(App_num))
        try:
            Delta_t = sympify(CB01_T_f) - sympify(CB01_T_i)
        except:
            E_01 = 1
    else :
        CB01_col_Time=st.columns([1,3])
        with CB01_col_Time[0]:
            st.write("入力：")    
        with CB01_col_Time[1]:
            
            CB01_T_d =  st.text_input(r"時間の変化量(App%2d)"%(App_num))
        try:
            Delta_t = sympify(CB01_T_d)
        except:
            E_01 = 1
    if E_01==1 :
        st.write("※ 時間の変化量の計算でエラーが出ています．")
        ECB = st.checkbox("詳細表示(App%2d-%2d)"%(App_num,1))
        if ECB : st.markdown(Error_Str)


    st.write("### Step2:速度の変化量")
    Cal_A_select_str_dv="速度の変化量の値を，変化の前後から計算するか，直接与えるか選択してください.("+str(App_num)+")"
    Select_cal_dv=st.selectbox(
        Cal_A_select_str_dv,
        ('１）変化の前後', '２）直接'))
    Method_Cal_dv={'１）変化の前後':0,'２）直接':1}
    if Method_Cal_dv[Select_cal_dv]==0:
        st.write("##### 変化する前・後の速度の各成分を入力してください．")
        E_02=0
        Nnn0=[1]
        for i in range(Num_Dim):
            Nnn0.append(3)
        CB01_col_V= st.columns(Nnn0)
        CB01_v_i=[]
        CB01_v_f=[]
        CB01_str_v_i=[]
        CB01_str_v_f=[]
        with CB01_col_V[0]:
            st.write("入力：")  
        for i in range(Num_Dim):
            with CB01_col_V[i+1]:
                CB01_str_v_i.append( "変化前の速度の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                CB01_v_i.append(st.text_input(CB01_str_v_i[i]))
                CB01_str_v_f.append( "変化後の速度の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                CB01_v_f.append(st.text_input(CB01_str_v_f[i]))
        try:
            Delta_r = []
            for i in range(len(CB01_v_i)):
                Delta_r.append(
                     sympify( CB01_v_f[i]) - sympify(CB01_v_i[i]) 
                 )
        except:
            E_02 = 1

    else:
        st.write("##### 速度の変化量の各成分を入力してください．")
        E_02=0
        Delta_r=[]
        CB01_str_v_d=[]
        Nnn0=[1]
        for i in range(Num_Dim):
            Nnn0.append(3)
        CB01_col_A= st.columns(Nnn0)
        with CB01_col_A[0]:
            st.write("入力：")  
        for i in range(Num_Dim):
            with CB01_col_A[i+1]:
                CB01_str_v_d.append( "速度の変化量の第"+str(int(i)+1)+"成分(App%2d)"%(App_num))
                try:
                    Delta_r.append(sympify(st.text_input(CB01_str_v_d[i])))
                except:
                    E_02 = 1
    
    if E_02==1 :
        st.write("※ 速度の変化量の計算でエラーが出ています．")
        ECB = st.checkbox("詳細表示(App%2d-%2d)"%(App_num,2))
        if ECB : st.markdown(Error_Str)

    st.write("### Step3:平均加速度が出力されます．")

    try:
        CB01_V_Average=PHYS_Functions01.Cal_Q_Average_ver01(Delta_t,Delta_r) 
    except:
        st.write("※ 平均加速度の計算でエラーが出ています．")
        ECB = st.checkbox("詳細表示(App%2d-%2d)"%(App_num,3))
        if ECB : st.markdown(Error_Str)
    else : 
        Result_V_Ave1 = "\\displaystyle \\overrightarrow{a}_{\\rm Ave.} = "
        Result_V_Ave2 = PHYS_Functions01.List_to_vec01(CB01_V_Average)
        st.latex(Result_V_Ave1+Result_V_Ave2)