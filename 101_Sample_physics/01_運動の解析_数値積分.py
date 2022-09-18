import streamlit as st
import pandas as pd
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import patches
# from matplotlib.patches import Ellipse, Polygon
from mpl_toolkits.mplot3d import Axes3D





def import_data():
    select_data_list={"サンプルデータを利用":0,\
                    "CSVファイルをアップロードし利用":1
                    }
    select_data_00 = st.selectbox("📝　実例の計算に使用するデータを選択",
                                    (list(select_data_list.keys()))
                                    )
    Data_00 = None
    select_data_n = select_data_list[select_data_00]
    if select_data_list[select_data_00] == 0:
        try:
            Data_00= pd.read_csv("./Sample_data_01.csv")
        except:
            data_link = "101_Sample_physics/Sample_data_01.csv"
            Data_00= pd.read_csv(data_link)
        tmp_title_tub01="#### 入力データの確認（サンプルデータ）を利用"

    elif select_data_list[select_data_00] == 1:
        Data_00= pd.read_csv("./Sample_data_01.csv")
        uploaded_file = st.sidebar.file_uploader("CSVファイルを選択", type={"csv"})
        if uploaded_file:
            try :
                Data_00= pd.read_csv(uploaded_file)
            except:
                Data_00= pd.read_csv(uploaded_file,encoding="SHIFT-JIS")          
            tmp_title_tub01="#### 入力データの確認（"+str(uploaded_file.name)+"）を利用"
    return Data_00,select_data_n

### グローバル変数の定義 ###
st.title("#### 加速度運動の解析")

acceleration_motion_ana_list=["等加速度運動直線運動","等加速度運動","加速度運動","実験データの解析"]
acceleration_motion_ana_tab =[]
acceleration_motion_ana_tab = st.tabs(acceleration_motion_ana_list)
with acceleration_motion_ana_tab[2]:
    st.markdown("#### 一般の加速度運動について")
    """
    空間中を運動する質量$~m\ \\rm [kg]~$を考える．時刻$~t\\rm [s]~$での，
    この質点の加速度を$~\overrightarrow{a}\ \\rm [m/s]~$，
    速度を$~\overrightarrow{v} \ \\rm[m/s]~$，
    位置を$~\overrightarrow{r} \ \\rm[m]~$とする．
    $$
        \\begin{align*}
            \overrightarrow{v} = \\frac{dr}{dt}
        \\end{align*}
    $$
    という関係がある．
    """
with acceleration_motion_ana_tab[3]:
    Data_00,select_data_n = import_data()
    select_data_n = int(select_data_n)
    st.session_state["Data_00"] = Data_00
    st.dataframe(Data_00.T)


