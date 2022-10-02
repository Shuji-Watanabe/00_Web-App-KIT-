import streamlit as st
import sympy as sym
from sympy import *
from sympy.simplify.sqrtdenest import sqrtdenest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import patches
import functions as myfunc


Lec01_contents_list=["基礎例題","標準例題","応用例題","数列(基礎)","総和記号(基礎)","数列の極限(基礎)"]
Lec01_contents_tab =[]
Lec01_contents_tab = st.tabs(Lec01_contents_list)

contents_num=0
####  基礎例題  ####
st.sidebar.markdown("**基礎例題の解答**")
with Lec01_contents_tab[0]:
    contents_num += 1
    st.markdown("### %s. %s"%(contents_num,Lec01_contents_list[0]))
    st.markdown("""##### [Lec.1-1]Q1 次の和を求めよ．""",unsafe_allow_html=True)
    Q_num_q11 = 0
 
 
    ##### q1
    Q_num_q11 +=1
    ans_q1_tmp_00=["k","k","1","14"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    if st.sidebar.checkbox("(1)の答え",key="q01_1_1"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
            ) 

    ##### q2    
    Q_num_q11 +=1
    ans_q1_tmp_00=["1","k","1","14"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    if st.sidebar.checkbox("(2)の答え",key="q01_1_2"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
        )  
        
    ##### q3    
    Q_num_q11 +=1
    ans_q1_tmp_00=["8*k^3","k","1","n"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    if st.sidebar.checkbox("(3)の答え",key="q01_1_3"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s = %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
        )  


    ##### q4
    Q_num_q11 +=1
    ans_q1_tmp_00=["6*k^2","k","1","n"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    if st.sidebar.checkbox("(4)の答え",key="q01_1_4"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s = %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
        )  



    ##### q5
    Q_num_q11 +=1
    ans_q1_tmp_00=["4^k","k","1","n"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    if st.sidebar.checkbox("(5)の答え",key="q01_1_5"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s = %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
        )  


    with st.expander("ヒント：総和の公式"):
        try :
            st.image("./30_Streamlit_Figs/30_Streamlit_Figs.003.tiff")
        except :
            st.image("06_Integrated_Math_and_Science_for_Engineering/30_Streamlit_Figs/30_Streamlit_Figs.003.tiff")

####  標準例題  ####
st.sidebar.markdown("**標準例題の解答**")
with Lec01_contents_tab[1]:
    contents_num += 1
    st.markdown("### %s. %s"%(contents_num,Lec01_contents_list[1]))
    st.markdown("""##### [Lec.1-2]Q1 次の和を求めよ．""",unsafe_allow_html=True)

    Q_num_q11 = 0
    Q_num_q11 += 1
    ##### q1
    ans_q1_tmp_00=["(2*k+1)","k","1","14"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    tmps[0]=myfunc.format_disp("(2*k+1)",2)
    if st.sidebar.checkbox("(1)の答え",key="q01_2_1"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
            ) 

    ##### q2
    Q_num_q11 += 1
    ans_q1_tmp_00=["k*(k+2)","k","1","n"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    tmps[0]=myfunc.format_disp("k*(k+2)",2)
    if st.sidebar.checkbox("(2)の答え",key="q01_2_2"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
            ) 

    ##### q3
    Q_num_q11 += 1
    ans_q1_tmp_00=["2^(k+1)","k","1","n"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    if st.sidebar.checkbox("(3)の答え",key="q01_2_3"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
            )
        

    with st.expander("ポイント：総和の公式"):
        try :
            st.image("./30_Streamlit_Figs/30_Streamlit_Figs.003.tiff")
        except :
            st.image("06_Integrated_Math_and_Science_for_Engineering/30_Streamlit_Figs/30_Streamlit_Figs.003.tiff")
####  応用例題  ####
st.sidebar.markdown("**応用例題の解答**")
with Lec01_contents_tab[2]:
    contents_num += 1
    st.markdown("### %s. %s"%(contents_num,Lec01_contents_list[2]))
    st.markdown(
    """
    ##### [Lec.1-3]Q1 次の和を求めよ．
    """,unsafe_allow_html=True)
    
    Q_num_q11 = 0  

    ##### q1
    Q_num_q11 += 1
    ans_q1_tmp_00=["(2*k+1)","k","4","14"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    tmps[0]=myfunc.format_disp(ans_q1_tmp_00[0],2)
    if st.sidebar.checkbox("(1)の答え",key="q01_3_1"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
            )

    ##### q2  
    Q_num_q11 += 1
    ans_q1_tmp_00=["(3*k^3+3*k^2+k)","k","1","n"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    tmps[0]=myfunc.format_disp(ans_q1_tmp_00[0],2)
    if st.sidebar.checkbox("(2)の答え",key="q01_3_2"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
            )

    ##### q3  
    Q_num_q11 += 1
    ans_q1_tmp_00=["2^(2*k+3)","k","1","n"]
    ans_q1_00,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
    tmps[0]=myfunc.format_disp(ans_q1_tmp_00[0],3)
    if st.sidebar.checkbox("(3)の答え",key="q01_3_3"):
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s =%s$"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0],ans_q1_00)
            )
    else:
        st.markdown(
            "(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s $"
            %(Q_num_q11,tmps[1],tmps[2],tmps[3],tmps[0])
            )

    with st.expander("ポイント：総和の公式"):
        try :
            st.image("./30_Streamlit_Figs/30_Streamlit_Figs.003.tiff")
        except :
            st.image("06_Integrated_Math_and_Science_for_Engineering/30_Streamlit_Figs/30_Streamlit_Figs.003.tiff")
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
    with st.expander("ポイント：下付き添字付きの記号について（補足）"):
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
    with st.expander("ポイント：数列の例"):
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
    with st.expander("ポイント：もう少し詳しく"):
        try :
            st.image("./30_Streamlit_Figs/30_Streamlit_Figs.002.tiff")
        except :
            st.image("06_Integrated_Math_and_Science_for_Engineering/30_Streamlit_Figs/30_Streamlit_Figs.002.tiff")

    with st.expander("ポイント：総和記号の読み方"):
        """
            - 記　号：$
                       \displaystyle \\sum_{i=\\square}^{\\triangle} a_{i} 
                       = a_{\\square} + a_{\\square+1} + a_{\\square+2} + \\cdots + a_{\\triangle} 
                     $
            - 解釈１：数列$~\{a_n\}~$があります．その中の第$~\\square~$項から第$~\\triangle~$項まで全て足しなさい．
            - 解釈２：$~i~$を$~\\square~$から$~\\triangle~$項まで１ずつ増やして得られる全ての項（数）を，全て足しなさい．  
            $\\phantom{a}$\n
        """
    
    #### 総和の公式
    """
        ##### 総和の公式
        **Ⅰ．$~N~$個の定数$~a\ (a \\ne 0)~$の総和**\n
        　状況設定：定数$~a~$が$~N~$個ある．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N a = a+a+\\cdots+a = N \cdot a$\n
        $\\phantom{a}$
        
        **Ⅱ．$~1~$から$~N~$までの自然数（$~1,\ 2,\ 3,\ \\cdots ,\ N~$）の総和**\n
        　状況設定：$~1~$から$~N~$までの自然数がある．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N i = 1+2+3+\\cdots+N = \\frac{1}{2}N\\big(N+1\\big)$\n
        　証　　明：数学ナビゲーションへ（[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/suuretu/henkan-tex.cgi?target=/math/category/suuretu/suuretu/siguma-k.html)）\n
        $\\phantom{a}$

        **Ⅲ．$~N~$個の数（$~1^2,\ 2^2,\ 3^2,\ \\cdots ,\ N^2~$）の総和**\n
        　状況設定：$~1~$から$~N~$までの自然数があり，そのそれぞれを２乗する．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N i^2 = 1^2+2^2+3^2+\\cdots+N^2 = \\frac{1}{6}N\\big(N+1\\big)\\big(2N+1\\big) $\n
        　証　　明：数学ナビゲーションへ（[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/suuretu/henkan-tex.cgi?target=/math/category/suuretu/suuretu/siguma-kk.html)）\n
        $\\phantom{a}$

        **Ⅳ．$~N~$個の数（$~1^3,\ 2^3,\ 3^3,\ \\cdots ,\ N^3~$）の総和**\n
        　状況設定：$~1~$から$~N~$までの自然数があり，そのそれぞれを３乗する．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N i^3 = 1^3+2^3+3^3+\\cdots+N^3 = \\left\{ \\frac{1}{2}N\\big(N+1\\big)\\right\}^2 $\n
        　証　　明：数学ナビゲーションへ（[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/suuretu/henkan-tex.cgi?target=/math/category/suuretu/suuretu/siguma-kkk.html)）\n
        $\\phantom{a}$

        **その他の公式については数学ナビゲーションの"数列"を参照：**[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/henkan-tex.cgi?target=/math/category/suuretu/index.html)
    """

    st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/NHbiNWkjHgd28K5C9)""")