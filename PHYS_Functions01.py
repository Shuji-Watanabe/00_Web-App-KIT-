from sympy import *

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
            List_to_vec01_STR=List_to_vec01_STR + "\\displaystyle" +latex(Val[i])+"&"
        else:
            List_to_vec01_STR=List_to_vec01_STR + "\\displaystyle" +latex(Val[i])
    List_to_vec01_STR=List_to_vec01_STR+"\\end{pmatrix}"
    return List_to_vec01_STR

#### 時間に依存する物理量の平均変化率を計算する関数 #######################
## 入力値：delta_t:時間の変化量
## 入力値：delta_Q：Qの変化量，リスト型変数
## 返り値：Average_Q：平均変化率，リスト型変数
## 使い方
##   A = Cal_Q_Average_ver01(dt,dQ)
##   A <- 平均変化率がリスト型でAに格納される
 #################################################################
def Cal_Q_Average_ver01(delta_t,delta_Q):
    Q_A_Num00=len(delta_Q)
    Average_Q=[]
    for i in range(Q_A_Num00):
        Average_Q.append(delta_Q[i]/delta_t)
    return Average_Q