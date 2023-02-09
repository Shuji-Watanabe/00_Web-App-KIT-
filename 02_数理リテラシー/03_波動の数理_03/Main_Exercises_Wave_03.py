import streamlit as st
import pandas as pd
from sympy import *
from sympy.simplify.sqrtdenest import sqrtdenest
from sympy import pi as sym_pi
import numpy as np
from matplotlib import pyplot as plt
from sympy.utilities.lambdify import lambdify

init_printing(order='grevlex')
init_printing(order='none')



def check_real(var_list):
    index = 0
    for var in var_list:
        if var.is_real :
            index += 1
        if index == 0: 
            return 0
        else:
            return 1 

def check_str(var_list):
    List_Integer = ["sympy.core.numbers.Zero","sympy.core.numbers.One","sympy.core.numbers.Integer"]
    List_Float = ["sympy.core.numbers.Float"]
    index = 1
    for var in var_list:
        # st.write(type(var),type(var) == type(simplify(1.0)))
        if type(var) == type(simplify(1.0)):
            return 0
        else:
            return 1

def check_float(var_list):
    List_Float = ["sympy.core.numbers.Float"]
    index = 1
    for var in var_list:
        # st.write(type(var),type(var) == type(simplify(1.0)))
        if type(var) == type(simplify(1.0)):
            return 0
        else:
            return 1
    
def check_vars(var_list):
    for var in var_list:
        try:
            var = float(var)
        except:
            return 0
        if not isinstance(var, (float, int)):
            return 0
    return 1

def pitonegapi(rad00):
    from sympy import pi as sym_pi
    if (rad00-sym_pi).evalf() >= 0 :
        rad01 = rad00 - 2*sym_pi
    elif (rad00+sym_pi).evalf() < 0:
        rad01 = rad00 + 2*sym_pi
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
        str00 = str00
    else:
        for i in range(len(tmp_str00)):
            if isinstance(sympify(tmp_str00[i]),Symbol):
                str00_Val01.append(tmp_str00[i]) 
    return str00_Val01

#################### begin main program ##############
st.markdown("##### 単振動(ばね振り子の運動)")
Q_col,Fig_col = st.columns([7,4])
with Q_col:
    """
    ##### 状況設定
    ばね定数 $k\\rm \ [N/m]$ の軽いばねを，水平で滑らかな床の上に置いた．ばねの一端を壁に取り付け，
    もう一端に質量 $m \\rm\  [kg]$ の小物体を取り付ける．水平右向きを $x$ 軸方向とし，ばねが自然長で
    小物体が静止する位置を原点$\\rm O$ とする．小物体が運動を開始した時刻を $t=0 \\rm\ s$ とするとき，
    時刻$\ t=0\ $における小物体の位置（初期位置）を$\ x_0 \ \\rm[m]\ $，
    小物体の速度（初速度）を$\ v_0 \ \\rm[m]\ $として
    時刻 $t \\rm\ [s]$ における小物体の運動の様子を考察する．
    """
with Fig_col:
    """
    $\\phantom{A}$  
    $\\phantom{A}$  

    """
    try:
        image = '単振動01.jpg'
        st.image(image,caption="ばねと質点の様子",use_column_width='auto')
    except:
        image = '02_数理リテラシー/03_波動の数理_03/単振動01.jpg'
        st.image(image,caption="ばねと小物体の様子",use_column_width='auto')

st.sidebar.markdown("#### **条件変更**")
if st.sidebar.checkbox("ばね振り子の質量，ばね定数，初期条件を変更") :
    col01,col02,col03,col04,col05 = st.columns(5)
    with col01:
        Mass = st.text_input("質量","m")
    with col02:
        Sp_const = st.text_input("バネ定数","k")
    with col03:
        x_ini = st.text_input("初期位置","x_0")
    with col04:
        v_ini = st.text_input("初速度","v_0")
    with col05:
        Significant_digits = st.number_input("有効桁数",value = 3,step=1,min_value=0)
        format_str= f"{{:.{Significant_digits}f}}"
    
    with st.expander("条件の変更方法"):
        """
        ばね振り子の質量，ばね定数，初期位置，初速度を変更することができます．
        数値を入力しても良いですし，文字で指定しても良いです．  
        - **整数で指定する場合**  
          x_0 を整数で指定したい場合， 2 や -3 としてください．  
        - **小数で指定する場合**  
          x_0 を整数で指定したい場合， 2.0 や -3.0 としてください．
          小数で指定した場合，有効桁数を考察し，適切な値に変えてください．  
        - **文字で指定する場合**  
          x_0 を2倍，-3倍にしたい場合は， x_0 の部分を 2\*x_0 や -3\*x_0 としてください．
          半角のアスタリスク( \* )は，かけるという意味です．
          また x_0+2\*x のように変数や項が2つ以上の場合エラーが出ますのでご注意ください．  
          $\\phantom{a}$

        """
