import streamlit as st
from sympy import *



############# 典型的なエラー：開始
Error_Str = "　　▷　全ての変数に，値または式が入力されていますか？\n\n "
Error_Str = Error_Str + "▷　半角で入力されていますか？\n\n "
Error_Str = Error_Str + "▷　式の書き方に問題ありませんか？ "
############# 終了
#
############# 空間次元の指定：開始
Select_Dim=st.sidebar.selectbox(
        '運動の解析を行う次元をしてください',
        ('１次元', '２次元', '３次元'))

Dim={'１次元':1,'２次元':2,'３次元':3}
Num_Dim=Dim[Select_Dim]
st.sidebar.write(r"### %s次元中の運動を解析します"%(Dim[Select_Dim]))
############# 終了
#
############# コンテンツの指定：開始
CB=[]
CB.append(st.sidebar.checkbox('平均速度'))
CB.append(st.sidebar.checkbox('平均加速度'))
if sum(CB) == 0:
    st.write("コンテンツを選んでください．")
############# 終了
#
############# 平均速度の計算コンテンツ：開始
if CB[0]:
    import PHYS01    
    st.write("### Step1:変化前・後の時刻か時間の変化量の値または式を入力してください．")
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
        CB0_V_Average=PHYS01.Add_1(Delta_t,CB0_V_i,CB0_V_f)    
    except:
        st.write("※ 平均速度の計算でエラーが出ています．")
        st.markdown(Error_Str)
    else : 
        Result_V_Ave = PHYS01.List_to_vec01(CB0_V_Average)
        st.latex(Result_V_Ave)
############# コンテンツ終了
#
############# 平均速度の計算コンテンツ：開始
if CB[1]:
    import PHYS01
    CB01_col= st.columns(Num_Dim)
    CB01_PRAM=[]
    str01=[]
    for i in range(Num_Dim):
        with CB01_col[i]:
            str01.append( "変化前の加速度：第"+str(i)+"成分")
            CB01_PRAM.append(st.text_input(str01[i]))
            #st.write(str01[i])
    try:
        XX=PHYS01.Add_1(CB01_PRAM)    
    except:
        st.write("必要な変数を入力してください．")
    else : 
        for i in range(len(XX)):
            st.write(r"変化前の速度：第%s成分=$%s$"%((i,XX[i])))
############# コンテンツ終了