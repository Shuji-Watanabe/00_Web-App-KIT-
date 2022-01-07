from sympy import *
import numpy  as np
#### Listをベクトル表示させる関数 ####################################
## 入力値：Val:リスト型の変数
## 返り値：ist_to_vec01_STR：streamlit のlatex()でベクトル表示できる文字列
## 使い方
##   A = List_to_vec01(Val)
##   st.write(A) <- 横ベクトル化された式が出力される
#################################################################
def List_to_vec01(Val):
    List_to_vec01_STR="\\displaystyle"
    List_to_vec01_STR=List_to_vec01_STR+" \\begin{pmatrix}"
    for i in range(len(Val)):
        if i < len(Val)-1 :
            List_to_vec01_STR=List_to_vec01_STR + "\\displaystyle " +latex(Val[i])+",&"
        else:
            List_to_vec01_STR=List_to_vec01_STR + "\\displaystyle " +latex(Val[i])
    List_to_vec01_STR=List_to_vec01_STR+"\\end{pmatrix}"
    return List_to_vec01_STR

#### 時間に依存する物理量の平均変化率を計算する関数 #######################
#################################################################
def Cal_Q_Average_ver01(delta_t,delta_Q):
    Q_A_Num00=len(delta_Q)
    Average_Q=[]
    for i in range(Q_A_Num00):
        Average_Q.append(delta_Q[i]/delta_t)
    return Average_Q

#### マークダウン形式の文字列への変換関数 ###########################
#日本ソフトウェア科学会第 33 回大会 (2016 年度) 講演論文集
#数学的記号処理システムを用いたソフトウェアの構成手法より
#################################################################
def md(*args):
    s = ''
    for x in args:
        if (isinstance(x, Basic) or isinstance(x, MutableDenseMatrix) or isinstance(x,tuple)):
            s += latex( sympify(x))
        elif isinstance(x,np.ndarray): 
            s += latex(Matrix(x))
        elif (isinstance(x, str)): 
            s += x
        elif (isinstance(x, int) or isinstance(x, float)): 
            s += str(x)
        else: print(type(x))
    return s