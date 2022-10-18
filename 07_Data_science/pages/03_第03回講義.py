import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import pingouin as pg
import math as math

Lec03_contents_list=["偏相関係数について","偏相関係数を用いた分析"]
Lec03_contents_tab =[]
Lec03_contents_tab = st.tabs(Lec03_contents_list)
contents_num =0
st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/MKA4kBiXPRiMzrju9) """)
#### 1st contents #########
#contents_num +=1
with Lec03_contents_tab[contents_num]:
    st.markdown("### %s.　%s"%(contents_num+1,Lec03_contents_list[contents_num]))
    #### 偏相関係数（3変量の場合）
    with st.container():
        """
        #### 偏相関係数とは
        3つの変量$X,\\ Y,\\ Z$があり，$X,\\ Y$がともに$Z$の影響を受ける場合，
        $X,\\ Y$から$Z$の影響を除いた変量$X',\\ Y'$の間の相関係数を**偏相関係数**という．
        
        　また変量が$~n~$個ある場合，ある2つの変量からそれ以外の変量の影響を除いた偏相関係数は
        相関係数行列を利用し求めることができる．

        　それ以外に，相関を求めたい対象となる２つの変量とそれ以外の変量の関係性について分析者が考察し，
        特定の変量の影響だけを取り除くことも可能である．
        """
        " "
        """
        #### 偏相関係数の求め方（３変量の場合）
        3つの変量$~X,\\ Y,\\ Z~$について，
        $X,\\ Y~$の相関係数を$~r_{xy}~$，
        $X,\\ Z~$の相関係数を$~r_{xz}~$，
        $Y,\\ Z~$の相関係数を$~r_{yz}~$とすると，
        $Z$の影響を除いた$~X,\\ Y~$の偏相関係数$~r_{xy:z}~$は
        $$
            r_{xy:z}
                = \\frac
                    { r_{xy} - r_{xz}r_{yz} }
                    { \sqrt{1 - r_{xz}^2} 
                    \sqrt{1 - r_{yz}^2} }
        $$
        によって得られる．
        ここでこの式を導出する際に用いた「$Z$の影響を除いた$~X,\\ Y~$」をそれぞれ$~\\tilde{X},\\ \\tilde{Y}~$とすると
        $$
        \\begin{align*}
        \\tilde{X} 
            &= X
            -
            \\bigg\{  \\frac{r_{xz}}{\sigma^2_z}\\big( Z- \mu_z \\big) + \mu_x\\bigg\}
        \\\\
            \\tilde{Y} 
            &= Y
            -
            \\bigg\{  \\frac{r_{yz}}{\sigma^2_y}\\big( Z- \mu_z \\big) + \mu_y\\bigg\}
        \\end{align*}
        $$
        で表される．
        """
        
        with st.expander("偏相関係数を用いる際の注意"):
            """
            この分析における「$~X~$に対する$~Z~$の影響」は「$~X~$と$~Z~$の単回帰式」で評価されていること，
            そして「$~Z~$の影響を除いた$~X~$」は，その残差に対応していることに注意してほしい．
            「$~Z~$の影響を除いた$~Y~$」も同様に単回帰式に基づいた分析が行われている．

            つまり$~Z~$と$~X,\\ Y~$の間の関係が，単回帰式でうまく表現できない場合，偏相関係数は
            $~X~$と$~Y~$の間の分析において，有益な情報を与えないことに注意してほしい．
            """
        """
        #### 偏相関係数の求め方（3変量以上の場合）
        """
        st.error("作成中")
#### 2nd contents Partial_Correlation_Coefficient ~Example~ #########
contents_num +=1
with Lec03_contents_tab[contents_num]:
    st.markdown("### %s.　%s"%(contents_num+1,Lec03_contents_list[contents_num]))


    #-----  section 1 : data input -----------------------------------------------
    section_num = 1 
    #== data input ===
    select_data_list={"サンプルデータを利用":0,\
                        "CSVファイルをアップロードし利用":1
                        }
    select_data_00 = st.sidebar.selectbox("📝　実例の計算に使用するデータを選択",
                                        (list(select_data_list.keys()))
                                        )
    inputdata_lec3_tub2 = None
    if select_data_list[select_data_00] == 0:
        try:
            data_link = "./Partial_Correlation_Coefficient_sample01.csv"
            inputdata_lec3_tub2 = pd.read_csv(data_link)
        except:
            data_link = "07_Data_science/Partial_Correlation_Coefficient_sample01.csv"
            inputdata_lec3_tub2 = pd.read_csv(data_link)
        section_title01="##### %s-%s　入力データの確認（サンプルデータを利用）"%(contents_num+1,section_num)

    elif select_data_list[select_data_00] == 1:
        uploaded_file = st.sidebar.file_uploader("CSVファイルを選択", type={"csv"})
        if uploaded_file:
            try :
                Data_00= pd.read_csv(uploaded_file)
            except:
                Data_00= pd.read_csv(uploaded_file,encoding="SHIFT-JIS")          
            section_title01="##### %s-%s　入力データの確認（"+str(uploaded_file.name)+"を利用）"%(contents_num+1,section_num)
    st.markdown(section_title01)
    st.write("")


    #== Display a dataframe ===
    st.dataframe(inputdata_lec3_tub2)
    if select_data_list[select_data_00] == 0:
        with st.expander("引用元"):
            st.info(\
                """
                - 気象データ：
                    気象庁
                    [クリック](https://www.data.jma.go.jp/gmd/risk/obsdl/index.php)，
                    （2022年10月17日データ取得）
                - アイスクリームの売上データ：
                    日本アイスクリーム協会
                    [クリック](https://www.icecream.or.jp/iceworld/data/expenditures.html)，
                    （2022年10月17日データ取得）
                """, \
                )

    #-----  section 2 : Dispay a pairplot -----------------------------------------------
    section_num += 1 
    section_title02="##### %s-%s　散布図行列（ペアプロット図）"%(contents_num+1,section_num)
    st.markdown(section_title02)
    sns.pairplot(inputdata_lec3_tub2,corner=True,kind='reg')
    st.pyplot(plt)
    st.write(" ")

    #-----  section 3 : Dispay a Correlation coefficient matrix --------------------------
    section_num += 1 
    section_title03="##### %s-%s　相関係数行列"%(contents_num+1,section_num)
    st.markdown(section_title03)
    Correlation_Coefficient_Matrix = inputdata_lec3_tub2.corr()
    st.dataframe(Correlation_Coefficient_Matrix)
    if select_data_list[select_data_00] == 0:
        with st.expander("サンプルデータの相関係数行列から読み取るデータの特徴と分析の例"):
            """
            ###### $\\blacksquare\ $相関係数行列で見るデータの特徴
            - **強い正の相関がある変量**\\
                平均気温とアイスへの支出
            - **正の相関がある変量**\\
                平均気温と日照時間，日照時間とアイスへの支出
            - **弱い負の相関がある変量**\\
                降水量の合計と平均気温，降水量とアイスへの支出
            - **負の相関がある変量**\\
                降水量の合計と日照時間
            """
            " "
            """
            ###### $\\blacksquare\ $相関関係に関する考察の例
            - 正：平均気温が高い（低い）とアイスへの支出も多い（少ない）\\
              正：アイスへの支出が大きい（小さい）と平均気温も高い（低い）
            
            - 正：平均気温が高い（低い）と日照時間も長い（短い）\\
              正：日照時間が長い（短い）と平均気温も高い（低い）
            
            - 正：日照時間が長い（短い）とアイスへの支出も大きい（小さい）\\
              正：アイスへの支出も大きい（小さい）と日照時間が長い（短い）
            """
            " "
            """
            ###### $\\blacksquare\ $因果関係に関する考察の例
            - 正：平均気温が高く（低く）なることによって，アイスへの支出が多く（少なく）なる\\
              誤：アイスへの支出が多く（少なく）なることによって，平均気温が高く（低く）なる
                         
            - 誤：平均気温が高く（低く）なることによって，日照時間が長く（短く）なる\\
              正：日照時間が長く（短く）なることによって，平均気温が高く（低く）なる
            
            - ？：日照時間が長く（短く）なることによって，アイスへの支出も大きく（小さく）なる\\
              誤：アイスへの支出が大きく（小さく）なることによって，日照時間が長くなる（短くなる）
            """

            caution=""""
                    因果関係の考察にあたっては，物理的な知見や生理学的な知見などを考慮し，慎重に進める必要がある．
                    上記の考察例はあくまでも「日照時間」が「アイスへの支出」に直接的な因果関係を持って影響を与えるのか
                    という問題提起を行うための考察である．
                    """
            st.error(caution)
    st.write(" ")
    
    #-----  section 3 : Dispay a Correlation coefficient matrix --------------------------
    section_num += 1 
    section_title03="##### %s-%s　偏相関係数行列"%(contents_num+1,section_num)
    st.markdown(section_title03)
    partial_corr_matrix = pg.pcorr(inputdata_lec3_tub2)
    st.dataframe(partial_corr_matrix)


    #===  日照時間とアイスへの支出から平均気温の影響を除いたデータの偏相関係数 ===
    tmp_df = Correlation_Coefficient_Matrix
    partial_corr_34 = tmp_df.iat[3,2] - tmp_df.iat[2, 1]*tmp_df.iat[3, 1]
    partial_corr_34 =partial_corr_34/math.sqrt((1-tmp_df.iat[2, 1]**2)*(1-tmp_df.iat[3, 1]**2))
    partial_corr_34_str="""
        $$
        r_{34:2} 
        = 
            \\frac
            { %.4f - \\big(%.4f\\big) \cdot \\big(%.4f\\big) }
            { \\sqrt{ 
                    \\left\{ 1- \\big(%.4f\\big)^2 \\right\}
                    \cdot
                    \\left\{ 1- \\big(%.4f\\big)^2 \\right\}
                    }
            }
        =
        %.4f
        $$
    """%(
        tmp_df.iat[3,2], tmp_df.iat[2, 1] , tmp_df.iat[3, 1],
        tmp_df.iat[2, 1] , tmp_df.iat[3, 1],
        partial_corr_34
        )
    if select_data_list[select_data_00] == 0:
            with st.expander("サンプルデータの偏相関係数行列から読み取るデータの特徴と分析の例"):
                """
                ###### $\\blacksquare\ $偏相関係数行列で見るデータの特徴
                - **強い正の相関がある変量**\\
                    平均気温とアイスへの支出
                - **弱い正の相関がある変量**\\
                    日照時間とアイスへの支出
                - **ほとんど相関なし**\\
                    降水量の合計と平均気温，降水量の合計とアイスへの支出，平均気温と日照時間
                - **負の相関がある変量**\\
                    降水量の合計と日照時間
                """
                " "
                """
                ###### $\\blacksquare\ $相関関係に関する考察の例
                - 正：平均気温が高い（低い）とアイスへの支出も多い（少ない）\\
                    正：アイスへの支出が大きい（小さい）と平均気温も高い（低い）
                
                """
                " "
                """
                ###### $\\blacksquare\ $因果関係に関する考察の例
                - 正：平均気温が高く（低く）なることによって，アイスへの支出が多く（少なく）なる\\
                    誤：アイスへの支出が多く（少なく）なることによって，平均気温が高く（低く）なる
                """

                " "
                """
                ###### $\\blacksquare\ $日照時間とアイスへの支出の相関係数と偏相関係数の比較
                - $0.6859$：日照時間とアイスへの支出の相関係数
                - $0.2501$：日照時間とアイスへの支出から平均気温と降水量の影響を除いた偏相関係数
                - $0.2406$：日照時間とアイスへの支出から平均気温を除いた偏相関係数
                """
                " "
                caution="""
                        偏相関係数を通して日照時間とアイスへの支出の関係性を見ると，
                        相関係数で見た関係性に比べて，大幅に関係性が小さくなっている．
                        つまり，日照時間とアイスへの支出から平均気温と降水量の影響を
                        除いた場合，日照時間とアイスへの支出の関係性が小さくなることから
                        日照時間とアイスへの支出に対して，平均気温と降水量が大きく影響していたことがわかる．
                        ここで，日照時間とアイスへの支出に対して平均気温の影響だけを除いた
                        偏相関係数は
                        となるので，日照時間とアイスへの支出の偏相関係数は平均気温の影響でほぼ説明できると
                        考えられる．
                        """
                st.error(caution)                