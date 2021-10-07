import streamlit as st
import pandas as pd
import math

Data_file00= st.file_uploader("**データファイルをアップロードしてください**", type={"csv", "txt"})
if Data_file00:
    Data_00= pd.read_csv(Data_file00,encoding="SHIFT-JIS")
    
    ##### １）入力データの表示（開始）#####
    st.write("## **Step01:入力されたデータの確認**")
    st.table(Data_00.T)
    Col_Names=Data_00.columns.values
    D00_sort=Data_00.sort_values(Col_Names[0])
    ##### 入力データの表示（終了）#####
    
    ##### ２）データの並べ替え（開始）#####
    st.write("## **Step02:データの並べ替え**")
    st.table(D00_sort.T)
    ##### データの並べ替え（終了）#####

    ##### 3)算術平均の計算（開始）#####
    st.write("## **Step03:算術平均の計算**")
    N = D00_sort.count()
    Ave_x = float(Data_00[Col_Names[0]].mean())
    st.write("$\ \ \quad$**計算結果**"r"""：算術平均$\ \overline{x}$ =$%r$""" % (Ave_x))

    N_CK03_1=st.checkbox("補足情報1：算術平均の定義")
    if N_CK03_1:
        st.write(
            "$\ \ \\quad\\displaystyle \\overline{x} =\
                 \\frac{1}{n} \\sum_{i=1}^{n} x_{i}\
                 =\\frac{1}{n} \\left(x_{1}+x_{2}+x_{3}+\\cdots \\cdots+x_{n}\\right)$"
            )
    N_CK03_2=st.checkbox("補足情報2：計算過程")
    if N_CK03_2:
        STR_03_01 = "$\ \ \\quad\\displaystyle \\overline{x}$=$"
        for i in range(len(Data_00[Col_Names[0]])):
            if i ==0 :
                STR_03_01 = STR_03_01 + "\\displaystyle\\frac{1}{" + str(int(N)) + "}"
                STR_03_01 = STR_03_01 + "\\Big(" + str( Data_00.iat[i,0]) 
            else : 
                STR_03_01 = STR_03_01 + "+" + str( Data_00.iat[i,0]) 
        STR_03_01 = STR_03_01 + "\\Big)$ "
        st.write(STR_03_01)
    ##### 算術平均の計算（終了）#####

    ##### 4)中央値の計算（開始）#####
    st.write("## **Step04:中央値の計算**")
    p = 0.5
    R0 = 1 + (N-1)*p
    s , r = math.modf(R0)
    X_num0 = (1-s)* D00_sort.iat[int(r)-1,0] + s*D00_sort.iat[int(r),0]
    st.write(
            r"""$\ \ \quad$中央値 = $%r$"""
                %
                (X_num0)
            )
    N_CK04_1=st.checkbox("途中計算：中央値の求め方")
    if N_CK04_1:
        if int(N) % 2 == 1 :
            st.write("$\ \ \quad$データ数が奇数なので，ソートされたデータの中央の値を求める") 
        else:
            st.write("$\ \ \quad$データ数が偶数なので，ソートされたデータの中央にある２つのデータの算術平均を求める") 
            st.write(
                r"""$\ \ \quad$中央値 = $\displaystyle\frac{%r + %r}{2}$ = $%r$"""
                %
                (D00_sort.iat[int(r)-1,0],D00_sort.iat[int(r),0],X_num0)
            )
    ##### 4)中央値の計算（終了）#####
    
    ##### 5)範囲の計算（開始）#####
    st.write("## **Step05:範囲の計算**")
    data_max = Data_00[Col_Names[0]].max()
    data_min = Data_00[Col_Names[0]].min()
    D_range = data_max - data_min
    st.write("$\ \ \quad$**計算結果**"r"""：範囲の値=$%d-%d$=$%r$""" % (data_max,data_min,D_range))
    ##### 範囲の計算（終了）#####

    ##### 6)分散の計算（開始）#####
    st.write("## **Step06:分散の計算**")
    Variance = Data_00[Col_Names[0]].var(ddof=0)
    Ave_sq_x = 0
    for i in range(len(Data_00[Col_Names[0]])):
        x_i = Data_00.iat[i,0]
        Ave_sq_x = Ave_sq_x + float(x_i)**2
    Ave_sq_x = Ave_sq_x / float(N)
    Variance_2 = float(Ave_sq_x) - float(Ave_x)**2
    st.write("$\ \ \quad$**計算結果**"r"""：(標本)分散$s^2$=$%r$""" % (Variance))
    N_CK06_1=st.checkbox("補足情報1：標本分散の定義")
    if N_CK06_1:
        st.write(
            "$\ \ \\quad\\displaystyle \\overline{x} =\
                 \\frac{1}{n} \\sum_{i=1}^{n} \\left(x_{i}-\\overline{x}\\right)^2\
                 =\\frac{1}{n}\
                    \\left\{\
                     \\left(x_{1}-\\overline{x}\\right)^2\
                        +\\left(x_{2}-\\overline{x}\\right)^2\
                        +\\cdots\
                        +\\left(x_{n}-\\overline{x}\\right)^2\
                    \\right\}$"
            )
    N_CK06_2=st.checkbox("補足情報2：標本分散の計算過程(方法１）")
    if N_CK06_2:
        st.write("$\ \ \\quad$"r"""分散 $s^2$""")
        STR_06_01 = ""
        for i in range(len(Data_00[Col_Names[0]])):
            if i ==0 :
                STR_06_01 = STR_06_01 + "$\ \ \\quad\\displaystyle=\\frac{1}{" + str(int(N)) + "}"
                STR_06_01 = STR_06_01 \
                            + "\\Big\\{" \
                            + "\\left(" \
                            + str(Data_00.iat[i,0])\
                            + "-"\
                            + str(Ave_x)\
                            + "\\right)^2"
            else : 
                STR_06_01 = STR_06_01 \
                            + "+"\
                            + "\\left("\
                            + str(Data_00.iat[i,0])\
                            + "-"\
                            + str(Ave_x)\
                            + "\\right)^2" 
        STR_06_01 = STR_06_01 + "\\Big\\}$ "
        st.write(STR_06_01)
        st.write( "$\ \ \\quad$=$" +str(Variance)+ "$ " )
    N_CK06_3=st.checkbox("補足情報3：標本分散の計算過程(方法２）")
    if N_CK06_3:
        
        st.write("$\ \ \\quad$ 途中計算１"r"""：算術平均の２乗 $(\overline{x})^2$=$%r$""" % (float(Ave_x)**2))
        st.write("$\ \ \\quad$ 途中計算２"r"""：2乗平均 $\overline{x^2}$=$%r$""" % (float(Ave_sq_x)))
        st.write("$\ \ \\quad$ 途中計算３"r"""：分散 $s^2$=$\overline{x^2}-(\overline{x})^2$=$%r$""" % (round(float(Variance_2),1) ))
    ##### 分散の計算（終了）#####

    ##### 7)範囲の計算（開始）#####
    st.write("## **Step07:標準偏差の計算**")
    st.write("$\ \ \quad$**計算結果**"r"""：標準偏差 $s$=$\sqrt{s^2}$=$\sqrt{%r}$=$%r$""" % (round(float(Variance_2),1),float(Variance_2)**0.5))
    ##### 範囲の計算（終了）#####

    ##### 8）分位数の計算（開始）#####
    st.write("## **Step08:第 X 四分位数の計算**")
    col1, col2=st.columns([1,1])
    with col2:
        X = st.radio(label = "[xの値を選択する]",options = ["1","2","3"])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    X_d = float(X)
    p = X_d*0.25
    R0 = 1 + (N-1)*p
    s , r = math.modf(R0)
    X_num = (1-s)* D00_sort.iat[int(r)-1,0] + s*D00_sort.iat[int(r),0]
    with col1:
        st.write("#### $\ \ \quad$計算結果")
        if int(X) == 2:
            st.write(
                r"""$\ \ \quad$第%s四分位数(中央値)　$Q_{%s}$ = $%r$"""
                %
                (X, X, X_num)
            )
        else:
            st.write(
                r"""$\ \ \quad$第%s四分位数　$Q_{%s}$= $%r$"""
                %
                (X, X,  X_num)
            )
    #st.write("$\ \ \quad$注意：第２四分位数は**中央値**とも呼ばれる" )
    N_CK08_1=st.checkbox("補足情報１：分位数の定義")
    if N_CK08_1:
        st.write(
            "$\ \ \quad$ 分位数の定義は，\
                [inclusive（INC）流儀の定義 R(type=7)](http://kj01.kgu.mydns.jp/fujimoto/tips/qptile.html#Inc)を採用"
            )
    N_CK08_2=st.checkbox("補足情報２：計算過程")
    if N_CK08_2:
        st.write("$\ \ \quad$ 各変数の計算結果は次の通り")
        st.write(
            r"""
                $\ \ \quad$ 
                ▶︎ $\displaystyle p=\frac{%r}{4}=%r$
            """
            %(int(X),p)
            )
        st.write(
            r"""
                $\ \ \quad$ 
                ▶︎ 順位$R=1 + %r \times (%d-1) = %r$
            """
            % (p, N, float(R0))
            )
        st.write(
            r"""
                $\ \ \quad$ 
                ▶︎ $R$の整数部分 $r=%d$,$\quad$ $R$の少数部分 $s=%r$
            """
            % (r,s)
            )
        st.write(
            r"""
                $\ \ \quad$ 
                ▶︎ 第%s四分位数$Q_{%s}$= $%r$ + $\big(%r-%r\big)\times%r$=$%r$
            """
            % (X, X, D00_sort.iat[int(r)-1,0], \
                D00_sort.iat[int(r),0],D00_sort.iat[int(r)-1,0],float(s),\
                X_num )
            )
    ##### 9)四分位偏差の計算（開始）#####
    st.write("## **Step09:四分位偏差の計算**")
    p1 = 1*0.25
    p3 = 3*0.25
    R0_1 = 1 + (N-1)*p1
    R0_3 = 1 + (N-1)*p3
    s1,r1 = math.modf(R0_1)
    s3,r3 = math.modf(R0_3)
    X1_num = (1-s1)* D00_sort.iat[int(r1)-1,0] + s1*D00_sort.iat[int(r1),0]
    X3_num = (1-s3)* D00_sort.iat[int(r3)-1,0] + s3*D00_sort.iat[int(r3),0]
    Per_variance = 0.5 * (X3_num - X1_num)
    st.write(
            r"""$\ \ \quad$四分位偏差
                =
                $\displaystyle \frac{1}{2}\Big(Q_3 - Q_1\Big)$
                 =
                $\displaystyle \frac{1}{2}\Big(%r - %r\Big)$
                =
                $%r$"""
            %
            (X3_num,X1_num, Per_variance)
    )
    ##### 四分位偏差の計算（終了）#####
    

else:
    st.write("データファイルをアップロードしてください．")
#st.table(Data_00.describe())