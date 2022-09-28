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


Lec02_contents_list=["基礎例題","標準例題","応用例題","数列の和の極限","リーマン積分","リーマン積分の例"]
Lec02_contents_tab =[]
Lec02_contents_tab = st.tabs(Lec02_contents_list)
contents_num =0
lec_num =2

####  基礎例題  ####
st.sidebar.markdown("**基礎例題の解答**")
#contents_num += 1
section_num = 1
with Lec02_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec02_contents_list[contents_num])) 
    q_num = 0

    ##### q1
    q_num += 1
    Q_num_q0 = 0
    st.markdown("##### [lec.%s-%s] Q%s  次の式を部分分数分解しなさい．"%(lec_num,section_num,q_num))
    
    ########## user set problems ################################
    Q_list_2_1 = ["1/(x*(x+1))","1/((x+2)*(x+1))","1/((2*x+1)*(2*x+3))"]
    ############################################################

    ########## make problems and the ansewrs Q01
    for i in range(len(Q_list_2_1)):
        Q_num_q0 += 1
        key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,Q_num_q0)
        cb_name = "Q%s-(%s)の答え"%(q_num,Q_num_q0)
        q_form_00 = Q_list_2_1[i]
        q_form = latex(sympify(q_form_00))
        ans_q  = apart(  sympify(q_form_00)  ) 
        ans_q_form1 = latex( ans_q )
        #ans_q_tmp1 = ans_q.as_ordered_terms()
        if st.sidebar.checkbox(cb_name,key=key_name):
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ %s=%s$"
                %(Q_num_q0,q_form,ans_q_form1)
                )
        else:
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ %s$"
                %(Q_num_q0,q_form)
                )
    st.write("")

    ##### q2
    q_num += 1
    Q_num_q0 = 0
    st.markdown("##### [lec.%s-%s] Q%s  次の和を求めなさい．"%(lec_num,section_num,q_num))
    
    ########## user set problems ################################
    Q_list_2_1_form = ["1/n","k/n","k^2/n^3"]
    ############################################################

    ########## make problems and the ansewrs Q02 
    for i in range(len(Q_list_2_1_form)):
        Q_num_q0 += 1
        key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,Q_num_q0)
        cb_name = "Q%s-(%s)の答え"%(q_num,Q_num_q0)
        ## cal summation
        q_form = latex( sympify(Q_list_2_1_form[i]) ) 
        ans_q1_tmp_00=[Q_list_2_1_form[i],"k","1","n"]
        ans_q,tmps = myfunc.cal_sum(*ans_q1_tmp_00)
        ans_q_form1 = latex( ans_q )

        ## display problem and answer
        if st.sidebar.checkbox(cb_name,key=key_name):
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s=%s$"
                %(Q_num_q0,ans_q1_tmp_00[1],ans_q1_tmp_00[2],ans_q1_tmp_00[3],q_form,ans_q_form1)
                )
        else:
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\sum_{%s=%s}^{%s} %s$"
                %(Q_num_q0,ans_q1_tmp_00[1],ans_q1_tmp_00[2],ans_q1_tmp_00[3],q_form)
                )
    st.write("")


    ##### q3
    q_num += 1
    Q_num_q0 = 0
    st.markdown("##### [lec.%s-%s] Q%s 次の曲線および直線で囲まれた領域を図示しなさい．"%(lec_num,section_num,q_num))
    
    #### user set problems ################################
    Q_list_2_3_form = [["x+1","1","3"],["3*x-2","1","4"],["2*x^2+2","0","1"]]
    #######################################################
    
    for i in range(len(Q_list_2_3_form)):
        Q_num_q0 += 1
        key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,Q_num_q0)
        cb_name = "Q%s-(%s)の答え"%(q_num,Q_num_q0)
        tmp_col=[]
        tmp_col = st.columns(2)
        ## Display Problems
        with tmp_col[0]:
            tmps = Q_list_2_3_form[i]
            ans_q1_tmp_00= sympify(tmps[0])
            tmps[0] = latex( sympify(tmps[0]) ) 
            ans_q_form1 = latex( ans_q )
            st.markdown(
                    "$\\quad $(%s) $\\displaystyle \\ y=%s,\\ y=0,\\ x=%s,\\ x=%s$"
                    %(Q_num_q0,tmps[0],tmps[1],tmps[2])
            )
            
        with tmp_col[1]:
            cb_val = st.sidebar.checkbox(cb_name,key=key_name)
            if cb_val :
                #### plot with plotly
                x_axis_min = -5 ; x_axis_max=5
                y_axis_min = -5 ; y_axis_max=5
                xs = np.linspace(-50,50, 10000)
                x_range = np.linspace(float(tmps[1]),float(tmps[2]), 100)
                x= symbols("x")

                f1 = ans_q1_tmp_00 
                ys1 = lambdify(x, f1, "numpy")(xs)
                yys1 = lambdify(x, f1, "numpy")(x_range)
                ys0 = np.full(len(xs), 0)

                fig = go.Figure()
                fig.add_hline(y=0,line_width=1)
                fig.add_vline(x=0,line_width=1)

                fig.add_trace(
                    go.Scatter(
                        x = x_range,
                        y = yys1, 
                        name=r'領域',
                        fill = 'tozeroy'
                    )
                )
                fig.add_trace(
                    go.Scatter(x=xs,y=ys1,name=r'y=f(x)', line_color="red")
                    )

                fig.add_vline(x=float(tmps[1]),line_dash="dash", line_color="black")
                fig.add_vline(x=float(tmps[2]),line_dash="dash", line_color="black")
                
                fig.update_layout(
                    width=450,height=450,
                    xaxis=dict(range=(x_axis_min,x_axis_max),dtick=1),
                    yaxis=dict(range=(y_axis_min,y_axis_max),dtick=1),
                    legend=dict(
                            xanchor='left',
                            yanchor='bottom',
                            x=0.01,
                            y=0.91,
                            orientation='h',
                            bgcolor="white",
                            bordercolor="grey",
                            borderwidth=1
                            ),
                    margin=dict(t=50, b=50, l=0, r=0),
                    autosize=False
                )
                st.plotly_chart(fig, use_container_width=True,sharing="streamlit")
        ## Display answers

                

                #### plot with matplotlib
                # x= symbols("x")
                # f1 = ans_q1_tmp_00 ; f1_label = latex(ans_q1_tmp_00)
                # f2 = float(tmps[1])
                # f3 = float(tmps[2])
                # x_axis_min = -5 ; x_axis_max=5
                # y_axis_min = -5 ; y_axis_max=5

                # xs = np.linspace(x_axis_min,x_axis_max, 100)
                # ys = np.linspace(y_axis_min,y_axis_max, 100)
                # ys1 = lambdify(x, f1, "numpy")(xs)
                # # set font 
                # plt.rcParams["mathtext.fontset"] = 'cm'
                # plt.rcParams['mathtext.default'] = 'it' 

                # # set plt
                # fig, ax = plt.subplots()
                # ax.set_aspect('equal', adjustable='box')
                # plt.xlim(x_axis_min,x_axis_max)
                # plt.ylim(y_axis_min,y_axis_max)
                # plt.vlines(0, y_axis_min,y_axis_max,colors="black", linestyles='solid',linewidth=1 )
                # plt.hlines(0, x_axis_min,x_axis_max,colors="black", linestyles='solid',linewidth=1 )
                # ax.grid()

                # # plot lines
                # ax.plot(xs,ys1,linewidth=2.5, label = "$y=%s$"%(f1_label),color='r')
                # ax.axvline(x=f2,ymin=y_axis_min,ymax=y_axis_max,linewidth=2.5,linestyle='--',color='black',label="$x=%s$"%(f2))
                # ax.axvline(x=f3,ymin=y_axis_min,ymax=y_axis_max,linewidth=2.5,linestyle='--',color='black',label="$x=%s$"%(f3))

                
                # # plot area
                # int_range=np.linspace(f2, f3)
                # yys1 = lambdify(x, f1, "numpy")(int_range)
                # ax.fill_between(int_range, yys1, facecolor='lime', alpha=0.5)
                
                # # plot area

                # plt.legend()
                # st.pyplot(fig)

    with st.expander("ヒント：軸に並行な直線の式"): 
        """
        - **$~x~$軸に並行な直線の方程式**  
            $~y=a~$：$~x~$軸に並行で,その直線上の点の$~y~$座標が$~a~$であるような直線の式．  
            $~y=0~$：$~x~$軸を表す式．
        - **$~y~$軸に並行な直線の方程式**  
            $~x=b~$：$~y~$軸に並行で,その直線上の点の$~x~$座標が$~b~$であるような直線の式．  
            $~x=0~$：$~y~$軸を表す式．
        """
            
    st.write("")

