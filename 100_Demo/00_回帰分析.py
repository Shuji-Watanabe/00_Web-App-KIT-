import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from decimal import Decimal
#from sklearn.linear_model import LinearRegression

### 使用するファイルの選択 ###

select_data_list={"サンプルデータを利用":0,\
                    "CSVファイルをアップロードし利用":1
                    }
select_data_00 = st.sidebar.selectbox("📝　実例の計算に使用するデータを選択",
                                    (list(select_data_list.keys()))
                                    )
Data_00 = None
if select_data_list[select_data_00] == 0:
    try:
        Data_00= pd.read_csv("./data0000.csv")
    except:
        data_link = "100_Demo/data0000.csv"
        Data_00= pd.read_csv(data_link)
    tmp_title_tub01="#### 入力データの確認（サンプルデータ）を利用"

elif select_data_list[select_data_00] == 1:
    Data_00= pd.read_csv("./data0000.csv")
    uploaded_file = st.sidebar.file_uploader("CSVファイルを選択", type={"csv"})
    if uploaded_file:
        try :
            Data_00= pd.read_csv(uploaded_file)
        except:
            Data_00= pd.read_csv(uploaded_file,encoding="SHIFT-JIS")          
        tmp_title_tub01="#### 入力データの確認（"+str(uploaded_file.name)+"）を利用"
    

### グローバル変数の定義 ###
st.session_state["Data_00"] = Data_00

### Main program ###
st.title("### 単回帰分析")
single_regression_ana_list=["単回帰分析とは","単回帰式の導出","単回帰分析の例（実行結果）"]
single_regression_ana_tab = []
single_regression_ana_tab = st.tabs(single_regression_ana_list)

with single_regression_ana_tab[0]:
    st.markdown("#### 単回帰分析とは")
    """
    身長と体重や，価格と売り上げのように，
    ２つの変量$~X,\ Y~$の組み$~\\big(X,\ Y\\big)~$で得られるデータがあるとき，
    一方の変量でもう一方の変量を表すことを考える．
    変量$~X~$と変量$~Y~$の間に
    $$
    y=ax+b
    $$
    という関係があることを仮定し，変量$~X~$と変量$~Y~$の関係を分析することを単回帰分析と呼ぶ．
    単回帰分析によって得られる式$~y=ax+b~$は単回帰式（線形回帰式）とも呼ばれ，
    変量$~X~$から変量$~Y~$を予測する際に用いられる．
    """

with single_regression_ana_tab[1]:
    st.markdown("#### 単回帰式")
    """
        ２つの変量$~X,\ Y~$の組み$~\\big(X,\ Y\\big)~$について，$~N~$個のデータがあり，
        変量$~X~$を説明変数，変量$~Y~$を目的変数とする．
        このとき，変量$~X~$と変量$~Y~$の間に成り立つ関係性を表した式
        $$
            y=\\frac{s_{xy}}{s^2_x}\\big(x-\\overline{x}\\big)+\\overline{y}
        $$
        を単回帰式と呼ぶ．ここで$~\\overline{x}~$は変量$~X~$の平均値，
        $\\overline{y}~$は変量$~Y~$の平均値，
        $~s_{xy}~$は変量$~X,\\ Y~$の共分散，
        $~s^2_x~$は変量$~X~$の分散である．
    """
    st.markdown("#### 単回帰式を求める流れ（公式の導出の流れ）")
    """
        1. ２つの変量$~X,\ Y~$の組み$~\\big(X,\ Y\\big)~$に対して，
            $$
                y=ax+b
            $$
            という関係を仮定する．
        2.  $~i~$番目のデータ$~\\big(x_i,\ y_i\\big)~$について，
            $y=ax+b$で予測した変量$~Y~$の値$~ax_i+b~$の値と実際の値$~y_i~$に対して
            $$
            \\begin{align*}
                E
                &=\\frac{1}{N}
                    \\Big[
                        \\big\\{y_1-(ax_1+b)\\big\\}^2 
                        +
                        \\big\\{y_2-(ax_2+b)\\big\\}^2 
                        +
                        \\cdots
                        +
                        \\big\\{y_N-(ax_N+b)\\big\\}^2 
                    \\Big] 
                \\\\
                &=\\frac{1}{N}
                    \\sum_i^N
                        \\big\\{y_i-(ax_i+b)\\big\\}^2 
            \\end{align*}
            $$
            という量$~E~$を求める．ここで$~N~$はデータ数である．
        3.  $~E~$が最小となる$~a,\ b~$を求める．
    """

