import streamlit as st

### Main program ###
st.markdown("### ３．標準偏差について")
standard_deviation_list00=["定義","その他の統計量との関係","実例","データ分析例"]
standard_deviation_tab=[]
standard_deviation_tab=st.tabs(standard_deviation_list00)
with standard_deviation_tab[0]:
    st.markdown("#### 変量$~X~$の分散$~s_x~$の定義")
    """
        変量$~X~$について$~N~$個のデータ$~\\big[x_1,\ x_2,\ x_3,\ \cdots,\ x_N\\big]~$があるとき，
        変量$~X~$の標準偏差$~s_x~$とは，
        $$ 
            s_x
            =
            \\sqrt{
                \\frac{1}{N}
                \\Big\\{
                \\big(x_1- \\overline{x}\\big)^2
                    +\\big(x_2- \\overline{x}\\big)^2
                    +\\big(x_3- \\overline{x}\\big)^2
                    + \cdots
                    +\\big(x_N- \\overline{x}\\big)^2
                \\Big\\}
                }
        $$
        で与えられる値である．これは総和記号$~\\Sigma~$や変量$~X~$の分散$~s_x^2~$を用いて，
        $$ 
            s_x
            =
            \\sqrt{
                \\frac{1}{N}
                \\sum_{i=1}^N \\Big( x_i - \\overline{x}\\Big)^2
            }
        $$
        と表すことができる．
        \n\n
    """
with standard_deviation_tab[1]:
    st.markdown("#### とその他の統計量との関係")
    """
        変量$~X~$の標準偏差$~s_x~$は，変量$~X~$の分散$~s_x^2~$を用いて，
        $$ 
            s_x
            =
            \sqrt{s_x^2}
        $$
        と表すことができる．
        \n\n
    """
with standard_deviation_tab[2]:
    Data_00=st.session_state["Data_00"]
    st.dataframe(Data_00.T)

with standard_deviation_tab[3]:
    st.write("標本標準偏差と母標準偏差")
