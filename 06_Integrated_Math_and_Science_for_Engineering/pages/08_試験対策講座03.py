import streamlit as st
import sympy as sym
import pandas as pd
import numpy as np
import plotly as plotly

st.sidebar.markdown("""このWebアプリについての意見・感想はこちらから[クリック](https://forms.gle/NHbiNWkjHgd28K5C9)""")

L03_contents_list=["小テスト１における必要最低限の知識","リーマン和とリーマン積分","置換積分","部分積分"]
L03_contents_tab =[]
L03_contents_tab = st.tabs(L03_contents_list)
contents_num =0

####  Tab１  ####
# contents_num += 1
section_num = 1
with L03_contents_tab[contents_num]:
    