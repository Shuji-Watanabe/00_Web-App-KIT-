import streamlit as st

st.markdown("##### 令和４年度 高大連携による数理教育研究会(第3回 定例研究会)")

"""
##### １．本日の占い
"""


import random as rad
dict_uranai01 ={
                0:"今日のあなたはビタミン不足．働き過ぎに注意．",
                1:"今日のあなたは元気いっぱい．働き過ぎに注意．",
                2:"今日のあなたはエネルギー不足．働き過ぎに注意．"
             }

dict_uranai02 ={
                0:"ラッキーアイテム：果汁100%ジュース",
                1:"ラッキーアイテム：スポーツドリンク",
                2:"ラッキーアイテム：エナジードリンクドリンク"
             }

col=st.columns([1,3])
with col[0]:
    result = st.button("占い結果の表示")
with col[1]:
    if result:
        number = rad.randrange(0,2)
        f"""
            **今日のあなたの運勢は**  
            {dict_uranai01[number]}  
            {dict_uranai02[number]}
        """

""" """
""" """

"""
##### ２．streamlitの参考資料
"""

"""
* 2-1) Google ColaboratoryでStreamlitを始める  
  [Google ColaboratoryでサクっとStreamlit（最小構成）](https://qiita.com/gudapys/items/62eda02bdb3de5530a23)

* 2-2) Streamlitの使い方  
  [【超簡単Webアプリ】streamlitでWebアプリを最速で作ってネット公開！](https://www.youtube.com/watch?v=4nsTce1Oce8)  
  [Streamlit 公式HP：Streamlit API reference](https://docs.streamlit.io/library/api-reference)

* 2-3) python用数式処理ライブラリ sympy  
  [SymPy による数式処理とグラフ作成](https://home.hirosaki-u.ac.jp/jupyter/sympy/)  
  [Sympyの公式HP](https://www.sympy.org/en/index.html)
"""