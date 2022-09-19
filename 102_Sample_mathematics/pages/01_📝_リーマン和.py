import streamlit as st
import pandas as pd
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import patches
import math

#### 関数の定義
def y_function(select_num,x_range,x_val):
    num_01 = select_num
    xr = x_range
    x = x_val
    if num_01 ==0:
        y_range = xr/2 + 1
        h = x/2 + 1 
        function0 =  lambda x: x/2 + 1
        y_form = "\\frac{1}{2}x+1"
    elif select_num == 1:
        y_range = 1/2*xr**2 + 1
        h = 1/2*x**2 + 1 
        function0 =  lambda x: 1/2*x**2+ 1
        y_form = "\\frac{1}{2}x^2 + 1"
    elif select_num == 2:
        y_range = xr*(xr-1)*(xr-3)
        h = x*(x-1)*(x-3)
        function0 =  lambda x:x*(x-1)*(x-3)
        y_form = "x^3-4x^2+3x"
    elif select_num == 3:
        y_range = 1/xr
        h=1/x
        function0 =  lambda x: 1/x
        y_form = "\\frac{1}{x}"
    elif select_num == 4:
        y_range = np.sin(xr)
        h = np.sin(x)
        function0 =  lambda x: np.sin(x)
        y_form = "\\sin x"
    elif select_num == 5:
        y_range = 2**xr
        h = 2**x 
        function0 =  lambda x: 2**x
        y_form = "\\displaystyle 2^x"
    elif select_num == 6:
        y_range = np.log2(xr)
        h = np.log2(x)
        function0 =  lambda x: np.log2(x)
        y_form = "\\log_{2}x"
    else:
        st.write("関数が設定されていません") 
        y_range = []
        h=0
    return y_range ,h,function0,y_form 

Riemann_sum_list=["総和記号","リーマン和と定積分","リーマン和の具体例"]
Riemann_sum_tab =[]
Riemann_sum_tab = st.tabs(Riemann_sum_list)

### 総和記号の説明
with Riemann_sum_tab[0]:
    st.markdown("#### 総和記号（$~\\Sigma~$）の定義")
    """
        $~N~$個の数$\\big\{ a_1,\ a_2,\ a_3,\ \cdots ,\ a_{N}\\big\}$があるとき，これらの数の総和$~S~$
        $$
            S = a_1 + a_2 + a_3 + \\cdots + a_{N}
        $$
        を
        $$
            S = \\sum_{i=1}^N a_i  
        $$
        と表す．ここで$~a_{i}~$は$\\big\{ a_1,\ a_2,\ a_3,\ \cdots ,\ a_{N}$の中の$~i~$番目の値を表す．
    """
    st.markdown("")
    st.markdown("#### 色々な数の総和の計算方法")
    """
        **Ⅰ．$~N~$個の定数$~a\ (a \\ne 0)~$の総和**\n
        　状況設定：定数$~a~$が$~N~$個ある．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N a = a+a+\\cdots+a = N \cdot a$\n
        $\phantom{a}$\n
        
        **Ⅱ．$~1~$から$~N~$までの自然数（$~1,\ 2,\ 3,\ \\cdots ,\ N~$）の総和**\n
        　状況設定：$~1~$から$~N~$までの自然数がある．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N i = 1+2+3+\\cdots+N = \\frac{1}{2}N\\big(N+1\\big)$\n
        　証　　明：数学ナビゲーションへ（[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/suuretu/henkan-tex.cgi?target=/math/category/suuretu/suuretu/siguma-k.html)）\n
        $\phantom{a}$\n

        **Ⅲ．$~N~$個の数（$~1^2,\ 2^2,\ 3^2,\ \\cdots ,\ N^2~$）の総和**\n
        　状況設定：$~1~$から$~N~$までの自然数があり，そのそれぞれを２乗する．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N i^2 = 1^2+2^2+3^2+\\cdots+N^2 = \\frac{1}{6}N\\big(N+1\\big)\\big(2N+1\\big) $\n
        　証　　明：数学ナビゲーションへ（[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/suuretu/henkan-tex.cgi?target=/math/category/suuretu/suuretu/siguma-kk.html)）\n
        $\phantom{a}$\n

        **Ⅳ．$~N~$個の数（$~1^3,\ 2^3,\ 3^3,\ \\cdots ,\ N^3~$）の総和**\n
        　状況設定：$~1~$から$~N~$までの自然数があり，そのそれぞれを３乗する．その総和を$~S~$とする．\n
        　総和の値：$\\displaystyle S=\sum_{i=1}^N i^3 = 1^3+2^3+3^3+\\cdots+N^3 = \\left\{ \\frac{1}{2}N\\big(N+1\\big)\\right\}^2 $\n
        　証　　明：数学ナビゲーションへ（[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/suuretu/henkan-tex.cgi?target=/math/category/suuretu/suuretu/siguma-kkk.html)）\n
        $\phantom{a}$\n

        **その他の公式については数学ナビゲーションの"数列"を参照：**[クリック](https://w3e.kanazawa-it.ac.jp/math/category/suuretu/henkan-tex.cgi?target=/math/category/suuretu/index.html)
    """
