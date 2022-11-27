import streamlit as st


st.markdown("###### １．判別式とは")
"""
2次方程式$~ax^2 + bx +c = 0~$実数解の個数は判別式 $~D~$
$$
    D = b^2 - 4ac
$$
の値によって，次のように分類できる．
$$
\\begin{align*}
D &> 0  \ \ \Longleftrightarrow \ \  \\text{\\small 異なる{\\color{red} ２つ}の実数解を持つ } 
\\\\ 
D &= 0  \ \ \Longleftrightarrow \ \  \\text{\\small {\\color{red} １つ}の実数解（重解）を持つ}
\\\\
D &< 0  \ \ \Longleftrightarrow \ \  \\text{\\small 実数解を持たない}
\\\\
\\end{align*}
$$
"""

st.markdown("###### ２．実数解の個数の視覚的理解")
st.video("./sample_mov.mov")
col = st.columns(3)
with col[0]:
    st.image("./Sample_fig_01.tiff")
with col[1]:
    st.image("./Sample_fig_02.tiff")
with col[2]:
    st.image("./Sample_fig_03.tiff")
