import streamlit as st
from sympy import *
import numpy as np
from fractions import Fraction
from sympy.codegen.cfunctions import log10
import lib_to_cal_2 

def converttotex(Str00):
    Str00=str(Str00).replace("(","{")
    Str00=str(Str00).replace(")","}")
    Str00=str(Str00).replace("*","\\cdot ")
    return Str00

def Sec01_Exercise01_02(Cal_Ave_Error_Str,Cal_Acceleration_App_num):
    rho = symbols(r"\rho")
    #基本情報の設定
    st.subheader("基本情報の変更")
    st.info("\
            電子密度$n$，導線の断面積$A$，導線を流れる電流$I$を自由に変更できます．\
            ただし問題文に示された単位に合わせて，入力してください．\
            変更された内容に従った問題文，解答，解説が表示されます．\
            ")
    col1, col2, col3,col4= st.columns(4)
    with col1:
        tmp_E = st.radio("▷電子の電荷",("文字を含む","数値のみ"))
        Charge=st.text_input('電荷を入力')
        if tmp_E == "数値のみ" and not Charge:
            if not Charge:
                Charge = "1.6 * 10^(-19)"
        else :
            if not Charge:
                Charge = sympify("e")

    with col2:
        tmp_ed = st.radio("▷電子の密度",("文字を含む","数値のみ"))
        PRAM01=st.text_input('電子密度を入力')
        if tmp_ed == "数値のみ":
            if not PRAM01:
                PRAM01="1.0*10^(29)"
        else:
            if not PRAM01:
                PRAM01 = Symbol("n")

    with col3:
        tmp_ed = st.radio("▷断面積",("文字を含む","数値のみ"))
        PRAM02=st.text_input('断面積を入力')
        if tmp_ed == "数値のみ":
            if not PRAM02:
                PRAM02 ="2.0*10^(-6)"
        else:
            if not PRAM02:
                PRAM02 = Symbol("A")

    with col4:
        tmp_ed = st.radio("▷電流",("文字を含む","数値のみ"))
        PRAM03=st.text_input('電流を入力')
        if tmp_ed == "数値のみ":
            if not PRAM03:
                PRAM03 = "1.0"
        else:
            if not PRAM03:
                PRAM03 = Symbol("I")
            # else :
            #     st.write(sympify(PRAM03),sympify(PRAM03).atoms(Number,Symbol))
            #     PRAM03 = Symbol(list(sympify(PRAM03).atoms(Symbol)) )
    #問題文
    st.subheader("問１：問題文")
    Q_STR0='$1\\rm\ m^3$ に'
    Q_STR0+=" $" + latex(converttotex(PRAM01)) + "$ 個 の自由電子が存在するような金属で，"
    Q_STR0+="断面積が $" + latex(converttotex(PRAM02)) +"{\ \\rm [m^2]}$ の導線を作り，"
    Q_STR0+="$" + latex(converttotex(PRAM03)) + "{\ \\rm [A]}$ の電流を流すと，"
    Q_STR0+="自由電子の平均速度 $v \\rm\ [m/s]$ はいくらになるか．"
    Q_STR0+="ただし，電子の電荷（素電荷または電気素量）を $e=1.6\\times 10^{-19}\\rm \ [C]$ とする．"
    st.write(Q_STR0)
    #解答
    st.subheader("解答")
    tmp_Ans01=st.checkbox("表示させる",key=1)
    v = sympify(PRAM03)/(sympify(PRAM01)*sympify(PRAM02))
    if tmp_Ans01:
        st.latex(r"v=%s \ \rm [m/s]"% latex(v/sympify(Charge)))
        st.write("注意：表示された計算結果は，有効数字が考慮されていない")
    #解説
    st.subheader("解説")
    tmp_Ans02=st.checkbox("表示させる",key=2)
    if tmp_Ans02:
        Q01_Ans_str01 ="- 導体中の全電子が右向きに速さ $v \\rm \ [m/s]$ で運動するの時，"
        Q01_Ans_str01+=" $1 \\rm \ s$ あたりに電子が移動する距離は"
        Q01_Ans_str01+=" $v \\times 1 = v \\rm \ [m]$ である．"
        st.markdown(Q01_Ans_str01)
        Q01_Ans_str02 ="- $1 \\rm\ s$ の間に，面積 $" + latex(converttotex(PRAM02)) + "\\rm\ [m^2]$"
        Q01_Ans_str02+="の断面を通過する電子は，"
        Q01_Ans_str02+="断面から左側 $v \\times " + latex(converttotex(PRAM02)) + "\\rm\ [m^3]$"
        Q01_Ans_str02+=" の領域内の電子である．"
        st.markdown(Q01_Ans_str02)        
        Q01_Ans_str03 ="- この領域内に存在する電子の数は，電子の密度 $" + latex(converttotex(PRAM01)) + "\\rm\ [\\text{個}/m^3]$"
        Q01_Ans_str03+=" を用いて，$" + latex(converttotex(PRAM01))
        Q01_Ans_str03+="\\cdot v \\cdot " + latex(converttotex(PRAM02))
        Q01_Ans_str03+="\ \\text{個}$ である．"
        st.markdown(Q01_Ans_str03)    
        Q01_Ans_str04 ="- 電流 $" + latex(converttotex(PRAM03)) +" \\rm [A]$ は，"
        Q01_Ans_str04+=" 面積 $" + latex(converttotex(PRAM02))
        Q01_Ans_str04+=" \\rm \ [m^2]$ の断面を $1 \\rm \ s$ あたりに通過する電荷量で定義される．"
        Q01_Ans_str04+=" よって，"
        Q01_Ans_str04+=" $" + latex(converttotex(PRAM03)) + " = " 
        Q01_Ans_str04+= latex(converttotex(Charge)) + " \\cdot " + latex(converttotex(PRAM01))
        Q01_Ans_str04+="\\cdot v \\cdot " + latex(converttotex(PRAM02))
        Q01_Ans_str04+="$ が成り立つ．"
        st.markdown(Q01_Ans_str04)

    #問題文
    st.subheader("-------")
    st.subheader("問２：問題文")
    Q_STR1="電流密度を $\\displaystyle J = \\frac{I}{S} \ \\rm [A/m^2]$ とするとき，問１における電流密度をもとめなさい．"
    st.write(Q_STR1)
    #解答
    st.subheader("解答")
    tmp_Ans01=st.checkbox("表示させる",key=3)
    J = sympify(PRAM03)/sympify(PRAM02)
    J_num = list(J.atoms(Number))[0]
    if tmp_Ans01:
        if J_num != -1 or J == 0 :
            index_val = int(log10(J_num))
            J=J/J_num
            J_num = J_num/(10**index_val)
            if index_val == 0:
                st.latex(r"J = %s \ \rm [A/m^2]"%(latex(J_num*J)))
            else :
                st.latex(r"J = %s \times 10^{%s}  \ \rm [A/m^2]"%(latex(J_num*J), index_val))                
        else :
            st.latex(r"J = %s \ \rm [A/m^2]"%(latex(J)))          
        # if isinstance(J,Float) :
        #    index_val = int(log10(J))
        #    J = J*10**((-1)*index_val) 
        #    st.latex(r"J = %s \times 10^{%s} \ \rm [A/m^2]"%(latex(J), index_val))
        #    st.write("注意：表示された計算結果は，有効数字が考慮されていない")
        # else:
        #    st.latex(r"J = %s \ \rm [A/m^2]"%(latex(J)))
    #解説
   