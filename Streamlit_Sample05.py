import streamlit as st
from sympy import *
from sympy.solvers import solve

init_printing()

x= symbols('x'); F0, F1 ,F2= symbols('F0 F1 F2', cls=Function)

st.title("""関数の極大点，極小点，変曲点""")
#st.latex('\\frac{1}{2}mx^2')

FORM_INPUT = st.sidebar.text_input('極大点，極小点，変曲点を調べたい関数を入力')



if not FORM_INPUT:
    st.write("数式をサイドバーに入力してください．")
else :
    F0 = sympify(FORM_INPUT)
    F1 = diff(F0)
    F1_Expand = expand(simplify(diff(F0)))
    F2 = simplify(diff(F1))
    F3 = simplify(diff(F2))
    X0 = solve(Eq(0,sympify(F1)),x)
    X00 = solve(Eq(0,F2),x)
    st.write('入力された関数は次の通りです．')
    st.latex(F0)
    """サイドバーの解答をみたい項目にチェックを入れてください．"""

    st.write('\
        ### **\[Step1：1次導関数および2次導関数の計算\]**\
        ',unsafe_allow_html=True)
        ### <span style="color:yellow"> \[Step1：1次導関数および2次導関数の計算\]</span>

    R01_check=st.sidebar.checkbox('1次導関数の計算結果')
    if (R01_check == 1) :
        st.write('▶︎ $f(x)\\,$の１次導関数は次の通りです．')
        st.write('導関数の求め方，微分の方法に関する説明は[こちらから](https://w3e.kanazawa-it.ac.jp/math/category/bibun/henkan-tex.cgi?target=/math/category/bibun/index.html)')
        st.latex(F1)

    R02_check=st.sidebar.checkbox('2次導関数の計算結果')
    if (R02_check == 1) :
        st.write('▶︎ $f(x)\\,$の２次導関数は次の通りです．')
        st.write('導関数の求め方，微分の方法に関する説明は[こちらから](https://w3e.kanazawa-it.ac.jp/math/category/bibun/henkan-tex.cgi?target=/math/category/bibun/index.html)')
        st.latex(F2)

    st.write('\
        ### **\[Step2：$f^\prime(x)=0$, $f^{\prime\prime}(x)=0$の解\]**'\
        ,unsafe_allow_html=True)
        #<span style="color:yellow"> \[Step2：$f^\prime(x)=0$, $f^{\prime\prime}(x)=0$の解\]</span>'

    Sol01=st.sidebar.checkbox('f\'(x)=0の解')
    if (Sol01 == 1) :
        try:
            X0 = solve(
                        Eq(0,F1),x
                        )
        except:
            st.write(' $f^\prime(x)=0$ の解なし')
        else:
            st.write('▶︎ $f^\prime(x)=0$ の解は次の通りです．')
            PRINT_STR1=" "
            for i in range(len(X0)) :
                PRINT_STR1=PRINT_STR1+"""x_"""+latex(i+1)+"""="""+latex(X0[i-1])
                if (i < len(X0)-1 ):
                    PRINT_STR1=PRINT_STR1+""",\quad """
        st.latex(PRINT_STR1)
    Sol02=st.sidebar.checkbox('f\'\'(x)=0の解')
    if (Sol02 == 1) :
        try:
            X00 = solve(
                        Eq(0,sympify(F2)),x
                        )
        except:
            st.write(' $f^{\prime\prime}(x)=0$ の解なし')
        else:
            st.write('▶︎ $f^{\prime\prime}(x)=0$ の解は次の通りです．')
            PRINT_STR1=" "
            for i in range(len(X00)) :
                PRINT_STR1=PRINT_STR1+"""x_"""+latex(i+1)+"""="""+latex(X00[i-1])
                if (i < len(X00)-1 ):
                    PRINT_STR1=PRINT_STR1+""",\quad """
        st.latex(PRINT_STR1)

    st.write('\
        ### **\[Step3：極大点，極小点，変曲点の座標\]**',\
        unsafe_allow_html=True)  
        ### <span style="color:yellow"> \[Step3：極大点，極小点，変曲点の判定\]</span>'
    MaxMimi_P=st.sidebar.checkbox('極大点，極小点の座標')
    if (MaxMimi_P == 1) :
        j=0
        k=0
        st.write('▶︎ 極大点，極小点：極大点，極小点に関する説明は[こちらから](https://w3e.kanazawa-it.ac.jp/math/category/bibun/henkan-tex.cgi?target=/math/category/bibun/kyokuti.html)')
        for i in range(len(X0)):
            try:
                aa=F2.subs(x,X0[i-1])
            except:
                st.write('　極大点または極小点であるかの判定不能')
            else:
                STR_PRINT=''
                STR_PRINT=STR_PRINT+"$\\left("+latex(X0[i-1])+",\ "+latex(F0.subs(x,X0[i-1]))
                STR_PRINT=STR_PRINT+"\\right)$"
                if (aa < 0 ):
                    j=j+1
                    st.write('$\quad$　極大点',latex(j),":",STR_PRINT)
                elif (aa > 0):
                    k=k+1
                    st.write('$\quad$　極小点',latex(k),":",STR_PRINT)
        
    Inflection_P=st.sidebar.checkbox('変曲点の座標')
    if (Inflection_P == 1) :
        st.write('▶︎ 変曲点：変曲点に関する説明は[こちらから](https://w3e.kanazawa-it.ac.jp/math/category/bibun/henkan-tex.cgi?target=/math/category/bibun/inflection_point.html)')
        l=0
        for i in range(len(X00)):
            try:
                aa=F3.subs(x,X00[i-1])
                
            except:
                st.write(' 変曲点であるかどうかの判定不能')
            else:
                STR_PRINT=''
                STR_PRINT=STR_PRINT+"$\\left("+latex(X00[i-1])+",\ "+latex(F0.subs(x,X00[i-1]))
                STR_PRINT=STR_PRINT+"\\right)$"
                if (aa < 0 or aa >0):
                    l=l+1
                    st.write('$\quad$　変曲点',latex(l),":",STR_PRINT)