import streamlit as st
import scipy as sci
import pandas as pd
import numpy as np
import plotly as plotly
from scipy.spatial.transform import Rotation as Rot


st.sidebar.markdown(""" **加速度データの取得**""")
st.sidebar.markdown(""" 
**webアプリの起動** [-> クリック](https://w3e.kanazawa-it.ac.jp/math/physics/category/experiment/mobile_device/orientation_acceleration/sensor_orientation_acceleration.html)  

**作成者**  
金沢工業大学 数理・データサイエンス・AI教育課程 准教授 西岡圭太
"""
)

##### Main 
section_num = 1 
contents_num = 0

st.markdown("""### 加速度データによる位置情報の計算（ノイズ除去あり）""")
""" """ ; """ """
#-----  input data  -----------------------------------------------
select_demodata_dict = {
                        # "放物運動（仮想，3d)":["Sample_data_00.csv",[2,0,5],[0,0,0]],
                        # "空間中の運動（仮想，3d)":["Sample_data_01.csv",[0,0.314159265,1],[1,0,0]],
                        "エレベータのデータ":["Sample_data_02.csv",[0,0,0],[0,0,0]]
                        }

#== input(make dataframe) ===
select_data_list = {"サンプルデータを利用":0, "CSVファイルをアップロードし利用":1}
select_data_00 = st.sidebar.selectbox("📝　実例の計算に使用するデータを選択",
                                        (list(select_data_list.keys()))
                                     )

if select_data_list[select_data_00] == 0:
    f"""##### {section_num}-{contents_num+1}　データの選択（サンプルデータを利用）"""
    contents_num +=1
    col_selected_data = st.columns([2,1])

    with col_selected_data[0]:
        selected_demodata_key = st.selectbox("分析に使用するデータを選択してください．",select_demodata_dict.keys())
        try:
            data_link = "./"+str(select_demodata_dict[selected_demodata_key][0])
            input_data_df = pd.read_csv(data_link)
        except:
            data_link = "10_Fundamental_Physics/"+str(select_demodata_dict[selected_demodata_key][0])
            input_data_df = pd.read_csv(data_link)
        section_title01=f"##### {section_num}-{contents_num+1}　入力データの確認"
        input_data_keys = list(input_data_df.keys())
    with col_selected_data[1]:
        """ """ ; """ """
        st.download_button(
        label="入力データをダウンロード",
        data=input_data_df.to_csv().encode('utf-8'),
        file_name='input.csv',
        mime='text/csv',
        )
        
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
f"""  ##### {section_num}-{contents_num+1}　データの選択"""
col_input_data =  st.columns([1,2])
with col_input_data[0] :
    selected_keys_val0 = st.selectbox("時間に対応するデータ列を選択",input_data_keys)
    selected_keys_val0 = str(selected_keys_val0)
with col_input_data[1] :
    selected_keys_vals = st.multiselect("加速度のデータ列を選択（最大３つ．x,y,zの順に選択）",input_data_keys)
    if (len(selected_keys_vals) == 0) or (3 < len(selected_keys_vals) ):
        st.error("積分するデータを１つ以上3以下で選択してください．")
        st.stop()     
""" """ ; """ """

#==  オリジナルの加速度のプロット　==
contents_num +=1
f"""  ##### {section_num}-{contents_num+1}　加速度データの可視化"""

time_val = input_data_df[selected_keys_val0]
keys = [selected_keys_val0]+selected_keys_vals
plot_data_a_df = input_data_df[keys]
n = len(selected_keys_vals)
Means_list0 = [plot_data_a_df.iloc[:,i+1].mean() for i in range(n)]

import plotly.graph_objects as go
col_a_fig = st.columns(n)
for i in range(n):
    with col_a_fig[i]:
         fig = go.Figure()
         fig.add_trace(go.Scatter(
                                    x=plot_data_a_df.iloc[:,0],
                                    y=plot_data_a_df.iloc[:,i+1],
                                    mode='lines+markers',
                                    name=f"第{i+1}成分"
                                    )
                        )
         fig.add_hline(y=Means_list0[i],line_color="green",name=f"第{i+1}成分の平均値")
         fig.update_layout(legend=dict(x=0.01,
                              y=0.99,
                              xanchor='left',
                              yanchor='top',
                              orientation='h',
                              ))
         st.plotly_chart(fig,use_container_width=True)


#== 分析区間の選択　==
contents_num +=1
f"""  ##### {section_num}-{contents_num+1}　前処理１：分析領域の選択"""
""" 
測定データの中で分析に使用する時間領域を定めます．開始時刻と終了時刻を設定してください．
"""
col_noise_reduction_interval = st.columns([1,1,3])
with col_noise_reduction_interval[0]:
     start_time = st.selectbox(
    '開始時刻',time_val
     )
