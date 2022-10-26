import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import pingouin as pg
import math as math

Lec04_contents_list=["単回帰式","単回帰分析","単回帰分析の例"]
Lec04_contents_tab =[]
Lec04_contents_tab = st.tabs(Lec04_contents_list)
contents_num =0
section_num =0
st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/MKA4kBiXPRiMzrju9) """)


with Lec04_contents_tab[contents_num]:
    st.markdown("### %s.　%s"%(contents_num+1,Lec04_contents_list[contents_num]))
    #### 単回帰式の導出####
    with st.container():
        section_num += 1
        st.markdown(f"##### {contents_num+1}-{section_num} 単回帰式")
        """
            2つの変量$~X,\\ Y~$について，
            変量$~Y~$を目的変数，変量$~X~$をその説明変数とする（線形）単回帰式は
            $$
                y = a \\cdot x + b 
                  = \\frac{C_{xy}}{\\sigma_x^2} \\cdot x 
                    + \\Big( \overline{y} - \\frac{C_{xy}}{\\sigma_x^2}\\cdot \\overline{x} \\Big)
                  = \\frac{C_{xy}}{\\sigma_x^2}
                        \\cdot \\big( x -  \\overline{x} )
                    + \overline{y} 

            $$
            で与えられる．ここで
            $$
                \\begin{align*}
                    ~X~\\text{の平均：}
                        \\ \\overline{x} &= \\frac{1}{N} \\sum_{k=1}^{N} x_k
                        \\\\
                    ~X~\\text{の分散：}
                        \\ \\sigma_x^2 &= \\frac{1}{N} 
                                                \\sum_{k=1}^{N} 
                                                \\big( x_k - \overline{x} \\big)^2
                                        = \overline{x^2} - \overline{x}^2
                        \\\\
                    ~Y~\\text{の平均：}
                        \\ \\overline{y} &= \\frac{1}{N} \\sum_{k=1}^{N} y_k
                        \\\\
                    ~X,\\ Y~\\text{の分散：}
                        \\ C_{xy} &= \\frac{1}{N} 
                                            \\sum_{k=1}^{N} 
                                            \\big( x_k - \overline{x} \\big)
                                            \\big( y_k - \overline{y} \\big)
                                 =\overline{xy} - \overline{x} \cdot \overline{y} 
                        \\\\
                     
                \\end{align*}
            $$
            である．
        """

        " "; " "; " "
        section_num += 1
        st.markdown(f"#####  {contents_num+1}-{section_num} 単回帰式の導出の準備")
        """
            2つの変量$~X,\\ Y~$について，平均値，分散をそれぞれ次のように書く．
            $$
                \\begin{align*}
                    X~\\text{の平均値：}~ \\overline{x}
                    &= 
                        \\frac{1}{N} 
                            \\sum_{k=1}^N
                            x_k
                \\\\
                    X~\\text{の分散：}~ \\sigma^2_x
                    &= 
                        \\frac{1}{N} 
                            \\sum_{k=1}^N
                            \\big( x_k - \\overline{x} \\big)^2
                        =
                        \\overline{x^2} - \\big( \\overline{x} \\big)^2
                \\\\
                    Y~\\text{の平均値：}~ \\overline{y}
                    &= 
                        \\frac{1}{N} 
                            \\sum_{k=1}^N
                            y_k
                \\\\
                    Y~\\text{の分散：}~ \\sigma^2_y
                    &= 
                        \\frac{1}{N} 
                            \\sum_{k=1}^N
                            \\big( y_k - \\overline{y} \\big)^2
                        =
                        \\overline{y^2} - \\big( \\overline{y} \\big)^2 
                \\end{align*}
            $$
            また$~X,\\ Y~$の共分散を次のように書く．
            $$
                \\begin{align*}
                    X,\\ Y~\\text{の共分散：}~ C_{xy}
                    = 
                        \\frac{1}{N} 
                            \\sum_{k=1}^N
                            \\big( x_k - \\overline{x}\\big)
                            \\big( y_k - \\overline{y}\\big)   
                    =
                       \\overline{xy} - \\overline{x} \\cdot \\overline{y}
                \\end{align*}
            $$
        """
        " "; " "; " "
        section_num += 1
        st.markdown(f"#####  {contents_num+1}-{section_num} 単回帰式を導出するときの方針")
        """
            $~x_k~$を用いて
            $$
                \\tilde{y}_{k} = ax_k + b
            $$
            と$~y_k~$を予測するとき，誤差$~y_k - \\tilde{y}_k~$の分散$~V~$
            $$
                V 
                =\\frac{1}{N}
                    \sum_{k=1}^N
                    \\Big(y_k - \\tilde{y}_k \\Big)^2
                =\\frac{1}{N}
                    \sum_{k=1}^N
                    \\Big\{ y_k - \\big( ax_k + b \\big) \\Big\}^2

            $$
            を最小にするような$~a,\\ b~$を求める．
        """
        " "; " "; " "
        section_num += 1
        st.markdown(f"##### {contents_num+1}-{section_num} 単回帰式の導出")
        """
            $$
            \\begin{align*}
                V &= \\frac{1}{N}
                    \\sum_{k=1}^N
                    \\Big(y_k - \\tilde{y}_k \\Big)^2
            \\\\  &=
                    \\frac{1}{N}
                    \\sum_{k=1}^N
                    \\Big\{ y_k  - \\big(ax_k + b \\big)\\Big\}^2
            \\\\  &=
                    \\frac{1}{N}
                    \\sum_{k=1}^N
                    \\Big( y_k  -  ax_k -  b \\Big)^2
            \\\\  &=
                    \\frac{1}{N}
                    \sum_{k=1}^N
                    \\Big( 
                            y^2_k + a^2x^2_k + b^2
                            - 2a  x_k y_k 
                            + 2ab x_k
                            - 2by_k  
                    \\Big)
            \\\\  &=
                    
                    \\frac{1}{N}
                        \sum_{k=1}^N
                        y^2_k 
                    + 
                    a^2
                    \\cdot 
                    \\frac{1}{N}
                        \sum_{k=1}^N
                        x^2_k 
                    + 
                    b^2
                    \\cdot 
                    \\frac{1}{N}
                        \sum_{k=1}^N
                    \\\\
                    &\\qquad \\qquad \\qquad \\qquad
                    \\begin{split}
                        - 
                        2a  
                        \\cdot 
                        \\frac{1}{N}
                            \sum_{k=1}^N
                            x_k y_k 
                        + 
                        2ab 
                        \\cdot 
                        \\frac{1}{N}
                            \sum_{k=1}^N
                            x_k
                        - 
                        2b
                        \\cdot 
                        \\frac{1}{N}
                        \sum_{k=1}^N
                            y_k  
                    \\end{split}
            \\\\  &=
                    \\overline{y^2}
                    + 
                    a^2 \\cdot \\overline{x^2}
                    + 
                    b^2
                    - 
                    2a  
                    \\cdot \\overline{xy}
                    + 
                    2ab
                    \\cdot \\overline{x}
                    - 
                    2b
                    \\cdot \\overline{y}
            \\end{align*}
            $$
        """
        """
            ここで，任意の$~a,\\ b~$に対して
            $$
            
                \\begin{vmatrix}
                ~
                  \\displaystyle
                  \\frac{\\partial^2 V}{\\partial a^2}
                        & 
                        \\displaystyle
                        \\frac{\\partial^2 V}{\\partial b \\partial a}
                        ~
                \\\\
                \\phantom{a}
                \\\\
                ~
                \\displaystyle
                  \\frac{\\partial^2 V}{\\partial a \\partial b}
                        & 
                        \\displaystyle
                        \\frac{\\partial^2 V}{\\partial b^2}
                        ~
                \\end{vmatrix}
                =
                \\begin{vmatrix}
                    2 \\overline{x^2} & 2 \\overline{x}
                    \\\\
                    2 \\overline{x} & 2
                \\end{vmatrix}
                =
                4 \\overline{x^2}
                -
                4 \\overline{x}^2
                \\ge 0
            $$
            であるから，
            $$
            \\begin{align*}
                    \\frac{\\partial V }{\\partial a } 
                    &= 0
                        \\ 
                        \\Rightarrow
                        \\ 
                        2 \\overline{x^2} a +2 \\overline{x} b  - 2\\overline{xy} 
                        =0
            \\\\
            \\phantom{a}
            \\\\
                \\frac{\\partial V }{\\partial b } 
                    &= 0
                        \\ 
                        \\Rightarrow
                        \\ 
                        2 \\overline{x} a + 2b- 2  \\overline{y} 
                        =0   
            \\end{align*}
            $$
            を満たす$~a,\\ b~$は$~V~$を最小にする．
            よって求める$~a,\\ b~$は
            $$
                a =
                    \\frac
                        { \\overline{xy} - \\overline{x} \\cdot \\overline{y} }
                        { \\overline{x^2} - \\overline{x}^2}
                    =
                    \\frac{C_{xy}}{\\sigma_x^2}
                \\quad
                ,\\ 
                \\quad 
                b = \\overline{y} - a \\overline{x}
                    = \\overline{y} - \\frac{C_{xy}}{\\sigma_x^2} \\cdot \\overline{x}
            $$
            である．
        """

        with st.expander("偏微分を利用しない単回帰式の導出"):
            """
                $$
                \\begin{align*}
                    V &= \\frac{1}{N}
                        \\sum_{k=1}^N
                        \\Big(y_k - \\tilde{y}_k \\Big)^2
                \\\\  &=
                        \\frac{1}{N}
                        \\sum_{k=1}^N
                        \\Big\{ y_k  - \\big(ax_k + b \\big)\\Big\}^2
                \\\\  &=
                        \\frac{1}{N}
                        \\sum_{k=1}^N
                        \\Big( y_k  -  ax_k -  b \\Big)^2
                \\\\  &=
                        \\frac{1}{N}
                        \sum_{k=1}^N
                        \\Big( 
                                y^2_k + a^2x^2_k + b^2
                                - 2a  x_k y_k 
                                + 2ab x_k
                                - 2by_k  
                        \\Big)
                \\\\  &=
                        
                        \\frac{1}{N}
                            \sum_{k=1}^N
                            y^2_k 
                        + 
                        a^2
                        \\cdot 
                        \\frac{1}{N}
                            \sum_{k=1}^N
                            x^2_k 
                        + 
                        b^2
                        \\cdot 
                        \\frac{1}{N}
                            \sum_{k=1}^N
                        \\\\
                        &\\qquad \\qquad \\qquad \\qquad
                        \\begin{split}
                            - 
                            2a  
                            \\cdot 
                            \\frac{1}{N}
                                \sum_{k=1}^N
                                x_k y_k 
                            + 
                            2ab 
                            \\cdot 
                            \\frac{1}{N}
                                \sum_{k=1}^N
                                x_k
                            - 
                            2b
                            \\cdot 
                            \\frac{1}{N}
                            \sum_{k=1}^N
                                y_k  
                        \\end{split}
                \\\\  &=
                        \\overline{y^2}
                        + 
                        a^2 \\cdot \\overline{x^2}
                        + 
                        b^2
                        - 
                        2a  
                        \\cdot \\overline{xy}
                        + 
                        2ab
                        \\cdot \\overline{x}
                        - 
                        2b
                        \\cdot \\overline{y}
                \\end{align*}
                $$
            """
            """
                ここで
                $$ 
                \\begin{align*}
                    \\sigma_x^2 
                    &= \\overline{x^2} - \\big( \\overline{x}\\big)^2 
                    \\Longrightarrow 
                    \\overline{x^2} =  \\sigma_x^2 + \\big( \\overline{x}\\big)^2 
                \\\\
                    \\sigma_y^2 
                    &= \\overline{y^2} - \\big( \\overline{y}\\big)^2 
                    \\Longrightarrow 
                    \\overline{y^2} =  \\sigma_y^2 + \\big( \\overline{y}\\big)^2 
                \\\\
                    
                \\end{align*}
                $$
                より，
            """
            """
                $$
                \\begin{align*}
                    V &=
                        \\Big\{ \\sigma_y^2 + \\big( \\overline{y}\\big)^2 \\Big\}
                        + 
                        a^2 
                        \\cdot
                        \\Big\{ \\sigma_x^2 + \\big( \\overline{x}\\big)^2  \\Big\}
                        + 
                        b^2
                        - 
                        2a  
                        \\cdot 
                        \\Big\{ C_{xy} + \\overline{x} \\cdot \\overline{y}  \\Big\}
                        + 
                        2ab
                        \\cdot \\overline{x}
                        - 
                        2b
                        \\cdot \\overline{y}
                \\\\ &=
                        \\sigma_y^2 + \\big( \\overline{y}\\big)^2 
                        + 
                        a^2 
                        \\cdot
                        \\sigma_x^2 
                        +
                        a^2 
                        \\cdot
                        \\big( \\overline{x}\\big)^2 
                        + 
                        b^2
                        - 
                        2a  
                        \\cdot 
                        C_{xy} 
                        + 
                        2a  
                        \\cdot 
                        \\overline{x} \\cdot \\overline{y} 
                        + 
                        2ab
                        \\cdot \\overline{x}
                        - 
                        2b
                        \\cdot \\overline{y}
                \\\\ &=
                        a^2 
                        \\sigma_x^2 
                        - 
                        2
                        a  
                        \\cdot 
                        C_{xy} 


                        + 
                        b^2
                        +
                        \\big( a \\overline{x}\\big)^2 
                        + 
                        \\big( \\overline{y}\\big)^2 
                        + 
                        2
                        \\cdot 
                        a \\overline{x} \\cdot \\overline{y} 
                        + 
                        2
                        \\cdot 
                        a\\overline{x}
                        \\cdot
                        b
                        - 
                        2
                        b
                        \\cdot 
                        \\overline{y}

                        + 
                        \\sigma_y^2 

                \\\\ &=
                        \\sigma_x^2 
                        \\left(
                            a^2 
                            - 
                            2
                            a  
                            \\cdot 
                            \\frac{C_{xy}}{\\sigma_x^2 } 
                        \\right)

                        + 
                        \\Big(
                            b
                            +
                            a \\overline{x}
                            -
                            \\overline{y}
                        \\Big)^2 

                        + 
                        \\sigma_y^2 
                \\\\ &=
                        \\sigma_x^2 
                        \\left(
                            a
                            - 
                            \\frac{C_{xy}}{\\sigma_x^2 }  
                        \\right)^2
                        -
                        \\frac{C^2_{xy}}{\\sigma_x^2 } 
                        + 
                        \\Big(
                            b
                            +
                            a \\overline{x}
                            -
                            \\overline{y}
                        \\Big)^2 

                        + 
                        \\sigma_y^2 
                \\\\ &=
                        \\sigma_x^2 
                        \\left(
                            a
                            - 
                            \\frac{C_{xy}}{\\sigma_x^2 }  
                        \\right)^2
                        + 
                        \\Big(
                            b
                            +
                            a \\overline{x}
                            -
                            \\overline{y}
                        \\Big)^2 

                        + 
                        \\sigma_y^2 
                        -
                        \\frac{C^2_{xy}}{\\sigma_x^2 } 
                \\end{align*}
                $$  
            """
            """
            となる．ここで
            $$
                \\sigma_x^2 
                    \\left(
                        a
                        - 
                        \\frac{C_{xy}}{\\sigma_x^2 }  
                    \\right)^2
                \\ge 0 
                \\quad
                ,\\ 
                \\quad
                \\Big(
                    b
                    +
                    a \\overline{x}
                    -
                    \\overline{y}
                \\Big)^2 
                \\ge 0
            $$
            であり，
            $$
                \\sigma_y^2 
                -
                \\frac{C^2_{xy}}{\\sigma_x^2 } 
            $$
            は，$~a,\\ b~$によらない定数である．よって
            $$
                \\left(
                    a
                    - 
                    \\frac{C_{xy}}{\\sigma_x^2 }  
                \\right)^2
                =
                0
                \\quad
                ,\\ 
                \\quad
                \\Big(
                    b
                    +
                    a \\overline{x}
                    -
                    \\overline{y}
                \\Big)^2
                =0
            $$
            のとき$~V~$が最小となるので，求める$~a,\\ b~$は
            $$
                a = \\frac{C_{xy}}{\\sigma^2_{x}}
                \\quad
                ,\ 
                \\quad
                b = \overline{y} - a\overline{x}
                  = \overline{y} - \\frac{C_{xy}}{\\sigma^2_{x}} \cdot \overline{x} 
            $$
            となる．
            """

        " "; " "; " "
