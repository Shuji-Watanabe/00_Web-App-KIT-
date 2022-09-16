import streamlit as st
import sympy as sy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from decimal import Decimal

### Main program ###
st.markdown("### ２．分散$~s^2~$について")
variance_list00=["定義","その他の統計量との関係","計算方法の実例"]
variance_tab=[]
variance_tab=st.tabs(variance_list00)
with variance_tab[0]:
    st.markdown("#### 変量$X$の分散$~s_x^2~$")
    """
        変量$~X~$について$~N~$個のデータ$~\\big[x_1,\ x_2,\ x_3,\ \cdots,\ x_N\\big]~$があるとき，
        変量$~X~$の分散$~s_x^2~$とは\n\n
        $$ 
            s_x^2
            =
            \\frac{1}{N}
            \\Big\\{
                \\big(x_1-\\overline{x}\\big)^2
                +\\big(x_2-\\overline{x}\\big)^2
                +\\big(x_3-\\overline{x}\\big)^2
                + \cdots
                +\\big(x_N-\\overline{x}\\big)^2
            \\Big\\}
        $$
        で与えられる値のことである．この式は総和記号$~\\Sigma~$を用いて
        $$
            s_x^2
            =
            \\frac{1}{N}
                \\sum_{i=1}^{N}
                    \\big(x_i-\\overline{x}\\big)^2
        $$
        と表すこともできる．
    """
with variance_tab[1]:
    st.markdown("#### 分散$~s_x^2~$とその他の統計量との関係")
    """
        変量$~X~$の分散$~s_x^2~$は，変量$~X~$の平均値$~\\overline{x}~$
        $$ 
            \\overline{x}
            =
            \\frac{1}{N}
            \\Big(
                x_1 + x_2 + x_3 + \cdots + x_N
            \\Big)
        $$
        と変量$~X~$の２乗の平均値$~\\overline{x^2}~$
        $$ 
            \\overline{x^2}
            =
            \\frac{1}{N}
            \\Big(
                x^2_1 + x^2_2 + x^2_3 + \cdots + x^2_N
            \\Big)
        $$
        を用いて
        $$
            s_x^2
            =
            \\overline{x^2}-\\big(\\overline{x}\\big)^2
        $$
        のようにもとめることもできる．
        \n\n
    """