####  標準例題  ####

st.sidebar.markdown("**標準例題の解答**")
section_num += 1
contents_num += 1
with Lec02_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec02_contents_list[contents_num])) 
    q_num = 0

    ##### q1
    q_num += 1
    Q_num_q0 = 0
    st.markdown("##### [lec.%s-%s] Q%s 次の和の極限値を求めなさい．"%(lec_num,section_num,q_num))
    
    oo = sym.oo
    n = symbols("n")
    
    #### user set problems ################################
    Q_list_2_1_form = ["1/n","k/n","k^2/n^3","(1/3)^(k+2)"]
    #######################################################
    
    for i in range(len(Q_list_2_1_form)):
        Q_num_q0 += 1
        key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,Q_num_q0)
        cb_name = "Q%s-(%s)の答え"%(q_num,Q_num_q0)
        ## cal summation
        q_form = latex( sympify(Q_list_2_1_form[i]) ) 
        ans_q1_tmp_00=[Q_list_2_1_form[i],"k","1","n"]
        ans_q,tmps = myfunc.cal_sum(*ans_q1_tmp_00,"sympy")
        
        ans_q_form1 = latex( sym.limit(sympify(ans_q),n,oo))
 
        ## display problem and answer
        if st.sidebar.checkbox(cb_name,key=key_name):
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\lim_{n \\to \\infty } \\sum_{%s=%s}^{%s} %s=%s$"
                %(Q_num_q0,ans_q1_tmp_00[1],ans_q1_tmp_00[2],ans_q1_tmp_00[3],q_form,ans_q_form1)
                )
        else:
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\lim_{n \\to \\infty } \\sum_{%s=%s}^{%s} %s$"
                %(Q_num_q0,ans_q1_tmp_00[1],ans_q1_tmp_00[2],ans_q1_tmp_00[3],q_form)
                )

    st.write("")

    ##### q2
    q_num += 1
    Q_num_q0 = 0
    st.markdown("##### [lec.%s-%s] Q%s 次の和の極限値を求めなさい．"%(lec_num,section_num,q_num))
    
    oo = sym.oo
    n,k = symbols("n,k")
    
    #### user set problems ################################
    Q_list_2_2_form = ["(2*k+3)/(n^2)","3/(4^k)","( 4*k^2/n^3 - 3*k/n^2 + 2/n )"]
    #######################################################
    
    for i in range(len(Q_list_2_2_form)):
        Q_num_q0 += 1
        key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,Q_num_q0)
        cb_name = "Q%s-(%s)の答え"%(q_num,Q_num_q0)

        ## cal summation
        ans_q1_tmp_00=[Q_list_2_2_form[i],"k","1","n"]
        ans_q,tmps = myfunc.cal_sum(*ans_q1_tmp_00,"sympy")
        ans_q_form1 = latex( sym.limit(sympify(ans_q),n,oo) )
 
        if i == 2:
            tmps[0]= "\\left(" + tmps[0] + "\\right)"

        ## display problem and answer
        if st.sidebar.checkbox(cb_name,key=key_name):
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\lim_{n \\to \\infty } \\sum_{%s=%s}^{%s} %s=%s$"
                %(Q_num_q0,tmps[1],tmps[2],tmps[3],tmps[0],ans_q_form1)
                )
        else:
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\lim_{n \\to \\infty } \\sum_{%s=%s}^{%s} %s$"
                %(Q_num_q0,tmps[1],tmps[2],tmps[3],tmps[0])
                )

    st.write("")

