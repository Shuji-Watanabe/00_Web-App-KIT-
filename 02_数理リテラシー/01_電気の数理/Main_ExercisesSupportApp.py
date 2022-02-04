import streamlit as st
import pandas as pd
from sympy import *

############# 典型的なエラー：開始
Error_Str = "　$\qquad$Check.1　全ての変数に，値または式が入力されていますか？\n\n "
Error_Str = Error_Str + "$\qquad$Check.2　半角で入力されていますか？\n\n "
Error_Str = Error_Str + "$\qquad$Check.3　式の書き方に問題ありませんか？ \n\n"
Error_Str = Error_Str + "$\qquad$※　\"$\Delta x$\"　は　Symbol(\"\Delta x\")　と書く．"
############# 終了
############# コンテンツの指定：開始
st.sidebar.write(r"＜電気の数理：演習サポートアプリ＞")
App_num=0
CB=[]
st.sidebar.write(r"#### 第１章")
CB.append(st.sidebar.checkbox('練習問題・問１，問２'))
CB.append(st.sidebar.checkbox('練習問題・問３'))
CB.append(st.sidebar.checkbox('練習問題・問４'))
CB.append(st.sidebar.checkbox('練習問題・問５'))
CB.append(st.sidebar.checkbox('練習問題・問６'))
CB.append(st.sidebar.checkbox('練習問題・問７'))
if sum(CB) == 0:
    st.write("コンテンツを選んでください．")
############# 終了
#
############# 問１，２の解説：開始
if CB[0]:
    import Sec01
    App_num=App_num+1
    begin01 = "<div style= \"text-align: left;\"> "
    begin01+= "-- 第１章練習問題 問１，２の演習サポート（アプリ %s）--"%(App_num)
    begin01+= " </div>"
    st.markdown(begin01,unsafe_allow_html=True)   
    Sec01.Sec01_Exercise01_02(Error_Str,App_num)
    end01 ="<div style= \"text-align: right;\"> "
    end01+=" --アプリ(%s) End--"%(App_num)
    end01+=" </div>"
    st.markdown(end01,unsafe_allow_html=True)
############# コンテンツ終了