else:
    Mass = "m"
    Sp_const = "k"
    x_ini = "x_0"
    v_ini = "v_0"

Mass_val = sympy_extractsymbols(Mass)
if len(Mass_val) == 0:
    Mass = sympify(Mass)
elif len(Mass_val) == 1 :
    tmp_Mass_symbol = symbols(str(Mass_val[0]))
    tmp_Mass_coeff  = sympify(Mass).as_coefficient(tmp_Mass_symbol)
    tmp_Mass_symbol = symbols(str(Mass_val[0]),real=True,positive=True)
    Mass = tmp_Mass_coeff*tmp_Mass_symbol
elif len(Mass_val) >=2 :
    st.error("パラメーターを表す文字は１文字にしてください．")
    st.stop()

# st.write(Mass)
# st.stop()

Sp_const_val = sympy_extractsymbols(Sp_const)
if len(Sp_const_val) == 0:
    Sp_const = sympify(Sp_const)
elif len(Sp_const_val) == 1 :
    tmp_Sp_const_symbol = symbols(str(Sp_const_val[0]))
    tmp_Sp_const_coeff  = sympify(Sp_const).as_coefficient(tmp_Sp_const_symbol)
    tmp_Sp_const_symbol = symbols(str(Sp_const_val[0]),real=True,positive=True)
    Sp_const = tmp_Sp_const_coeff*tmp_Sp_const_symbol
elif len(Sp_const_val) >= 2 :
    st.error("パラメーターを表す文字は１文字にしてください．")
    st.stop()

x_ini_val = sympy_extractsymbols(x_ini)
if len(x_ini_val) == 0:
    x_ini = sympify(x_ini)
elif len(x_ini_val) == 1 :
    tmp_x_ini_symbol = symbols(str(x_ini_val[0]))
    tmp_x_ini_coeff  = sympify(x_ini).as_coefficient(tmp_x_ini_symbol)
    tmp_x_ini_symbol = symbols(str(x_ini_val[0]),real=True,positive=True)
    x_ini = tmp_x_ini_coeff*tmp_x_ini_symbol
elif len(x_ini_val) >= 2 :
    st.error("パラメーターを表す文字は１文字にしてください．")
    st.stop()

v_ini_val = sympy_extractsymbols(v_ini)
if len(v_ini_val) == 0:
    v_ini = sympify(v_ini)
elif len(v_ini_val) == 1 :
    tmp_v_ini_symbol = symbols(str(v_ini_val[0]))
    tmp_v_ini_coeff  = sympify(v_ini).as_coefficient(tmp_v_ini_symbol)
    tmp_v_ini_symbol = symbols(str(v_ini_val[0]),real=True,positive=True)
    v_ini = tmp_v_ini_coeff*tmp_v_ini_symbol
elif len(x_ini_val) >= 2 :
    st.write("初速度に入力できるパラメーターを意味する文字は１文字までです．")
# st.write(Mass_val,Sp_const_val,x_ini_val,v_ini_val)


##### Step 01 
st.markdown("##### ▷ Step 1：バネに繋がれた小物体の運動方程式")

if check_float([Mass]) == 0:
    Mass_disp = latex(Mass.evalf(Significant_digits))
else :
    Mass_disp = latex(Mass)
if check_float([Sp_const]) == 0:
    Sp_const_disp = latex(-1*Sp_const.evalf(Significant_digits))
else :
    Sp_const_disp = latex(-1*Sp_const)

st.sidebar.markdown("#### **各計算結果の表示**")
if st.sidebar.checkbox("運動方程式を表示") :
    STR1_01 = f"{Mass_disp} \\cdot \\frac{{d^2 x}}{{dt^2}} = {Sp_const_disp } \\cdot x"
    st.latex(STR1_01)


##### Step 02
st.markdown("##### ▷ step 2：特性方程式")
lambda_0 = Symbol(r"\lambda")
lambda_0 = symbols('lambda_0')
omega = Symbol(r"\omega")
omega = symbols('omega', positive=True)

omega_0 = sqrt( simplify(Sp_const/Mass))

if check_float([Mass,Sp_const]) == 0:
    omega_0_disp = latex(omega_0.evalf(Significant_digits))
else :
    omega_0_disp = latex(omega_0)
if check_float([Sp_const]) == 0:
    Sp_const_disp1_2 = latex(Sp_const.evalf(Significant_digits))
else :
    Sp_const_disp1_2 = latex(Sp_const)

