import streamlit as st

### Main program ###
st.markdown("### ６．単回帰直線の式について")
correlation_coefficient_list00=["単回帰直線の式の導出の流れ","実例","単回帰直線によるデータ分析"]
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