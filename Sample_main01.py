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
App_num=0
CB=[]
CB.append(st.sidebar.checkbox('平均速度'))
CB.append(st.sidebar.checkbox('平均加速度'))
if sum(CB) == 0:
    st.write("コンテンツを選んでください．")
############# 終了
#
############# 平均速度の計算コンテンツ：開始
if CB[0]:
    import PHYS_Functions01
    import PHYS_V_Ave
    App_num=App_num+1
    st.write(r"## **○ 平均速度の計算アプリ(%s)**"%(App_num))
    PHYS_V_Ave.Cal_Velocity_Ave(Num_Dim,Error_Str,App_num)
    st.write(r"### --------------------------------------------------------------------アプリ(%s) End"%(App_num))
############# コンテンツ終了
#
############# 平均加速度の計算コンテンツ：開始
if CB[1]:
    App_num=App_num+1
    st.write(r"## **○ 平均加速度の計算アプリ(%s)**"%(App_num))
    import PHYS_Functions01   
    import PHYS_A_Ave
    PHYS_A_Ave.Cal_Acceleration_Ave(Num_Dim,Error_Str,App_num)
    st.write(r"### --------------------------------------------------------------------アプリ(%s) End"%(App_num))
############# コンテンツ終了