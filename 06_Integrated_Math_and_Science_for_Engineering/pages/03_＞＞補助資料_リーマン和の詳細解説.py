from ast import Num
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
from sympy.calculus.util import *

Lec02_contents_list=["リーマン和の例","リーマン和とリーマン積分の例"]
Lec02_contents_tab =[]
Lec02_contents_tab = st.tabs(Lec02_contents_list)
contents_num =0
lec_num =2

####  リーマン和の例  ####
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

    set_param_graph_col02 = st.columns([4,3,3,3,3])
    with set_param_graph_col02[0]:                                     
        select_rtype_list01={
                            "右リーマン和":0,\
                            "中点リーマン和":1,\
                            "左リーマン和":2,\
                            "上リーマン和":3,\
                            "下リーマン和":4
                            }
        Type_riemann = st.selectbox("リーマン和のタイプ",select_rtype_list01.keys())
        Num_Type_riemann = int(select_rtype_list01[Type_riemann])
    with set_param_graph_col02[1]:
        Num_separate = st.number_input("区間の分割数",value=10,min_value=1)
    with set_param_graph_col02[2]:
        tmp_lower_limit = st.text_input("積分区間の下端", lower_limit)
        lower_limit = sympify(tmp_lower_limit)
    with set_param_graph_col02[3]:
        tmp_upper_limit = st.text_input("積分区間の上端", upper_limit)
        upper_limit = sympify(tmp_upper_limit)
    with set_param_graph_col02[4]:
        Lec2_radio02_list = {"0番目":0,"1番目":1}
        lower_limit_num = st.radio("下端の番号",Lec2_radio02_list.keys())
        lower_limit_num = Lec2_radio02_list[lower_limit_num]


    dx= (upper_limit - lower_limit)/Num_separate

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

        xis = np.linspace(float(lower_limit),float(upper_limit), Num_separate+1)
        for i in range(len(xis)):
            if ( i == 0 ) or ( i == len(xis)-1) :
                fig.add_vline(x=xis[i],line_dash="dash", line_color="black", line_width = 2 )
            else:
                fig.add_vline(x=xis[i],line_dash="dash", line_color="gray", line_width = 0.5 )

        for i in range(len(xis)-1):
            tmp_x = np.linspace(xis[i],xis[i+1],100)
            if Num_Type_riemann == 0 :
                tmp_y = np.full(len(tmp_x), float(f0.subs(x, xis[i+1])))
            elif Num_Type_riemann == 1 :
                tmp_y = np.full(len(tmp_x), float(f0.subs(x, (xis[i]+xis[i+1])/2)))
            elif Num_Type_riemann == 2 :
                tmp_y = np.full(len(tmp_x), float(f0.subs(x,xis[i])))
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
    
    
    if lower_limit < 0 :
        str_lower_limit = "\\left( %s \\right)"%(latex(lower_limit))
    else :
        str_lower_limit = "%s"%(latex(lower_limit))




    ####  リーマン積分のパラメータに合わせた解説  ####
    st.markdown(" ##### 上の設定に合わせたリーマン和と定積分の定義の解説")
    str_closed_interval = "\\big[%s,\\ %s \\big]"%(latex(lower_limit),latex(upper_limit))
    """
        $~y=%s~$と，$~x~$軸（$y=0$の直線），直線$~x=%s~$，$~x=%s~$で囲まれた領域$~A~$について考える．
        以下，$~%s \le x \le %s~$を閉区間$~%s~$と呼び，
        閉区間$~%s~$の最小値を"下限$~a~$"，最大値を"上限$~b~$"と呼ぶことにする．
    """%( 
        latex(f0),latex(lower_limit),latex(upper_limit),
        latex(lower_limit),latex(upper_limit),str_closed_interval,
        str_closed_interval
        )
    st.write("")
    str_each_x = "x_{%s} "%(lower_limit_num)
    if Num_separate <= 6 :
        for i in range(Num_separate):
            str_each_x += "< x_{%s} "%(i+1)
    else :
        for i in range(3):
            str_each_x += "< x_{%s} "%(i+1)
        str_each_x += "< \\cdots "
        str_each_x += " < x_{%s} "%(Num_separate-1)
        str_each_x += " < x_{%s} "%(Num_separate)
    
    if lower_limit_num == 0 :
        coefficient_dx = "k"
    else :
        coefficient_dx = " \\left( k - 1 \\right) "
    
    i,k,n = symbols("i k n")
    x_k_form = lower_limit + sym.summation(dx,(i,1,k-1))
    """
        ###### Step1：区間の分割と$x_k$を表す式
        閉区間$~%s~$を
        $$
            %s
        $$
        のように$~n=%s~$等分する．
        ここで$~x_{%s} = a = %s~$であり，$~x_{%s} = b = %s~$である．

        分割によって生じた$~%s~$個の小区間は同じ幅$~\\Delta x~$をもち，その値は
        $$
            \\Delta x =\\frac{b-a}{n} = \\frac{ %s - %s }{%s} = %s
        $$
        である．
        小区間の幅が$~\\Delta x~$であり，下端$~a~$が$~%s~$番目であるから，$~k~$番目の$~x~$の値$~x_{k}~$は
        $$
            x_{k} = x_{%s} + %s \\cdot \\Delta x =  %s + %s \\cdot %s = %s
        $$
        と表すことができる．
    """%(
        str_closed_interval,#1
        str_each_x,#1
        Num_separate,#1
        lower_limit_num, latex(lower_limit),latex(Num_separate + lower_limit_num),upper_limit,#4
        Num_separate,#1
        latex(upper_limit), latex(lower_limit), Num_separate,latex(dx),
        lower_limit_num,#1
        lower_limit_num,coefficient_dx,lower_limit,coefficient_dx,latex(dx),latex(x_k_form)
        )
    st.write("")

    k = symbols("k")
    x_k, x_k_1 = symbols("x_{k} x_{k+1} ")
    if Num_Type_riemann == 0 :
        tmp_ck0 = x_k_1
        tmp_ck1 = lower_limit + (k - lower_limit_num + 1 ) * dx
        str_fck = "\\left( " + str(latex(f0.subs(x,tmp_ck0 ))) + " \\right)"
        str_sk = f0.subs(x,tmp_ck1) * dx
    elif Num_Type_riemann == 1:
        tmp_ck0 = (x_k + x_k_1)/Num_separate
        tmp_ck1 = lower_limit + sym.Rational(3,2)*(k - lower_limit_num) * dx
        str_fck = "\\left( " + str(latex(f0.subs(x,tmp_ck0 ))) + " \\right)"
        str_sk = f0.subs(x,tmp_ck1) * dx
    elif Num_Type_riemann == 2:
        tmp_ck0 = x_k
        tmp_ck1 = lower_limit + (k - lower_limit_num) * dx
        str_fck = "\\left( " + str(latex(f0.subs(x,tmp_ck0 ))) + " \\right)"
        str_sk = f0.subs(x,tmp_ck1) * dx
    elif Num_Type_riemann == 3:
        x_k_max = sym.symbols("x_{k\:\max}")
        tmp_ck0 = x_k_max
        str_fck = " \\left( " + str(latex(f0.subs(x,tmp_ck0))) + " \\right)" 
        tmp_ck1 = x_k_max       
        str_sk = f0.subs(x,tmp_ck1) * dx
    elif Num_Type_riemann == 4:
        x_k_min = sym.symbols("x_{k\:\min}")
        tmp_ck0 = x_k_min 
        str_fck = " \\left( " + str(latex(f0.subs(x,tmp_ck0))) + " \\right) " 
        tmp_ck1 = x_k_min
        str_sk = f0.subs(x,tmp_ck1) * dx      
    """
        ###### Step2：小区間に長方形を作る
        次に各小区間に長方形を定め，それによって領域$~A~$を埋め尽くすことを考える．
        $~k~$番目の小区間$~\\big[x_{k},\\ x_{k+1}\\big]~$における長方形に対して次のような値$s_k$を考える．
        $$
            s_k = f\\big( c_k \\big)\\Delta x
        $$
        ここで$~c_{k}~$は$~k~$番目の小区間$~\\big[x_{k},\\ x_{k+1}\\big]~$の代表値を表している．
        %sを考える場合，代表値$~c_{k}~$は
        $$
            c_k = %s
        $$
        で与えられる．%s 
        $~s_k~$は横$~\\Delta x~$，縦$~f\\big(c_k\\big)~$の長方形の面積のような値であるが，
        負の値も取りうることに注意してほしい．
        $~f(x) = %s~$であるから$~s_k~$は小区間の番号$~k~$を用いて
        $$
            s_k = f \\big( c_k \\big) \\cdot \\Delta x = %s \\cdot %s = %s
        $$
        と表すことができる．
    """%(Type_riemann,
        myfunc.str_c_i(Num_Type_riemann)[0],
        myfunc.str_c_i(Num_Type_riemann)[1],
        latex(f0),
        str_fck,latex(dx),
        latex(str_sk)
        )
    st.write("")

    n = symbols("n")
    
    if Num_Type_riemann <3:
        Riemann_sum_n = sym.summation(str_sk,(k,1,n))
        str_Riemann_sum_n = "=" + latex(Riemann_sum_n)
        Riemann_sum = sym.summation(str_sk,(k,1,4))
    elif Num_Type_riemann == 3 :
        Riemann_sum_n = ""
        str_Riemann_sum_n = ""
        y_max_k = []
        Riemann_sum = 0
        for i in range(Num_separate):
            tmp_x_k = lower_limit + (i-lower_limit_num)*dx
            tmp_x_k_1 = lower_limit + (i+1-lower_limit_num)*dx
            tmp_y_max_k = maximum(f0,x,Interval(tmp_x_k,tmp_x_k_1))
            y_max_k.append(tmp_y_max_k)
            Riemann_sum += tmp_y_max_k * dx

    elif Num_Type_riemann == 4 :
        Riemann_sum_n = ""
        str_Riemann_sum_n = ""
        y_min_k = []
        Riemann_sum = 0
        for i in range(Num_separate):
            tmp_x_k = lower_limit + (i-lower_limit_num)*dx
            tmp_x_k_1 = lower_limit + (i+1-lower_limit_num)*dx
            tmp_y_min_k = minimum(f0,x,Interval(tmp_x_k,tmp_x_k_1))
            y_min_k.append(tmp_y_min_k)
            Riemann_sum += tmp_y_min_k * dx

    """
        ###### Step3：$~n~$分割した時のリーマン和を求める．
        分割数が$~n~$のとき，区間$~%s~$には$~n~$個の長方形がある．
        それぞれの$~s_k~$を計算し，それらを全て足し合わせたものを
        リーマン和といい，$~S_n~$と書く．リーマン和は代表値の選び方によりいくつかの種類があり．今は%sである．
        $$
            S_{n}
            =
            \sum_{i=1}^{n}
                f\\big( c_{i} \\big) \\cdot \Delta x_{i}
            =
            \sum_{i=1}^{n}
                \\left\{ %s \\right\}
            %s
        $$
        今の設定に従い，分割数が$~%s~$のときの%s$~S_{%s}~$を求めると，その値は
        $$
            S_{%s} = %s = %s
        $$
        である．
    """%(
        str_closed_interval,
        Type_riemann,
        latex(str_sk),
        str_Riemann_sum_n,
        Num_separate,Type_riemann,Num_separate,
        Num_separate,latex(Riemann_sum),float(Riemann_sum)
        )
    
    st.write("")



    
