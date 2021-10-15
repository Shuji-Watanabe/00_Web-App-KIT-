import streamlit as st
from sympy import *

############# 典型的なエラー：開始
Error_Str = "　$\qquad$Check.1　全ての変数に，値または式が入力されていますか？\n\n "
Error_Str = Error_Str + "$\qquad$Check.2　半角で入力されていますか？\n\n "
Error_Str = Error_Str + "$\qquad$Check.3　式の書き方に問題ありませんか？ \n\n"
Error_Str = Error_Str + "$\qquad$※　\"$\Delta x$\"　は　Symbol(\"\Delta x\")　と書く．"
############# 終了
############# 空間次元の指定：開始
st.sidebar.write(r"### ＜空間次元の指定＞")
radio_Dim=st.sidebar.radio(
        '運動の解析を行う次元をしてください',
        ('１次元', '２次元', '３次元'))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
Dim={'１次元':1,'２次元':2,'３次元':3}
Dim_Num=Dim[radio_Dim]
############# 終了
############# コンテンツの指定：開始
st.sidebar.write(r"### ＜自動計算コンテンツの指定＞")
App_num=0
CB=[]
CB.append(st.sidebar.checkbox('平均速度'))
CB.append(st.sidebar.checkbox('平均加速度'))
CB.append(st.sidebar.checkbox('位置，速度，加速度'))
if sum(CB) == 0:
    st.write("コンテンツを選んでください．")
############# 終了
#
############# 平均速度の計算コンテンツ：開始
if CB[0]:
    import PHYS_V_Ave_ver2
    App_num=App_num+1
    st.write(r"# **平均速度(%s)**"%(App_num))
    PHYS_V_Ave_ver2.Cal_Velocity_Ave(Dim_Num,Error_Str,App_num)
    st.write(r" ----------------------------------------アプリ(%s) End------------------------------------------"%(App_num))
############# コンテンツ終了
#
############# 平均加速度の計算コンテンツ：開始
if CB[1]:
    App_num=App_num+1
    st.write(r"# **平均加速度(%s)**"%(App_num))
    import PHYS_A_Ave_ver2
    PHYS_A_Ave_ver2.Cal_Acceleration_Ave(Dim_Num,Error_Str,App_num)
    st.write(r" ------------------------------------------アプリ(%s) End------------------------------------------"%(App_num))
############# コンテンツ終了
#
############# 位置，速度，加速度の計算コンテンツ：開始
# if CB[2]:
#     App_num=App_num+1
#     st.write(r"# **位置，速度，加速度の関係(%s)**"%(App_num))
#     import PHYS_A_Ave_ver2
#     PHYS_A_Ave_ver2.Cal_Acceleration_Ave(Dim_Num,Error_Str,App_num)
#     st.write(r"##### -----------------------------------アプリ(%s) End-----------------------------------"%(App_num))
############# コンテンツ終了