### リーマン和とリーマン積分の説明
with Riemann_sum_tab[1]:
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
    st.write("")
    """
        #### 代表値の取り方によるリーマン和の異なる表現
         区間$~\\big[x_{i},\\ x_{i+1}\\big]~$における代表値$~\\xi_{i}\ (x_{i} < \\xi_{i} < x_{i+1})~$を次のように\
        定める方法がある．
         1. 左リーマン和：$~\\xi_{i} = x_{i} ~$
         2. 中点リーマン和：$~\\displaystyle \\xi_{i} = \\frac{x_{i}+x_{i+1}}{2}~$
         3. 右リーマン和：$~\\xi_{i} = x_{i+1} ~$
         4. 上リーマン和：区間$~\\big[x_{i},\\ x_{i+1}\\big]~$において，$f(x)$が最大となる$~x~$を$~\\xi_{i}~$とする．
         5. 下リーマン和：区間$~\\big[x_{i},\\ x_{i+1}\\big]~$において，$f(x)$が最小となる$~x~$を$~\\xi_{i}~$とする．
        ※ これらの違いは，次のコンテンツ”リーマン和の具体例”を参考に理解を深めると良い．
    """

with Riemann_sum_tab[2]:
    st.markdown("#### リーマン和とリーマン積分の視覚的理解")
    st.markdown("##### 各種設定")
    ###　サイドバーによる関数の選択
    select_f_list01={
                        "例１：一次関数":0,\
                        "例２：二次関数":1,\
                        "例３：三次関数":2,\
                        "例４：分数関数":3,\
                        "例５：三角関数":4,\
                        "例６：指数関数":5,\
                        "例７：対数関数":6,\
                        }
    select_f = st.sidebar.selectbox(
                                    "使用する関数を選んでください",
                                    select_f_list01.keys()
                                    )
    select_f_num = select_f_list01[select_f]
    
    ### 各種パラメータの設定（グラフの範囲）
    set_param_graph_col01 = st.columns(4)
    with set_param_graph_col01[0]:
        x_axis_min = st.number_input("x軸の最小値",value=-5)
    with set_param_graph_col01[1]:
        x_axis_max = st.number_input("x軸の最大値",value=5)
    with set_param_graph_col01[2]:
        y_axis_min = st.number_input("y軸の最小値",value=-5)
    with set_param_graph_col01[3]:
        y_axis_max = st.number_input("y軸の最大値",value=5)

    ### 各種パラメータの設定（積分範囲とリーマン和についての設定：分割数，代表値，区間の左端，区間の右端）
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
        Interval_left = st.text_input("積分区間の左端", "1")
        Interval_left = float(Interval_left)
    with set_param_graph_col02[3]:
        Interval_right = st.text_input("積分区間の右端","3")
        Interval_right = float(Interval_right)

    ### リーマン和とリーマン積分の例（グラフ）
    st.write("")
    '''
        ##### リーマン和とリーマン積分
    '''
    Riemann_col01=[] ; Riemann_col01=st.columns(2)
    ### リーマン積分（グラフと値）
    with Riemann_col01[1]:
        st.markdown("##### リーマン積分 $~\\big(\\text{%s}\\big)~$"%("定積分"))
        plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
        plt.rcParams['mathtext.fontset'] = 'cm' # math fontの設定
        fig,ax= plt.subplots(figsize = (4,4))
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(which='major',direction='inout',length=5)
        ax.tick_params(direction='inout')
        
        x_tics_min = int(math.modf(x_axis_min)[1])
        x_tics_max = int(math.modf(x_axis_max)[1])
        y_tics_min = int(math.modf(y_axis_min)[1])
        y_tics_max = int(math.modf(y_axis_max)[1])
        
        ax.set_xticks([ i for i in range(x_tics_min,x_tics_max+1,1) ])
        ax.set_xticklabels( [(i if i != 0 else '') for i in range(x_tics_min,x_tics_max+1,1)])
        ax.set_yticks([ i for i in range(y_tics_min,y_tics_max+1,1) ])
        ax.set_yticklabels( [(i if i != 0 else '') for i in range(y_tics_min,y_tics_max+1,1)])
        plt.xlim(x_axis_min,x_axis_max)
        plt.ylim(y_axis_min,y_axis_max)
        # plt.xlabel(r"$x$",fontsize = 15)
        # plt.ylabel(r"$y$",fontsize = 15)
        plt.minorticks_on()
        # main関数
        x_axis_dx = 0.001*(x_axis_max - x_axis_min)
        x = np.arange(x_axis_min,x_axis_max, x_axis_dx )
        if select_f_num ==3:
            x = np.delete(x,0)
        y = y_function(select_num=select_f_num,x_range=x,x_val=1)[0]
        plt.plot(x,y, color = 'black', linewidth=1.0) 
        
        x2 = np.arange(Interval_left,Interval_right,0.001)
        y2 = y_function(select_num=select_f_num,x_range=x2,x_val=1)[0]
        ax.fill_between(x2, y2, 0, facecolor='lime', alpha=0.5)
        plt.vlines(Interval_left, y_axis_min,y_axis_max,colors="Blue", linestyles='solid',linewidth=1,alpha=0.5 )   
        plt.vlines(Interval_right, y_axis_min,y_axis_max,colors="Blue", linestyles='solid',linewidth=1,alpha=0.5 )    
        plt.vlines(0, y_axis_min,y_axis_max,colors="black", linestyles='solid',linewidth=1 )
        plt.hlines(0, x_axis_min,x_axis_max,colors="black", linestyles='solid',linewidth=1 )
        st.pyplot(fig)

        ### リーマン積分の式と結果　###
        y3 = y_function(select_num=select_f_num,x_range=x2,x_val=1)[2]
        Integrate_out = integrate.quad(y3,Interval_left,Interval_right)[0]
        y_form01= y_function(select_num=select_f_num,x_range=x2,x_val=1)[3]
        """
            $$
                \int_{%s}^{%s} \\Big( %s \\Big) dx = %s 
            $$
        """%\
            (Interval_left,Interval_right,y_form01,'{:.6f}'.format(Integrate_out))

    ### リーマン和（グラフと値）
    with Riemann_col01[0]:
        st.markdown( ("##### %s $~\\big(N=%s\\big)~$")%(Type_riemann,Num_separate))
        plt.rcParams['font.family'] = 'Times New Roman' # font familyの設定
        plt.rcParams['mathtext.fontset'] = 'cm' # math fontの設定
        fig,ax= plt.subplots(figsize = (4,4))
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(which='major',direction='inout',length=5)
        ax.tick_params(direction='inout')
        
        x_tics_min = int(math.modf(x_axis_min)[1])
        x_tics_max = int(math.modf(x_axis_max)[1])
        y_tics_min = int(math.modf(y_axis_min)[1])
        y_tics_max = int(math.modf(y_axis_max)[1])
        
        ax.set_xticks([ i for i in range(x_tics_min,x_tics_max+1,1) ])
        ax.set_xticklabels( [(i if i != 0 else '') for i in range(x_tics_min,x_tics_max+1,1)])
        ax.set_yticks([ i for i in range(y_tics_min,y_tics_max+1,1) ])
        ax.set_yticklabels( [(i if i != 0 else '') for i in range(y_tics_min,y_tics_max+1,1)])
        plt.xlim(x_axis_min,x_axis_max)
        plt.ylim(y_axis_min,y_axis_max)
        # plt.xlabel(r"$x$",fontsize = 15)
        # plt.ylabel(r"$y$",fontsize = 15)
        plt.minorticks_on()
        # main関数
        x_axis_dx = 0.001*(x_axis_max - x_axis_min)
        x = np.arange(x_axis_min,x_axis_max, x_axis_dx )
        if select_f_num ==3:
            x = np.delete(x,0)
        y = y_function(select_num=select_f_num,x_range=x,x_val=1)[0]
        plt.plot(x,y, color = 'black', linewidth=1.0) 
        # リーマン和
        dx = (Interval_right -Interval_left ) / Num_separate
        for i in range(Num_separate):
            n0=int(i)
            xr_l = Interval_left + float(n0)*dx
            xr_r = Interval_left + float(n0+1)*dx
            if Num_Type_riemann  == 0 :
                select_point = xr_l
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]
            elif Num_Type_riemann  == 1:
                select_point = (xr_l+xr_r)/2
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]
            elif Num_Type_riemann  == 2:
                select_point = xr_r
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]                
            elif Num_Type_riemann  == 3:
                xi_range=np.arange(xr_l,xr_r,0.001*(xr_r-xr_l))
                yi = y_function(select_num=select_f_num,x_range=xi_range,x_val=1)[0]
                yi_max_index = np.argmax(yi)
                select_point = xi_range[yi_max_index]
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]              
            elif Num_Type_riemann  == 4:
                xi_range=np.arange(xr_l,xr_r,0.001*(xr_r-xr_l))
                yi = y_function(select_num=select_f_num,x_range=xi_range,x_val=1)[0]
                yi_max_index = np.argmin(yi)
                select_point = xi_range[yi_max_index]
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]         
            else:
                st.write("エラー")
            yr_b = 0
            patch = patches.Rectangle(
                                xy=(xr_l, yr_b), 
                                width=dx, 
                                height=yr_t,
                                facecolor = "blue", 
                                alpha = 0.2)
            ax.add_patch(patch)
            plt.vlines(select_point, yr_b, yr_t, colors="black", linestyles='dashed',linewidth=0.5 )
            plt.vlines(xr_l, yr_b, yr_t ,colors="Blue", linestyles='solid',linewidth=0.2) 
            plt.vlines(xr_r, yr_b, yr_t ,colors="Blue", linestyles='solid',linewidth=0.2) 
            plt.hlines(yr_t,xr_l,xr_r ,colors="Blue", linestyles='solid',linewidth=0.2)

        plt.vlines(Interval_left, y_axis_min,y_axis_max,colors="Blue", linestyles='solid',linewidth=1,alpha=0.5 )   
        plt.vlines(Interval_right, y_axis_min,y_axis_max,colors="Blue", linestyles='solid',linewidth=1,alpha=0.5 )    
        plt.vlines(0, y_axis_min,y_axis_max,colors="black", linestyles='solid',linewidth=1 )
        plt.hlines(0, x_axis_min,x_axis_max,colors="black", linestyles='solid',linewidth=1 )
        st.pyplot(fig)

        ### リーマン和の式と結果　###
        S_riemann = 0
        dx = (Interval_right -Interval_left ) / Num_separate
        for i in range(Num_separate):
            n0=int(i)
            xr_l = Interval_left + float(n0)*dx
            xr_r = Interval_left + float(n0+1)*dx
            if Num_Type_riemann  == 0 :
                select_point = xr_l
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]
            elif Num_Type_riemann  == 1:
                select_point = (xr_l+xr_r)/2
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]
            elif Num_Type_riemann  == 2:
                select_point = xr_r
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]                
            elif Num_Type_riemann  == 3:
                xi_range=np.arange(xr_l,xr_r,0.001*(xr_r-xr_l))
                yi = y_function(select_num=select_f_num,x_range=xi_range,x_val=1)[0]
                yi_max_index = np.argmax(yi)
                select_point = xi_range[yi_max_index]
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]              
            elif Num_Type_riemann  == 4:
                xi_range=np.arange(xr_l,xr_r,0.001*(xr_r-xr_l))
                yi = y_function(select_num=select_f_num,x_range=xi_range,x_val=1)[0]
                yi_max_index = np.argmin(yi)
                select_point = xi_range[yi_max_index]
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]         
            else:
                st.write("エラー")
            S_riemann += yr_t*dx
        """
            $$
                \\sum_{i=1}^{\\color{red}%s}
                    \\Big(%s \\Big) \\cdot \\Delta x
                    = %s
            $$
        """\
            %(\
                Num_separate,\
                y_form01.replace('x', '{x_{i}}'),\
                '{:.6f}'.format(S_riemann)
            )
    