with col_noise_reduction_interval[1]:
     end_time = st.selectbox(
    '終了時刻',time_val
     )
with col_noise_reduction_interval[2]:
    if start_time >= end_time:
        st.error("選択時刻に誤りがあります．開始時刻 < 終了時刻 となるように調整してください．")
        st.stop()
    else:
        """**選択完了**"""
        st.markdown(f"時刻 {start_time} から {end_time} の間のデータを分析に使用します．")

plot_data_a_nd_df = plot_data_a_df[ 
                                      (plot_data_a_df.iloc[:,0] >= start_time) 
                                    & (plot_data_a_df.iloc[:,0] <= end_time)
                                    ]
""" """ ; """ """



#== ノイズ除去　==
contents_num +=1
f"""  ##### {section_num}-{contents_num+1}　前処理２：ゼロの調整とノイズ除去"""

import scipy.signal
len_data_num = len(plot_data_a_nd_df.iloc[:,i+1])
if int(len_data_num/6) %2 == 0:
    w_length = int(len_data_num/6)-1
else :
    w_length = int(len_data_num/6)

data0 = plot_data_a_nd_df.to_numpy()
data0 = [data0[:,i] for i in range(n+1)]
data = (n+1)*[0]
Means_list0 = [data0[i+1].mean() for i in range(n)]
window_len , poly_order = (n+1)*[0], (n+1)*[0]
data[0],window_len[0],poly_order[0] = data0[0],1,0

"""###### 各種調整量の設定１：ゼロの調整"""
f""" 
「第XXX成分のゼロの調整」にチェックを入れると，静止中または等速直線運動中の加速度が０となるように第XXX成分全体を平行移動します．初期値はデータの平均値です．  
"""
col_noise_reduction_base = st.columns(n)
""" """ ; """ """
for i in range(n) :
    with col_noise_reduction_base[i]:        
        if st.checkbox(f"第{i+1}成分のゼロの調整"):
            Num_subs_float = st.text_input("値の入力(半角数字)",value=Means_list0[i])
            if Num_subs_float:
                Num_subs_float = float(Num_subs_float)
            else:
                Num_subs_float = 0
            data[i+1] = [j- Num_subs_float for j in data0[i+1]]
        else:
            data[i+1] = [j for j in data0[i+1]]

"""###### 各種調整量の設定２：ノイズ除去"""
f""" 
「第XXX成分のノイズ除去」チェックを入れると，Savitzky-Golayフィルタをもちいて第XXX成分全体のノイズ除去を行います．

サンプルデータの場合，次のように値を設定すると良い．  
[第１成分:窓の幅201,次数１／第２成分：窓の幅201,次数１／第３成分：窓の幅は51,次数は2]
"""
col_noise_reduction_base = st.columns(n)
""" """ ; """ """
for i in range(n) :
    with col_noise_reduction_base[i]:        
        if st.checkbox(f"第{i+1}成分のノイズ除去"):
            window_len[i+1] = st.number_input(f"第{i+1}成分の窓の幅（入力値は奇数）",min_value=1,max_value=len_data_num,step=2,value=w_length )
            poly_order[i+1] = st.number_input(f"第{i+1}成分の近似関数の次数",min_value=1,value= 1)
        else:
            window_len[i+1], poly_order[i+1] = 1,0

for i, tmp_d in enumerate(data):
    data[i] = scipy.signal.savgol_filter(tmp_d,window_len[i],poly_order[i])

Means_list = [data[i+1].mean() for i in range(n) ]

""" """ ; """ """
"""###### 調整済みデータのプロット"""
import plotly.graph_objects as go
col_a_fig = st.columns(n)
for i in range(n):
    with col_a_fig[i]:
         fig1 = go.Scatter(
                                    x=data0[0],
                                    y=data0[i+1],
                                    mode='lines+markers',
                                    name=f"第{i+1}成分-Original"
                        )
         fig2 = go.Scatter(
                                    x=data[0],
                                    y=data[i+1],
                                    mode='lines+markers',
                                    name=f"第{i+1}成分-Noise reduced",
                                    line_color="magenta"
                        )
         fig = go.Figure([fig1,fig2])
        #  fig = go.Figure(fig1)
         fig.update_layout(legend=dict(x=0.01,
                            y=-0.2,
                            xanchor='left',
                            yanchor='top',
                            orientation='h',
                            ))
         fig.add_hline(y=Means_list0[i],line_color="green")
         fig.add_hline(y=Means_list[i],line_color="red")
         st.plotly_chart(fig,use_container_width=True)

