import streamlit as st
import scipy as sci
import pandas as pd
import numpy as np
from scipy.spatial.transform import Rotation as Rot


st.sidebar.markdown(""" **加速度データの取得**""")
st.sidebar.markdown(""" 
**webアプリの起動**  
[クリック](https://w3e.kanazawa-it.ac.jp/math/physics/category/experiment/mobile_device/orientation_acceleration/sensor_orientation_acceleration.html)  

**作成者**  
金沢工業大学 数理・データサイエンス・AI教育課程 准教授 西岡圭太
"""
)

##### Main 
section_num = 1 
contents_num = 0

st.markdown("""#### 加速度データによる位置情報の取得""")
""" """ ; """ """
#-----  input data  -----------------------------------------------
select_demodata_dict = {
                        "放物運動（仮想，3d)":["Sample_data_00.csv",[2,0,5],[0,0,0]],
                        "空間中の運動（仮想，3d)":["Sample_data_01.csv",[0,0.314159265,1],[1,0,0]]
                        # "エスカレーターでの運動（実測）":["Sample_data_02.csv",[0,0,0],[0,0,0]],
                        # "学内ウォーキング（実測）":["Sample_data_03.csv",[0,0,0],[0,0,0]]
                        }

#== input(make dataframe) ===
select_data_list = {"サンプルデータを利用":0, "CSVファイルをアップロードし利用":1}
select_data_00 = st.sidebar.selectbox("📝　実例の計算に使用するデータを選択",
                                        (list(select_data_list.keys()))
                                     )



if select_data_list[select_data_00] == 0:
    f"""##### {section_num}-{contents_num+1}　データの選択（サンプルデータを利用）"""
    contents_num +=1
    selected_demodata_key = st.selectbox("分析に使用するデータを選択してください．",select_demodata_dict.keys())
    try:
        data_link = "./"+str(select_demodata_dict[selected_demodata_key][0])
        input_data_df = pd.read_csv(data_link)
    except:
        data_link = "201_高大連携用サンプル/"+str(select_demodata_dict[selected_demodata_key][0])
        input_data_df = pd.read_csv(data_link)
    section_title01=f"##### {section_num}-{contents_num+1}　入力データの確認"
    input_data_keys = list(input_data_df.keys())

    
elif select_data_list[select_data_00] == 1:
    f"""##### {section_num}-{contents_num+1}　データの選択（アップロードされたファイルを利用）"""
    contents_num +=1
    uploaded_file = st.sidebar.file_uploader("CSVファイルを選択", type={"csv"})
    if uploaded_file:
        try :
            input_data_df= pd.read_csv(uploaded_file)
        except:
            input_data_df= pd.read_csv(uploaded_file,encoding="SHIFT-JIS")          
        section_title01=f"##### {section_num}-{contents_num+1}　入力データの確認"
        input_data_keys = list(input_data_df.keys())
    else :
        st.error("データを入力してください．")
        st.stop()
""" """ ; """ """
st.markdown(section_title01)
st.dataframe(input_data_df)
""" """ ; """ """

#== input(make dataframe) ===
contents_num +=1
f"""  ##### {section_num}-{contents_num+1}　データ解析"""
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
coordinate_label_dict = {0:"第1",1:"第2",2:"第3"}
n = len(selected_keys_vals)
col_init_v = st.columns(n) ; col_init_r = st.columns(n)
init_v_val = []
init_r_val = []
if select_data_list[select_data_00] == 0 :
    tmp_init_v_val = select_demodata_dict[selected_demodata_key][1]
    tmp_init_r_val = select_demodata_dict[selected_demodata_key][2]
for i in range(n):
    with col_init_v[i]:
        str_text_input_title = f"初速度の{coordinate_label_dict[i]}成分を入力"
        if select_data_list[select_data_00] == 0 :
            init_v_val.append( float( st.text_input(str_text_input_title,tmp_init_v_val[i])) )  
        else :
            init_v_val.append( float( st.text_input(str_text_input_title,"0")) )   

    with col_init_r[i]:
        str_text_input_title = f"初期位置の{coordinate_label_dict[i]}成分を入力"
        if select_data_list[select_data_00] == 0 :
            init_r_val.append( float( st.text_input(str_text_input_title,tmp_init_r_val[i]) ) )  
        else :
            init_r_val.append( float( st.text_input(str_text_input_title,"0")) )    
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


