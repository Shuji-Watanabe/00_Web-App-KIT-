import streamlit as st
import pandas as pd
import math as math
import altair as alt

Lec01_contents_list = ["クロス集計について", "クロス集計を用いた分析"]
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
    inputdata_lec1_tub2 = None
    if select_data_list[select_data_00] == 0:
        try:
            data_link = "./PropertyInformation_nonoichi.csv"
            inputdata_lec1_tub2 = pd.read_csv(data_link)
        except:
            data_link = "07_Data_science/PropertyInformation_nonoichi.csv"
            inputdata_lec1_tub2 = pd.read_csv(data_link)
        section_title01 = "##### %s-%s　入力データの確認（サンプルデータを利用）" % (
            contents_num+1, section_num)

    elif select_data_list[select_data_00] == 1:
        uploaded_file = st.sidebar.file_uploader("CSVファイルを選択", type={"csv"})
        if uploaded_file:
            try:
                inputdata_lec1_tub2 = pd.read_csv(uploaded_file)
            except:
                inputdata_lec1_tub2 = pd.read_csv(
                    uploaded_file, encoding="SHIFT-JIS")
            section_title01 = "##### %s-%s　入力データの確認（アップロードされたファイルを利用）" % (
                contents_num+1, section_num)
    st.markdown(section_title01)
    st.write("")

    # == Display a dataframe ===
    st.dataframe(inputdata_lec1_tub2)
    if select_data_list[select_data_00] == 0:
        with st.expander("引用元"):
            st.info(
                """
                    無し（自作データ）
                    """,
            )
        count = [1 for i in range(len(inputdata_lec1_tub2['築年数']))]
        yearsConstruction = []
        for i in inputdata_lec1_tub2['築年数']:
            if 0 < i <= 5:
                yearsConstruction.append('1~5年目')
            elif 5 < i <= 10:
                yearsConstruction.append('6~10年目')
            elif 10 < i <= 15:
                yearsConstruction.append('11~15年目')
            elif 15 < i <= 20:
                yearsConstruction.append('16~20年目')
            elif 20 < i <= 25:
                yearsConstruction.append('21~25年目')
            elif 25 < i <= 30:
                yearsConstruction.append('26~30年目')
            elif 30 < i <= 35:
                yearsConstruction.append('31~35年目')
            elif 35 < i <= 40:
                yearsConstruction.append('35~40年目')
            elif 40 < i <= 45:
                yearsConstruction.append('41~45年目')
            elif 45 < i <= 50:
                yearsConstruction.append('46~50年目')
            elif 50 < i <= 55:
                yearsConstruction.append('51~55年目')
        inputdata_lec1_tub2['築年数（5年毎）'] = yearsConstruction
        inputdata_lec1_tub2['物件数'] = count
        stacked_bar = alt.Chart(inputdata_lec1_tub2).mark_bar(size=35).encode(
            x=alt.X('sum(物件数)', axis=alt.Axis(labelFontSize=20,
                    ticks=True, titleFontSize=20, labelAngle=0)),
            y=alt.Y('築年数（5年毎）', axis=alt.Axis(labelFontSize=20, ticks=True, titleFontSize=20, labelAngle=0), sort=[
                '1~5年目', '6~10年目', '11~15年目', '16~20年目', '21~25年目', '26~30年目', '31~35年目', '35~40年目', '41~45年目', '46~50年目', '51~55年目']),
            color='管理費（円）',
            row=alt.Row('タイプ', header=alt.Header(
                labelFontSize=20, titleFontSize=20)),
            tooltip=['物件数', '家賃（円）']
        ).properties(
            width=500,
            height=420,
        )
        st.write(stacked_bar)

    # == Select data from dataFrame ===
