import streamlit as st

### Main program ###
st.markdown("### ４．共分散について")
covariance_list00=["共分散の定義","その他の統計量との関係","実例","共分散によるデータ分析"]
covariance_tab=[]
covariance_tab=st.tabs(covariance_list00)
with covariance_tab[0]:
    st.markdown("#### 変量$~X~$と$~Y~$の共分散$~s_{xy}~$の定義")
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
        があるとき，変量$~X,\ Y~$の共分散$~s_{xy}~$とは，
        $$ 
            s_{xy}
            =
                \\frac{1}{N}
                \\Big\\{
                     \\big(x_1- \\overline{x}\\big)
                     \\big(y_1- \\overline{y}\\big)
                    +\\big(x_2- \\overline{x}\\big)
                     \\big(y_2- \\overline{y}\\big)
                    + \cdots
                    +\\big(x_N- \\overline{x}\\big)
                     \\big(y_N- \\overline{y}\\big)
                \\Big\\}
        $$
        で与えられる値である．これは総和記号$~\\Sigma~$を用いて，
        $$ 
            s_{xy}
            =
                \\frac{1}{N}
                \\sum_{i=1}^N 
                    \\Big( x_i - \\overline{x}\\Big)
                    \\Big( y_i - \\overline{y}\\Big)
        $$
        と表すことができる．ここで$~\\overline{x}~$と$~\\overline{y}~$は,
        それぞれ変量$~X~$と変量$~Y~$の平均値である．
        \n\n
    """
with covariance_tab[1]:
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
with covariance_tab[2]:
    Data_00=st.session_state["Data_00"]
    st.dataframe(Data_00.T)

with covariance_tab[3]:
    st.write("標本標準偏差と母標準偏差")