"""**速度と位置の計算**"""
f"""
次の示されるのは
$$
    \\vec{{v}}(t) = \\vec{{v}}_0 + \\int_0^t \\vec{{a}}(t) dt 
\\qquad 
\\text{{及び}}
\\qquad
    \\vec{{r}}(t) = \\vec{{r}}_0 + \\int_0^t \\vec{{v}}(t) dt 
$$
の結果です．初期条件は次のとおりです．
$$
    \\vec{{v}}_0 = {init_v_str}
    \\qquad 
    \\text{{及び}}
    \\qquad
    \\vec{{r}}_0 = {init_r_str}
$$

"""


##== 数値積分の実行(速度の計算) ==

# time_val = input_data_df[selected_keys_val0]
# keys = [selected_keys_val0]+selected_keys_vals
# Noise_Reduction_dict = {
#                         "ノイズ除去なし":0,
#                         "ノイズ除去あり（Savitzky-Golay法）":1
#                         }
# Noise_Reduction_radio = st.radio("ノイズ除去について選択してください．", Noise_Reduction_dict.keys(),horizontal=True)
# if Noise_Reduction_dict[Noise_Reduction_radio] == 0:
#     a_val_df = input_data_df[keys]
# elif Noise_Reduction_dict[Noise_Reduction_radio] == 1:
#     import scipy.signal
#     a_val_df = input_data_df[keys]
#     col_noise_red = st.columns(2)
#     with col_noise_red[0]:
#         window = st.number_input("Window",value=21,min_value=1)
#     with col_noise_red[1]:
#         deg = st.number_input("deg",value=3,min_value=1)
#     for i in range(len(keys)):
#         a_val_df = scipy.signal.savgol_filter(a_val_df, window, deg)

time_val = input_data_df[selected_keys_val0]
keys = [selected_keys_val0]+selected_keys_vals
a_val_df = input_data_df[keys]
plot_data_a_df = a_val_df

st.dataframe(a_val_df)
numerical_intagration_method_dict = {"区分求積法":0,"シンプソン公式":2,"台形公式":1,}
selected_method_str = st.radio("数値積分の方法を選択してください．",numerical_intagration_method_dict.keys(), horizontal=True)
if st.button("積分の実行"):
    #---速度の計算--
    with st.spinner('速度の計算中'):
        v_val = []
        if numerical_intagration_method_dict[selected_method_str] == 0 :
            sum_result = 0
            for i in range(n) :
                val1_tmp = input_data_df[selected_keys_vals[i]]
                integrated_val = []
                integrated_val.append(init_v_val[i])
                for t_range in range(1,len(time_val)) :
                    tmp_integrate_val = init_v_val[i]
                    for j in range(1,t_range+1,1) :
                        dt = time_val[j] - time_val[j-1]
                        tmp_integrate_val +=  val1_tmp[j-1]*dt
                    integrated_val.append(tmp_integrate_val)
                v_val.append(integrated_val)

        elif numerical_intagration_method_dict[selected_method_str] == 1 :
            st.error("ただいま作成中")
            st.stop()

        elif numerical_intagration_method_dict[selected_method_str] == 2 :
            from scipy import integrate 
            for i in range(n) :
                integrated_val = []
                val1_tmp = input_data_df[selected_keys_vals[i]]
                for j in range(len(time_val)):
                    t = time_val[0:j+1]
                    a = val1_tmp[0:j+1]
                    tmp_integrate_val = init_v_val[i] + sci.integrate.simps(a,t)
                    integrated_val.append(tmp_integrate_val)
                v_val.append(integrated_val)

    v_val_df = pd.DataFrame(v_val).T


    #---位置の計算--
    with st.spinner('位置の計算中'):
        r_val = []
        if numerical_intagration_method_dict[selected_method_str] == 0 :
            sum_result = 0
            for i in range(n) :
                val2_tmp = v_val_df[i]
                integrated_val = []
                for t_range in range(len(time_val)) :
                    if t_range == 0 :
                        integrated_val.append(init_r_val[i])
                    else :
                        tmp_integrate_val = init_r_val[i]
                        for j in range(1,t_range+1) :
                            dt = time_val[j] - time_val[j-1]
                            tmp_integrate_val += val2_tmp[j-1]*dt
                        integrated_val.append(tmp_integrate_val)
                r_val.append(integrated_val)
        elif numerical_intagration_method_dict[selected_method_str] == 1 :
            st.error("ただいま作成中")
            st.stop()
        elif numerical_intagration_method_dict[selected_method_str] == 2 :
            from scipy import integrate 
            for i in range(n) :
                integrated_val = []
                val2_tmp = v_val_df[i]
                for j in range(len(time_val)-1):
                    t = time_val[0:j+1]
                    v = val2_tmp[0:j+1]
                    tmp_integrate_val = init_v_val[i] + sci.integrate.simps(v,t)
                    integrated_val.append(tmp_integrate_val)
                r_val.append(integrated_val)

    r_val_df = pd.DataFrame(r_val).T