### リーマン和の途中計算の表示
    st.markdown("##### リーマン和の途中計算")
    tmp_xi_list = { "最初の３項程度を示す":0,"全ての項を示す":1}
    tmp_xi = st.radio("▶︎ 計算過程の表示設定１（分割されたxの値を小数第2位まで表示）",tmp_xi_list.keys(),horizontal=True)
    Dx01 = (Interval_right - Interval_left)/Num_separate
    if tmp_xi:
        str_xi = ""
        if tmp_xi_list[tmp_xi] == 0 :
            if Num_separate < 5:
                for i in range(Num_separate):
                    if i == 0 :
                        str_xi += '{x_{%s}}=%s'%(i+1,'{:.2f}'.format(Interval_left + float(i)*dx))
                    else:
                        str_xi += ',\ \ {x_{%s}}=%s'%(i+1,'{:.2f}'.format(Interval_left + float(i)*dx))    
            else:
                str_xi += '{x_{%s}}=%s,\ \ '%(1,'{:.2f}'.format(Interval_left + 0*dx)) 
                str_xi += '{x_{%s}}=%s,\ \ '%(2,'{:.2f}'.format(Interval_left + 1*dx)) 
                str_xi += '{x_{%s}}=%s,\ \ '%(3,'{:.2f}'.format(Interval_left + 2*dx)) 
                str_xi += "\\cdots,\ \ "
                str_xi += '{x_{%s}}=%s'%(Num_separate,'{:.2f}'.format(Interval_left + float(Num_separate)*dx)) 
        elif tmp_xi_list[tmp_xi] == 1 :
            for i in range(Num_separate):
                if i == 0 :
                    str_xi += '{x_{%s}}=%s'%(i+1,'{:.2f}'.format(Interval_left + float(i)*dx))
                else:
                    str_xi += ',\ \ {x_{%s}}=%s'%(i+1,'{:.2f}'.format(Interval_left + float(i)*dx))
    """
        $$
            %s
        $$
    """%(str_xi)

    tmp_Rsum_list = { "最初の３項程度を示す":0,"全ての項を示す":1}
    tmp_Rsum = st.radio("▶︎ 計算過程の表示設定２（計算過程とリーマン和の値の小数第6位までを表示）",tmp_Rsum_list.keys(),key=2,horizontal=True)
    if tmp_Rsum:
        str_fxi = ""
        if tmp_Rsum_list[tmp_Rsum] == 0 :
            if Num_separate < 5 :
                for i in range(Num_separate):
                    if i == 0 :
                        str_fxi += "\\Big(" + y_form01.replace('x', '{x_{%s}}'%(i+1)) + "\\Big)"
                    else:
                        str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(i+1)) + "\\Big)"
            else:        
                str_fxi += "\\Big(" + y_form01.replace('x', '{x_{%s}}'%(1)) + "\\Big)"
                str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(2)) + "\\Big)"
                str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(3)) + "\\Big)"
                str_fxi += "+\\cdots"
                str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(Num_separate)) + "\\Big)"
        elif tmp_Rsum_list[tmp_Rsum] == 1 :
            for i in range(Num_separate):
                if i == 0 :
                    str_fxi += "\\Big(" + y_form01.replace('x', '{x_{%s}}'%(i+1)) + "\\Big)"
                else:
                    str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(i+1)) + "\\Big)"
        """
            $$
                \\sum_{i=1}^{\\color{red}%s}
                        \\Big(%s \\Big) \\cdot \\Delta x
                = %s
                = %s
            $$
        """\
                %(\
                    Num_separate,\
                    y_form01.replace('x', '{x_{i}}'),\
                    str_fxi,\
                    '{:.6f}'.format(S_riemann)
                )

