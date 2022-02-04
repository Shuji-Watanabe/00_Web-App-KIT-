import streamlit as st
import pandas as pd
from sympy import *
from sympy.simplify.sqrtdenest import sqrtdenest
import numpy as np
from matplotlib import pyplot as plt
from sympy.utilities.lambdify import lambdify
from PIL import Image
#from sympy.abc import _clash1, _clash2 
init_printing()

def pitonegapi(rad00):
    if rad00 >= pi:
        rad01 = rad00 - 2*pi
    elif rad00 <= -pi:
        rad01 = 2*pi + rad00
    else :
        rad01 = rad00
    return rad01

def converttotex(Str00):
    Str00=str(Str00).replace("(","{")
    Str00=str(Str00).replace(")","}")
    Str00=str(Str00).replace("*","\\cdot ")
    return Str00

def sympy_extractsymbols(str00):
    str00 = str00.replace("**","^")
    tmp_str00 = str00.split("*")
    str00_Val01=[]

    if isinstance(sympify(str00),Float) or isinstance(sympify(str00),Integer):
        str00 = sympify(str00)
    else:
        for i in range(len(tmp_str00)):
            if isinstance(sympify(tmp_str00[i]),Symbol):
                str00_Val01.append(sympify(tmp_str00[i])) 
    return str00_Val01

#################### begin main program ##############
st.markdown("##### 単振動(ばね振り子の運動)")
st.markdown("""
    ##### 状況設定
    ばね定数 $k\\rm \ [N/m]$ の軽いばねを，水平で滑らかな床の上に置いた．ばねの一端を壁に取り付け，
    もう一端に質量 $m \\rm\  [kg]$ の小物体を取り付ける．水平右向きを $x$ 軸方向とし，ばねが自然長で
    小物体が静止する位置を原点$\\rm O$ とする．小物体が運動を開始した時刻を $t=0 \\rm\ s$ とするとき，
    時刻 $t \\rm\ [s]$ における小物体の運動の様子を考察する．
""")
IMAGE_URL = 'https://github.com/Shuji-Watanabe/00_Web-App-KIT-/03_TEST/fig01.jpg'
st.image(IMAGE_URL,caption='ある時刻における小物体の様子')

tmp_CB01=st.sidebar.checkbox("ばね振り子の質量，ばね定数，初期条件を変更")
if tmp_CB01 :
    col01,col02,col03,col04 = st.columns(4)
    with col01:
        Mass = st.text_input("質量","m")
    with col02:
        Sp_const = st.text_input(latex(r"バネ定数"),"k")
    with col03:
        x_ini = st.text_input("初期位置","x_0")
    with col04:
        v_ini = st.text_input("初速度","v_0")
else:
    Mass = "m"
    Sp_const = "k"
    x_ini = "x_0"
    v_ini = "v_0"

Mass_val = sympy_extractsymbols(Mass)
if len(Mass_val) == 0:
    Mass = sympify(Mass)
elif len(Mass_val) == 1 :
    Mass_val = Symbol(str(Mass_val[0]),real=True,positive=True)
    Mass = sympify(Mass)
elif len(Mass_val) >=2 :
    st.error("質量に入力できるパラメーターを意味する文字は１文字までです．")

Sp_const_val = sympy_extractsymbols(Sp_const)
if len(Sp_const_val) == 0:
    Sp_const = sympify(Sp_const)
elif len(Sp_const_val) == 1 :
    Sp_const_var = Symbol(str(Sp_const_val[0]),real=True,positive=True)
    Sp_const = sympify(Sp_const)
elif len(Sp_const_val) >= 2 :
    st.error("バネ定数に入力できるパラメーターを意味する文字は１文字までです．")

x_ini_val = sympy_extractsymbols(x_ini)
if len(x_ini_val) == 0:
    x_ini = sympify(x_ini)
elif len(x_ini_val) == 1 :
    x_ini_val = Symbol(str(x_ini_val[0]),positive = True)
    x_ini = sympify(x_ini)