####  リーマン和の例  ####
contents_num += 1
with Lec02_contents_tab[contents_num]:
    st.markdown("### %s. 「%s」について"%(contents_num+1,Lec02_contents_list[contents_num]))
    #=========================
    st.write("")
    st.markdown("""#####  リーマン積分の値と%sの比較"""%(Type_riemann))
    Riemann_integral = sym.integrate(f0,(x,lower_limit,upper_limit))
    n = symbols("n")
    fxi_n = f0.subs(x,lower_limit+n*dx)
    Riemann_sum = sym.summation(fxi_n*dx,(n,1,Num_separate))
    dsi_str_list ={
            "右リーマン和":"%s"%(latex(f0).replace("x","x_{i+1}")),\
            "中点リーマン和":"%s"%(latex(f0).replace("x","\\left( \\frac{x_i + x_{i+1}}{2}\\right)")),\
            "左リーマン和":"%s"%(latex(f0).replace("x","x_i")),\
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

    st.markdown("#####  %sの途中計算の詳細"%(Type_riemann))
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
                        "右リーマン和":"区間の上限$~x_{i}~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "中点リーマン和":"区間の中点$~\\displaystyle \\frac{x_i+x_{i+1}}{2}~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "左リーマン和":"区間の下限$~x_{i}~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "上リーマン和":"$~y~$が最大となる$~x~$を$~\\tilde{x}_{i}~$とするとき，",\
                        "下リーマン和":"$~y~$が最小となる$~x~$を$~\\tilde{x}_{i}~$とするとき，",\
                    }    
    #====== make height and ds_i  =========
    x_i_maxs = [];x_i_mins = []
    if Num_Type_riemann == 0 :
        dsi_str =  "f \\left( x_{i+1} \\right)\\cdot \\Delta x"
        fxi_str = latex(f0).replace("x","x_{i+1}")
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
        dsi_str =  "f \\left( x_{i} \\right)\\cdot\\Delta x"
        fxi_str = latex(f0).replace("x","x_{i}")
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