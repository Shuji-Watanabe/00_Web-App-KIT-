from tkinter import N
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Main program ###
st.markdown("### １．平均値$~\\overline{x}~$について")
variance_list00=["平均値の定義","データ分析の具体例"]
variance_tab=[]
variance_tab=st.tabs(variance_list00)
with variance_tab[0]:
    st.markdown("#### 変量$~X~$の平均値$~\\overline{x}~$の定義")
    """
    変量$~X~$について$~N~$個のデータ$~\\big[x_1,\ x_2,\ x_3,\ \cdots,\ x_N\\big]~$があるとき，
    変量$~X~$の平均値（算術平均）$~\\overline{x}~$とは\n\n
    $$ 
        \\overline{x}
        =
        \\frac{1}{N}
        \\Big(
            x_1 + x_2 + x_3 + \cdots + x_N
        \\Big)
    $$
    で与えられる値のことである．この式は総和記号$~\\Sigma~$を用いて
    $$
        \\overline{x}
        =
        \\frac{1}{N}\\sum_{i=1}^{N}x_i
    $$
    と表すこともできる．
    \n\n
"""
with variance_tab[1]:
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
        Form_Average_str01 = ""
        if tmp_02_list[tmp_02] == 0 :
            Form_Average_str00  = "x_1 + x_2 + x_3 + \\cdots + x_{%s}"%(Data_11_N)
            Form_Average_str01 += str('{:}'.format(Data_11[0]) )
            Form_Average_str01 += str("+") + str( '{:}'.format(Data_11[1]) )
            Form_Average_str01 += str("+") + str( '{:}'.format(Data_11[2]) )
            Form_Average_str01 += str( "+\cdots+" ) + str( '{:}'.format(Data_11[Data_11_N-1]) )
        else :
            for i in range(Data_11_N):
                if i == 0 :
                    Form_Average_str01 += str( '{:}'.format(Data_11[i]) )
                    Form_Average_str00  = "x_1"
                else:
                    Form_Average_str00 += "+x_{%s}"%(str(i+1))
                    Form_Average_str01 += str( '{:+}'.format(Data_11[i]) )
        """
            $$
                \\begin{align*}
                    \\overline{x}
                        &= \\frac{1}{%s}\\sum_{i=1}^{\\color{red}%s} x_{i}
                        \\\\ \\\\
                        &= \\frac{1}{%s}\\Big( %s \\Big)
                        \\\\ \\\\
                        &= \\frac{1}{%s}\\Big( %s \\Big)
                        \\\\ \\\\
                        &=\\frac{%s}{%s}
                        \\\\ \\\\
                        &=%s
                \\end{align*}
            $$
        """\
        %(  Data_11_N,Data_11_N,\
            Data_11_N,Form_Average_str00,\
            Data_11_N,Form_Average_str01,\
            Data_11_Total,Data_11_N,\
            Data_11_Total/Data_11_N
        )
    st.markdown("#### 平均値を用いたデータ分析（平均値から期待されること）")
    """
        > - 変量$~X~$（%s）のデータの多くは平均値$~\\overline{x}=%s$の近くに集中していることが期待される．

        > - 変量$~X~$（%s）についてデータを集めると，その多くが平均値$~\\overline{x}=%s$に近い値をとることが期待される．
    """%( \
            var_name,'{:.1f}'.format(Data_11_Total/Data_11_N),\
            var_name,'{:.1f}'.format(Data_11_Total/Data_11_N),\
        )
    st.markdown("#### 平均値を用いたデータ分析（データの可視化）")
    fig_col01=[]
    fig_col01=st.columns(2)
    with fig_col01[1]:
        x_range_min = st.number_input('横軸の最小値',
                                step=1,
                                value=Data_11.min()
                                )
        x_range_max = st.number_input('横軸の最大値',
                                step=1,
                                value=Data_11.max()
                                )
        y_range_min = st.number_input('縦軸の最小値',
                                step=1,
                                value=0
                                )
        y_range_max = st.number_input('縦軸の最大値',
                                step=1,
                                value=Data_11_N
                                )
        n_bins = st.number_input('棒の数（binsの設定）',
                                step=1,
                                value=10
                                )
    with fig_col01[0]:
        fig = plt.figure(figsize = (6,6))   
        plt.xlim(x_range_min ,x_range_max )
        plt.ylim(y_range_min ,y_range_max )
        plt.ylabel('度数',fontsize = 15)
        plt.xlabel('%s'%(var_name),fontsize = 15)
        plt.title('%sのヒストグラム'%(var_name),fontsize = 15)
        plt.hist(Data_11,bins = n_bins, color = "blue")
        plt.axvline(Data_11.mean(), color='red', linestyle='dashed', linewidth=2, label='平均値')
        plt.legend()
        st.pyplot(fig)