import streamlit as st
from sympy import *

def converttotex(Str00):
    
    Str00=str(Str00).replace("(","{")
    Str00=str(Str00).replace(")","}")
    Str00=str(Str00).replace("*"," ")
    return Str00

def centering(Str00):
    centerd_text  ="<div style= \"text-align: center;\"> "
    centerd_text +=str(Str00)
    centerd_text +=" </div>"
    return centerd_text



text01 ="\
単位体積（$1\ \\rm m^3$）あたりに約 $++param01++$ の自由電子が存在する金属でできた導線がある．この導線に\
 $++param02++$ の電流が流れるとき，自由電子の平均速度の大きさ $\\overline{v}\ \\rm [m/s]$ を求めなさい．\
 ただし，導線の断面積は $++param03++$ であり，自由電子の平均速度は断面に対して垂直であるものとする．また自由電子の電荷は\
 電気素量 $e = 1.6 \\times 10^{-10} \ \\rm C$ を用いる．\
"

tmp_CB01=st.sidebar.checkbox("状況設定の変更")
if tmp_CB01 :
    st.markdown("##### ▷ パラメータの変更",unsafe_allow_html=True)
    col01,col02,col03= st.columns(3)
    st.info("単位体積あたりの電子数，導線を流れる電流値，断面積を変更したときの平均速度を求めて見ましょう．\
    初期設定は，$n_0,\ I_0,\ S_0$ です．\
    入力欄には$12.5$や$1.3 * 10^{(4)}$のような数値が入力可能です．文字は2\*m，x_0\*10^(-3)のように文字の数値倍の範囲で入力可能です．")

    with col01:
        p_num = st.text_input("電子数","n_0")
    with col02:
        current = st.text_input("電流値","I_0")
    with col03:
        area = st.text_input("断面積","S_0")
else:
    p_num = "n_0"
    current = "I_0"
    area = "S_0"

PARAM00 = {"++param01++":p_num, "++param02++":current, "++param03++":area}
for i in PARAM00:
    tmp_00 = converttotex(PARAM00[i])
    text01=text01.replace(i,tmp_00)

st.markdown("##### ▷ 問題文")
st.markdown(text01)