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
    Q_list_2_1_form = ["1/n","1/((2*k+1)*(2*k+3))","k/n","k^2/n^3"]
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
        # st.markdown("$%s$"%(ans_q_form1))
        ## display problem and answer
        if st.sidebar.checkbox(cb_name,key=key_name):
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\sum_{%s = %s}^{%s} %s = %s $"
                %(Q_num_q0,ans_q1_tmp_00[1],ans_q1_tmp_00[2],ans_q1_tmp_00[3], q_form, ans_q_form1)
                )
        else:
            st.markdown(
                "$\\quad $(%s) $\\displaystyle \\ \\sum_{%s = %s}^{%s} %s $"
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

####  リーマン積分の例  ####
contents_num += 1
with Lec02_contents_tab[contents_num]:
    st.markdown("### %s. 「%s」について"%(contents_num+1,Lec02_contents_list[contents_num]))
    st.markdown(" ##### 各種設定")

    Lec2_f_list ={
        "1次関数:授業演習課題より":["3*x-2",1,4],
        "2次関数:授業演習課題より":["2*x^2+2",0,1],
        "分数関数":["1/x",1,3]
        }
    Lec2_f_list_keys = Lec2_f_list.keys()

    Lec2_select_col01 = [] ; Lec2_select_col01 = st.columns(2)
    with Lec2_select_col01[1]:
         Lec2_radio01_list = {"プルダウンから選択":0,"自分で関数，区間を入力":1}
         tmp_num = st.radio("入力スタイルの選択",Lec2_radio01_list.keys())
         Lec2_radio01_num = Lec2_radio01_list[tmp_num]
    with Lec2_select_col01[0]:
         if Lec2_radio01_num == 0:
            select_key =st.selectbox("関数と区間の選択",Lec2_f_list_keys)
            f0 = sympify(Lec2_f_list[select_key][0])
            lower_limit = Lec2_f_list[select_key][1]
            upper_limit = Lec2_f_list[select_key][2]
         else :
            st.error("作成中")

    set_param_graph_col02 = st.columns(4)
    with set_param_graph_col02[0]:
        Num_separate = st.number_input("区間の分割数",value=10,min_value=1)
    with set_param_graph_col02[1]:                                     
        select_rtype_list01={
                            "左リーマン和":0,\
                            "中点リーマン和":1,\
                            "右リーマン和":2,\
                            "上リーマン和":3,\
                            "下リーマン和":4
                            }
        Type_riemann = st.selectbox("リーマン和のタイプ",select_rtype_list01.keys())
        Num_Type_riemann = int(select_rtype_list01[Type_riemann])
    with set_param_graph_col02[2]:
        tmp_lower_limit = st.text_input("積分区間の下端", lower_limit)
        lower_limit = sympify(tmp_lower_limit)
    with set_param_graph_col02[3]:
        tmp_upper_limit = st.text_input("積分区間の上端", upper_limit)
        upper_limit = sympify(tmp_upper_limit)

    dx= (upper_limit - lower_limit)/Num_separate
    st.markdown(" ##### 基本情報の確認")
    """
        - 関数：$\\displaystyle f(x)=%s$
        - 区間：$\\displaystyle \\left[%s,\\ %s\\right]$
        - 分割数：$%s$
        - 間隔：$\\displaystyle \\Delta x = x_{i+1} - x_{i} = %s$
        - タイプ：%s
    """%\
        (latex(f0),
         latex(lower_limit),
         latex(upper_limit),
         Num_separate,
         latex(dx),
         Type_riemann)
    st.write("")



    st.markdown("##### 状況の可視化")
    Lec2_select_col02 = [] ; Lec2_select_col02 = st.columns(2)
    with Lec2_select_col02[1]:
        st.markdown("###### 〜分割の様子〜")
        #### plot with plotly
        x= symbols("x")
        xs = np.linspace(-50,50, 10000)
        x_range = np.linspace(float(lower_limit),float(upper_limit), 100)
        ys1 = lambdify(x, f0, "numpy")(xs)
        ys0 = np.full(len(xs), 0)
        yys1 = lambdify(x, f0, "numpy")(x_range)
        ys0 = np.full(len(xs), 0)

        x_axis_min = float(lower_limit)-1 ; x_axis_max=float(upper_limit)+1
        if  ( np.amin(yys1)-0.5 >= 0 ) :
             y_axis_min = -1 ; y_axis_max = np.max(yys1)+1
        elif ( np.amin(yys1)-0.5 < 0 ) and ( np.max(yys1)+0.5 >=0 ):
             y_axis_min = np.amin(yys1)-1 ; y_axis_max = np.max(yys1)+1

        fig = go.Figure()
        fig.add_hline(y=0,line_width=1)
        fig.add_vline(x=0,line_width=1)
        fig.add_trace(
            go.Scatter(x=xs,y=ys1,name=r"$y=f(x)$", line_color="black")
            )

        xis = np.linspace(float(lower_limit),float(upper_limit), Num_separate)

        for i in range(len(xis)):
            if ( i == 0 ) or ( i == len(xis)-1 ) :
                fig.add_vline(x=xis[i],line_dash="dash", line_color="black", line_width = 2 )
            else:
                fig.add_vline(x=xis[i],line_dash="dash", line_color="gray", line_width = 0.5 )

        for i in range(len(xis)-1):
            tmp_x = np.linspace(xis[i],xis[i+1],100)
            if Num_Type_riemann == 0 :
                tmp_y = np.full(len(tmp_x), float(f0.subs(x,xis[i])))
            elif Num_Type_riemann == 1 :
                tmp_y = np.full(len(tmp_x), float(f0.subs(x, (xis[i]+xis[i+1])/2)))
            elif Num_Type_riemann == 2 :
                tmp_y = np.full(len(tmp_x), float(f0.subs(x, xis[i+1])))
            elif Num_Type_riemann == 3 :
                tmp_y = lambdify(x, f0, "numpy")(tmp_x)
                tmp_y = np.full(len(tmp_x), np.amax(tmp_y))
            elif Num_Type_riemann == 4 :
                tmp_y = lambdify(x, f0, "numpy")(tmp_x)
                tmp_y = np.full(len(tmp_x), np.min(tmp_y))

            fig.add_trace(
                go.Scatter(
                    x = tmp_x,
                    y = tmp_y, 
                    fill = 'tozeroy',
                    fillcolor = 'rgba(64,224,208,0.5)',#"turquoise",
                    line = dict(color = "blue"),
                    #opacity=0.01
                )
            )

        fig.update_layout(
            width=450,height=450,
            xaxis=dict(range=(x_axis_min,x_axis_max),dtick=1),
            yaxis=dict(range=(y_axis_min,y_axis_max),dtick=1),
            showlegend = False,
            # legend=dict(
            #         xanchor='left',
            #         yanchor='bottom',
            #         x=0,#x=0.01,
            #         y=1,#y=0.91,
            #         orientation='h',
            #         bgcolor="white",
            #         bordercolor="grey",
            #         borderwidth=1
            #         ),
            margin=dict(t=50, b=50, l=0, r=0),
            autosize=False
        )
        st.plotly_chart(fig, use_container_width=True,sharing="streamlit")
    with Lec2_select_col02[0]:
        st.markdown("###### 〜領域$~A~$の様子〜") 
        #### plot with plotly
        x= symbols("x")
        xs = np.linspace(-50,50, 10000)
        x_range = np.linspace(float(lower_limit),float(upper_limit), 100)
        ys1 = lambdify(x, f0, "numpy")(xs)
        ys0 = np.full(len(xs), 0)
        yys1 = lambdify(x, f0, "numpy")(x_range)
        ys0 = np.full(len(xs), 0)

        x_axis_min = float(lower_limit)-1 ; x_axis_max=float(upper_limit)+1
        if  ( np.amin(yys1)-0.5 >= 0 ) :
             y_axis_min = -1 ; y_axis_max = np.max(yys1)+1
        elif ( np.amin(yys1)-0.5 < 0 ) and ( np.max(yys1)+0.5 >=0 ):
             y_axis_min = np.amin(yys1)-1 ; y_axis_max = np.max(yys1)+1

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
            go.Scatter(x=xs,y=ys1,name=r"$y=f(x)$", line_color="black")
            )
        fig.add_vline(x=float(lower_limit),line_dash="dash", line_color="black")
        fig.add_vline(x=float(upper_limit),line_dash="dash", line_color="black")
        
        fig.update_layout(
            width=450,height=450,
            xaxis=dict(range=(x_axis_min,x_axis_max),dtick=1),
            yaxis=dict(range=(y_axis_min,y_axis_max),dtick=1),
            showlegend = False,
            margin=dict(t=50, b=50, l=0, r=0),
            autosize=False
        )
        st.plotly_chart(fig, use_container_width=True,sharing="streamlit")
        

    #=========================
    st.write("")
    st.markdown("""#####  リーマン積分の値と%sの比較"""%(Type_riemann))
    Riemann_integral = sym.integrate(f0,(x,lower_limit,upper_limit))
    n = symbols("n")
    fxi_n = f0.subs(x,lower_limit+n*dx)
    Riemann_sum = sym.summation(fxi_n*dx,(n,1,Num_separate))
    dsi_str_list ={
            "左リーマン和":"%s"%(latex(f0).replace("x","x_i")),\
            "中点リーマン和":"%s"%(latex(f0).replace("x","\\left( \\frac{x_i + x_{i+1}}{2}\\right)")),\
            "右リーマン和":"%s"%(latex(f0).replace("x","x_{i+1}")),\
            "上リーマン和":"%s"%(latex(f0).replace("x","\\tilde{x}_{i}")),\
            "下リーマン和":"%s"%(latex(f0).replace("x","\\tilde{x}_{i}"))
            }
    """
        - リーマン積分（定積分）
            $$
                \\int_{%s}^{%s} \\left(%s \\right) dx = %s =%s
            $$
        - %s( 分割数 =$~%s~$)
            $$
                \\sum_{i=1}^{%s} \\left\{ %s\\right\} \\cdot \\Delta x = %s = %s
            $$
    """%(
        lower_limit,upper_limit,latex(f0),latex(Riemann_integral),float(Riemann_integral),
        Type_riemann, Num_separate,
        Num_separate, dsi_str_list[Type_riemann], latex(Riemann_sum) ,float(Riemann_sum)
        )
    st.write("")

    st.markdown("#####  %sについての詳細解説"%(Type_riemann))
    with st.expander("途中計算の詳細表示"):
        Lec2_select_col03=st.columns(2)
        tmp_select = []
        with Lec2_select_col03[0]:
            tmp_select.append(st.checkbox("分割された区間の詳細表示"))
        with Lec2_select_col03[1]:
            tmp_select.append(st.checkbox("%sの詳細表示"%(Type_riemann)))  
    """
        $~y=%s~$と$~y~$軸，直線$~x=%s~$，$~x=%s~$で囲まれた領域$~A~$を考える(左の図)．
        
        まず，区間$~\\left[%s,\ %s\\right]~$を$~%s~$等分する．このとき
    """%( 
        latex(f0),latex(lower_limit),latex(upper_limit),
        latex(lower_limit),latex(upper_limit),Num_separate
        )

    #===== make str of x_i =======
    tmp_x_i_str = ""
    if Num_separate <= 5 :
        for l in range(Num_separate+1):
            if l == 0 :
                tmp_x_i_str += "x_{%s} &= %s + %s \\cdot %s = %s \\\\"%\
                                (l+1,latex(lower_limit),l,latex(dx),latex(lower_limit+l*dx))
            else :
                tmp_x_i_str += "\\\\"
                tmp_x_i_str += "x_{%s} &= %s + %s \\cdot %s = %s \\\\"%\
                                (l+1,latex(lower_limit),l,latex(dx),latex(lower_limit+l*dx))
    if Num_separate > 5:
        if tmp_select [0] : 
            for l in range(Num_separate):
                    tmp_x_i_str += "x_{%s} &= %s + %s \\cdot %s = %s,\\quad "%\
                                    (l+1,latex(lower_limit),l,latex(dx),latex(lower_limit+l*dx))
            tmp_x_i_str += "x_{%s} &= %s + %s \\cdot %s = %s,\\quad "%\
                            (Num_separate+1,latex(lower_limit),Num_separate,latex(dx),latex(lower_limit+Num_separate*dx))
        else :
            for l in range(4):
                if l < 3:
                    tmp_x_i_str += "x_{%s} &= %s + %s \\cdot %s  = %s,\\quad "%\
                                    (l+1,latex(lower_limit),l,latex(dx),latex(lower_limit+l*dx))
                else :
                    tmp_x_i_str += "\\cdots ,\\quad "
            tmp_x_i_str += "x_{%s} &= %s + %s \\cdot %s = %s \\\\"%\
                            (Num_separate+1,latex(lower_limit),Num_separate,latex(dx),latex(lower_limit+Num_separate*dx))
    
    """
    $$
        \\begin{align*}
            %s
        \\end{align*}
    $$
    """%(tmp_x_i_str)
    Lec2_str_list01 = {
                        "左リーマン和":"区間の下限$~x_{i}~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "中点リーマン和":"区間の中点$~\\displaystyle \\frac{x_i+x_{i+1}}{2}~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "右リーマン和":"区間の上限$~x_{i}~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "上リーマン和":"$~y~$が最大となる$~x~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "下リーマン和":"$~y~$が最小となる$~x~$を$~\\tilde{x}_{i}~$とするとき，",\
                    }    
    #====== make height and ds_i  =========
    x_i_maxs = [];x_i_mins = []
    if Num_Type_riemann == 0 :
        dsi_str =  "f \\left( x_{i} \\right)\\cdot\\Delta x"
        fxi_str = latex(f0).replace("x","x_{i}")
        dsi_str_subs = "\\left( %s \\right)\\cdot %s"%( fxi_str , latex(dx) )
        fxi_str2 = latex(f0).replace("x","XXX")
        dsi_str_subs2 = "\\left\{ %s \\right\}\\cdot %s"%( fxi_str2 , latex(dx) ) 
    elif Num_Type_riemann == 1 :
        dsi_str =  "f \\left(\\frac{x_{i}+x_{i+1}}{2} \\right) \\cdot \\Delta x"
        fxi_str = latex(f0).replace("x","\\left(\\frac{x_{i}+x_{i+1}}{2} \\right)")
        dsi_str_subs = "\\left\{ %s \\right\} \\cdot %s"%( fxi_str , latex(dx) )
        fxi_str2 = latex(f0).replace("x","XXX")
        dsi_str_subs2 = "\\left\{ %s \\right\}\\cdot %s"%( fxi_str2 , latex(dx) ) 
    elif Num_Type_riemann == 2 :
        dsi_str =  "f \\left( x_{i+1} \\right)\\cdot \\Delta x"
        fxi_str = latex(f0).replace("x","x_{i+1}")
        dsi_str_subs = "\\left( %s \\right)\\cdot %s"%( fxi_str , latex(dx) )
        fxi_str2 = latex(f0).replace("x","XXX")
        dsi_str_subs2 = "\\left\{ %s \\right\}\\cdot %s"%( fxi_str2 , latex(dx) ) 
    elif Num_Type_riemann == 3 :
        x_i_maxs = []
        for k in range(Num_separate):
            tmp_x = np.linspace(float(lower_limit)+k*float(dx),float(upper_limit)+(k+1)*float(dx),100)
            x_i_maxs.append(np.max(tmp_x))
        dsi_str =  "f \\left( x_{i:\\rm max} \\right)\\cdot \\Delta x"
        fxi_str = latex(f0).replace("x","x_{i:\\rm max}")
        dsi_str_subs = "\\left( %s \\right)\\cdot %s"%( fxi_str , latex(dx) )
        fxi_str2 = latex(f0).replace("x","XXX")
        dsi_str_subs2 = "\\left\{ %s \\right\}\\cdot %s"%( fxi_str2 , latex(dx) ) 
    elif Num_Type_riemann == 4 :
        x_i_mins = []
        for k in range(Num_separate):
            tmp_x = np.linspace(float(lower_limit)+k*float(dx),float(upper_limit)+(k+1)*float(dx),100)
            x_i_mins.append(np.min(tmp_x))  
        dsi_str =  "f \\left( x_{i:\\rm min} \\right)\\cdot \\Delta x"
        fxi_str = latex(f0).replace("x","x_{i:\\rm min}")
        dsi_str_subs = "\\left( %s \\right)\\cdot %s"%( fxi_str , latex(dx) )
        fxi_str2 = latex(f0).replace("x","XXX")
        dsi_str_subs2 = "\\left\{ %s \\right\}\\cdot %s"%( fxi_str2 , latex(dx) ) 
    """
        次に，区間$~\\left[x_i,\\ x_{i+1} \\right]~$において
        %s
        $~f\\left( \\tilde{x}_{i}\\right)~$を高さとする微小な長方形を考えると，その微小な面積$~ds_i~$は
        $$
            ds_i 
            = f\\left( \\tilde{x}_i \\right) \\Delta x 
            = %s 
            = %s
        $$
        である．
    """%(
        Lec2_str_list01[Type_riemann],
        dsi_str,dsi_str_subs
    )
    st.error("修正中")
    # tmp_Riemann_sum_str =[[],[],[],[],[]] 
    # for l in range(Num_separate+1) :
    #     tmp_str = dsi_str.replace( "i+1","%s"%(l+2) )
    #     tmp_str = tmp_str.replace( "{i","{%s"%(l+1) )
    #     tmp_Riemann_sum_str[0].append(tmp_str)

    #     ### 
    #     tmp_str = fxi_str.replace("i+1","%s"%(l+1))
    #     tmp_str = tmp_str.replace("{i","{%s"%(l))
    #     tmp_Riemann_sum_str[1].append(tmp_str)
        
    #     ###
    #     if Num_Type_riemann == 0 :
    #         tmp_num = lower_limit + l* float(dx)
    #     elif Num_Type_riemann == 1:
    #         tmp_num = lower_limit + 1.5*l* float(dx)
    #     elif Num_Type_riemann == 2:       
    #         tmp_num = lower_limit + (l+1)* float(dx)
    #     elif Num_Type_riemann == 3:
    #         if len(x_i_maxs) > 1:
    #             tmp_num = x_i_maxs[l]
    #     elif Num_Type_riemann == 4:       
    #         if len(x_i_mins) > 1 :
    #             tmp_num = x_i_mins[l] 
        
    #     tmp_str = latex(f0).replace("x","\\cdot %s"%latex(tmp_num))
    #     tmp_str = tmp_str.replace("{i","{%s"%(l))
    #     tmp_Riemann_sum_str[2].append(tmp_str)

    # for l in range(len(tmp_Riemann_sum_str[0])) :
    #     st.markdown("$%s$"%(tmp_Riemann_sum_str[2][l]) )



    # Riemann_sum_str=["","","","",""]
    # if  tmp_select[1] :
    #     for m in range(Num_separate) :
    #         tmp_m = f0.subs(x,lower_limit+m*dx) * dx
    #         if m ==0 :
    #             dsi_str_01 = dsi_str.replace("i+1","%s"%(m+1))
    #             dsi_str_01 = dsi_str.replace("{i","{%s"%(m))
    #             Riemann_sum_str[0] += dsi_str_01 

    #             
    #             Riemann_sum_str[1] += "\\left\{" + fxi_str_01 + "\\right\} \\cdot %s"%(latex(dx))


    #             fxi_str_02 = latex(f0).replace("x","\\cdot %s"%lat(ex(lower_limit + m * dx)))                       
    #             Riemann_sum_str[2] += "\\left(" +  + "\\right) \\cdot %s"%(latex(dx))
    #             if f0.subs(x,lower_limit+m*dx) >=0 :
    #                 Riemann_sum_str[3] += latex(f0.subs(x,lower_limit+m*dx)) + "\\cdot %s"%(latex(dx))
    #             else :
    #                 Riemann_sum_str[3] += "\\left(" + latex(f0.subs(x,lower_limit+m*dx)) + "\\right)" 
                
    #             if tmp_m >=0 :
    #                 Riemann_sum_str[4] += "%s"%(latex(tmp_m))
    #             else :
    #                 Riemann_sum_str[4] += "\\left(%s\\right)"%(latex(tmp_m))
    #         else :
    #             Riemann_sum_str[0] += "+" + dsi_str.replace("i","%s"%(latex(m)))
    #             Riemann_sum_str[1] += "+" + "\\left\{" + latex(f0).replace("x","x_{%s}"%(latex(m)))+ "\\right\} \\cdot %s"%(latex(dx))
    #             Riemann_sum_str[2] += "+" +  "\\left(" +  latex(f0).replace("x","\\cdot %s"%(latex(lower_limit + m * dx))) + "\\right) \\cdot %s"%(latex(dx))
    #             if f0.subs(x,lower_limit+m*dx) >=0 :
    #                 Riemann_sum_str[3] += "+" + latex(f0.subs(x,lower_limit+m*dx)) + "\\cdot %s"%(latex(dx))
    #             else :
    #                 Riemann_sum_str[3] += "+" + "\\left(" + latex(f0.subs(x,lower_limit+m*dx)) + "\\right)" + "\\cdot %s"%(latex(dx))  
    #             if tmp_m >=0 :
    #                 Riemann_sum_str[4] += "+ %s"%(latex(tmp_m))
    #             else :
    #                 Riemann_sum_str[4] += "+ \\left(%s\\right)"%(latex(tmp_m))
    # else :
    #     if Num_separate <= 5 :
    #         for m in range(Num_separate+1) :
    #             tmp_m = f0.subs(x,lower_limit+m*dx) * dx
    #             if m == 0 :
    #                 Riemann_sum_str[0] += dsi_str.replace("i","%s"%(latex(m)))
    #                 Riemann_sum_str[1] += "\\left\{" + latex(f0).replace("x","x_{%s}"%(latex(m)))+ "\\right\} \\cdot %s"%(latex(dx))
    #                 Riemann_sum_str[2] += "\\left(" + latex(f0).replace("x","\\cdot %s"%(latex(lower_limit + m * dx))) + "\\right)\\cdot %s"%(latex(dx))
    #                 if f0.subs(x,lower_limit+m*dx) >=0 :
    #                     Riemann_sum_str[3] += latex(f0.subs(x,lower_limit+m*dx)) + "\\cdot %s"%(latex(dx))
    #                 else :
    #                     Riemann_sum_str[3] += "\\left(" + latex(f0.subs(x,lower_limit+m*dx)) + "\\right)\\cdot %s"%(latex(dx)) 
    #                 if tmp_m >=0 :
    #                     Riemann_sum_str[4] += "%s"%(latex(tmp_m))
    #                 else :
    #                     Riemann_sum_str[4] += "\\left(%s\\right)"%(latex(tmp_m))
    #             elif m < 5 :
    #                 Riemann_sum_str[0] += "+" + dsi_str.replace("i","%s"%(latex(m)))
    #                 Riemann_sum_str[1] += "+" + "\\left\{" +  latex(f0).replace("x","x_{%s}"%(latex(m)))+ "\\right\} \\cdot %s"%(latex(dx))
    #                 Riemann_sum_str[2] += "+" +  "\\left(" + latex(f0).replace("x","\\cdot %s"%(latex(lower_limit + m * dx))) + "\\right)\\cdot %s"%(latex(dx))
    #                 if f0.subs(x,lower_limit+m*dx) >=0 :
    #                     Riemann_sum_str[3] += "+" + latex(f0.subs(x,lower_limit+m*dx)) + "\\cdot %s"%(latex(dx))
    #                 else :
    #                     Riemann_sum_str[3] += "+" + "\\left(" + latex(f0.subs(x,lower_limit+m*dx)) + "\\right)\\cdot %s"%(latex(dx))
    #                 if tmp_m >=0 :
    #                     Riemann_sum_str[4] += "+ %s"%(latex(tmp_m))
    #                 else :
    #                     Riemann_sum_str[4] += "+ \\left(%s\\right)"%(latex(tmp_m))
    #     elif Num_separate > 5 :
    #         for m in range(3) :
    #             tmp_m = f0.subs(x,lower_limit+m*dx) * dx
    #             if m == 0 :
    #                 Riemann_sum_str[0] += dsi_str.replace("i","%s"%(latex(m)))
    #                 Riemann_sum_str[1] += "\\left\{" + latex(f0).replace("x","x_{%s}"%(latex(m)))+ "\\right\} \\cdot %s"%(latex(dx))
    #                 Riemann_sum_str[2] +=  "\\left(" + latex(f0).replace("x","\\cdot %s"%(latex(lower_limit + m * dx))) + "\\right)\\cdot %s"%(latex(dx))
    #                 if f0.subs(x,lower_limit+m*dx) >=0 :
    #                     Riemann_sum_str[3] += latex(f0.subs(x,lower_limit+m*dx)) + "\\cdot %s"%(latex(dx))
    #                 else :
    #                     Riemann_sum_str[3] += "\\left(" + latex(f0.subs(x,lower_limit+m*dx)) + "\\right)\\cdot %s"%(latex(dx))
    #                 if tmp_m >=0 :
    #                     Riemann_sum_str[4] += "%s"%(latex(tmp_m)) 
    #                 else :
    #                     Riemann_sum_str[4] += "\\left(%s\\right)"%(latex(tmp_m))
    #             else :
    #                 Riemann_sum_str[0] += "+" + dsi_str.replace("i","%s"%(latex(m)))
    #                 Riemann_sum_str[1] += "+" + "\\left\{" + latex(f0).replace("x","x_{%s}"%(latex(m)))+ "\\right\} \\cdot %s"%(latex(dx))
    #                 Riemann_sum_str[2] += "+" +  "\\left(" + latex(f0).replace("x","\\cdot %s"%(latex(lower_limit + m * dx))) + "\\right)\\cdot %s"%(latex(dx)) 
    #                 if f0.subs(x,lower_limit+m*dx) >=0 :
    #                     Riemann_sum_str[3] += "+" + latex(f0.subs(x,lower_limit+m*dx)) + "\\cdot %s"%(latex(dx))
    #                 else :
    #                     Riemann_sum_str[3] += "+" + "\\left(" + latex(f0.subs(x,lower_limit+m*dx)) + "\\right)\\cdot %s"%(latex(dx))                   
    #                 if tmp_m >=0 :
    #                     Riemann_sum_str[4] += "+ %s"%(latex(tmp_m))
    #                 else :
    #                     Riemann_sum_str[4] += "+ \\left(%s\\right)"%(latex(tmp_m))
    #         Riemann_sum_str[0] += "+ \\cdots"
    #         Riemann_sum_str[1] += "+ \\cdots"
    #         Riemann_sum_str[2] += "+ \\cdots"
    #         Riemann_sum_str[3] += "+ \\cdots"
    #         Riemann_sum_str[4] += "+ \\cdots"
            
    #         m = Num_separate + 1
    #         tmp_m = f0.subs(x,lower_limit+m*dx) * dx
    #         Riemann_sum_str[0] += "+" + dsi_str.replace("i","%s"%(latex(m)))
    #         Riemann_sum_str[1] += "+" + "\\left\{" + latex(f0).replace("x","x_{%s}"%(latex(m)))+ "\\right\} \\cdot %s"%(latex(dx))
    #         Riemann_sum_str[2] += "+" +  "\\left(" + latex(f0).replace("x","\\cdot %s"%(latex(lower_limit + m * dx))) + "\\right)"
    #         if f0.subs(x,lower_limit+m*dx) >=0 :
    #             Riemann_sum_str[3] += "+" + latex(f0.subs(x,lower_limit+m*dx)) + "\\cdot %s"%(latex(dx))
    #             if tmp_m >=0 :
    #                 Riemann_sum_str[4] += "+ %s"%(latex(tmp_m))
    #             else :
    #                 Riemann_sum_str[4] += "+ \\left(%s\\right)"%(latex(tmp_m))
               
    #         else :
    #             Riemann_sum_str[3] += "+" + "\\left(" + latex(f0.subs(x,lower_limit+m*dx)) + "\\right)" + "\\cdot %s"%(latex(dx))
    #             if tmp_m >=0 :
    #                 Riemann_sum_str[4] += "+ %s"%(latex(tmp_m))
    #             else :
    #                 Riemann_sum_str[4] += "+ \\left(%s\\right)"%(latex(tmp_m))


    # re_sub_str = 'r[0-9]{1,%s}ght'%(len(str(Num_separate)))
    # Riemann_sum_str[0] = re.sub(re_sub_str,'right',Riemann_sum_str[0]) 
    # """
    #     今，区間$~\\left[%s,\ %s\\right]~$に長方形が$~%s~$個あるので，それらの総和（%s）$~S_{%s}~$は
    #     $$
    #         \\begin{align*}
    #             S_{%s}
    #             &= \\sum_{i=1}^{%s} %s

    #             \\\\
    #             &= %s \\\\
    #             \\\\
    #             &= %s \\\\
    #             \\\\
    #             &= %s \\\\
    #             \\\\
    #             &= %s \\\\
    #             \\\\
    #             &= %s \\\\

    #             \\\\
    #             &= %s \\\\
    #             \\\\
    #             &= %s
    #         \\end{align*}
    #     $$
    #     となる．
    # """%\
    #     ( 
    #     latex(lower_limit),latex(upper_limit),Num_separate,Type_riemann,Num_separate,
    #     Num_separate,
    #     Num_separate, dsi_str,
    #     Riemann_sum_str[0],
    #     Riemann_sum_str[1],
    #     Riemann_sum_str[2],
    #     Riemann_sum_str[3],
    #     Riemann_sum_str[4],
    #     latex(Riemann_sum),
    #     float(Riemann_sum)
    #     )
    
    

st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/NHbiNWkjHgd28K5C9)""")