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

#### 平均速度を計算する関数 ##########################################
## 入力値：delta_t:時間の変化量
## 入力値：V_i：変化前の速度，リスト型変数
## 入力値：V_f：変化後の速度，リスト型変数
## 返り値：Average_V
## 使い方
##   A = Cal_V_Average_ver01(dt,v1,v2)
##   A <- 平均速度がリスト型でAに格納される
 #################################################################
def Cal_V_Average_ver01(delta_t,V_i,V_f):
    Add_1_Num00=len(V_i)
    Average_V=[]
    for i in range(Add_1_Num00):
        Average_V.append(
              (sympify(V_f[i]) - sympify(V_i[i]))
                /
                delta_t
         )
    return Average_V