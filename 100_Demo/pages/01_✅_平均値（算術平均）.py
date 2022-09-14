import streamlit as st

### Main program ###
st.markdown("### １．平均値$~\\overline{x}~$について")
variance_list00=["平均値の定義","計算方法の実例","データ分析例"]
variance_tab=[]
# variance_tab1, variance_tab2, variance_tab3=st.tabs(variance_list00)
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

with variance_tab[2]:
    st.markdown("#### データ分析")