if st.sidebar.checkbox("特性方程式とその解を表示") : 
    STR1_02 = f"\\lambda^2 + \\frac{{ {Sp_const_disp1_2} }}{{ {Mass_disp} }} = 0"
    STR1_03 = f"\\lambda_1 = i\\omega, \ \\lambda_2 = -i\\omega,\ \\omega = {omega_0_disp}"
    st.latex(STR1_02)
    st.latex(STR1_03)

##### Step 03
st.markdown("##### ▷ Step 3：微分方程式の一般解")
# x_ini 
if st.sidebar.checkbox("一般解を表示") :
    if omega_0 == 1 :
        STR1_04 =f" x(t)= A\cos \\big(  \\omega t +  \\phi \\big) = A\\cos \\left( t +  \\phi \\right)"
    else:
        STR1_04 =f" x(t)= A\cos \\big(  \\omega t +  \\phi \\big) = A\\cos \\left(  {omega_0_disp} t +  \\phi \\right)"
    st.latex(STR1_04)


    if st.checkbox("一般解を求める過程を表示"):
        """
        　　- 特製方程式が２つの複素数解 $\lambda_1=-i\omega,\ \lambda_2=i\omega$ を持つことから，求める$x(t)$の一般解は次のようになる．
        """
        st.latex( "x(t)=c_1 e^{-i\omega t} + c_2e^{i \omega t}" )
        """
        　　- さらに
            [オイラーの公式](https://w3e.kanazawa-it.ac.jp/math/category/fukusosuu/henkan-tex.cgi?target=/math/category/fukusosuu/euler-no-kousiki.html)より\n
        　　$x(t) = c_1 e^{-i\omega t} + c_2e^{i \omega t}$\n
        　　$\\phantom{x(t)} = c_1 \cos (-\omega t )+ i c_1  \sin(-\omega t) + c_2 \cos \omega t  + i c_2 \sin \omega t$\n
        　　$\\phantom{x(t)} = \\big( c_1 + c_2 \\big) \cos \omega t + i\\big(c_1 - c_2\\big) \sin (-\omega t)$\n
        　　$\\phantom{x(t)} = C_1 \cos \omega t - C_2 \sin \omega t$\n
        　　$\\displaystyle \\phantom{x(t)} = \\sqrt{C_1^2 + C_2^2}\\bigg( \\frac{C_1}{\\sqrt{C_1^2 + C_2^2} } \cos \omega t - \\frac{C_2}{\\sqrt{C_1^2 + C_2^2} } \sin \omega t \\bigg)$\n
        　　$\\displaystyle \\phantom{x(t)} = A\\Big( \cos \phi\cos \omega t - \sin \phi \sin \omega t \\Big)$\n
        　　$\\displaystyle \\phantom{x(t)} = A\cos\\big( \phi + \omega t  \\big)$\n
        　　$\\displaystyle \\phantom{x(t)} = A\cos\\big(  \omega t +  \phi\\big)$\n
        """




##### Step 04
title_step4 = r"##### ▷ Step 4：微分方程式の初期条件を満たす特殊解"
st.markdown(title_step4)

#-- set symbols and parameter
phi = Symbol(r"\phi", real = True)
AA , v, t , phi= symbols('AA v t phi', real = True)
A, m, k= symbols('A m k', positive=True, real = True)
x_t , v_t= symbols('x_t v_t', cls=Function)


#-- set function
from sympy.simplify.sqrtdenest import sqrtdenest
# x_t = AA * cos( omega * t + phi)
v_t = diff(x_t,t)
Ans_A = sqrtdenest(  sqrt(sympify(x_ini)**2 + sympify(v_ini)**2/omega**2 ))
Ans_A_1 = Ans_A.subs(omega,omega_0)


#-- cal param
Eq_cos = Eq(cos(phi), x_ini/Ans_A_1 )
Eq_sin = Eq(sin(phi), -1*(v_ini/(Ans_A_1*omega_0)))
Eq_cos_sol = solve(Eq_cos,phi, interval=[-sym_pi,sym_pi])
Eq_sin_sol = solve(Eq_sin,phi, interval=[-sym_pi,sym_pi])
import itertools
for i in  itertools.product(Eq_cos_sol,Eq_sin_sol):
    eq0 = (i[0]-i[1]).rewrite(acos)
    if trigsimp(cos(expand(eq0, trig=True))) == 1 :
        if (i[0]/sym_pi)%2 == 0:
            Ans_phi = sympify(0)
        else:
            Ans_phi = sympify(i[0])

theta = omega * t + phi
theta = theta.subs(omega,omega_0)

if check_float([Ans_A_1]) == 0 :
    A_disp =latex( simplify(Ans_A_1).evalf(Significant_digits))