### リーマン和の極限とリーマン積分
    st.markdown("##### リーマン和の極限のイメージ")
    Rsum_lim_col = st.columns(2)
    with Rsum_lim_col[0]:
        Num_separate02 = int(st.text_input("十分大きな分割数を入力",50))
    with Rsum_lim_col[1]:
        Rsum_lim_disp_list={"N=5まで":5,"N=20まで":20,"すべて":Num_separate02}
        Rsum_lim_disp_keys = st.radio("各分割数におけるリーマン和の表示",Rsum_lim_disp_list.keys(),horizontal=True)

    ### 各分割数におけるリーマン和
    Rsum_lim_RsN = []
    x = np.arange(x_axis_min,x_axis_max, x_axis_dx ) 
    for j in range(1,Num_separate02+1):
        S_riemann = 0
        dx = (Interval_right -Interval_left ) / j
        for i in range(1,j+1):
            n0=int(i)
            xr_l = Interval_left + float(n0-1)*dx
            xr_r = Interval_left + float(n0)*dx
            if Num_Type_riemann  == 0 :
                select_point = xr_l
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]
            elif Num_Type_riemann  == 1:
                select_point = (xr_l+xr_r)/2
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]
            elif Num_Type_riemann  == 2:
                select_point = xr_r
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]                
            elif Num_Type_riemann  == 3:
                xi_range=np.arange(xr_l,xr_r,0.001*(xr_r-xr_l))
                yi = y_function(select_num=select_f_num,x_range=xi_range,x_val=1)[0]
                yi_max_index = np.argmax(yi)
                select_point = xi_range[yi_max_index]
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]              
            elif Num_Type_riemann  == 4:
                xi_range=np.arange(xr_l,xr_r,0.001*(xr_r-xr_l))
                yi = y_function(select_num=select_f_num,x_range=xi_range,x_val=1)[0]
                yi_max_index = np.argmin(yi)
                select_point = xi_range[yi_max_index]
                yr_t = y_function(select_num=select_f_num,x_range=x,x_val=select_point)[1]         
            else:
                st.write("エラー")
            S_riemann += yr_t*dx
        Rsum_lim_RsN.append(S_riemann)
    ### リーマン積分の値
    Integrate_out = integrate.quad(y3,Interval_left,Interval_right)[0]
    Rsum_lim_integrate = [ (Integrate_out) for i in range(1,Num_separate02+1)]
    Rsum_lim_datas ={
                    'リーマン積分':Rsum_lim_integrate,
                    'リーマン和':Rsum_lim_RsN
                    }
    Dataframe_Rsums = pd.DataFrame(Rsum_lim_datas)
    ### 計算結果の表示
    Rsum_lim_result=""
    if Num_separate02 < Rsum_lim_disp_list[Rsum_lim_disp_keys]:
        tmp_num00 = Num_separate02
    else :
        tmp_num00 = Rsum_lim_disp_list[Rsum_lim_disp_keys]
    
    for j in range(tmp_num00 ):
        str_fxi = ""
        if j < 3 :
            for i in range(j+1):
                if i == 0 :
                    str_fxi += "\\Big(" + y_form01.replace('x', '{x_{%s}}'%(i+1)) + "\\Big)"
                else:
                    str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(i+1)) + "\\Big)"
        else:        
            str_fxi += "\\Big(" + y_form01.replace('x', '{x_{%s}}'%(1)) + "\\Big)"
            str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(2)) + "\\Big)"
            # str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(3)) + "\\Big)"
            str_fxi += "+\\cdots"
            str_fxi += "+\\Big(" + y_form01.replace('x', '{x_{%s}}'%(j+1)) + "\\Big)"
        
        Rsum_lim_result +="\
                            \\sum_{i=1}^{\\color{red}%s}\
                                    \\Big(%s \\Big) \\cdot \\Delta x\
                            &= %s\
                            &&= %s\
                            &&&: %s\
                            \\\\\
                             "%(\
                                j+1,\
                                y_form01.replace('x', '{x_{i}}'),\
                                str_fxi,\
                                '{:.6f}'.format(Dataframe_Rsums['リーマン和'][j]),\
                                '{:.6f}'.format(Dataframe_Rsums['リーマン積分'][j])
                                )
    st.markdown("$\phantom{a}$\n")
    st.markdown("##### リーマン和の極限 ")
    """
        $$
            \\lim_{N \\to \\infty}
            \\sum_{i=1}^{N}\\Big( %s \\Big)
            =
            %s
        $$
    """%(
            y_form01.replace('x', '{x_{i}}'),
            '{:.6f}'.format(Dataframe_Rsums['リーマン積分'][0])
        )
    st.markdown("$\phantom{a}$\n")
    st.markdown("##### 各分割数におけるリーマン和とリーマン積分の値の比較")
    if Num_separate02 <= Rsum_lim_disp_list[Rsum_lim_disp_keys]:
        """
            $$
            \\begin{align*}
                & &&\\text{リーマン和の結果} &&& \\text{リーマン積分の値} 
                \\\\
                %s
            \\end{align*}
            $$
        """%(Rsum_lim_result)
    else:
        """
            $$
            \\begin{align*}
                & &&\\text{リーマン和の結果} &&& \\text{リーマン積分の値} 
                \\\\
                %s
                \\\\
                \\vdots
            \\end{align*}
            $$
        """%(Rsum_lim_result)