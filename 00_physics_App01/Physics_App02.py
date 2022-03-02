import streamlit as st
from PIL import Image
from sympy import *
from sympy.solvers import solve
from sympy import I, pi, E

init_printing()


st.title("""小物体の投射""")

col1, col2, col3, col4 = st.columns(4)
with col1:
    PRAM01=st.text_input('質量を入力')
with col2:
    PRAM02=st.text_input('高さを入力')
with col3:
    PRAM03=st.text_input('角度を入力')
with col4:
    PRAM04=st.text_input('速さを入力')

x,y,z,t= symbols('x y z t', real = True)
theta = symbols(r"\theta")
theta, m, h, v_0 = symbols('theta, m, h, v_0', real = True)
g = symbols('g',real=True)
var('theta m, h, v_0, g', positive = True)
FX, FY ,FZ = symbols('FX FY FZ', cls=Function)
FVX, FVY ,FVZ = symbols('FVX FVY FVZ', cls=Function)

if not PRAM01:
    PRAM01=sympify(m)
else :
    PRAM01=sympify(PRAM01)
if not PRAM02:
    PRAM02=sympify(h)
else :
    PRAM02=sympify(PRAM02)
if not PRAM03:
    CK_P03=0
    PRAM03_0=sympify(theta)
    PRAM03=PRAM03_0
else :
    PRAM03_0=sympify(PRAM03)
    try :
        PRAM03=Rational(sympify(PRAM03),180)*pi
    except :
        PRAM03=sympify(PRAM03)
        PRAM03_0=sympify(PRAM03)
if not PRAM04:
    PRAM04=sympify(v_0)
else :
    PRAM04=sympify(PRAM04)


col2_1, col2_2= st.columns([3,1])
with col2_2:
    IMAGE_URL = 'https://github.com/Shuji-Watanabe/00_Web-App-KIT-/blob/main/00_physics_App01/Figs/projectile_motion1.png?raw=true'
    #image = Image.open(IMAGE_URL)
    st.image(IMAGE_URL)

with col2_1:
    #問題文
    Q_STR0="図のようには，質量"
    Q_STR0=Q_STR0 + " $" + latex(PRAM01) + "{\\rm [kg]}$ "
    Q_STR0=Q_STR0 + "の小球を，"
    Q_STR0=Q_STR0 + "高さ $" + latex(PRAM02) +"{\\rm [m]}$ "
    Q_STR0=Q_STR0 + "のところから，"
    Q_STR0=Q_STR0 + "水平面に対して $" + latex(PRAM03_0) +"{\\rm [{}^\\circ]}$ "
    Q_STR0=Q_STR0 + "の方向へ， 速さ"
    Q_STR0=Q_STR0 + " $" + latex(PRAM04) +"{\\rm [m/s]}$ "
    Q_STR0=Q_STR0 + "で斜方投射した．"+ "小球が運動を始めた時刻を $$0\ {\\rm s}$$ ，重力加速度の大きさを"
    Q_STR0=Q_STR0 + " $" + "g {\\rm [m/s^2]}" + "$ "
    Q_STR0=Q_STR0 + "とし，空気抵抗は無視できるものとする．"
    st.write(Q_STR0)

    #時刻tにおける速度と位置
    FVX= PRAM04 * cos(PRAM03)
    FVY= PRAM04 * sin(PRAM03) - g*t
    FX = PRAM04 * cos(PRAM03) * t 
    FY = PRAM02 + PRAM04 * sin(PRAM03) * t + (-g)*t**2/2

    #第1問
    Q_STR1="(1) 加速度ベクトルを"+\
            "$\\displaystyle \\frac{d^2}{dt^2} \\left(\\begin{matrix} x \\\\ y \\end{matrix}\\right)$"\
            +"とし，運動方程式を立てよ．"
    st.write(Q_STR1)
    ## 解答
    Disp_Ans01 = st.checkbox('--> (1)の解答を見る')
    force_g = sympify(PRAM01)*(-g)
    if Disp_Ans01:
        if PRAM01 == m :
            A_STR1 = "\\quad \\displaystyle\
                        m \\frac{d^2}{dt^2}\
                        \\begin{pmatrix}\
                             x \\\\ y \
                        \\end{pmatrix}\
                        =\
                        \\begin{pmatrix}\
                             0 \\\\ -mg\
                        \\end{pmatrix}"
        else :
            A_STR1 = "\\quad \\displaystyle "
            A_STR1 = A_STR1 + latex(sympify(PRAM01))
            A_STR1 = A_STR1 + "\\cdot \\frac{d^2}{dt^2}\
                        \\begin{pmatrix}\
                             x \\\\ y \
                        \\end{pmatrix}\
                        =\
                        \\begin{pmatrix}\
                             0 \\\\ " + latex(force_g) \
                        +"\\end{pmatrix}"
        st.latex(A_STR1)

    #第2問
    Q_STR2="(2) 最高点に達する時刻 $$t_{\\rm top}$$ を求めよ．"
    st.write(Q_STR2)

    ## 解答
    Disp_Ans02 = st.checkbox('--> (2)の解答を見る')
    Ans02 = solve(Eq(0,PRAM04*sin(PRAM03)-g*t),t)
    if Disp_Ans02:
        st.latex(r"t_{\rm top} = %s\ {[\rm s]}" % latex(Ans02[0]))


    #第3問
    Q_STR3="(3) 最高点の高さ $$y_{\\rm top}$$ を求めよ．"
    st.write(Q_STR3)

    ## 解答
    Disp_Ans03 = st.checkbox('--> (3)の解答を見る')
    Ans03 = latex(FY.subs(t,Ans02[0]))
    if Disp_Ans03:
        st.latex(r"y_{\rm top} = %s\ {[\rm s]}" % Ans03)

    #第4問
    Q_STR3="(4) 地上に達する時刻 $$t_1$$ を求めよ．"
    st.write(Q_STR3)

    ## 解答
    Disp_Ans04 = st.checkbox('--> (4)の解答を見る')
    Ans04 = solve(Eq(0,FY),t)
    if Disp_Ans04:
        for i in range(len(Ans04)):
            # 何か良い方法がないものか．．．
            # CK_val = Ans04[i].subs([ (theta,pi/6),(m,1),(h,1),(v_0,1),(g,10)])
            CK_val = Ans04[i].subs([ (PRAM01,1),(PRAM02,1),(PRAM03,pi/6),(PRAM04,1),(g,10)])
            if 0 < CK_val:
                st.latex(r"t_{1}=%s {[\rm s]}" % latex(Ans04[i]))