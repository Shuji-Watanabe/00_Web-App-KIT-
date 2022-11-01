# import ginza
# import spacy
# import unidic_lite
# import MeCab
import pandas as pd 
import streamlit as st

# dic_path = unidic_lite.__path__[0].replace('\\','/') + '/dicdir/'
# rc_path = unidic_lite.__path__[0].replace('\\','/') + '/dicdir/mecabrc'
# mecaboption = "-r '" + rc_path + "' -d '" + dic_path + "'"


# st.markdown("""####  形態素解析と構文分析""")
# sentence = st.text_input("文章を入力してください．","頭が赤い魚を食べる猫．")

# if len(sentence) == 0 :
#     st.error("文章を入力してください．")
#     st.stop()

# st.markdown("""####  形態素解析の結果（MeCab）""")

# mecab_option_list = {"ノーマル":"","全情報":"-Odump","辞書:UniDic":mecaboption}
# mecab_option = st.radio("出力情報",mecab_option_list.keys(),horizontal=True)
# m_option = mecab_option_list[mecab_option]
# mecab = MeCab.Tagger(m_option)
# parses = mecab.parse(sentence)
# # st.write(parses.split('\n'))

# ##### MeCab：形態素解析の結果のデータフレーム化
# parses_df = []
# counta = 0
# if mecab_option == "ノーマル" :
#     for line in parses.split('\n'):
#         counta += 1
#         if line == "EOS":
#             break
#         else :
#             tmp =  line.split('\t')
#             parses_df.append(tmp)
# elif mecab_option == "全情報" :
#     for line in parses.split('\n'):
#         counta += 1
#         if line == "EOS":
#             break
#         else :
#             if 1 < counta < len(parses.split('\n'))-1:
#                 feature = line.split('\t')
#                 # st.write(feature[0].split(' ')[2].split(','))
#                 tmp1 = feature[0].split(' ')[1]
#                 tmp2 = feature[0].split(' ')[2]
#                 tmp2 = [f for f in tmp2.split(',')]
#                 parses_df.append([tmp1, *tmp2])
#                 #st.write(f"No.{counta:02} Done")
# elif mecab_option == "辞書:UniDic" :
#     for line in parses.split('\n'):
#         counta += 1
#         if line == "EOS":
#             break
#         else :
#             tmp =  line.split('\t')
#             parses_df.append(tmp)
# parses_df = pd.DataFrame(parses_df) 
# st.dataframe(parses_df)
# outfile_csv_ginza = parses_df .to_csv( encoding="utf_8_sig")
# outfile_csv_filename = 'Output_MeCab.csv'
# st.download_button(label="csvファイルのダウンロード",data=outfile_csv_ginza,file_name=outfile_csv_filename)
# " ";" ";" "

# #--------- Ginza ---------------
# st.markdown("""####  形態素解析の結果（Ginza）""")
# nlp = spacy.load('ja_ginza_electra')
# doc = nlp(sentence)
# ginza.set_split_mode(nlp, "C")

# # 結果をデータフレームに格納
# result_list = []
# for sent in doc.sents:
#     result_list = result_list + [[str(token.i), token.text, token.lemma_, token.pos_, token.tag_] for token in sent]
# df_result = pd.DataFrame(result_list, columns = ['token_no', 'text', 'lemma', 'pos', 'tag'])

# st.dataframe(df_result)
# outfile_csv_ginza = df_result.to_csv( encoding="shift-jis")
# # outfile_csv_ginza = df_result.to_csv( encoding="utf_8_sig")
# # outfile_csv_ginza = df_result.to_string()
# outfile_csv_filename = 'Output_ginza.csv'
# st.download_button(label="csvファイルのダウンロード",data=outfile_csv_ginza,file_name=outfile_csv_filename)

import os

os.system('git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && cd mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -y -u -p $PWD')
os.system('git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git && cd mecab-unidic-neologd && ./bin/install-mecab-unidic-neologd -n -y -u -p $PWD')

import streamlit as st

import MeCab

st.set_page_config(page_title="NEologd demo")
st.title('NEologd demo')


"""
Input the text you'd like to analyze. See the [NEologd][] docs for more details.
[NEologd]: https://github.com/neologd
"""

if st.button('Update NEologd', help='It may take some time'):
    os.system('cd mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -y -u -p $PWD')
    os.system('cd mecab-unidic-neologd && ./bin/install-mecab-unidic-neologd -n -y -u -p $PWD')

text = st.text_area("input", "麩菓子は、麩を主材料とした日本の菓子。")

def make_row(word, kana_index=7, lemma_index=6):
    # https://stackoverflow.com/a/49774255/5602117
    ff = dict(enumerate(word.feature.split(",")))
    return dict(surface=word.surface, kana=ff.get(kana_index), lemma=ff.get(lemma_index), 
            pos1=ff.get(0), pos2=ff.get(1), pos3=ff.get(2), pos4=ff.get(3))

"""
#### [mecab-ipadic-NEologd : Neologism dictionary for MeCab](https://github.com/neologd/mecab-ipadic-neologd)
"""

data = []

tagger = MeCab.Tagger('-r /etc/mecabrc -d /home/user/app/mecab-ipadic-neologd')
node = tagger.parseToNode(text)
while node:
    if node.feature.startswith('BOS/EOS'):
        pass
    else:
        data.append(make_row(node))
    node = node.next

st.table(data)

"""
#### [mecab-unidic-NEologd : Neologism dictionary for unidic-mecab](https://github.com/neologd/mecab-unidic-neologd)
"""

data = []

tagger = MeCab.Tagger('-r /etc/mecabrc -d /home/user/app/mecab-unidic-neologd')
node = tagger.parseToNode(text)
while node:
    if node.feature.startswith('BOS/EOS'):
        pass
    else:
        data.append(make_row(node, kana_index=9, lemma_index=7))
    node = node.next

st.table(data)

"""
#### [MeCab](https://taku910.github.io/mecab/)
"""

data = []

tagger = MeCab.Tagger('-r /etc/mecabrc')
node = tagger.parseToNode(text)
while node:
    if node.feature.startswith('BOS/EOS'):
        pass
    else:
        data.append(make_row(node))
    node = node.next

st.table(data)