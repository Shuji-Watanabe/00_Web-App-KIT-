import streamlit as st
import sympy as sym
from sympy import *
from sympy.simplify.sqrtdenest import sqrtdenest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import patches
import plotly.graph_objs as go
import functions as myfunc
import re
import random as rd
from pages.basicknowledges import Lec03_contents
from pages.problems import Lec04_problems


Lec07_contents_list=["小テスト１における必要最低限の知識","リーマン和とリーマン積分","置換積分","部分積分"]
Lec07_contents_tab =[]
Lec07_contents_tab = st.tabs(Lec07_contents_list)
contents_num =0
lec_num =7
st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/NHbiNWkjHgd28K5C9)""")
####  Tab１  ####
# contents_num += 1
section_num = 1
q_num = 0

with Lec07_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec07_contents_list[contents_num])) 
    ## 積分公式について
    col02 = st.columns(2)
    with col02[0]:  
        with st.container():
            """
            ##### 積分基本公式(Lv.1)
            $$
            \\begin{align*}
                &\\blacksquare \\quad
                    \\int
                    \,
                    x^{\,\\alpha}
                    \,
                    dx
                    =
                    \\left\{
                        \\begin{align*}
                            &\\alpha \\ne -1 \\ \\text{のとき}
                            \\\\
                            &\\quad 
                                \\frac{1}{\\alpha+1} x^{\\alpha+1}+C 
                        \\\\
                        &\\phantom{a}
                        \\\\
                            &\\alpha = -1 \\ \\text{のとき}
                            \\\\
                            &\\quad \\ln|x| +C
                        \\end{align*}
                    \\right.

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, e^x\, dx
                    =
                    e^x + C

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, a^x\, dx
                    =
                    \\frac{1}{\\ln a }\cdot a^x + C
                    \\quad \\left( a > 0  \\right)

                \\\\
                &\\phantom{a}
                \\\\
                &\\blacksquare \\quad
                    \\int\, \\sin x \, dx
                    =
                    -\\cos x +C

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, \\cos x \, dx
                    =
                    \\sin x +C     

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, \\sec^2 x \, dx
                    =
                    \\tan x +C           
            \\end{align*}
            $$
            """
    with col02[1]:  
        with st.container():
            """
            ##### 積分基本公式(Lv.2)
            $$
            \\begin{align*}
                &\\blacksquare \\quad
                    \\int\, 
                        \\frac{1}{\\sqrt{1-x^2}} 
                    \, dx
                    =
                    \\sin^{-1} x +C

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, 
                        \\frac{1}{\\sqrt{1+x^2}} 
                    \, dx
                    =
                    \\ln\\left| x + \\sqrt{1+x^2} \\right| + C

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, 
                        \\frac{1}{1+x^2}  
                    \, dx
                    =
                    \\tan^{-1} x +C     

            \\end{align*}
            $$
            """
        " " 
        with st.container():
            """
            ##### 積分基本公式(Lv.3)
            $$
            \\begin{align*}
                &\\blacksquare \\quad
                    \\int\, 
                        \\csc^2 x  
                    \, dx
                    =
                    \\cot x +C

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, 
                        \\sec x \\tan x 
                    \, dx
                    =
                    \\sec x + C

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, 
                        \\csc x \\cot x 
                    \, dx
                    =
                    -\\csc x +C     

                  \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\int\, 
                        \\frac{1}{1-x^2}
                    \, dx
                    =
                    \\frac{1}{2}\\ln \\left| \\frac{1+x}{1-x} \\right| x + C                            
            \\end{align*}
            $$
            """

    ## 指数・対数について
    " " ;  " "  ; " "   
    col_01 = st.columns(2)
    #-- 指数について
    with col_01[0]:
        with st.container():
            """
            ##### 指数についての基礎知識(Lv. 1)
            以下$~a,\\ b~$は$~a,\\ b > 0~$である実数とする．
            $$
            \\begin{align*}  
                &\\blacksquare \\quad
                    a^0 = 1

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    a^{\\ln b} = b 

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\frac{1}{a}
                    =
                    a^{-1} 
                
                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    a^x \cdot a^y = a^{x + y} 

            \\end{align*}
            $$
            """
    #-- 対数について
    with col_01[1]:
        with st.container():
            """
            ##### 対数についての基礎知識(Lv. 1)
            以下$~a,\\ b~$は$~a,\\ b > 0~$である実数とする．
            $$
            \\begin{align*}  
                &\\blacksquare \\quad
                    \\ln 1 = 0

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\ln e = 1

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\ln a^x = x \\ln a

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\ln \\big( a \\cdot b \\big)
                    =
                    \\ln a + \\ln b

                \\\\
                &\\phantom{space}
                \\\\
                &\\blacksquare \\quad
                    \\log_a b = \\frac{\\ln a}{\\ln b} 
                    \\quad \\text{底の変換公式($ a\\to e $)}
            \\end{align*}
            $$
            """
            with st.expander("対数の底の変換公式が有効な場面"):
                st.error("作成中")

    " " ;  " "  ; " "   
    ## 三角関数について
    with st.container():
        """
        ##### 三角関数についての基礎知識(Lv. 1)
        $$
        \\begin{align*}  
            &\\blacksquare \\quad
                \\cos^2 x + \\sin^2 x = 1

            \\\\
            &\\phantom{space}
            \\\\
            &\\blacksquare \\quad
                1 + \\tan^2 x = \\frac{1}{\\cos^2 x}
                \\quad
                {\\rm or}
                \\quad
                1 + \\tan^2 x = \\sec^2 x
        \\end{align*}
        $$
        """
    
    " " ;  " "  ; " "   
    ## 合成関数の導関数について
    with st.container():
        """
        ##### 合成関数の導関数（微分）
        関数$~f(x)~$と$~g(x)~$の合成関数$~f\circ g(x)=f\\Big( g(x) \\Big)~$を$~x~$について
        その導関数$~\\frac{d}{dx}\\left\{ f \\circ g (x)\\right\}~$は，
        $u = g(x)$として
        $$
            \\frac{d}{dx}\\left\{ f \\circ g (x)\\right\}
            =
            \\frac{df}{du}
            \\cdot 
            \\frac{du}{dx}
        $$
        となる．
        """
        with st.expander("合成関数かそうでないかの見分け方(基本)"):
            """
            以下の関数を初等関数と呼び，初等関数の$~x~$の部分が，単項式または多項式，別な初等関数となっているものは
            合成関数であると思って良い．
            \n\n
            """
            " "

            """
            ###### 代表的な初等関数
            - べき関数$~x^\\alpha~$\\
                例：
                $~x^2~$
                ，$~x^3~$
                ，$~\\frac{1}{x} = x^{-1}~$
                ，$~\\sqrt{x} = x^{\\frac{1}{2}}~$
                ，$~\\sqrt[3]{x^2} = x^{\\frac{2}{3}}~$\\
                $\phantom{a}$
            - 指数関数$~e^x,\\ a^x~$（ただし，$~a>0~$の実数とする）\\
                例：
                $~e^x~$
                ，$~3^x~$
                ，$~8^x~$
                ，$~\\left(\\frac{1}{2}\\right)^x~$\\
                $\phantom{a}$
            - 三角関数\\
                $\\sin x$
                ，$\\cos x$
                ，$\\tan x$\\
                $\\csc x = \\frac{1}{\\sin x}$
                ，$\\sec x = \\frac{1}{\\cos x}$
                ，$\\cot x = \\frac{1}{\\tan x}$
                \\
                $\phantom{a}$
            - 逆三角関数\\
                $\\sin^{-1} x$
                ，$\\cos^{-1} x$
                ，$\\tan^{-1} x$\\
                $\\csc^{-1} x $
                ，$\\sec^{-1} x$
                ，$\\cot^{-1} x$
                \\
                $\phantom{a}$
            """

            """
            ###### 合成関数の例
            - $\\big( 2x + 1 \\big)^4$は$~f(x) = x ^4~$と$~g(x) = 2x +1~$の合成関数
                \\
                $\phantom{a}$
            - $2^{3x - 2}~$は$~f(x) = 2 ^x~$と$~g(x) = 3x -2~$の合成関数
                \\
                $\phantom{a}$
            - $\\tan\\big(3x + \\frac{\\pi}{6}\\big)~$は$~f(x) = \\tan x~$と$~g(x) = 3x + \\frac{\\pi}{6}~$の合成関数
            """




contents_num +=1
with Lec07_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec07_contents_list[contents_num])) 
    """
    リーマン積分（定積分，または「リーマン和を用いて面積を求める問題」）を求めるとき，毎回行われる作業，計算の流れを
    以下に示す．
    """

    " " ;  " "  ; " "  
    st.markdown("""##### 問題文""")
    """
    $~y=f(x)~$と$~x~$軸，$~x=a~$，$~x=b~$で囲まれた領域の面積を， **リーマン和（右リーマン和）** を用いてもとめなさい．
    """

    " " ;  " "  ; " "  
    st.markdown("""##### Step0：問題文を可視化する""")
    """
    $~y=f(x)~$と$~x=a~$，$~x=b~$のグラフを描き，求めたい領域を図示する．
    """
    
    " " ;  " "  ; " "  
    st.markdown("""##### Step1：区間の分割と区間の幅を求める""")
    """
    区間$~\\Big[a ,\\ b\\Big]~$を$~n~$等分することによって
    $~n~$個の小区間が作られる．

    区間$~\\Big[a ,\\ b\\Big]~$を$~n~$等分しているので，
    各小区間の幅は等しく，その幅$~\Delta x~$は，
    $$
        \\Delta x = \\frac{b-a}{n} 
    $$
    となる．
    """
    with st.expander("この問題における区間とは"):
        """
            $~x=a~$から$~x=b~$の間の範囲のこと．
            記号を用いて
            $$
                a \le x \le b 
                \\quad 
                \\text{または}
                \\quad 
                \\Big[a ,\\ b\\Big]
            $$
            と表される．
        """
    with st.expander("分割と小区間についてイメージが湧かない人へ"):
        """
        具体例として区間$~\\Big[-2,\\ 4 \\Big]~$を$~5~$等分した場合を考え，
        その時作られる小区間の数と各小区間の幅を求める方法を考察してみる．

        - **小区間の数** \\
            区間$~\\Big[-2,\\ 4 \\Big]~$を$~5~$等分することで
            $~x=-2~$から$~x=4~$の間に$~5~$つの区間ができる．
        - **小区間の幅** \\
            今 **"等分"** していることから各小区間の幅はどれも同じ値になり，
            その値は$\\frac{6}{5}$である．
        - **小区間の幅$~\\frac{6}{5}$がどのように得られたか** \\
            $~x=-2~$から$~x=4~$までの幅（長さ）は$~2+4=6~$となる．
            そして，それを$~5~$等分するので$~\\frac{6}{5}$となった．
        - **小区間の幅をもとめる方法の一般化** \\
            小区間の幅$~\\frac{6}{5}$を長さをもとに計算したが，
            区間について問題文で与えられる情報は
            $~x=-2~$や$~x=4~$のように，座標で与えられる．
            さらに，与えられる座標が文字の場合もある．
            
            そこで，区間の幅を **$~x~$座標** から求める方法を考える必要があるが，
            その方法は難しいことではなく
                **大きい$~x~$座標から小さい$~x~$座標を引く** 
            ことで得られる．例えば
            $$
                4-(-2) = 4+2 = 6
            $$
            である．
            このことから区間$~\\Big[-2,\\ 4 \\Big]~$を$~5~$等分した際の
            各小区間の幅$~\\Delta x~$は
            $$
                \\Delta x = \\frac{4-(-2)}{5} = \\frac{6}{5}
            $$
            となる．
        """

    " " ;  " "  ; " "  
    st.markdown("""##### Step2：$~k~$番目の小区間における長方形の面積をもとめる""")
    """
    $~k~$番目の小区間$\\Big[x_{k-1},\\ x_{k}\\Big]$に，
    - $~x~$軸上の点$\\big( x_{k-1} ,\\ 0 \\big)$ と点$\\big( x_{k} ,\\ 0 \\big)$ を結ぶ線
    - 点$\\big( x_{k} ,\\ 0 \\big)$と点$\\big( x_{k} ,\\ f(x_k) \\big)$を結ぶ線
    を辺とする長方形を定める．
    ここで点$\\big( x_{k-1} ,\\ 0 \\big)$ と点$\\big( x_{k} ,\\ 0 \\big)$ を結ぶ線の長さ$\\Delta x$は
    $$
        \\Delta x = x_{k} -  x_{k-1} = \\frac{b-a}{n}
    $$
    であるから，この長方形の面積$~s_k~$は
    $$
        s_k = f(x_k)\\cdot \\Delta x
    $$
    と表すことができる．
    """
    



