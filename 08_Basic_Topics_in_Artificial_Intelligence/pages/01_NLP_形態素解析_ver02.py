# import os
# import pkg_resources, imp
import streamlit as st
# import spacy_streamlit

st.error("調整中")

models = ["ja_core_news_lg", "ja_core_news_md", "ja_core_news_sm"]

# # 未ダウンロードのモデルファイルがある場合はダウンロード
# for model in models:
#     try:
#         imp.find_module(model)
#     except ImportError:
#         os.system("python -m spacy download {}".format(model))
#         imp.reload(pkg_resources)


# spacy_streamlit.visualize(models, "")

# """
# ### Dependency Parse & Part-of-speech tags の見方
# 係り受けタグと品詞タグについてはこちらから --> 
# [タグの見方](https://qiita.com/kei_0324/items/400f639b2f185b39a0cf)        
# """