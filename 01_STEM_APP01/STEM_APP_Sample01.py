import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import math

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
Data_file00= st.file_uploader("**データファイルをアップロードしてください**", type={"csv", "txt"})
if Data_file00:
    Data_00= pd.read_csv(Data_file00,encoding="SHIFT-JIS")
    
    ##### １）入力データの表示（開始）#####
    st.write("## **Step01:入力されたデータの確認**")
    st.dataframe(Data_00)
    Col_name = list(Data_00.columns.values)
    MS_View_data01 = st.multiselect(
                            "プロットしたいデータを選択してください．",
                             Col_name,
                            key="View_data_key01"
                            )
    p_list = MS_View_data01
    chart_data = Data_00.loc[:,p_list]
    #st.dataframe(chart_data)
    #st.line_chart(chart_data,height=400)
    ##### 入力データの表示（終了）#####
    
    p = figure(
        title='simple line example',
        x_axis_label='x',
        y_axis_label='y')
    
    p.line(x, y,line_width=2)
    st.bokeh_chart(p, use_container_width=True)