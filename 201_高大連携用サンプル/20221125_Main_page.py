import streamlit as st

st.markdown("##### 令和４年度 高大連携による数理教育研究会(第3回 定例研究会)")

"""
##### １．本日の占い
"""


import random as rad
dict_uranai01 ={
                0:"今日のあなたはビタミン不足．",
                1:"今日のあなたは元気いっぱい．動きすぎに注意",
                2:"今日のあなたはエネルギー不足．"
             }

dict_uranai02 ={
                0:"ラッキーアイテム：オロナミンC",
                1:"ラッキーアイテム：経口補水液",
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