else:
    A_disp =latex(simplify(Ans_A_1))
if check_float([omega_0,Ans_phi]) == 0 :
    theta_disp = latex( collect( theta.evalf(Significant_digits),t))
else:
    theta_disp = latex(collect(theta,t))
if check_float([x_ini/Ans_A_1]) == 0 :
    phi_str01 = latex( (x_ini/Ans_A_1).evalf(Significant_digits)  )
else:
    phi_str01 = latex( (x_ini/Ans_A_1))
if check_float([v_ini/(Ans_A_1*omega_0)] ) == 0 :
    phi_str02 = latex( (-1*( v_ini/(Ans_A_1*omega_0)) ).evalf(Significant_digits) )
else:
    phi_str02 = latex( (-1*(v_ini/(Ans_A_1*omega_0))) )
if st.sidebar.checkbox("特殊解を表示") :
    if omega_0 == 1 :
        STR1_06 =f"x(t) = { A_disp } \\cdot \\cos\\left( t+\\phi \\right)"
    else:
        STR1_06 =f"x(t) = { A_disp } \\cdot \\cos\\left( { omega_0_disp }t+\\phi \\right)"
    st.latex(STR1_06)
    
    if Ans_phi.is_real :
        Ans_phi_disp0 = Ans_phi
        Ans_phi_disp1 = Ans_phi.evalf(Significant_digits)
        from sympy import S
        if Ans_phi.is_zero or Ans_phi.is_integer:
            STR1_07 = f"A={A_disp}\ {{\\rm [m]}},\\quad \\phi  = {latex(Ans_phi.rewrite(atan))} \ \\rm[rad]"
        elif Ans_phi.is_Float :
            STR1_07 = f"A={A_disp}\ {{\\rm [m]}},\\quad \\phi  = {latex(Ans_phi.evalf(Significant_digits))} \ \\rm[rad]"
        else:
            STR1_07 = f"A={A_disp}\ {{\\rm [m]}},\\quad \\phi  = {latex(Ans_phi)} ={latex(Ans_phi.rewrite(atan))} = {latex(Ans_phi_disp1)} \ \\rm[rad]"
    else :
        Ans_phi_disp = Ans_phi
        STR1_07 = f"A={A_disp}\ {{\\rm [m]}},\ \\phi = {latex(Ans_phi_disp)} \ \\rm[rad]"    

    f"""
        初期条件 $\ \ x(0)={latex(x_ini)},\\quad v(0) = {latex(v_ini)}\ \ $より
    """
    st.latex(STR1_07)
    f"""
        ここで$\ \\phi\ $ は
        $\ \ \\displaystyle \\cos \\phi = { phi_str01 } \ \ $
        かつ
        $\ \ \\displaystyle \\sin \\phi = {phi_str02}\ \ $
        を満たす$\ \ -\\pi < \\phi \\le \\pi \ \ $ の角度である．
    """

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
import math
from math import pi as math_pi
from sympy import pi as sym_pi

T = simplify(2*sym_pi/omega_0)
if omega_0.is_Float or omega_0.is_integer or omega_0.is_zero :
    T=T.evalf(Significant_digits)
else:
    T =  sqrtdenest(sqrt( (T)**2 ))

if st.sidebar.checkbox("角振動数と周期を表示") :
    st.latex(\
            f"\\displaystyle\
                \\text{{角振動数：}} \\omega = { omega_0_disp }\
                ，\\text{{周期：}}  T = \\frac{{2\pi}}{{\omega}} = {latex(T)}"\
                )



##### Step 06
st.markdown("##### ▷ Step 6：特殊解のグラフ")
CB_Step06_1 = st.sidebar.checkbox("特殊解のグラフを表示")
if CB_Step06_1 :
    try:
        function0 = Ans_A_1 * cos( omega_0 * t + Ans_phi)
        ts = np.linspace( 0, 10, 1)
        ys = lambdify(t, function0, "numpy")(ts)
        
    except:
        st.error("エラー：質量，ばね定数，初期位置，初速度を数値で指定してください．")
        st.error("この図は $\\displaystyle A = 1.0,\ \\omega = \\frac{2\\pi}{10} ,\ \\phi = 0$の図です．")
        function0 = cos( pi/5 * t )
        col2_01,col2_02=st.columns([3,1]) 
        with col2_02:
            xrange_min = st.number_input("▷ xの最小値",value=0,key=2)            
            xrange_max = st.number_input("▷ xの最大値",value=10,key=3)
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
            xrange_max = st.number_input("▷ xの最大値",value=10,key=2)
        with col2_01:
            ts = np.linspace( xrange_min, xrange_max, 1000)
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

st.sidebar.markdown("#### ver3.1(更新：2023.2.9)")