elif len(x_ini_val) >= 2 :
    st.error("初期位置に入力できるパラメーターを意味する文字は１文字までです．")

v_ini_val = sympy_extractsymbols(v_ini)
if len(v_ini_val) == 0:
    v_ini = sympify(v_ini)
elif len(v_ini_val) == 1 :
    v_ini_val = Symbol(str(v_ini_val[0]),positive=True)
    v_ini = sympify(v_ini)
elif len(x_ini_val) >= 2 :
    st.write("初速度に入力できるパラメーターを意味する文字は１文字までです．")




##### Step 01 
st.markdown("##### ▷ Step 1：バネに繋がれた小物体の運動方程式")
STR1_01 = "%s \\cdot \\frac{d^2 x}{dt^2} = -%s \\cdot x"%(converttotex(Mass),converttotex(Sp_const))
CB_Step01_1 = st.sidebar.checkbox("運動方程式を表示")
if CB_Step01_1 :
    st.latex(STR1_01)





##### Step 02
st.markdown("##### ▷ step 2：特性方程式")
CB_Step01_2 = st.sidebar.checkbox("特性方程式とその解を表示")


lambda_0 = Symbol(r"\lambda")
lambda_0 = symbols('lambda_0')
omega = Symbol(r"\omega")
omega = symbols('omega', positive=True)

omega_0 = simplify(sympify(Mass)/sympify(Sp_const))
eq01 = lambda_0**2 + omega**2
Ans01 = solve( Eq(0,sympify(eq01)),lambda_0)

if CB_Step01_2 : 
    STR1_02 = " \\lambda^2 + \\frac{%s}{%s} = 0"%(converttotex(Sp_const),converttotex(Mass))
    st.latex(STR1_02)
    if len(Ans01) == 2:
        st.latex( r"\lambda_1 = %s, \ \lambda_2 = %s,\ \omega = \sqrt{%s}"\
            %(latex(Ans01[0]),latex(Ans01[1]),latex(omega_0)))

##### Step 03
st.markdown("##### ▷ Step 3：微分方程式の一般解")
CB_Step03_1 = st.sidebar.checkbox("一般解を表示")
if CB_Step03_1 :
    st.latex(r"x(t)= A\cos \big(  \omega t +  \phi \big) = A\cos \left(  %s t +  \phi\right)"%(latex(omega_0)))
    if st.checkbox("一般解を求める過程を表示"):
        """
        　　- 特製方程式が２つの複素数解 $\lambda_1=-i\omega,\ \lambda_2=i\omega$ を持つことから，求める$x(t)$の一般解は次のようになる．
        """
        st.latex( "x(t)=c_1 e^{-i\omega t} + c_2e^{i \omega t}" )

        """
        　　- さらに
            [オイラーの公式](https://w3e.kanazawa-it.ac.jp/math/category/fukusosuu/henkan-tex.cgi?target=/math/category/fukusosuu/euler-no-kousiki.html)
        より\n
        　　$x(t) = c_1 e^{-i\omega t} + c_2e^{i \omega t}$\n
        　　$\\phantom{x(t)} = c_1 \cos \omega t + i c_1 \sin \omega t + c_2 \cos (-\omega t ) + i c_2 \sin(-\omega t)$\n
        　　$\\phantom{x(t)} = \\big( c_1 + c_2 \\big) \cos \omega t + i\\big(c_1 - c_2\\big) \sin (-\omega t)$\n
        　　$\\phantom{x(t)} = C_1 \cos \omega t + C_2 \sin \omega t$\n
        　　$\\displaystyle \\phantom{x(t)} = \\sqrt{C_1^2 + C_2^2}\\bigg( \\frac{C_1}{\\sqrt{C_1^2 + C_2^2} } \cos \omega t + \\frac{C_2}{\\sqrt{C_1^2 + C_2^2} } \sin \omega t \\bigg)$\n
        　　$\\displaystyle \\phantom{x(t)} = A\\Big( \cos \phi\cos \omega t + \sin \phi \sin \omega t \\Big)$\n
        　　$\\displaystyle \\phantom{x(t)} = A\cos\\big( \phi + \omega t  \\big)$\n
        　　$\\displaystyle \\phantom{x(t)} = A\cos\\big(  \omega t +  \phi\\big)$\n
        """