a_val_df = pd.DataFrame(data).T
a_val_df.columns = plot_data_a_df.keys() 
a_val_csv = a_val_df.to_csv().encode('utf-8')
st.download_button(
    label="前処理済みデータのダウンロード",
    data=a_val_csv,
    file_name='前処理済みデータ.csv',
    mime='text/csv',
)
# st.dataframe(a_val_df)
""" """ ; """ """


#== 初期条件の入力　==
contents_num +=1
f"""  ##### {section_num}-{contents_num+1}　初期条件の設定"""

# coordinate_label_dict = {0:"第1",1:"第2",2:"第3"}
n = len(selected_keys_vals)
col_init_v , col_init_r = st.columns(n) , st.columns(n)
init_v_val,init_r_val = [],[]

for i in range(n):
    with col_init_v[i]:
        str_text_input_title = f"初速度の第{i+1}成分を入力"
        init_v_val.append( float( st.text_input(str_text_input_title,"0")) )   

    with col_init_r[i]:
         str_text_input_title = f"初期位置の第{i+1}成分を入力"
         init_r_val.append( float( st.text_input(str_text_input_title,"0")) )    

if n == 1:
    init_v_str = f"(\\ {init_v_val[0]} \\ )"
    init_r_str = f"(\\ {init_r_val[0]} \\ )"
elif n == 2 :
    init_v_str = f"(\\ {init_v_val[0]},\\ {init_v_val[1]}\\ )" 
    init_r_str = f"(\\ {init_r_val[0]},\\ {init_r_val[1]}\\ )" 
elif n == 3 :
    init_v_str = f"(\\ {init_v_val[0]},\\ {init_v_val[1]},\\ {init_v_val[2]}\\ )" 
    init_r_str = f"(\\ {init_r_val[0]},\\ {init_r_val[1]},\\ {init_r_val[2]}\\ )"

""" """ ; """ """

#== 速度と位置の計算　==
contents_num +=1
f"""  ##### {section_num}-{contents_num+1}　速度と位置の計算  

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

#= 積分方法の選択
"""###### 積分方法の選択"""
col_select_method = st.columns(2)

with col_select_method[0] :
    numerical_intagration_method_dict = {"区分求積法(左リーマン和)":0,"台形公式":1}
    selected_method_str = st.radio("選択肢",numerical_intagration_method_dict.keys(), horizontal=True)
with col_select_method[1] :
    ''' '''
    button_integration = st.button("速度と位置の計算（積分の実行）")

