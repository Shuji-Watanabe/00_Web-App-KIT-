import streamlit as st
import sympy as sym
import pandas as pd
import numpy as np
import plotly as plotly


Contents_list=["小テスト４のポイント","領域の図示","面積","体積","重心"]
Contents_tab = st.tabs(Contents_list)
Contents_num , Section_num = 0 , 0 

st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/Q9xzdkAdUFoE4fYr9) """)

### 1st contents
with Contents_tab [Contents_num]:
    st.markdown(f"### {Contents_num+1}.　{Contents_list[Contents_num]}")
    """
    #### 目標点：60~70％
    """
    #---
    """ 
    ① 図示された積分量域を数式で表現できる．
    """
    key_str = str(f"{Contents_num+1}_{Section_num}")
    col_Q = st.columns([1,30,30])
    with col_Q[1]:
        Selected_cb_bool = st.checkbox("例の表示",key = key_str)
    with col_Q[2]:
        Selected_radio_str = st.radio("難易度",("Lv.1","Lv.2","Lv.3"),horizontal=True)
    if Selected_cb_bool :
        col = st.columns([1,30,30])
        if Selected_radio_str  == "Lv.1":
            with col[1]:
                """
                **問　題**  
                次の図のように$y=2,\ x=2$，$~x~$軸，$~y~$軸で囲まれた領域を式で表しなさい．    
                """
                x, y = sym.symbols("x y")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                Graphs= sym.plot_implicit((0 <= x) & ( x <= 2) & ( 0 <= y) & ( y <= 3),(x,-1,3),(y,-2,4) , show=False, line_color="b")
                p1 = sym.plot_implicit( sym.Eq(x, 2),(x,-1,3),(y,-2,4), show=False, line_color="black")
                Graphs.extend(p1)
                p2 = sym.plot( 3 , show=False, line_color="black")
                Graphs.extend(p2)
                st.pyplot(Graphs.show())
            with col[2]:
                """                
                **解答例**  
                $$
                    D : 0 \\le x \\le 2,\ 0 \\le y \\le 3
                $$
                """
        elif Selected_radio_str  == "Lv.2":
            with col[1]:
                """
                **問　題**  
                次の図のように$y=x,\ y=2x,\ x=1,\ x=3$で囲まれた領域を式で表しなさい．  
                """
                x, y = sym.symbols("x y")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                Graphs= sym.plot_implicit((1 <= x) & ( x <= 3) & ( x <= y) & ( y <= 2*x) , (x,-1,4),(y,-2,7),show=False, line_color="b")
                p1 = sym.plot_implicit( sym.Eq(x, 1) , (x,-1,4),(y,-2,7), show=False, line_color="black")
                Graphs.extend(p1)
                p1 = sym.plot_implicit( sym.Eq(x, 3) , (x,-1,4),(y,-2,7), show=False, line_color="black")
                Graphs.extend(p1)
                p2 = sym.plot( x , show=False, line_color="black")
                Graphs.extend(p2)
                p2 = sym.plot( 2*x, show=False, line_color="black")
                Graphs.extend(p2)
                st.pyplot(Graphs.show())
            with col[2]:
                """
                **解答例（$~x~$ベース）**  
                $$
                    D : 1 \\le x \\le 3,\ x \\le y \\le 2x
                $$  

                **別　解（$~y~$ベース）**  
                $$
                    D_1 : 1 \\le y \\le 2,\ 1 \\le x \\le 2
                $$  
                $$
                    D_2 : 2 \\le y \\le 3,\ \\frac{1}{2}y \\le x \\le y
                $$  
                $$
                    D_3 : 3 \\le y \\le 6,\ \\frac{1}{2}y \\le x \\le 3
                $$  

                別解も含めて理解できましたか？
                """
        elif Selected_radio_str  == "Lv.3":
            with col[1]:
                """
                **問　題**  
                次の図のように$y=x^2 - 1,\ x=2$，$~x~$軸で囲まれた領域を式で表しなさい．  
                """
                x, y = sym.symbols("x y")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                Graphs= sym.plot_implicit((  y >= x**2-1 ) & ( 0 <=x ) & ( x <= 1 ) & (y <= 0), (x,-1,3),(y,-2,4),show=False, line_color="b")
                p1 = sym.plot_implicit( ( y <= x**2-1 ) & ( 0<=y) & ( 1 <= x ) & ( x<= 2 ), (x,-1,3),(y,-2,4), show=False, line_color="b")
                Graphs.extend(p1)

                p1 = sym.plot_implicit( sym.Eq(x, 1) , (x,-1,3),(y,-2,4), show=False, line_color="black")
                Graphs.extend(p1)
                p1 = sym.plot_implicit( sym.Eq(x, 2) , (x,-1,3),(y,-2,4), show=False, line_color="black")
                Graphs.extend(p1)
                p1 = sym.plot_implicit( sym.Eq(x**2-1,y) , (x,-1,3),(y,-2,4), show=False, line_color="black")
                Graphs.extend(p1)
                st.pyplot(Graphs.show())
            with col[2]:
                """
                **解答例（$~x~$ベース）**   
                $$
                    D_1 : 0 \\le x \\le 1,\ x^2-1 \\le y \\le 0 
                $$  
                $$
                    D_2 : 1 \\le x \\le 2,\ 0 \\le y \\le x^2-1 
                $$  

                **解答例（$~y~$ベース）**   
                $$
                    D_1 : -1 \\le y \\le 0,\ 0 \\le x \\le \\sqrt{y+1}
                $$  
                $$
                    D_2 :  0 \\le y \\le 3,\ \\sqrt{y+1} \\le x \\le 2
                $$  
                別解も含めて理解できましたか？
                """

    """ """;""" """
    #--- 
    """
    ② 面積を求めるための式を示すことができる．
    """
    Section_num +=1
    key_cb_str = str(f"{Contents_num+1}_{Section_num}_cd")
    key_rd_str = str(f"{Contents_num+1}_{Section_num}_rd")
    col_Q = st.columns([1,30,30])
    with col_Q[1]:
        Selected_cb_bool = st.checkbox("例の表示",key = key_cb_str)
    with col_Q[2]:
        Selected_radio_str = st.radio("難易度",("Lv.1","Lv.2","Lv.3"),horizontal=True,key = key_rd_str)
    if Selected_cb_bool :
        col = st.columns([1,30,30])
        if Selected_radio_str  == "Lv.1":
            with col[1]:
                """
                **問　題**  
                区間$\\big[0,\ 1\\big]$において，$~y=x^2~$と$~x~$で囲まれた領域の面積を求める式を書きなさい．   
                """
                x, y = sym.symbols("x y")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                Graphs= sym.plot_implicit(( 0 <= y ) & (y <= x**2) & ( 0<= x )&(x<= 1),(x,-1,1.5),(y,-1,1.5), show=False, line_color="b")
                p1 = sym.plot_implicit( sym.Eq(x, 1),(x,-1,1.5),(y,-1,1.5), show=False, line_color="black")
                Graphs.extend(p1)
                p1 = sym.plot_implicit( sym.Eq(x**2, y),(x,-1,1.5),(y,-1,1.5), show=False, line_color="black")
                Graphs.extend(p1)
                st.pyplot(Graphs.show())
            with col[2]:
                """                
                **解答例**  
                $$
                    \\int_{0}^{1} 
                        x^2
                    \\,
                    dx
                $$
                **別解１**  
                $$
                    \\int_{0}^{1} 
                        \\Big| x^2 - 0\\Big|
                    \\,
                    dx
                $$
                **別解２**  
                $$
                    \\int_{x=0}^{x=1} 
                    \\int_{y=0}^{y=x^2}
                    \\,
                    dxdy
                $$
                """
        elif Selected_radio_str  == "Lv.2":
            with col[1]:
                """
                **問　題**  
                $~y=x^2~$と$y=x$で囲まれた領域の面積を求める式を書きなさい．   
                """
                x, y = sym.symbols("x y")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                Graphs= sym.plot_implicit((x**2 <= y) & ( y <= x),(x,-1,1.5),(y,-1,1.5), show=False, line_color="b")
                p1 = sym.plot_implicit( sym.Eq(x, 1),(x,-1,1.5),(y,-1,1.5), show=False, line_color="black")
                Graphs.extend(p1)
                p1 = sym.plot_implicit( sym.Eq(x**2, y),(x,-1,1.5),(y,-1,1.5), show=False, line_color="black")
                Graphs.extend(p1)
                p1 = sym.plot_implicit( sym.Eq(x, y),(x,-1,1.5),(y,-1,1.5), show=False, line_color="black")
                Graphs.extend(p1)
                st.pyplot(Graphs.show())
            with col[2]:
                """                
                **解答例**  
                $$
                    \\int_{0}^{1} 
                        \\Big( x - x^2\\Big)
                    \\,
                    dx
                $$
                **別解１**  
                $$
                    \\int_{0}^{1} 
                        \\Big| x - x^2\\Big|
                    \\,
                    dx
                    \\ \\ {\\rm or} \\ \\ 
                    \\int_{0}^{1} 
                        \\Big| x^2 - x\\Big|
                    \\,
                    dx
                $$
                **別解２**  
                $$
                    \\int_{x=0}^{x=1} 
                    \\int_{y=x^2}^{y=x}
                    \\,
                    dxdy
                $$
                """
        elif Selected_radio_str  == "Lv.3":
            with col[1]:
                """
                **問　題**  
                $~y=x^3 - 3x^2 +3x~$と$y=x$で囲まれた領域の面積を求める式を書きなさい．   
                """
                x, y = sym.symbols("x y")
                st.set_option('deprecation.showPyplotGlobalUse', False)
                Graphs= sym.plot_implicit( ( y <= x**3 - 3*x**2 +3*x ) & ( x <= y) & ( 0 <= x)  & ( x <= 1),(x,-0.5,2.5),(y,-0.5,3), show=False, line_color="b")
                p1 = sym.plot_implicit( sym.Eq(x, y),(x,-0.5,2.5),(y,-0.5,3), show=False, line_color="black")
                Graphs.extend(p1)           
                p1 = sym.plot_implicit( ( y <= x ) & ( x**3 - 3*x**2 +3*x <= y ) & ( 1 <= x)  & ( x <= 2),(x,-0.5,2.5),(y,-0.5,3), show=False, line_color="b")
                Graphs.extend(p1)
                p1 = sym.plot_implicit( sym.Eq(x**3 - 3*x**2 +3*x, y),(x,-0.5,2.5),(y,-0.5,3), show=False, line_color="black")
                Graphs.extend(p1)
                st.pyplot(Graphs.show())
            with col[2]:
                """                
                **解答例**  
                $$
                    \\int_{0}^{1} 
                        \\Big\\{ \\big( x^3 - 3x^2 +3x\\big) - x\\Big\\}
                    \\,
                    dx
                    +
                    \\int_{1}^{2} 
                        \\Big\\{ x - \\big( x^3 - 3x^2 +3x\\big) \\Big\\}
                    \\,
                    dx
                $$
                **別解１**  
                $$
                    \\int_{0}^{2} 
                        \\Big|  \\big( x^3 - 3x^2 +3x\\big) - x \\Big|
                    \\,
                    dx
                    \\ \\ {\\rm or} \\ \\ 
                    \\int_{0}^{2} 
                        \\Big|  x - \\big( x^3 - 3x^2 +3x\\big) \\Big|
                    \\,
                    dx
                $$
                **別解２**  
                $$
                    \\int_{x=0}^{x=1} 
                    \\int_{y=x}^{y=x^3 - 3x^2 +3x}
                    \\,
                    dxdy
                    +
                    \\int_{x=1}^{x=2} 
                    \\int_{y=x^3 - 3x^2 +3x}^{y=x}
                    \\,
                    dxdy
                $$
                """

    """
    ③ 体積を求めるための式を示すことができる．
    """
    """
    ④ 重心を求めるための式を示すことができる．
    """



### 2nd contents
Section_num = 0
Contents_num += 1
with Contents_tab [Contents_num]:
    st.markdown(f"### {Contents_num+1}.　{Contents_list[Contents_num]}")
    ## section 1
    Section_num += 1
    st.markdown(f"#### {Contents_num+1}-{Section_num}：領域の表し方")

### 3rd contents
Section_num = 0
Contents_num += 1
with Contents_tab [Contents_num]:
    st.markdown(f"### {Contents_num+1}.　{Contents_list[Contents_num]}")

### 4th contents
Section_num = 0
Contents_num += 1
with Contents_tab [Contents_num]:
    st.markdown(f"### {Contents_num+1}.　{Contents_list[Contents_num]}")

### 5th contents
Section_num = 0
Contents_num += 1
with Contents_tab [Contents_num]:
    st.markdown(f"### {Contents_num+1}.　{Contents_list[Contents_num]}")