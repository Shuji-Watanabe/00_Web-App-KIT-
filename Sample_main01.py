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
    import PHYS_Functions01   
    import PHYS_V_Ave
    PHYS_V_Ave.Cal_Ave(Num_Dim,Error_Str)
############# コンテンツ終了
#
############# 平均速度の計算コンテンツ：開始
if CB[1]:
    import PHYS_Functions01 
    CB01_col= st.columns(Num_Dim)
    CB01_PRAM=[]
    str01=[]
    for i in range(Num_Dim):
        with CB01_col[i]:
            str01.append( "変化前の加速度：第"+str(i)+"成分")
            CB01_PRAM.append(st.text_input(str01[i]))
            #st.write(str01[i])
    try:
        XX=PHYS_Functions01.Cal_V_Average_ver01(CB01_PRAM)    
    except:
        st.write("必要な変数を入力してください．")
    else : 
        for i in range(len(XX)):
            st.write(r"変化前の速度：第%s成分=$%s$"%((i,XX[i])))
############# コンテンツ終了