with variance_tab[2]:
    st.markdown("#### 平均値の計算")
    Data_00=st.session_state["Data_00"]

    st.dataframe(Data_00.T)
    var_name = st.selectbox(
                "平均値を計算したい変量を選択してください",
                list(Data_00.columns.values),
                key=1)
    Data_11 = Data_00[var_name]
    Data_11_N = len(Data_11)
    Data_11_Total = Data_11.sum()

    ####  平均値の計算例 ####
    tmp_01_list = { "最初の３項程度を示す":0,"全ての項を示す":1}
    tmp_01 = st.radio("▶︎ 変量の表示設定",list(tmp_01_list.keys()),horizontal=True)

    if tmp_01:
        Var_num_01 = ""
        if tmp_01_list[tmp_01] == 0 :
            Var_num_01 += "x_{%s}=%s,\ "%(1,str(Data_11[0]))
            Var_num_01 += "x_{%s}=%s,\ "%(2,str(Data_11[1]))
            Var_num_01 += "x_{%s}=%s,\ "%(3,str(Data_11[2]))
            Var_num_01 += "\\cdots,\ "
            Var_num_01 += "x_{%s}=%s"%(Data_11_N,str(Data_11[Data_11_N-1]))
        else :
            for i in range(Data_11_N):
                if i < Data_11_N-1 :
                    Var_num_01 += "x_{%s}=%s,\ "%(i+1,str(Data_11[i]))
                else:
                    Var_num_01 += "x_{%s}=%s"%(i+1,str(Data_11[i-1]))
        """
        $$
            \\begin{align*}
                &\\text{変量}~X~&&:%s\\text{の値}
                \\\\
                &\\text{データ}&&:%s
            \\end{align*}
        $$
        """%(var_name,Var_num_01)


    tmp_02_list = { "最初の３項程度を示す":0,"全ての項を示す":1}
    tmp_02 = st.radio("▶︎ 計算過程の表示設定",("最初の３項程度を示す","全ての項を示す"),horizontal=True)

    if tmp_02:
        Form_variance_str01 = ""
        Form_variance_str02 = ""
        tmp_Variance_01 = 0
        for i in range(Data_11_N):
            tmp_Variance_01 += (Data_11[i]-Data_11.mean())**2
        if tmp_02_list[tmp_02] == 0 :
            Form_variance_str00  = "\\big(x_1-\\overline{x}\\big)^2 \
                                    + \\big(x_2-\\overline{x}\\big)^2 \
                                    + \\big(x_3-\\overline{x}\\big)^2 \
                                    + \\cdots \
                                    + \\big(x_{%s}-\\overline{x}\\big)^2"%(Data_11_N)
            Form_variance_str01 += "\\big( %s - %s \\big)^2"%(Data_11[0],'{:.1f}'.format(Data_11.mean()))
            Form_variance_str01 += "+\\big( %s - %s \\big)^2"%(Data_11[1],'{:.1f}'.format(Data_11.mean()))
            Form_variance_str01 += "+\\big( %s - %s \\big)^2"%(Data_11[2],'{:.1f}'.format(Data_11.mean()))
            Form_variance_str01 += str( "+\cdots" )
            Form_variance_str01 += "+\\big( %s - %s \\big)^2"%(Data_11[Data_11_N-1],'{:.1f}'.format(Data_11.mean()))
            
            Form_variance_str02 += "\\big(%s\\big)^2"%('{:+.1f}'.format(Data_11[0]-Data_11.mean()))
            Form_variance_str02 += "+\\big(%s\\big)^2"%('{:+.1f}'.format(Data_11[1]-Data_11.mean()))
            Form_variance_str02 += "+\\big(%s\\big)^2"%('{:+.1f}'.format(Data_11[2]-Data_11.mean()))
            Form_variance_str02 += str( "+\cdots" )
            Form_variance_str02 += "+\\big(%s\\big)^2"%('{:+.1f}'.format(Data_11[Data_11_N-1]-Data_11.mean()))
        else :
            for i in range(Data_11_N):
                if i == 0 :
                    Form_variance_str00 = "\\big(x_1-\\overline{x}\\big)^2"
                    Form_variance_str01 = "\\big( %s - %s \\big)^2"%(Data_11[i],'{:.1f}'.format(Data_11.mean()))
                    Form_variance_str02 = "\\big(%s\\big)^2"%('{:+.1f}'.format(Data_11[i]-Data_11.mean()))

                else:
                    Form_variance_str00 += "+\\big(x_{%s}-\\overline{x}\\big)^2"%(i+1)
                    Form_variance_str01 += "+\\big( %s - %s \\big)^2"%(Data_11[i],'{:.1f}'.format(Data_11.mean()))
                    Form_variance_str02 += "+\\big(%s\\big)^2"%('{:+.1f}'.format(Data_11[i]-Data_11.mean()))
        """
            ##### 定義に従った分散の計算
            $$
                \\begin{align*}
                    s^2_{x}
                        &= \\frac{1}{%s}\\sum_{i=1}^{\\color{red}%s} 
                            \\big( x_{i} - \\overline{x} \\big)^2
                        \\\\ \\\\
                        &= \\frac{1}{%s}\\Big\{ %s \\Big\}
                        \\\\ \\\\
                        &= \\frac{1}{%s}\\Big\{ %s \\Big\}
                        \\\\ \\\\
                        &= \\frac{1}{%s}\\Big\{ %s \\Big\}
                        \\\\ \\\\
                        &=\\frac{%s}{%s}
                        \\\\ \\\\
                        &=%s
                \\end{align*}
            $$
        """\
        %(  Data_11_N,Data_11_N,\
            Data_11_N,Form_variance_str00,\
            Data_11_N,Form_variance_str01,\
            Data_11_N,Form_variance_str02,\
            tmp_Variance_01,Data_11_N,\
            sy.Rational(tmp_Variance_01,Data_11_N).evalf(6)
        )

        ##### 2乗平均と平均の２乗の差
        tmp_Variance_02 = 0
        for i in range(Data_11_N):
            tmp_Variance_02 += Data_11[i]**2

        Form_variance_str03 = ""
        Form_variance_str04 = ""
        if tmp_02_list[tmp_02] == 0 :
            Form_variance_str03  = "x^2_1 + x^2_2 + x^2_3 + \\cdots + x^2_{%s}"%(Data_11_N)
            Form_variance_str04 += " %s^2 + %s^2 + %s^2"%(Data_11[0], Data_11[1],Data_11[2])
            Form_variance_str04 += "+ \\cdots + %s^2"%( Data_11[Data_11_N-1])
        else :
            for i in range(Data_11_N):
                if i == 0 :
                    Form_variance_str03  = "x^2_1"
                    Form_variance_str04 += "%s^2"%(Data_11[i+1])
                else:
                    Form_variance_str03 += "+x^2_{%s}"%( i+1 )
                    Form_variance_str04 += "+%s^2"%(Data_11[i])
        """ 
            ##### $~\\overline{x^2} - \\overline{x}^2~$を利用した分散の計算
            $$
                \\begin{align*}
                    \\text{・}\\overline{x^2}
                        &= \\frac{1}{%s}\\sum_{i=1}^{\\color{red}%s} x^2_{i}
                        \\\\ \\\\
                        &= \\frac{1}{%s}\\Big( %s \\Big)
                        \\\\ \\\\
                        &= \\frac{1}{%s}\\Big( %s \\Big)
                        \\\\ \\\\
                        &=\\frac{%s}{%s}
                        \\\\ \\\\
                        &=%s
                    \\\\ \\\\
                    \\text{・}s_x^2
                        &= \\overline{x^2}-\\overline{x}^2
                        \\\\ \\\\
                        &= %s - %s^2
                        \\\\ \\\\
                        &= %s - %s
                        \\\\ \\\\
                        &= %s
                \\end{align*}
            $$
            ※ 定義に従った計算結果と$\\overline{x^2}-\\big(\\overline{x}\\big)^2$の計算結果の間に
            微小な差があり，それが気になる場合は”浮動小数点数”について調べてみると良い．
        """\
        %(  Data_11_N,Data_11_N,\
            Data_11_N,Form_variance_str03,\
            Data_11_N,Form_variance_str04,\
            tmp_Variance_02,Data_11_N,\
            tmp_Variance_02/Data_11_N,\
            tmp_Variance_02/(Data_11_N), Data_11.mean(),\
            tmp_Variance_02/(Data_11_N), Decimal(Data_11.mean())**2,\
            tmp_Variance_02/(Data_11_N) - (Data_11.mean() )**2
        )
    # st.markdown("#### 平均値を用いたデータ分析（平均値から期待されること）")
    # """
    #     > - 変量$~X~$（%s）のデータの多くは平均値$~\\overline{x}=%s$の近くに集中していることが期待される．

    #     > - 変量$~X~$（%s）についてデータを集めると，その多くが平均値$~\\overline{x}=%s$に近い値をとることが期待される．
    # """%( \
    #         var_name,'{:.1f}'.format(Data_11_Total/Data_11_N),\
    #         var_name,'{:.1f}'.format(Data_11_Total/Data_11_N),\
    #     )

