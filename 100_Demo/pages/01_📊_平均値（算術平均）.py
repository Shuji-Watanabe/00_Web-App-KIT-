import streamlit as st

### Main program ###
st.markdown("### １．平均値$~\\overline{x}~$について")
variance_list00=["平均値の定義","計算方法の実例","データ分析例"]
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
    Data_00=st.session_state["Data_00"]
    st.dataframe(Data_00.T)
    val_name = st.selectbox(
                "平均値を計算したい変量を選択してください",
                list(Data_00.columns.values),
                key=1)
    Data_11 = Data_00[val_name]
    Data_11_N = len(Data_11)
    Data_11_Total = Data_11.sum()

    ####  平均値の計算例　１行目　####
    tmp_01_list = { "最初の３項程度を示す":0,"全ての項を示す":1}
    tmp_01 = st.radio("選択：",("最初の３項程度を示す","全ての項を示す"),horizontal=True)

    if tmp_01:
        Form_Average_str = ""
        if tmp_01_list[tmp_01] == 0 :
            Form_Average_str += str( '{:}'.format(Data_11[0]) )
            Form_Average_str += str("+")
            Form_Average_str += str( '{:}'.format(Data_11[1]) )
            Form_Average_str += str("+")
            Form_Average_str += str( '{:}'.format(Data_11[2]) )
            Form_Average_str += str( "+\cdots+" )
            Form_Average_str += str( '{:}'.format(Data_11[Data_11_N-1]) )
        else :
            for i in range(Data_11_N):
                if i == 0 :
                    Form_Average_str += str( '{:}'.format(Data_11[i]) )
                else:
                    Form_Average_str += str( '{:+}'.format(Data_11[i]) )
        """
            $$
                \\begin{align*}
                    \\overline{x} &= \\frac{1}{%s}\\Big( %s \\Big)
                    \\\\
                    \\\\
                    &=\\frac{%s}{%s}
                    \\\\
                    \\\\
                    &=%s
                \\end{align*}
            $$
        """\
        %(  Data_11_N,Form_Average_str,\
            Data_11_Total,Data_11_N,\
            Data_11_Total/Data_11_N
        )

with variance_tab[2]:
    st.markdown("#### 平均値から推測できること")
