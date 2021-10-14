from sympy import *
#import streamlit as st

def List_to_vec01(Val):
    List_to_vec01_STR="\\displaystyle"
    List_to_vec01_STR=List_to_vec01_STR+" \\overrightarrow{v}_{\\rm Ave.} = "
    List_to_vec01_STR=List_to_vec01_STR+" \\begin{pmatrix}"
    for i in range(len(Val)):
        if i < len(Val)-1 :
            List_to_vec01_STR=List_to_vec01_STR + "\\displaystyle" +latex(Val[i])+"&"
        else:
            List_to_vec01_STR=List_to_vec01_STR + "\\displaystyle" +latex(Val[i])
    List_to_vec01_STR=List_to_vec01_STR+"\\end{pmatrix}"
    return List_to_vec01_STR

def Add_1(delta_t,V_i,V_f):
    Add_1_Num00=len(V_i)
    Average_V=[]
    for i in range(Add_1_Num00):
        Average_V.append(
              (sympify(V_f[i]) - sympify(V_i[i]))
                /
                delta_t
         )
    return Average_V