import streamlit as st
import scipy as sci
import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as Rot


#-----  input data  -----------------------------------------------
section_num = 1 
contents_num = 0
#== input(make dataframe) ===
select_data_list={"サンプルデータを利用":0,\
                    "CSVファイルをアップロードし利用":1
                    }
select_data_00 = st.sidebar.selectbox("📝　実例の計算に使用するデータを選択",
                                    (list(select_data_list.keys()))
                                    )
if select_data_list[select_data_00] == 0:
    try:
        data_link = "./Sample_data_02.csv"
        input_data_df = pd.read_csv(data_link)
    except:
        data_link = "201_高大連携用サンプル/Sample_data_02.csv"
        input_data_df = pd.read_csv(data_link)
    section_title01=f"##### {section_num}-{contents_num+1}　入力データの確認（サンプルデータを利用）"
    input_data_keys = list(input_data_df.keys())
elif select_data_list[select_data_00] == 1:
    uploaded_file = st.sidebar.file_uploader("CSVファイルを選択", type={"csv"})
    if uploaded_file:
        try :
            input_data_df= pd.read_csv(uploaded_file)
        except:
            input_data_df= pd.read_csv(uploaded_file,encoding="SHIFT-JIS")          
        section_title01=f"##### {section_num}-{contents_num+1}　入力データの確認（アップロードされたファイルを利用）"
        input_data_keys = list(input_data_df.keys())
    else :
        st.error("データを入力してください．")
        st.stop()
    
st.markdown(section_title01)
st.dataframe(input_data_df)
"""  """
#== input(make dataframe) ===
contents_num +=1
f"""  ##### {section_num}-{contents_num+1}　データ解析"""
"""
ここでは，シンプソン公式を利用して数値積分を行い，加速度データから速度と位置を求めます．
"""
""" """ ; """ """

"""**データの選択**"""
col_input_data =  st.columns([1,2])
with col_input_data[0] :
    selected_keys_val0 = st.selectbox("時間に対応するデータ列を選択",input_data_keys)
    selected_keys_val0 = str(selected_keys_val0)
with col_input_data[1] :
    selected_keys_vals = st.multiselect("加速度のデータ列を選択（最大３つ．x,y,zの順に選択）",input_data_keys)
    if len(selected_keys_vals) < 1:
        st.error("積分するデータを１つ以上選択してください．")
        st.stop()     
""" """ ; """ """

"""**初期条件の選択**"""
coordinate_label_dict = {0:"x",1:"y",2:"z"}
n = len(selected_keys_vals)
col_init_v = st.columns(n) ; col_init_r = st.columns(n)
init_v_val = [] ; init_r_val = []
for i in range(n):
    with col_init_v[i]:
        str_text_input_title = f"初速度の{coordinate_label_dict[i]}成分を入力"
        init_v_val.append( st.text_input(str_text_input_title,"0"))        
    with col_init_r[i]:
        str_text_input_title = f"初期位置の{coordinate_label_dict[i]}成分を入力"
        init_r_val.append(st.text_input(str_text_input_title,"0"))
""" """ ; """ """


#== 数値積分 ===
init_v_str = "(\\ " ; init_r_str = "(\\ "
if n == 1:
    init_v_str += str(init_v_val[0]) 
    init_r_str += str(init_r_val[0]) 
elif n == 2 :
    init_v_str += str(init_v_val[0]) + "," + str(init_v_val[1])
    init_r_str += str(init_r_val[0]) + "," + str(init_r_val[1])
elif n == 3 :
    init_v_str += str(init_v_val[0]) + "," + str(init_v_val[1]) + "," + str(init_v_val[2])
    init_r_str += str(init_r_val[0]) + "," + str(init_r_val[1]) + "," + str(init_v_val[2])
init_v_str += "\\ )" ; init_r_str += "\\ )"

"""**速度の計算**"""
f"""
次の示されるのは
$$
    \\vec{{v}}(t) = \\vec{{v}}_0 + \\int_0^t \\vec{{a}}(t) dt 
\\qquad 
\\text{{及び}}
\\qquad
    \\vec{{r}}(t) = \\vec{{r}}_0 + \\int_0^t \\vec{{v}}(t) dt 
$$
の結果です．積分はシンプソン公式を利用した数値積分を行っています．  
初期条件は次のとおりです．
$$
    \\vec{{v}}_0 = {init_v_str}
    \\qquad 
    \\text{{及び}}
    \\qquad
    \\vec{{r}}_0 = {init_r_str}
$$
"""


##== 数値積分の実行(速度の計算) ==
from scipy import integrate 
time_val = input_data_df[selected_keys_val0]
#---速度の計算--
v_val = []
for i in range(n) :
    integrated_val = []
    val1_tmp = input_data_df[selected_keys_vals[i]]
    for j in range(len(time_val)):
        t = time_val[0:j+1]
        a = val1_tmp[0:j+1]
        integrate_num = float(init_v_val[i]) + sci.integrate.simps(a,t)
        integrated_val.append(integrate_num)
    v_val.append(integrated_val)
v_val_df = pd.DataFrame(v_val).T


#---位置の計算--
r_val = []
for i in range(n) :
    integrated_val = []
    val2_tmp = v_val_df[i]
    for j in range(len(time_val)):
        t = time_val[0:j+1]
        v = val2_tmp[0:j+1]
        integrate_num = float(init_r_val[i]) + sci.integrate.simps(v,t)
        integrated_val.append(integrate_num)
    r_val.append(integrated_val)

#== 可視化 ===   
r_val_df = pd.DataFrame(r_val).T
if n == 1 :
    plot_data_df = pd.concat([time_val, pd.DataFrame(r_val).T], axis=1)
    plot_data_df.columns = ["t","x"]
    r_val_df.columns = ["x"]
    v_val_df.columns = ["v_x"]
elif n == 2 :
    plot_data_df = pd.concat([time_val, pd.DataFrame(r_val).T], axis=1)
    plot_data_df.columns = ["t","x","y"] 
    r_val_df.columns = ["x","y"]
    v_val_df.columns = ["v_x","v_y"]
elif n == 3 :
    plot_data_df = pd.concat([time_val, pd.DataFrame(r_val).T], axis=1)
    plot_data_df.columns = ["t","x","y","z"]
    r_val_df.columns = ["x","y","z"]
    v_val_df.columns = ["v_x","v_y","v_z"]


import plotly.express as px
if n == 1 : 
    plot_data_df['y']=0
    # st.dataframe(r_val_df)
    plot_data_df_key = plot_data_df.keys()
    fig = px.scatter(data_frame=plot_data_df,
                        x=plot_data_df_key[1],
                        y=plot_data_df_key[2],
                        color=plot_data_df_key[0]
                    )

elif n == 2 :
    plot_data_df_key = plot_data_df.keys()
    fig = px.scatter(data_frame=plot_data_df,
                        x=plot_data_df_key[1],
                        y=plot_data_df_key[2],
                        color=plot_data_df_key[0]
                    )
elif n == 3 :
    plot_data_df_key = plot_data_df.keys()
    fig = px.scatter_3d(plot_data_df,
                        x=plot_data_df_key[1],
                        y=plot_data_df_key[2], 
                        z=plot_data_df_key[3],
                        color=plot_data_df_key[0],
                        color_continuous_scale='Bluered_r')

st.plotly_chart(fig)

output_df = pd.concat([time_val,input_data_df[selected_keys_vals],v_val_df,r_val_df],axis=1)
output_csv = output_df.to_csv().encode('utf-8')

st.download_button(
    label="計算結果をダウンロード",
    data=output_csv,
    file_name='output.csv',
    mime='text/csv',
)