##### Step 04
title_step4 = r"##### ▷ Step 4：微分方程式の初期条件 $x(0) = %s,\ v(0) = %s$ を満たす特殊解"%( converttotex(x_ini),converttotex(v_ini))
st.markdown(title_step4)
phi = Symbol(r"\phi", real = True)
A , v, t , phi= symbols('A v t phi', real = True)
x_t , v_t= symbols('x_t v_t', cls=Function)
x_t = A * cos( omega * t + phi)
v_t = diff(x_t,t)

Ans_A = sqrt( sympify(x_ini)**2 + sympify(v_ini)**2/omega**2 )   

# set_Ans_Eqx = acos( powdenest(x_ini/Ans_A,force =True) )
# set_Ans_Eqv = asin(-powdenest(v_ini/(Ans_A*omega),force =True) )

Ans_A_1 = Ans_A.subs(omega,sqrt(omega_0))
Eqx = Eq(cos(phi), x_ini/Ans_A_1)
set_Ans_Eqx = solve( Eqx,phi) 
Eqv = Eq(sin(phi), -v_ini/(Ans_A_1 * sqrt(omega_0)))
set_Ans_Eqv = solve( Eqv,phi )



for i in range(len(set_Ans_Eqx)):
    try:
        pitonegapi(set_Ans_Eqx[i])
    except:
        set_Ans_Eqx[i] = simplify( set_Ans_Eqx[i] )
    else:
        set_Ans_Eqx[i] = simplify( pitonegapi(set_Ans_Eqx[i]))


for i in range(len(set_Ans_Eqv)):
    try:
        pitonegapi(set_Ans_Eqv[i])
    except:
        set_Ans_Eqv[i] = simplify( set_Ans_Eqv[i] )
    else:
        set_Ans_Eqv[i] = simplify( pitonegapi(set_Ans_Eqv[i]))

Ans_phi = set( set_Ans_Eqx ) & set( set_Ans_Eqv )
if len(Ans_phi) == 0 :
    Ans_phi = phi
else :
    Ans_phi = list(Ans_phi)[0]

theta = omega * t + Ans_phi

CB_Step04_1 = st.sidebar.checkbox("特殊解を表示")
if CB_Step04_1 :
    Ans_A = Ans_A.subs(omega,sqrt(omega_0))
    theta = theta.subs(omega,sqrt(omega_0))
    st.latex(r"x(t) = %s \cdot \cos\left( %s \right)"%(latex( simplify(Ans_A)),latex(theta )) )
    if Ans_phi == phi:
        st.markdown("$\\phi$ は，$\\displaystyle \\cos \\phi = %s$ かつ $\\displaystyle \\sin \\phi = %s$ を満たす $-\\pi < \\phi \\le \\pi$ の角度である．"\
            %(latex( simplify( sympify(x_ini)/Ans_A)) ,latex( simplify(sympify(v_ini)/(Ans_A*sqrt(omega_0))) ))
            )
    if st.checkbox("特殊解を得るまでの途中計算を表示(一般的な初期条件に対する特殊解の求め方)"):
        st.markdown("""\
            - ある時刻における小物体の位置と速度は，それぞれ次式で与えられる．\n\n\
            　　$x(t) = %s$\n\n\
            　　$v(t) = %s$\n\n\
            - また初期条件を $x(0) = x_0,\ v(0) = v_0$ とする．
        """%(latex(x_t),latex(v_t)))
        st.markdown("""\
            - 位置および速度に対する初期条件より，次式が得られる．\n\n\
            　　$\\displaystyle x_0 = A \cos \phi \ \\to\ A \cos \phi = x_0$，\
            　　$\\displaystyle v_0 = -A \omega \sin \phi \ \\to\ A \sin \phi = -\\frac{v_0}{\omega}$\n\n\
            - これにより $A\ (A \\ge 0)$ が，次のように得られる．\n\n\
            　　$\\displaystyle \\big(A\cos \phi \\big)^2 + \\big(A\sin \phi \\big)^2 = x_0^2 + \\left( -\\frac{v_0}{\\omega}\\right)^2$\n\n\
            　　$\\displaystyle A^2= x_0^2 + \\left( \\frac{v_0}{\\omega}\\right)^2$\n\n\
            　　$\\displaystyle A= \\sqrt{x_0^2 + \\frac{v_0^2}{\\omega^2}} = \\frac{\\sqrt{\omega^2 x_0^2 + v_0^2}}{\\omega}$\n\n\
            """)
        st.markdown("""\
            - よって，$\phi\ (-\\pi < \\phi \\le \\pi)$ は得られた $A$ を用いて，次の関係を満たす角として得られる．\n\n\
            　　$\\displaystyle \cos\phi = \\frac{x_0}{A}$，かつ　$\\displaystyle \sin\phi = -\\frac{v_0}{A\\omega}$\
            """)




