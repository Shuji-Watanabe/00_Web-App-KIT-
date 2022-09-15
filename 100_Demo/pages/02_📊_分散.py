import streamlit as st

### Main program ###
st.markdown("### ２．分散$~s^2~$について")
variance_list00=["定義","その他の統計量との関係","計算方法の実例","データ分析"]
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
        のようにもとめることもできる．証明【*クリック*】
        \n\n
    """

with variance_tab[2]:
    Data_00=st.session_state["Data_00"]
    st.dataframe(Data_00.T)

with variance_tab[3]:
    st.write("分散によるデータの評価")
