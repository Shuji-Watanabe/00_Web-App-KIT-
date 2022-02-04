import streamlit as st
import CaboCha

#sentence="今日は天気が良いですね．"
C_Param = CaboCha.Parser()
sentence = '猫は道路を渡る犬を見た。'
print(C_Param.parseToString(sentence))

#sentence=st.text_input("文章を入力してください．")
#sentence="今日は天気が良いですね．"
#c = CaboCha.Parser()
#tree = cp.pares(sentence)

#st.write("======= 形態素解析 =======")
#st.write("")
#for i in range(tree.size()):
#    tok = tree.token(i)
#    st.write('品詞：',tok.feature)
#    st.write('表層形：',tok.surface)
#    st.write("-"*40)
