import streamlit as st
import sympy as sym
from sympy import *
from sympy.simplify.sqrtdenest import sqrtdenest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from matplotlib import patches
import plotly.graph_objs as go
import functions as myfunc
import re
import random as rd
from pages.basicknowledges import Lec03_contents
from pages.problems import Lec04_problems

Lec03_contents_list=["基礎例題","標準例題","応用例題","微分積分学の基本定理","不定積分に関する公式集"]
Lec03_contents_tab =[]
Lec03_contents_tab = st.tabs(Lec03_contents_list)
contents_num =0
lec_num =3

####  Tab１  ####
# contents_num += 1
section_num = 1
q_num = 0

with Lec03_contents_tab[contents_num]:
    from pages.makeprb import makefunc

    q_num_0 = 0
    st.markdown("### %s. %s"%(contents_num+1,Lec03_contents_list[contents_num])) 
    key_name_b = "%s_%s"%(lec_num,contents_num)
    st.sidebar.button("問題の更新",key=key_name_b)
    st.sidebar.error("注意：更新ボタンを押さなくても，アクセスするたびに問題が変わります．また，標準例題や応用例題の問題も変わります．")
    q_num += 1
    st.markdown("##### Lec.%s-%s Q%s 次の不定積分を求めなさい．ただし，積分定数は$~C~$とする．"%(lec_num,section_num,q_num))
 
    ##### make Q1 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list=[]
            q_list=Lec04_problems.prob_indefinite_integral(integrand_type = "power",difficulty_level=1)
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))
        with col_q01[1]:
            with st.expander("解答の表示"): 
                if q_list[0][0] == 0 :
                    """
                    **解答：$\\displaystyle C$**
                    """
                else :
                    """
                    **解答：$\\displaystyle %s+C$**
                    """%(q_list[0][1])
    st.empty()

    ##### make Q2 ###############################################################################################
    with st.container():
        q_list = []
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = Lec04_problems.prob_indefinite_integral(integrand_type = "log", difficulty_level=1)
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))
        with col_q01[1]:
            with st.expander("解答の表示"): 
                    """
                    **解答：$\\displaystyle %s+C$**
                    """%(q_list[0][1].replace("(","|").replace(")","|"))

    ##### make Q3 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=1, integrand_type = "exp")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))

        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                """%(q_list[0][1])

    ##### make Q4 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=2, integrand_type = "exp")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            q_list[0][0] = q_list[0][0].replace('\\left\(','').replace('\\right\)','')
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))

        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                """%(q_list[0][1])

    ##### make Q5 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=1, integrand_type = "trig")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            q_list[0][0] = q_list[0][0].replace('\\left\(','').replace('\\right\)','')
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))
        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                """%(q_list[0][1])

    st.empty()

    ##### make Q6 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=2, integrand_type = "trig")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            q_list[0][0] = q_list[0][0].replace('\\left\(','').replace('\\right\)','')
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))

        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                """%(q_list[0][1])

    st.empty()

####  Tab２  ####
contents_num += 1
section_num += 1
q_num_0 = 0
with Lec03_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec03_contents_list[contents_num])) 
    q_num += 1 
    st.markdown("##### Lec.%s-%s Q%s. 次の不定積分を求めなさい．ただし，積分定数は$~C~$とする．"%(lec_num,section_num,q_num))

    ##### make Q1 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(integrand_type = "power",difficulty_level=2)
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))
        with col_q01[1]:
            with st.expander("解答の表示"): 
                if q_list[0][0] == "0" :
                    """
                    **解答：$\\displaystyle C$**
                    """
                else :
                    """
                    **解答：$\\displaystyle %s+C$**
                    """%(q_list[0][1])

    ##### make Q2 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=2, integrand_type = "log")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))
        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                _ _ _ _ _
                **開発中**
                """%(q_list[0][1].replace("(","|").replace(")","|"))

    ##### make Q3 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=3, integrand_type = "exp")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))
        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                _ _ _ _ _
                **開発中**
                """%(q_list[0][1])

    ##### make Q4 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=4, integrand_type = "exp")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            q_list[0][0] = q_list[0][0].replace('\\left\(','').replace('\\right\)','')
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))

        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                _ _ _ _ _
                **開発中**
                """%(q_list[0][1])

    ##### make Q5 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=3, integrand_type = "trig")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            q_list[0][0] = q_list[0][0].replace('\\left\(','').replace('\\right\)','')
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))

        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                """%(q_list[0][1])


####  Tab３  ####
contents_num += 1
section_num = 1
with Lec03_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec03_contents_list[contents_num])) 
    q_num = 0
    q_num_0 = 0

    ##### make Q1 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(integrand_type = "power",difficulty_level=3)
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))
        with col_q01[1]:
            with st.expander("解答の表示"): 
                if q_list[0][0] == "0" :
                    """
                    **解答：$\\displaystyle C$**
                    """
                else :
                    """
                    **解答：$\\displaystyle %s+C$**
                    """%(q_list[0][1])

    ##### make Q3 ###############################################################################################
    with st.container():
        col_q01 = st.columns([5,4])
        with col_q01[0]:
            #---- make problems and answers ----
            q_list = []
            q_list=Lec04_problems.prob_indefinite_integral(difficulty_level=4, integrand_type = "trig")
            #---- display ----
            q_num_0 += 1
            key_name = "q%0d_%s_%s_%s"%(q_num,lec_num,section_num,q_num)
            cb_name = "Q%s-(%s)の答え"%(q_num,q_num_0)
            q_list[0][0] = q_list[0][0].replace('\\left\(','').replace('\\right\)','')
            st.markdown("$\\displaystyle \\quad (%s) \int\\ %s\\ dx$"%(q_num_0,q_list[0][0]))

        with col_q01[1]:
            with st.expander("解答の表示"): 
                """
                **解答：$\\displaystyle %s+C$**
                """%(q_list[0][1])
####  Tab４  ####
contents_num += 1
section_num = 1
with Lec03_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec03_contents_list[contents_num])) 
    q_num = 0
    st.markdown(Lec03_contents.fundamental_theorem_of_calculus())

####  Tab５  ####
contents_num += 1
section_num = 1
with Lec03_contents_tab[contents_num]:
    st.markdown("### %s. %s"%(contents_num+1,Lec03_contents_list[contents_num])) 
    q_num = 0
    st.markdown(Lec03_contents.integral_calculus_formulas())