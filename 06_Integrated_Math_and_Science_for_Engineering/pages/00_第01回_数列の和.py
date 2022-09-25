import streamlit as st
import sympy as sym
from sympy import *
from sympy.simplify.sqrtdenest import sqrtdenest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import patches

Lec01_contents_list=["基礎例題","標準例題","応用例題","数列(基礎)","総和記号(基礎)","数列の極限(基礎)"]
Lec01_contents_tab =[]
Lec01_contents_tab = st.tabs(Lec01_contents_list)

contents_num=0
####  基礎例題  ####
with Lec01_contents_tab[0]:
    contents_num += 1
    st.markdown("### %s. %s"%(contents_num,Lec01_contents_list[0]))
    st.markdown(
    """
    ##### Q1.1-1 次の和を求めよ．
    """,unsafe_allow_html=True)

    Q_num_q11 = 0


    Q_num_q11 +=1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{14} k $
    """%(Q_num_q11)
    )

    Q_num_q11 +=1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{14} 1 $
    """%(Q_num_q11)
    )

    Q_num_q11 +=1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{n} 8k^3$
    """%(Q_num_q11)
    )

    Q_num_q11 +=1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{n} 6k^2$
    """%(Q_num_q11)
    )

    Q_num_q11 +=1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{n} 4^{k}$
    """%(Q_num_q11)
    )

####  標準例題  ####
with Lec01_contents_tab[1]:
    contents_num += 1
    st.markdown("### %s. %s"%(contents_num,Lec01_contents_list[1]))
    st.markdown(
    """
    ##### Q1.1-2 次の和を求めよ．
    """,unsafe_allow_html=True)

    Q_num_q11 = 0
    Q_num_q11 += 1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{14} \\big( 2k+1\\big)$
    """%(Q_num_q11)
    )

    Q_num_q11 += 1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{n} k\\Big( k+2\\Big)$
    """%(Q_num_q11)
    )
    
    Q_num_q11 += 1
    st.markdown(
    """
    (%s) $\\displaystyle \\ \\sum_{k=1}^{n} \\Big( 2^{k+1}\\Big)$
    """%(Q_num_q11)
    )


####  応用例題  ####
with Lec01_contents_tab[2]:
    contents_num += 1
    st.markdown("### %s. %s"%(contents_num,Lec01_contents_list[2]))
    st.markdown(
    """
    ##### Q1.1-3 次の和を求めよ．
    """,unsafe_allow_html=True)

    st.markdown(
    """
    (1) $\\displaystyle \\ \\sum_{k=4}^{14} \\big( 2k+1\\big)$
    """
    )
    st.markdown(
    """
    (2) $\\displaystyle \\ \\sum_{k=1}^{n} \\Big( 3k^3+3k^2+k\\Big)$
    """
    )
    st.markdown(
    """
    (3) $\\displaystyle \\ \\sum_{k=1}^{n} \\Big( 2^{2k+3}\\Big)$
    """
    )
####  数列  ####
with Lec01_contents_tab[3]:
    contents_num += 1
    st.markdown("### %s. 「%s」について"%(contents_num,Lec01_contents_list[3]))
    """
        ##### 数列とは
        数列とは，規則に従って並べられた数の列のこと．
        \\
        $\phantom{a}$
    """
    """
        ##### 基本的な用語
        - 項数：項の数のこと
        - 初項：第１項のこと
        - 一般項：第$~n~$項を与える式のこと（数列の規則を表す式）
        - 末項：数列の最後の項のこと
        $\phantom{a}$
    """
    """
        ##### 添字付きの記号
        記号による第$~k~$項の値の抽象的な表現  
        $$
            a_{k}
        $$
        $\phantom{a}$
    """
    with st.expander("ワンポイント：下付き添字付きの記号について（補足）"):
        try :
            st.image("./30_Streamlit_Figs/30_Streamlit_Figs.001.tiff")
        except :
            st.image("06_Integrated_Math_and_Science_for_Engineering/30_Streamlit_Figs/30_Streamlit_Figs.001.tiff")
            
    """
        ##### 数列の表し方
        - 抽象的に表す場合：$~\\{a_n\\}~$
        - 第$~N~$項（末項）を強調する場合：$~a_1,\ a_2,\ a_3,\ \\cdots ,\ a_N~$
        - 第$~n~$項（任意の項）を強調する場合：$a_1,\ a_2,\ a_3,\ \\cdots ,\ a_n,\ \\cdots ,\ a_N$
    """
    with st.expander("ワンポイント：数列の例"):
        """
        一般項が表す項を$~n~$とした場合  
        - **例１）$~1,\ 2,\ 3,\ \\cdots,\ 50~$**
        $\\phantom{\\quad\ }$
        初項：$1$，末項：$50$，一般項：$~n~$，項数：$50$
        """
        """
        - **例２）$~3,\ 5,\ 7,\ \\cdots,\ 29~$**
        $\\phantom{\\quad\ }$
        初項：$3$，末項：$29$，一般項：$~2n+1~$，項数$14$
        """
        """
        - **例３）$~1,\ -1,\ 1,\ -1,\ \\cdots,\ 1~$**
        $\\phantom{\\quad\ }$
        初項：$1$，末項：$1$，一般項：$~(-1)^{n-1}~$ or $~(-1)^{n+1}~$，項数：不明（情報不足）
        """
    # st.markdown("### %s. 数列を作ってみる"%(contents_num))

####  総和記号  ####
with Lec01_contents_tab[4]:
    contents_num += 1
    st.markdown("### %s. 「%s」について"%(contents_num,Lec01_contents_list[4]))
    """
        ##### 総和記号$~\Sigma~$の定義
        数列$~\{a_n\}~$の項数を$~N~$とするとき，初項$~a_1~$から末項$~a_N~$までの総和
        $$
            a_1 + a_2 + a_3 + \\cdots + a_N  
        $$
        を
        $$
            \\sum_{i=1}^{N} a_i
        $$
        と表す．つまり
        $$
            \\sum_{i=1}^{N} a_i = a_1 + a_2 + a_3 + \\cdots + a_N
        $$
        である．
        \\
        $\phantom{a}$
    """
    """
        ##### 総和記号$~\Sigma~$を用いた総和の表現方法の例
        数列$~\{a_n\}~$の項数を$~N~$とする．
        - 基本：初項（第$~1~$項）から末項（第$~N~$）項までの総和
            $$
                \\sum_{i=\color{red}1}^{\color{red}N} a_i
                =
                a_1 + a_2 + a_3 + \\cdots + a_N 
            $$
    """
    """
        - 応用：第$~3~$項から第$~8~$項までの総和
            $$
                \\sum_{i=\color{red}3}^{\color{red}8} a_i 
                = 
                a_3 +a_4 + a_5 + a_6 + a_7 + a_8
            $$
    """
    """
        - 応用：$~N=10~$とし，偶数項の総和を求める場合  
            $~i~$番目の偶数は$~2i~$と書くことができるので，求める総和は
            $$
                \\sum_{i=\color{red}1}^{\color{red}5} a_{\\scriptstyle \color{blue}2i} 
                =
                a_{(2*1)} + a_{(2*2)}  + a_{(2*3)}  + a_{(2*4)}  + a_{(2*5)}
                = 
                a_2 +a_4 + a_6 + a_8 + a_{10}
            $$
            と表すことができる．
    """
    with st.expander("ワンポイント：もう少し詳しく"):
        try :
            st.image("./30_Streamlit_Figs/30_Streamlit_Figs.002.tiff")
        except :
            st.image("06_Integrated_Math_and_Science_for_Engineering/30_Streamlit_Figs/30_Streamlit_Figs.002.tiff")

    with st.expander("ワンポイント：総和記号の読み方"):
        """
            - 記　号：$
                       \displaystyle \\sum_{i=\\square}^{\\triangle} a_{i} 
                       = a_{\\square} + a_{\\square+1} + a_{\\square+2} + \\cdots + a_{\\triangle} 
                     $
            - 解釈１：数列$~\{a_n\}~$があります．その中の第$~\\square~$項から第$~\\triangle~$項まで全て足しなさい．
            - 解釈２：$~i~$を$~\\square~$から$~\\triangle~$項まで１ずつ増やして得られる全ての項（数）を，全て足しなさい．
        """
    
    #### 総和の公式
    """
        ##### 総和に関する公式
        $~N~$を数列$~\{a_n\}~$の項数とする．
        - 初項$~a_1~$から末項$~a_N~$までの総和は
        $$
            a_1 + a_2 + a_3 + \\cdots + a_N  
        $$
        $$
            \\sum_{i=1}^{N} a_i
        $$
        と表す．つまり
        $$
            \\sum_{i=1}^{N} a_i = a_1 + a_2 + a_3 + \\cdots + a_N
        $$
        である．
        \\
        $\phantom{a}$
    """
####  数列の極限  ####
with Lec01_contents_tab[5]:
    contents_num += 1
    st.markdown("### %s. 「%s」について"%(contents_num,Lec01_contents_list[5]))   
    st.markdown("""
        ##### 数列の極限値の定義（簡易版）
        項数が無限個の数列$~\{a_n\}~$（無限数列）を考える．項の番号$~n~$が限りなく大きくなったとき，$~a_n~$がある数$~\\alpha~$に
        限りなく近づくとき，数列$~\{a_n\}~$は$~\\alpha~$に収束すると良い，$~\\alpha~$を数列$~\{a_n\}~$の極限値という．
        ，$~\\alpha~$が数列$~\{a_n\}~$の極限値であるということは，記号で
        $$
            \\lim_{n \\to \\infty} a_{n} = \\alpha
        $$
        と表す．\\
        ※ 数学的に厳密な数列の極限値の定義\\
        （参考：東京大学大学院数理科学研究科　会田茂樹　講義ノートより）
         [[クリック]](https://www.ms.u-tokyo.ac.jp/~aida/lecture/20/4-22.pdf)
        \\
        $\\phantom{a}$
    """,unsafe_allow_html=True)
    """
        ##### 数列の極限の例  
    """
    st.error("作成中")