####  応用例題  ####
st.sidebar.markdown("**応用例題の解答**")
section_num += 1
contents_num += 1

with Lec02_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec02_contents_list[contents_num])) 

####  数列の極限  ####
contents_num += 1  
with Lec02_contents_tab[contents_num]:
    st.markdown("### %s. 「%s」について"%(contents_num+1,Lec02_contents_list[contents_num]))   
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

####  リーマン和とリーマン積分  ####
contents_num += 1
with Lec02_contents_tab[contents_num]:
    st.markdown("### %s. 「%s」について"%(contents_num+1,Lec02_contents_list[contents_num])) 
    """
        #### リーマン和と定積分の定義
         関数$~f~$が閉区間$~\\big[a,\\ b\\big]~$で定義されているものとする．\
            また閉区間$~\\big[a,\\ b\\big]~$を
        $$
            a=x_1 < x_2 < x_3 < \\cdots < x_{i} < x_{i+1} < \\cdots < x_{N} < x_{N+1} = b
        $$
         のように$~N~$分割する．\
            さらに区間$~\\big[x_{i},\\ x_{i+1}\\big]~$における$~i~$番目の\
            代表値$~\\xi_{i}\ (x_{i} < \\xi_{i} < x_{i+1})~$を定める．このとき，
        $$
            S_{N}
            =
            \sum_{i=1}^{N}
                f\\big( \\xi_{i} \\big) \\cdot \Delta x_{i}
        $$
         をリーマン和と呼ぶ．ここで$~\Delta x_i = x_{i+1} - x_{i}~$である．\
            通常，区間$~\\big[x_{i},\\ x_{i+1}\\big]~$を$~N~$等分する場合を考えるため，
        $$
            \Delta x = \Delta x_1 = \Delta x_2 = \cdots = \Delta x_N = \\frac{b-a}{N}
        $$
         である．
         $~N~$を限りなく大きくしたとき，リーマン和$~S_N~$がある値$~S~$に収束するならば，すなわち
        $$
            \\lim_{N \\to \\infty}
               \\sum_{i}^{N} f(\\xi_i) \cdot \\Delta x = S
        $$
         であるならば，関数$~f~$は区間$~\\big[a,\\ b\\big]~$でリーマン積分可能といい，\
            $~S~$を．
        $$
            S = \\int_{a}^{b} f(x) dx
        $$
         と書く．また$~S~$は，関数$~f~$は区間$~\\big[a,\\ b\\big]~$におけるリーマン積分は定積分という．
    """
    
st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/NHbiNWkjHgd28K5C9)""")