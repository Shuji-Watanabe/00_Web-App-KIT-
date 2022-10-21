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
        "3次関数:第２回宿題より":["(x+2)*(x-1)*(x-3)",0,1],
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
        Num_separate = st.number_input("区間の分割数",value=4,min_value=1)
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




#    
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