import gensim
import streamlit as st

st.sidebar.markdown(
    """
    **感想を教えてください**  
    [ご意見・ご感想はこちらから](https://forms.gle/rHhJJ6538V1m7eZT6)
    """)
"""
### gensim を利用したword2vec
"""
st.write(gensim.__version__)
models_list = ["ja","model"]
selected_model_num = st.selectbox("使用する学習済みモデルを選択してください．",models_list)
try :
    if selected_model_num == "ja":
        model = gensim.models.Word2Vec.load('./ja.bin')
    elif selected_model_num == "model":
        model = gensim.models.KeyedVectors.load_word2vec_format('./model.vec', binary=False)
except :
    if selected_model_num == "ja":
        model = gensim.models.Word2Vec.load('08_Basic_Topics_in_Artificial_Intelligence/ja.bin')
    elif selected_model_num == "model":
        model = gensim.models.KeyedVectors.load_word2vec_format('08_Basic_Topics_in_Artificial_Intelligence/model.vec', binary=False)
# model = gensim.models.KeyedVectors.load_word2vec_format("./ja.bin", binary=True)
""" """;""" """
st.markdown("### 1. 単語ベクトルの表示")
col01= st.columns(2)
with col01[0]:
    input_text01 = st.text_input("ベクトル化したい単語を入力してください．","猫",key='input_text01')
    wordvec1 = model.wv[input_text01]
with col01[1]:
    st.write(f"”{input_text01}”ベクトルは次のようなベクトルです．")
    st.dataframe(wordvec1)

""" """;""" """
st.markdown("### 2. 類似する単語")
col02= st.columns(2)
with col02[0]:
    input_text02 = st.text_input("調べたい単語を入力してください．","猫",key='input_text02')
    num02 = st.number_input("類似した単語の上位何個を表示させますか？",1,key='num02')
with col02[1]:
    st.markdown(f"”{input_text02}”に類似した単語は次の通りです．")
    wordvec2 = model.wv.most_similar(positive=[input_text02],topn=num02)
    st.dataframe(wordvec2)

""" """;""" """
st.markdown("### 3. 単語の計算")
st.markdown("##### 3-1. 単語の和(A+B)")
col03= st.columns(2)
with col03[0]:
    input_text03 = ["",""]
    input_text03[0] = st.text_input("Aに入力する単語を入れてください","神",key='input_text03-0')
    input_text03[1] = st.text_input("Bに入力する単語を入れてください．","太陽",key='input_text03-1')
    num03 = st.number_input("計算結果の上位何個を表示させますか？",1,key='num03')
with col03[1]:
    st.markdown(f"”{input_text03[0]}”＋”{input_text03[1]}”に相当する単語は次の通りです．")
    wordvec3 = model.wv.most_similar(positive=[input_text03[0],input_text03[1]],topn=num03)
    st.dataframe(wordvec3)

""" """;""" """
st.markdown("##### 3-2. 単語の差(A-B)")
col04= st.columns(2)
with col04[0]:
    input_text04 = ["",""]
    input_text04[0] = st.text_input("Aに入力する単語を入れてください","神",key='input_text04-0')
    input_text04[1] = st.text_input("Bに入力する単語を入れてください．","太陽",key='input_text04-1')
    num04 = st.number_input("計算結果の上位何個を表示させますか？",1,key='num04')
with col04[1]:
    st.markdown(f"”{input_text04[0]}”-”{input_text04[1]}”に相当する単語は次の通りです．")
    wordvec4 = model.wv.most_similar(positive=[input_text04[0]],negative=[input_text04[1]],topn=num04)
    st.dataframe(wordvec4)

""" """;""" """
st.markdown("##### 3-3. 単語の和と差(A-B＋C)")
col05= st.columns(2)
with col05[0]:
    input_text05 = ["","",""]
    input_text05[0] = st.text_input("Aに入力する単語を入れてください","東京",key='input_text05-0')
    input_text05[1] = st.text_input("Bに入力する単語を入れてください．","日本",key='input_text05-1')
    input_text05[2] = st.text_input("Cに入力する単語を入れてください．","アメリカ",key='input_text05-2')
    num05 = st.number_input("計算結果の上位何個を表示させますか？",1,key='num05')
with col05[1]:
    st.markdown(f"”{input_text05[0]}”-”{input_text05[1]}+”{input_text05[2]}”に相当する単語は次の通りです．")
    wordvec5 = model.wv.most_similar(positive=[input_text05[0],input_text05[2]],negative=[input_text05[1]],topn=num04)
    st.dataframe(wordvec5)