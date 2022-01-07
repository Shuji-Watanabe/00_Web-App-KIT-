
def View_data(Data_00, App_num):
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
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
    st.line_chart(chart_data,height=400)
    
    fig = plt.figure(figsize=(12,9))
    ax  = plt.axes()
    x   = Data_00.loc[:,Col_name[0]]
    y1  = Data_00.loc[:,Col_name[3]]
    y2  = Data_00.loc[:,Col_name[6]]
    plt.plot(y1,y2)
    st.pyplot(fig)