if button_integration :
    a_val_array = a_val_df.to_numpy()
    v_val_array = np.zeros((len(a_val_array[:,0]),(n+1)))
    r_val_array = np.zeros((len(a_val_array[:,0]),(n+1)))
    #---速度の計算--
    with st.spinner('速度の計算中'):
        #区分求積法(左リーマン和)
        v_val_keys_list = []
        if numerical_intagration_method_dict[selected_method_str] == 0 :
            for i in range(n+1):
                if i == 0 :
                    v_val_array[0,i] = a_val_array[0,i]
                    v_val_keys_list.append(f"time")
                else :
                    v_val_array[0,i] = init_v_val[i-1] 
                    v_val_keys_list.append(f"vの第{i}成分")        

            for index in range(1,len(a_val_array[:,0])):
                v_val_array[index,0] = a_val_array[index,0]
                for i in range(n):
                    dv_float = a_val_array[index-1,i+1]*(a_val_array[index,0]-a_val_array[index-1,0])
                    v_val_array[index,i+1] = v_val_array[index-1,i+1] + dv_float
            # st.dataframe(v_val_array)

        #台形公式
        elif numerical_intagration_method_dict[selected_method_str] == 1 :
            for i in range(n+1):
                if i == 0 :
                    v_val_array[0,i] = a_val_array[0,i]
                    v_val_keys_list.append(f"time")
                else :
                    v_val_array[0,i] = init_v_val[i-1] 
                    v_val_keys_list.append(f"速度の第{i}成分")         

            for index in range(1,len(a_val_array[:,0])):
                v_val_array[index,0] = a_val_array[index,0]
                for i in range(n):
                    dv_float = 0.5*(a_val_array[index-1,i+1]+a_val_array[index,i+1])*(a_val_array[index,0]-a_val_array[index-1,0])
                    v_val_array[index,i+1] = v_val_array[index-1,i+1] + dv_float
                                                
        """###### 速度のプロット"""
        import plotly.graph_objects as go
        col_a_fig_v = st.columns(n)
        for i in range(n):
            with col_a_fig_v[i]:
                fig_v_main = go.Scatter(
                                            x=v_val_array[:,0],
                                            y=v_val_array[:,i+1],
                                            mode='lines+markers',
                                            name=f"第{i+1}成分"
                                )
                fig_v = go.Figure(fig_v_main)
                fig_v.update_layout(legend=dict(x=0.01,
                                    y=-0.2,
                                    xanchor='left',
                                    yanchor='top',
                                    orientation='h',
                                    ))
                st.plotly_chart(fig_v,use_container_width=True)


    #---位置の計算--
    with st.spinner('位置の計算中'):
        #区分求積法(左リーマン和)
        r_val_keys_list = []
        if numerical_intagration_method_dict[selected_method_str] == 0 :
            for i in range(n+1):
                if i == 0 :
                    r_val_array[0,i] = v_val_array[0,i]
                    r_val_keys_list.append(f"time")
                else :
                    r_val_array[0,i] = init_r_val[i-1]         
                    r_val_keys_list.append(f"位置の第{i}成分")

            for index in range(1,len(a_val_array[:,0])):
                r_val_array[index,0] = v_val_array[index,0]
                for i in range(n):
                    dr_float = v_val_array[index-1,i+1]*(v_val_array[index,0]-v_val_array[index-1,0])
                    r_val_array[index,i+1] = r_val_array[index-1,i+1] + dr_float
            # st.dataframe(v_val_array)

        #台形公式
        elif numerical_intagration_method_dict[selected_method_str] == 1 :
            for i in range(n+1):
                if i == 0 :
                    r_val_array[0,i] = v_val_array[0,i]
                    r_val_keys_list.append(f"time")
                else :
                    r_val_array[0,i] = init_r_val[i-1]         
                    r_val_keys_list.append(f"位置の第{i}成分")    

            for index in range(1,len(a_val_array[:,0])):
                r_val_array[index,0] = v_val_array[index,0]
                for i in range(n):
                    dr_float = 0.5*(v_val_array[index-1,i+1]+v_val_array[index,i+1])*(v_val_array[index,0]-v_val_array[index-1,0])
                    r_val_array[index,i+1] = r_val_array[index-1,i+1] + dr_float
        
        """###### 位置のプロット1"""
        import plotly.graph_objects as go
        col_a_fig_v = st.columns(n)
        for i in range(n):
            with col_a_fig_v[i]:
                fig_rmain = go.Scatter(
                                            x=r_val_array[:,0],
                                            y=r_val_array[:,i+1],
                                            mode='lines+markers',
                                            name=f"第{i+1}成分"
                                )
                fig_r = go.Figure(fig_rmain)
                fig_r.update_layout(legend=dict(x=0.01,
                                    y=-0.2,
                                    xanchor='left',
                                    yanchor='top',
                                    orientation='h',
                                    ))
                st.plotly_chart(fig_r,use_container_width=True)

        r_val_df = pd.DataFrame(r_val_array)

        r_val_df.columns = r_val_keys_list

        output_array = np.concatenate([a_val_array,v_val_array,r_val_array], axis=1)
        output_df = pd.DataFrame(output_array)
        output_keys = list(a_val_df.keys())
        output_keys.extend(v_val_keys_list)
        output_keys.extend(r_val_keys_list)
        output_df.columns = output_keys

        """###### 位置のプロット2"""
        import plotly.express as px
        layout = go.Layout(yaxis=dict(scaleanchor='x'))
        if n == 1 :
            fig_3d = px.scatter(data_frame=r_val_df,
                                x=r_val_df.keys()[0],
                                y=r_val_df.keys()[1],
                                color=r_val_df.keys()[0]
                            )
            st.plotly_chart(fig_3d )
        elif n == 2 :
            fig_3d = px.scatter(data_frame=r_val_df,
                                x=r_val_df.keys()[1],
                                y=r_val_df.keys()[2],
                                color=r_val_df.keys()[0]
                            )
            st.plotly_chart(fig_3d )
        elif n == 3 :
            fig_3d = px.scatter_3d(data_frame=r_val_df,
                                x=r_val_df.keys()[1],
                                y=r_val_df.keys()[2],
                                z=r_val_df.keys()[3],
                                color=r_val_df.keys()[0],
                                color_continuous_scale='Bluered_r')

            st.plotly_chart(fig_3d )


        output_csv = output_df.to_csv().encode('utf-8')
        st.download_button(
            label="解析結果のダウンロード",
            data=output_csv,
            file_name='解析結果.csv',
            mime='text/csv',
            )
else :
    st.stop()