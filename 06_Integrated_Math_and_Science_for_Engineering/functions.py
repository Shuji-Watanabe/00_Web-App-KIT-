from ast import Num
from dataclasses import replace
import streamlit as st
import sympy as sym
from sympy import *
import numpy as np


def cal_sum (formula,index_val,start_index,stop_index,output_form_key = "latex"):
    input_form = sympify(formula)
    output_form = sym.summation(input_form,(index_val,start_index,stop_index))
    if output_form_key == "latex":
        output_form = latex(factor(output_form))
    elif output_form_key == "sympy":
        output_form = factor(output_form)
    
    tmp_1 = latex( sympify(formula) )
    tmp_2 = latex( sympify(index_val) )
    tmp_3 = latex( sympify(start_index) )
    tmp_4 = latex( sympify(stop_index) )
    output_tmps = [tmp_1,tmp_2,tmp_3,tmp_4]
    return output_form , output_tmps

def format_disp(tmp_str,index_blac=0,index_bbrac=0):
    tmp_str = tmp_str.replace("**","^")
    tmp_str = tmp_str.replace("*"," ")

    if index_blac == 0:
        tmp_str = tmp_str.replace("(","\\left(")
        tmp_str = tmp_str.replace(")","\\right)")
    elif index_blac == 1:   
        tmp_str = tmp_str.replace("(","\\big(")
        tmp_str = tmp_str.replace(")","\\big)")
    elif index_blac == 2:
        tmp_str = tmp_str.replace("(","\\Big(")
        tmp_str = tmp_str.replace(")","\\Big)")
    elif index_blac == 3:
        tmp_str = tmp_str.replace("(","{")
        tmp_str = tmp_str.replace(")","}")        

    
    if index_blac == 1:
        tmp_str = tmp_str.replace("\{","\\big\{")
        tmp_str = tmp_str.replace("\}","\\big\}")
    elif index_blac == 2:
        tmp_str = tmp_str.replace("\{","\\Big\{")
        tmp_str = tmp_str.replace("\}","\\Big\}")
    else :
        tmp_str = tmp_str.replace("\{","\\left\{")
        tmp_str = tmp_str.replace("\}","\\right\}")
        
    return tmp_str

#日本ソフトウェア科学会第 33 回大会 (2016 年度) 講演論文集:数学的記号処理システムを用いたソフトウェアの構成手法より
# def md(*args):
#     s = ''
#     for x in args:
#         if (isinstance(x, Basic) or isinstance(x, MutableDenseMatrix) or isinstance(x,tuple)):
#             s += latex( sympify(x))
#         elif isinstance(x,np.ndarray): 
#             s += latex(Matrix(x))
#         elif (isinstance(x, str)): 
#             s += x
#         elif (isinstance(x, int) or isinstance(x, float)): 
#             s += str(x)
#         else: print(type(x))
#     return s

def str_brack(val, out_bracket_index = 0):
    if val >= 0:
        bracked_val = " %s "%(latex(val))
        if out_bracket_index == 1:
            bracket_index = 1
        else :
            bracket_index = 0
    else :
        bracked_val = " \\left(  %s  \\right) "%(latex(val))
        if out_bracket_index == 1:
            bracket_index = -1
        else :
            bracket_index = 0
    return bracked_val, bracket_index

def str_c_i(Num_Type_riemann):
    if Num_Type_riemann == 0:
        c_i = "x_{k}"
        text = ""
    elif Num_Type_riemann == 1:
        c_i = "\\frac{x_{k}+x_{k+1}}{2}"
        text = "ここで$~\\displaystyle \\frac{x_{k} + x_{k+1}}{2}~$は，\
                小区間$~\\big[x_{k},x_{k+1} \\big]~$の中央の$~x~$座標である．"
    elif Num_Type_riemann == 2:
        c_i = "x_{k-1}"
        text = ""
    elif Num_Type_riemann == 3:
        c_i = "x_{k:\\rm max}"
        text = "ここで$x_{k:\\rm max}$は，小区間$~\\big[x_{k},x_{k+1}\\big]~$において$~f(x)~$が最大となる$~x~$の値のことである．"
    elif Num_Type_riemann == 4:
        c_i = "x_{k:\\rm min}"
        text = "ここで$x_{k:\\rm min}$は，小区間$~\\big[x_{k},x_{k+1}\\big]~$において$~f(x)~$が最小となる$~x~$の値のことである．"
    return c_i, text

