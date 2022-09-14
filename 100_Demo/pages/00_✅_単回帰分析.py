import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from chardet.universaldetector import UniversalDetector
 
def GetFEncod( file_path ) :
    detector = UniversalDetector()
    with open(file_path, mode= "rb" ) as f:
        for binary in f:
            detector.feed( binary )
            if detector.done:
                break
    detector.close()
    return detector.result[ "encoding" ]

def read_make_data_default():
    file_encod_data = GetFEncod( "data0000.csv" )
    Data_00= pd.read_csv("data0000.csv")
    return Data_00

def read_make_data_upload(uploaded_file):
    if uploaded_file :
        try :
            Data_00= pd.read_csv(uploaded_file)
        except:
            Data_00= pd.read_csv(uploaded_file,encoding="SHIFT-JIS")          
    return Data_00

def Data_analysis_1st():
    Col_name = list(Data_00.columns.values)
    da1st_col01, da1st_col02 = st.columns(2) 
    with da1st_col01:
        Data_Ana01_x = st.selectbox(
                        "X軸に利用するデータを選択してください．",
                        Col_name,key=1
                        )
    with da1st_col02:
        Data_Ana01_y = st.selectbox(
                        "Y軸に利用するデータを選択してください．",
                        Col_name,key=2
                        )

    if st.button("データの分析結果を表示"):
        da1st_col11, da1st_col12 = st.columns(2) 
        with da1st_col11:
            da1st_col11_str01 = "##### ■"+str(Data_Ana01_x)+"の統計量"
            st.markdown(da1st_col11_str01)
            st.write("   -- 最大値 =",str(Data_00[Data_Ana01_x].max()),
                    " \n -- 最小値 =",str(Data_00[Data_Ana01_x].min()),
                    " \n -- 合計値 =",str(Data_00[Data_Ana01_x].sum()),   
                    " \n -- 平均値 =",str(Data_00[Data_Ana01_x].mean()),
                    " \n -- 分　散 =",str(Data_00[Data_Ana01_x].var(ddof=0)),
                    " \n -- 標準偏差 =",str(Data_00[Data_Ana01_x].std(ddof=0)),
                    " \n")                     

    
        with da1st_col12:
            da1st_col12_str01 = "##### ■"+str(Data_Ana01_y)+"の統計量"
            st.markdown(da1st_col12_str01)
            st.write("   -- 最大値 =",str(Data_00[Data_Ana01_y].max()),
                    " \n -- 最小値 =",str(Data_00[Data_Ana01_y].min()),
                    " \n -- 合計値 =",str(Data_00[Data_Ana01_y].sum()),   
                    " \n -- 平均値 =",str(Data_00[Data_Ana01_y].mean()),
                    " \n -- 分　散 =",str(Data_00[Data_Ana01_y].var(ddof=0)),
                    " \n -- 標準偏差 =",str(Data_00[Data_Ana01_y].std(ddof=0)),
                    " \n")         

        da1st_col21, da1st_col22 = st.columns(2) 
        with da1st_col21:
            da1st_col21_str01 = "##### ■共分散と相関係数"
            st.markdown(da1st_col21_str01)
            if Data_Ana01_x == Data_Ana01_y:
                st.write("同じデータ同士です．")
            else:
                Data_Ana_01 = pd.concat([Data_00[Data_Ana01_x],Data_00[Data_Ana01_y]],axis='columns')
                Cov_matrix = Data_Ana_01.cov()
                Corr_matrix = Data_Ana_01.corr()
                Sxy = Cov_matrix.iat[1,0]
                rxy = Corr_matrix.iat[1,0]
                Ave_x = Data_00[Data_Ana01_x].mean()     
                Ave_y = Data_00[Data_Ana01_y].mean()
                ver_x = Data_00[Data_Ana01_x].var(ddof=0)
                y_a =  Sxy/ver_x
                y_b = Ave_y - y_a * ver_x
                st.write(
                        "    -- 共分散 =",(str(Sxy)),
                        " \n -- 相関係数 =",(str(rxy)),
                        " \n")
                da1st_col22_str02 = "##### ■回帰直線の式"
                st.markdown(da1st_col22_str02)
                Form_SRL = str("y=") \
                            + str('{:.2f}'.format(y_a)) \
                            + str("x")\
                            + str('{:+.2f}'.format(y_b))
                st.latex(Form_SRL)


        with da1st_col22:
            st.markdown("##### ■散布図と回帰直線")
            fig = plt.figure(figsize = (6,6))
            plt.scatter(Data_00[Data_Ana01_x],Data_00[Data_Ana01_y])
            plt.xlabel(Data_Ana01_x,fontsize = 15)
            plt.ylabel(Data_Ana01_y,fontsize = 15)
            st.pyplot(fig)



### Main program ###
st.title("### 単回帰分析")
Data_00 = None
select_data_00=None
select_data_list=["サンプルデータの利用","CSVファイルをアップロード"]
select_data_00=st.selectbox(
                            "分析にしようするデータの選択",
                            select_data_list
                            )

st.markdown("### １. データの確認")
if select_data_00==select_data_list[0]:
    Data_00 = read_make_data_default()
    st.write("サンプルデータ")
    st.dataframe(Data_00.T)
elif select_data_00==select_data_list[1]:
    uploaded_file = None
    uploaded_file = st.file_uploader("CSVファイルを選択してください．", type={"csv"})
    if uploaded_file:
        Data_00 = read_make_data_upload(uploaded_file)
        st.write("アップロードされたデータ")
        st.dataframe(Data_00.T)


if "Data_00" not in st.session_state:
    st.session_state["Data_00"] = Data_00
  
st.markdown("### ２. データの選択と分析")
if Data_00 is None:
    st.write("データなし")
else:
    Data_analysis_1st()


