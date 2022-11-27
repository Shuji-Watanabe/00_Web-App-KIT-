import streamlit as st
import sympy as sym

def textcolor (text,color):
    output_str = f'<span style="color: {color}; ">{text}</span>'
    return output_str
contents_list=["曲線の表し方","曲線の長さの求め方","練習"]
contents_tab = st.tabs(contents_list)
contents_num =0 ; container_num = 0
st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/MKA4kBiXPRiMzrju9) """)
#### 1st contents #########
#contents_num +=1
with contents_tab[contents_num]:
    st.markdown(f"### {contents_num+1}.　{contents_list[contents_num]}")
    #曲線の表し方
    #### 曲線の陽関数表示 
    container_num += 1  
    with st.container():
        f"""
        ##### {contents_num+1}-{container_num}　曲線の陽関数表示  

        座標平面中の曲線$~C~$を
        $$
            y=f(x) 
        $$
        のように表すことを**曲線$~C~$の陽関数表示**と呼ぶ．
        """
        with st.expander("曲線の陽関数表示の気持ちとその例"):
             col_expander01 = st.columns([2,1])
             with col_expander01[0]:
                st.markdown(
                    f"""
                    　座標平面に曲線を描くといことは，**ある条件**を満たす点$~(x,\ y)~$の集まりを作り出すことに対応している．
                    曲線の陽関数表示は，その“**ある条件**”として  
                     - $~x~$ 座標は定義域の範囲で適当に決めてください    
                     - $~y~$ 座標は$~ f(x) ~$の計算結果としてください  
                    $\\phantom{{a}}$  
                    と定めたとみることができる．  
                    　例えば，右の図のような直線は，
                    $$
                    \\footnotesize 
                        \\text{{直線}}~y=2x+1~
                    $$
                    と書かれる．これは，直線を陽関数表示したものであり，
                    この直線が
                     - $~x~$ 座標は実数の範囲で適当に決めてください    
                     - $~y~$ 座標は$~ 2x+1 ~$の計算結果としてください 
                    $\\phantom{{a}}$  
                    という条件で作られる無数の点を集めて作られる直線という意味である．
                    そして，この直線を特徴づけている$~y~$座標の計算方法$~y=2x+1~$
                    をこの直線の名前として採用しているのである．
                    
                    以上のように考えることで，陽関数表示の気持ちを理解することができる．
                    """,unsafe_allow_html=True)
             with col_expander01[1]:
                st.image("./Sample_fig_curve01.tiff")
    """ """
    #### 曲線の陰関数表示 
    container_num += 1 
    with st.container():
            f"""
            ##### {contents_num+1}-{container_num}　曲線の陰関数表示 

            座標平面中の曲線$~C~$を
            $$
                F(x,y)=0
            $$
            のように表すことを**曲線$~C~$の陰関数表示**と呼ぶ．
            """
            with st.expander("曲線の陰関数表示の気持ちとその例"):
                col_expander01 = st.columns([2,1])
                with col_expander01[0]:
                    st.markdown(
                        f"""
                        　座標平面に曲線を描くといことは，**ある条件**を満たす点$~(x,\ y)~$の集まりを作り出すことに対応している．
                        曲線の陰関数表示は，その“**ある条件**”として  
                        - 方程式$~F(x,\ y)=0~$を満たすような$~x~$と$~y~$の組にしてください
                        $\\phantom{{a}}$  
                        と定めたとみることができる．  
                        　例えば，右の図のような直線は，
                        $$
                        \\footnotesize 
                            \\text{{直線}}~y=2x+1~
                        $$
                        と書かれる．これを陰関数表示で表すと
                        $$
                        \\footnotesize 
                            \\text{{直線：}}~2x+1-y=0~
                        $$
                        となる．これは単に$~y~$を移行しただけの式であるが，
                        直線を定めるための条件が
                        $$
                        \\footnotesize 
                        x~\\text{{座標を決めて，その値から}}~y~\\text{{座標を求める}}~
                        $$
                        という考え方から
                        $$
                        \\footnotesize 
                        2x+1-y=0 ~\\text{{を満たすような}}~x,\\ y~\\text{{の組を求める}}~
                        $$
                        という考え方に変わったと解釈することで，
                        陰関数表示の気持ちを理解することができる．
                        
                        また，円やサイクロイドなど複雑な曲線は陰関数表示で表した方がすっきりと表すことができる．
                        """,unsafe_allow_html=True)
                with col_expander01[1]:
                    st.image("./Sample_fig_curve01.tiff")
    """ """
    #### 曲線のパラメータ表示（媒介変数表示） 
    container_num += 1 
    with st.container():
            f"""
            ##### {contents_num+1}-{container_num}　パラメータ表示（媒介変数表示） 

            座標平面中の曲線$~C~$を，新たな変数$~t~$（パラメーター または 媒介変数）を用いて
            $$
            \\left\\{{ 
            \\begin{{align*}}
                x &= f(t)
                \\\\
                y &= g(t)
            \\end{{align*}}
            \\right.
            $$
            のように表すことを**曲線$~C~$のパラメータ表示**と呼ぶ．
            """
            with st.expander("曲線のパラメータ表示の気持ちとその例"):
                col_expander01 = st.columns([2,1])
                with col_expander01[0]:
                    st.markdown(
                        f"""
                        　座標平面に曲線を描くといことは，**ある条件**を満たす点$~(x,\ y)~$の集まりを作り出すことに対応している．
                        曲線の陰関数表示は，その“**ある条件**”として  
                        - $~t~$を定められた範囲で適当に決めてください
                        - $~x~$座標は$~f(t)~$の計算結果としてください
                        - $~y~$座標は$~g(t)~$の計算結果としてください
                        $\\phantom{{a}}$  
                        と定めたとみることができる．  
                        　例えば，右の図のような直線は，
                        $$
                        \\footnotesize 
                            \\text{{直線}}~y=2x+1~
                        $$
                        と書かれる．これを強引にパラメータ表示で表すと
                        $$
                        \\footnotesize 
                            \\text{{直線：}}~x=t,\ y=2t+1~
                        $$
                        となる．これは単に$~x~$を$~t~$に書き換えただけのようにも見えるが，
                        直線を定めるための条件が
                        $$
                        \\footnotesize 
                        x~\\text{{座標を決めて，その値から}}~y~\\text{{座標を求める}}~
                        $$
                        という考え方から
                        $$
                        \\footnotesize 
                        x,\ y~\\text{{を別々に計算する}}
                        $$
                        という考え方に変わったと解釈することで，
                        パラメータ表示の気持ちを理解することができる．
                        
                        また，円やサイクロイドなど複雑な曲線は陰関数表示で表した方がすっきりと表すことができる．
                        """,unsafe_allow_html=True)
                with col_expander01[1]:
                    st.image("./Sample_fig_curve01.tiff")
    """ """
    #### 原点を中心とする半径１の円の表現方法
    container_num += 1 
    with st.container():
        f"""
        ##### {contents_num+1}-{container_num}　曲線の表現方法の例：原点を中心とする半径１の円の表現方法 
        """
        """ """
        col_example = st.columns(3)
        with col_example[0]:
            """
            ###### 陽関数表示  
            """
            st.image("./Sample_円の陽関数表示.tiff")
            """
            $$
            \\footnotesize
            \\begin{align*}
                \\text{上半分} &: y=\\sqrt{1-x^2}
                \\\\
                \\text{下半分} &: y=-\\sqrt{1-x^2}
            \\end{align*}
            $$
            ただし，$ -1 \le x \le 1$．

            """
        with col_example[1]:
            """
            ###### 陰関数表示  
            """
            st.image("./Sample_円の陰関数表示.tiff")
            """
            $$
            \\footnotesize
                x^2 + y^2 = 1
            $$
            """
        with col_example[2]:
            """
            ###### パラメータ表示  
            """
            st.video("./Sample_円のパラメータ表示.mov")
            """
            $$
            \\footnotesize
            \\begin{align*}
                & 0 \\le t \\le 360^\circ
                \\\\
                & x = \\cos t
                \\\\
                & y = \\sin t
            \\end{align*}
            $$
            """

#### 2nd contents #########
contents_num +=1
container_num = 0
with contents_tab[contents_num]:
    st.markdown(f"### {contents_num+1}.　{contents_list[contents_num]}")
    #曲線の長さの求め方のアイディア
    # with st.container():
    #     f"""
    #     ##### {contents_num+1}-{container_num}　曲線の長さの求め方のアイディア

    #     座標平面中に
    #     """
    #曲線の長さの求め方（その１）：陽関数表示
    container_num += 1
    with st.container():
        f"""
        ##### {contents_num+1}-{container_num}　曲線の長さの求め方（その１）：陽関数表示
        """
        """ """
        col_2nd_1 = st.columns([2,1])
        with col_2nd_1[0]:
            """
            区間$~[a,\ b]\ (a<b)~$における曲線$~y=f(x)~$の長さは
            $$
                \\int_{x=a}^{x=b} 
                    \\,
                      \sqrt{
                            1+\Big(\\frac{dy}{dx} \\Big)^2
                            }
                    \\,
                    dx
            $$
            で求めることができる．
            """
        """ """
        with col_2nd_1[1]:
            """ -- Fig -- """
        """ """

        ##### 例題（問題）
        col_ans_01 = st.columns([2,1])
        with col_ans_01[0] :               
            """
            ##### 例題
            
            区間$~\\big[1,\ 4\\big]~$における曲線$~\\dfrac{1}{8}x^4 + \\dfrac{1}{4}x^{-2}~$の長さを求めよ．
            """
            """ """
        with col_ans_01[1] :
            ##### 答え
            key_str = f"{contents_num}_{container_num}_01"
            """ ##### 答え """
            if st.checkbox("解答の表示",key=key_str):    
                """
                $$
                \\dfrac{2055}{64}
                $$
                """

        radio_dict = {"なし":0,
                      "サラッと":1,
                      "ガッツリと":2
                      }
        col_ans_01_1 = st.columns([4,1])
        with col_ans_01_1[1]:
            radio_str = st.radio("［ヒントの表示］",radio_dict.keys())
        with col_ans_01_1[0]: 
            """　"""
            if radio_dict[radio_str]==0:
                """がんばって！"""
            elif radio_dict[radio_str]==1:
                """**ヒント : このような流れで考えてみましょう**"""
                """
                - この曲線の式は陽関数表示ですか？それともパラメータ表示ですか？ 
                - 曲線の長さを求める式はなんですか？ 
                - まずはわかる範囲で公式を具体化しましょう． 
                - 積分できる状態ならば積分しましょう． 
                """
            elif radio_dict[radio_str]==2:
                """**ヒント : 各項目の式を自分で書けるようにしましょう**"""
                st.markdown(
                    f"""
                    - この曲線の式は陽関数表示ですか？それともパラメータ表示ですか？  
                      {textcolor('陽関数表示','blue')}
                    - 曲線の長さを求める公式はなんですか？  
                      $$
                        \\color{{blue}}
                        \\footnotesize
                        \\int_{{x=a}}^{{x=b}} \\sqrt{{1+\\Big(\\frac{{dy}}{{dx}}\\Big)^2}} \\, dx
                      $$
                    - まずはわかる範囲で公式を具体化しましょう，  
                      $$
                        \\color{{blue}}
                        \\footnotesize
                        \\begin{{align*}}
                                &\\blacksquare\ \  
                                a = 1
                            \\\\
                                &\\blacksquare\ \  
                                b = 4
                            \\\\
                                &\\blacksquare\ \  
                                \\frac{{dy}}{{dx}}
                                  = \\frac{{d}}{{dx}}
                                    \\left( \\dfrac{{1}}{{8}}x^4 + \\dfrac{{1}}{{4}}x^{{-2}} \\right)
                                   = 
                                     \\dfrac{{1}}{{2}}x^3 - \\dfrac{{1}}{{2}}x^{{-3}}         
                            \\\\
                                &\\blacksquare\ \  
                                \\left( \\frac{{dy}}{{dx}} \\right)^2
                                  = 
                                    \\left( \\dfrac{{1}}{{2}}x^3 - \\dfrac{{1}}{{2}}x^{{-3}} \\right)^2
                                   =
                                    \\dfrac{{1}}{{4}}\\left( x^3 - x^{{-3}} \\right)^2 
                                   = 
                                    \\dfrac{{1}}{{4}}\\Big( x^6 -2 + x^{{-6}} \\Big) 
                                    = 
                                    \\dfrac{{1}}{{4}} x^6 - \\dfrac{{1}}{{2}}  + \\dfrac{{1}}{{4}}  x^{{-6}} 
                            \\\\
                                &\\blacksquare\ \  
                                1+\\left( \\frac{{dy}}{{dx}} \\right)^2
                                  = 
                                    1 + \\dfrac{{1}}{{4}} x^6 - \\dfrac{{1}}{{2}}  + \\dfrac{{1}}{{4}}  x^{{-6}}  
                                    = 
                                    \\dfrac{{1}}{{4}} x^6 + \\dfrac{{1}}{{2}}  + \\dfrac{{1}}{{4}}  x^{{-6}}  
                                    = 
                                    \\dfrac{{1}}{{4}}\\Big( x^6 + 2 + x^{{-6}} \\Big) 
                                    =
                                    \\dfrac{{1}}{{4}}\\left( x^3 + x^{{-3}} \\right)^2 
                                     
                        \\end{{align*}}
                      $$
                    - 積分できる状態ならば積分しましょう． 
                      $$
                        \\color{{blue}}
                        \\footnotesize
                        \\begin{{align*}}
                            \\int_{{x=a}}^{{x=b}} \\sqrt{{1+\\Big(\\frac{{dy}}{{dx}}\\Big)^2}} \\, dx
                            &=
                            \\int_{{x=1}}^{{x=4}} 
                                \\, 
                                    \\sqrt{{ 
                                        \\dfrac{{1}}{{4}}
                                        \\left( x^3 + x^{{-3}} \\right)^2   
                                    }}
                                \\, 
                                dx     
                            \\\\
                            &=
                            \\dfrac{{1}}{{2}}
                            \\int_{{1}}^{{4}} 
                                \\, 
                                    \\left| x^3 + x^{{-3}} \\right|
                                \\, 
                                dx   
                            \\\\
                            &=
                            \\dfrac{{1}}{{2}}
                            \\int_{{1}}^{{4}} 
                                \\, 
                                    \\left( x^3 + x^{{-3}} \\right)
                                \\, 
                                dx      
                            \\\\              
                            &=
                            \\dfrac{{1}}{{2}}
                            \\left[
                                \\, 
                                    \\frac{{1}}{{4}} x^4 - \\frac{{1}}{{2}}x^{{-2}} 
                                \\, 
                            \\right]_{{1}}^{{4}}        
                            \\\\              
                            &=
                            \\dfrac{{1}}{{8}}
                            \\left(
                                \\, 
                                    4^4 - 1^4 
                                \\, 
                            \\right)
                            -
                            \\dfrac{{1}}{{4}}
                            \\left(
                                \\, 
                                    4^{{-2}}
                                    - 
                                    1^{{-2}}
                                \\, 
                            \\right) 
                            \\\\
                            &=
                            \\dfrac{{2055}}{{64}}
                        \\end{{align*}}
                      $$
                    """,unsafe_allow_html=True)
    """ """
    #曲線の長さの求め方（その２）：パラメータ表示
    container_num += 1
    with st.container():
        f"""
        ##### {contents_num+1}-{container_num}　曲線の長さの求め方（その２）：パラメータ表示
        """
        col_2nd_2 = st.columns([2,1])
        with col_2nd_2[0]:
            """
            $~a \\le t \\le b\ (a<b)~$における曲線$~x=x(t),\\ y=y(t)~$の長さは
            $$
                \\int_{t=a}^{t=b} 
                    \\,
                      \sqrt{
                            \Big(\\frac{dx}{dt} \\Big)^2
                            +
                            \Big(\\frac{dy}{dt} \\Big)^2
                            }
                    \\,
                    dt
            $$
            で求めることができる．
            """