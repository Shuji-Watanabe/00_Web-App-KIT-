import streamlit as st


st.markdown("""####  構文分析""")
sentence = st.text_input("文章を入力してください．","頭が赤い魚を食べる猫．")

if len(sentence) == 0 :
    st.error("文章を入力してください．")
    st.stop()

st.markdown("""####  構文分析の結果（Ginza）""")

import spacy
import ginza

text = sentence

nlp = spacy.load("ja_ginza_electra")
doc = nlp(text)

st.write('---- bunsetu_spans ----')
for span in ginza.bunsetu_spans(doc):
    for token in span.lefts:
        st.write(f'{token} : {str(ginza.bunsetu_span(token))} → {str(span)}')


st.write('---- bunsetu_phrase_spans (主辞) ----')
for span in ginza.bunsetu_phrase_spans(doc):
    for token in span.lefts:
        st.write(f'{token} : {str(ginza.bunsetu_span(token))} → {str(span)}')