else :
    st.stop()


#== 可視化 ===   
if n == 1 :
    r_val_df.columns = ["r_1"]
    plot_data_r_df = pd.concat([time_val, r_val_df], axis=1)
    plot_data_r_df.columns = ["t","r_1"]

    plot_data_v_df = pd.concat([time_val,v_val_df], axis=1)
    plot_data_v_df.columns = ["t","v_1"]
    v_val_df.columns = ["v_1"]

elif n == 2 :
    r_val_df.columns = ["r_1","r_2"]
    plot_data_r_df = pd.concat([time_val, r_val_df], axis=1)
    plot_data_r_df.columns = ["t","r_1","r_2"] 

    plot_data_v_df = pd.concat([time_val,v_val_df], axis=1)
    plot_data_v_df.columns = ["t","v_1","v_2"]
    v_val_df.columns = ["v_1","v_2"]

elif n == 3 :
    r_val_df.columns = ["r_1","r_2","r_3"]
    plot_data_r_df = pd.concat([time_val, r_val_df], axis=1)
    plot_data_r_df.columns = ["t","r_1","r_2","r_3"]

    plot_data_v_df = pd.concat([time_val, v_val_df ], axis=1)
    plot_data_v_df.columns = ["t","v_1","v_2","v_3"]
    v_val_df.columns = ["v_1","v_2","v_3"]


##  加速度のプロット
"""###### 加速度のプロット"""
import plotly.graph_objects as go
col_a_fig = st.columns(n)

plot_data_a_df_key = plot_data_a_df.keys()
for i in range(n):
    with col_a_fig[i]:
         fig = go.Figure()
         fig.add_trace(go.Scatter(
                                    x=plot_data_a_df[plot_data_a_df_key[0]],
                                    y=plot_data_a_df[plot_data_a_df_key[i+1]],
                                    mode='lines+markers',
                                    name=plot_data_a_df_key[i+1]
                                    )
                        )
         st.plotly_chart(fig,use_container_width=True)

##  速度のプロット
"""###### 速度のプロット"""
import plotly.graph_objects as go
col_v_fig = st.columns(n)
plot_data_v_df_key = plot_data_v_df.keys()
for i in range(n):
    with col_v_fig[i]:
         fig = go.Figure()
         fig.add_trace(go.Scatter(
                                    x=plot_data_v_df[plot_data_v_df_key[0]],
                                    y=plot_data_v_df[plot_data_v_df_key[i+1]],
                                    mode='lines+markers',
                                    name=plot_data_v_df_key[i+1]
                                    )
                        )
         st.plotly_chart(fig,use_container_width=True)
##  位置のプロット
"""###### 位置のプロット"""
import plotly.express as px
layout = go.Layout(yaxis=dict(scaleanchor='x'))
if n == 1 : 
    plot_data_r_df['y']=0
    # st.dataframe(r_val_df)
    plot_data_r_df_key = plot_data_r_df.keys()
    fig = px.scatter(data_frame=plot_data_r_df,
                        x=plot_data_r_df_key[1],
                        y=plot_data_r_df_key[2],
                        color=plot_data_r_df_key[0]
                    )
elif n == 2 :
    plot_data_r_df_key = plot_data_r_df.keys()
    fig = px.scatter(data_frame=plot_data_r_df,
                        x=plot_data_r_df_key[1],
                        y=plot_data_r_df_key[2],
                        color=plot_data_r_df_key[0]
                    )
elif n == 3 :
    plot_data_r_df_key = plot_data_r_df.keys()
    fig = px.scatter_3d(plot_data_r_df,
                        x=plot_data_r_df_key[1],
                        y=plot_data_r_df_key[2], 
                        z=plot_data_r_df_key[3],
                        color=plot_data_r_df_key[0],
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