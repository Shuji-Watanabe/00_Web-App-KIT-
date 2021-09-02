import streamlit as st
from sympy import *
from sympy.solvers import solve

x= symbols('x'); F0, F1 ,F2= symbols('F0 F1 F2', cls=Function)

st.title("""関数の極大点，極小点，変曲点""")
#st.latex('\\frac{1}{2}mx^2')

FORM_INPUT = st.sidebar.text_input('極大点，極小点，変曲点を調べたい関数を入力')
R01_check=st.sidebar.checkbox('1次導関数の計算結果')
R01_1_check=st.sidebar.checkbox('1次導関数の計算結果（展開版）')
R02_check=st.sidebar.checkbox('2次導関数の計算結果')

F0 = sympify(FORM_INPUT)
F1 = simplify(diff(F0))
F1_Expand = expand(simplify(diff(F0)))
F2 = simplify(diff(F1))
F3 = simplify(diff(F2))
F4 = simplify(diff(F3))

"""
\nこのWebアプリは現在開発中のものであり，練習のために作成しています．
間違いがあってもそっとしておいてください．僕をいじめないでください．
今僕は頑張っているんです．アドバイスは優しく丁寧にお願いします．
"""
st.write('$f(x)\\,$の１次導関数は次の通りです．')
if (R01_check == 1) :
    st.latex(F1)
if (R01_1_check == 1) :
    st.latex(F1_Expand)

st.write('$f(x)\\,$の２次導関数は次の通りです．')
if (R02_check == 1) :
    st.latex(F2)


lcolumn, rcolumn=st.columns(2)
lcolumn.write('入力された関数$\\,f(x)$')
lcolumn.latex(F0)

lcolumn.write('$f(x)\\,$の3次導関数')
lcolumn.latex(F3)


lcolumn.write('$f(x)\\,$の4次導関数')
lcolumn.latex(F4)



