import streamlit as st
import pandas as pd
import math as math

Lec01_contents_list = ["相関関係と相関係数", "例：相関係数行列の計算"]
Lec01_contents_tab = []
Lec01_contents_tab = st.tabs(Lec01_contents_list)
contents_num = 0
st.sidebar.markdown(
    """このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/MKA4kBiXPRiMzrju9) """)
#### 1st contents #########
#contents_num +=1
with Lec01_contents_tab[contents_num]:
    st.markdown("### %s.　%s" %
                (contents_num+1, Lec01_contents_list[contents_num]))


#### 2nd contents Partial_Correlation_Coefficient ~Example~ #########
contents_num += 1
with Lec01_contents_tab[contents_num]:
    st.markdown("### %s.　%s" %
                (contents_num+1, Lec01_contents_list[contents_num]))

    # -----  section 1 : data input -----------------------------------------------
    section_num = 1
    # == data input ===
    select_data_list = {"サンプルデータを利用": 0,
                        "CSVファイルをアップロードし利用": 1
                        }
    select_data_00 = st.sidebar.selectbox("📝　実例の計算に使用するデータを選択",
                                          (list(select_data_list.keys()))
                                          )
    input_data_df = None
    if select_data_list[select_data_00] == 0:
        try:
            input_data_fname = "./PropertyInformation_nonoichi.csv"
            input_data_df = pd.read_csv(input_data_fname)
        except:
            input_data_fname = "07_Data_science/PropertyInformation_nonoichi.csv"
            nput_data_df = pd.read_csv(input_data_fname)
        section_title01 = f"##### {contents_num+1}-{section_num}　入力データの確認（サンプルデータを利用）"

    elif select_data_list[select_data_00] == 1:
        uploaded_file_csv = st.sidebar.file_uploader("CSVファイルを選択", type={"csv"})
        if uploaded_file_csv:
            try:
                input_data_df = pd.read_csv(uploaded_file_csv)
            except:
                input_data_df = pd.read_csv(uploaded_file_csv, encoding="SHIFT-JIS")
            section_title01 = f"##### {contents_num+1}-{section_num}　入力データの確認（アップロードされたファイルを利用）" 
    st.markdown(section_title01)
    st.write("")
    if st.checkbox("データの確認"):
        st.dataframe(input_data_df)

    input_data_keys = input_data_df.keys()
    
st.error("作成中")