with single_regression_ana_tab[2]:
    ### 説明変数（X）と目的変数（Y）の設定 
    if Data_00 is None:
        st.write("データなし．「データの選択」で利用するデータを選択してください．")
    else:
        Col_name = list(Data_00.columns.values)
        Data_ana_col_01 = []
        Data_ana_col_01 = st.columns(2) 
        with Data_ana_col_01[0]:
            tmp_x = st.selectbox(
                            "説明変数に利用するデータを選択してください．",
                            Col_name,key=1
                            )
        with Data_ana_col_01[1]:
            tmp_y = st.selectbox(
                            "目的変数に利用するデータを選択してください．",
                            Col_name,key=2
                            )
        Data_Ana01_var01 = [tmp_x,tmp_y]
    if "Data_Ana01_var01" not in st.session_state:
        st.session_state["Data_Ana01_var01"] = Data_Ana01_var01
    
    ### データ分析（基本統計量の計算） 
    if st.button("データの分析結果を表示"):
        Data_ana_col_02 = []
        Data_ana_col_02 = st.columns(2) 
        ### 説明変数Xについての基本統計量の計算 
        with Data_ana_col_02[0]:
            Data_Ana01_Str_X = "##### ■"+str(Data_Ana01_var01[0])+"の統計量"
            st.markdown(Data_Ana01_Str_X)
            st.write("   -- 最大値 =",str(Data_00[Data_Ana01_var01[0]].max()),
                    " \n -- 最小値 =",str(Data_00[Data_Ana01_var01[0]].min()),
                    " \n -- 合計値 =",str(Data_00[Data_Ana01_var01[0]].sum()),   
                    " \n -- 平均値 =",str(Data_00[Data_Ana01_var01[0]].mean()),
                    " \n -- 分　散 =",str(Data_00[Data_Ana01_var01[0]].var(ddof=0)),
                    " \n -- 標準偏差 =",str(Data_00[Data_Ana01_var01[0]].std(ddof=0)),
                    " \n")                     
        ### 説明変数Xについての基本統計量の計算 
        with Data_ana_col_02[1]:
            Data_Ana01_Str_Y = "##### ■"+str(Data_Ana01_var01[1])+"の統計量"
            st.markdown(Data_Ana01_Str_Y)
            st.write("   -- 最大値 =",str(Data_00[Data_Ana01_var01[1]].max()),
                    " \n -- 最小値 =",str(Data_00[Data_Ana01_var01[1]].min()),
                    " \n -- 合計値 =",str(Data_00[Data_Ana01_var01[1]].sum()),   
                    " \n -- 平均値 =",str(Data_00[Data_Ana01_var01[1]].mean()),
                    " \n -- 分　散 =",str(Data_00[Data_Ana01_var01[1]].var(ddof=0)),
                    " \n -- 標準偏差 =",str(Data_00[Data_Ana01_var01[1]].std(ddof=0)),
                    " \n")        
                                 
        ### 共分散と相関係数の計算
        Data_ana_col_03 = []
        Data_ana_col_03 = st.columns(2) 
        with Data_ana_col_03[0]:
            da1st_col21_str01 = "##### ■共分散と相関係数"
            st.markdown(da1st_col21_str01)
            if Data_Ana01_var01[0] == Data_Ana01_var01[1]:
                st.write("同じデータ同士です．")
            else:
                Data_Ana01_matrix01 = pd.concat([Data_00[Data_Ana01_var01[0]],Data_00[Data_Ana01_var01[1]]],axis='columns')
                Cov_matrix = Data_Ana01_matrix01.cov()
                Corr_matrix = Data_Ana01_matrix01.corr()
                Sxy = Cov_matrix.iat[1,0]
                rxy = Corr_matrix.iat[1,0]
                Ave_x = Data_00[Data_Ana01_var01[0]].mean()     
                Ave_y = Data_00[Data_Ana01_var01[1]].mean()
                ver_x = Data_00[Data_Ana01_var01[0]].var(ddof=0)
                y_a =  Sxy/ver_x
                y_b = Ave_y - y_a * Ave_x
                st.write(
                        "    -- 共分散 =",(str(Sxy)),
                        " \n -- 相関係数 =",(str(rxy)),
                        " \n")
                st.markdown("##### ■回帰直線の式")
                Form_SRL = str("y=") \
                            + str('{:.2f}'.format(y_a)) \
                            + str("x")\
                            + str('{:+.2f}'.format(y_b))
                st.latex(Form_SRL)


        with Data_ana_col_03[1]:
            st.markdown("##### ■散布図と回帰直線")
            fig = plt.figure(figsize = (6,6))
            
            # ライブラリを利用した回帰直線
            # mod = LinearRegression()
            # df_x = pd.DataFrame(Data_00[Data_Ana01_var01[0]])
            # df_y = pd.DataFrame(Data_00[Data_Ana01_var01[1]])
            # # 線形回帰モデル、予測値、R^2を評価
            # mod_lin = mod.fit(df_x, df_y)
            # y_lin_fit = mod_lin.predict(df_x)
            # plt.plot(df_x,y_lin_fit, color = 'red', linewidth=1.0)
            
            l_max=Data_00[Data_Ana01_var01[0]].max()
            l_min=Data_00[Data_Ana01_var01[0]].min()
            x = np.linspace(l_min,l_max, 10)
            y = y_a * x + y_b
            plt.plot(x,y, color = 'red', linewidth=2.0)

            plt.scatter(Data_00[Data_Ana01_var01[0]],Data_00[Data_Ana01_var01[1]])
            plt.xlabel("説明変数 : "+Data_Ana01_var01[0],fontsize = 15)
            plt.ylabel("目的変数 : "+Data_Ana01_var01[1],fontsize = 15)
            st.pyplot(fig)
