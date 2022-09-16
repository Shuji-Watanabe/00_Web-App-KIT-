import streamlit as st

### Main program ###
st.markdown("### ５．相関係数について")
correlation_coefficient_list00=["相関係数の定義","実例","相関係数によるデータ分析","ベクトルの類似性と相関係数"]
correlation_coefficient_tab=[]
correlation_coefficient_tab=st.tabs(correlation_coefficient_list00)
with correlation_coefficient_tab[0]:
    st.markdown("#### 変量$~X~$と$~Y~$の相関係数$~\\gamma~$の定義")
    """
        ２つの変量$~X,\ Y~$の組み$~\\big(X,\\ Y\\big)~$について
        $~N~$個のデータ
        $$
        \\Big[
            \\big(x_1, y_1\\big)
            ,\ 
            \\big(x_2, y_2\\big)
            ,\ 
            \\big(x_3, y_3\\big)
            ,\ 
            \\cdots
            ,\ 
            \\big(x_N, y_N\\big)
        \\Big]
        $$
        があるとき，変量$~X,\ Y~$の相関係数$~\\gamma~$とは，
        $$ 
            \\gamma
            =
            \\frac{s_{xy}}{s_x \cdot s_y}
        $$
        で与えられる値である．
        ここで$~s_{xy}~$は変量$~X,\\ Y~$の共分散であり，$~s_x~$と$~s_y~$は
        それぞれ変量$~X~$と変量$~Y~$の標準偏差である．
        \n\n
    """
with correlation_coefficient_tab[1]:
    st.markdown("#### 共分散$~s_{xy}~$とその他の統計量との関係")
    """
        ２つの変量$~X~$と変量$~Y~$の組み$~\\big(X,\\ Y\\big)~$について$~N~$個のデータがあり，
        $~i~$番目のデータを$~\\big(x_i,\\ y_i\\big)~$と表す．
        $~x_iy_i~$で得られる$~N~$個のデータ
        $~\\big( x_1y_1,\ x_2y_2,\ x_3y_3,\ \cdots,\\ x_Ny_N \\big)~$
        の平均値を
        $$ 
            \\overline{xy}
            =
            \\frac{1}{N}
            \\Big(
                x_1y_1 + x_2y_2 + \cdots + x_Ny_N
            \\Big)
        $$
        ，変量$~X~$の平均値を$~\\overline{x}$，データ$~Y~$の平均値を$\\overline{y}~$とすると，
        変量$~X,\ Y~$の共分散$~s_{xy}~$は
        $$
            s_{xy}= \\overline{xy} - \\overline{x}\cdot \\overline{y}
        $$
        を計算することによっても求められる．
    """
with correlation_coefficient_tab[2]:
    Data_00=st.session_state["Data_00"]
    st.dataframe(Data_00.T)

with correlation_coefficient_tab[3]:
    st.write("標本標準偏差と母標準偏差")