##### Step 05
st.markdown("##### ▷ Step 5：角振動数と周期")
CB_Step05_1 = st.sidebar.checkbox("角振動数と周期を表示")
if CB_Step05_1 :
    T = 2*pi/sqrt(omega_0)
    st.latex(r"\displaystyle \text{角振動数：} \omega = %s，\text{周期：}  T = \frac{2\pi}{\omega} = %s"%( latex(sqrt(omega_0)),latex(T) ))




##### Step 06
st.markdown("##### ▷ Step 6：特殊解のグラフ")
CB_Step06_1 = st.sidebar.checkbox("特殊解のグラフを表示")
if CB_Step06_1 :
    try:
        function0 = Ans_A_1 * cos( sqrt(omega_0) * t + Ans_phi)
        ts = np.linspace( 0, 10, 1)
        ys = lambdify(t, function0, "numpy")(ts)
        
    except:
        st.error("エラー：質量，ばね定数，初期位置，初速度を数値で指定してください．")
        st.error("この図は $\\displaystyle A = 1.0,\ \\omega = \\frac{2\\pi}{10} ,\ \\phi = 0$の図です．")
        function0 = cos( pi/5 * t )
        col2_01,col2_02=st.columns([3,1]) 
        with col2_02:
            xrange_min = st.number_input("▷ xの最小値",value=0,key=2)            
            xrange_max = st.number_input("▷ xの最大値",value=10,key=2)
        with col2_01:
            ts = np.linspace( xrange_min, xrange_max, 100)
            ys = lambdify(t, function0, "numpy")(ts)
            fig, ax = plt.subplots()
            plt.xlabel("$t$軸")
            plt.ylabel("$x$軸")
            ax.plot(ts, ys)
            ax.grid()
            st.pyplot(fig)
    else:
        col2_01,col2_02=st.columns([3,1]) 
        with col2_02:
            xrange_min = st.number_input("▷ xの最小値",value=0,key=1)            
            xrange_max = st.number_input("▷ xの最大値",value=10,key=1)
        with col2_01:
            ts = np.linspace( xrange_min, xrange_max, 100)
            ys = lambdify(t, function0, "numpy")(ts)
            fig, ax = plt.subplots()
            plt.xlabel("$t$軸")
            plt.ylabel("$x$軸")
            ax.plot(ts, ys)
            ax.grid()
            st.pyplot(fig)
        
end1_01 ="<div style= \"text-align: right;\"> "
end1_01+=" --アプリEnd--"
end1_01+=" </div>"
st.markdown(end1_01,unsafe_allow_html=True)