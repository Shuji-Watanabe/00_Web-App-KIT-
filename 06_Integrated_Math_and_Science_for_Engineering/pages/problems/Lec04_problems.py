from cmath import sin
import streamlit as st
import sympy as sym
import re
import random as rd
from pages.makeprb import makefunc
from pages.basicknowledges import Lec03_contents

def prob_indefinite_integral(integrand_type = "power", difficulty_level=1):
    """
      integrad_type = power, log, exp, trig
      difficulty_level=1 : c f(x) or f(cx)
      difficulty_level=2 : f(ax+b)
    """
    q_list = [] 
    #-------- power ---------------------------------------------------------------------------------------------------
    if integrand_type == "power" :
    #---- make answers ----
        if difficulty_level == 1 :
            ans,index_ans,num_exp = makefunc.make_power_func(n_range=10,difficulty_level=difficulty_level,inner_function="x")
            n_rad = rd.randrange(1,9,1)
            if sym.Mod(n_rad, 2)  == 0 :
                coff , sign_coff = makefunc.make_coefficient()
            elif sym.Mod(n_rad, 2)  == 1 :
                coff , sign_coff = makefunc.make_rational()
            ans = sign_coff*sym.sympify(coff)*ans
        elif difficulty_level == 2 :
            a0,b0 = 2,4
            while sym.gcd(a0,b0) != 1 :
                a0  , sign_a_f = makefunc.make_coefficient()
                b0  , sign_b_f = makefunc.make_coefficient()
            f0 = "%s*x + (%s)"%(a0,b0)
            ans,index_ans,num_exp  = makefunc.make_power_func(n_range=10,difficulty_level=2,inner_function=f0)
        elif difficulty_level == 3 :
            a0,b0 = 2,4
            while sym.gcd(a0,b0) != 1 :
                a0  , sign_a_f = makefunc.make_coefficient()
                b0  , sign_b_f = makefunc.make_coefficient()
            f0 = "%s*x + (%s)"%(a0,b0)
            ans,index_ans,num_exp= makefunc.make_power_func(n_range=10,difficulty_level=3,inner_function=f0)

    #-------- logarithm ---------------------------------------------------------------------------------------------------
    elif integrand_type == "log" :
        #--- make coefficient --
        n_rad = rd.randrange(1,9,1)
        if sym.Mod(n_rad, 2)  == 0 :
            coff , sign_coff = makefunc.make_coefficient()
        elif sym.Mod(n_rad, 2)  == 1 :
            coff , sign_coff = makefunc.make_rational()
        #--- make answers
        if difficulty_level == 1 :
            ans, base = makefunc.make_log_func(difficulty_level=1, base ="e", inner_function="x" )   
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)
        elif difficulty_level == 2 :
            a0,b0 = 2,4
            while sym.gcd(a0,b0) != 1 :
                a0,sign_a_f = makefunc.make_coefficient()
                b0,sign_b_f = makefunc.make_coefficient()
            f0 = "%s*x + (%s)"%(a0,b0)
            ans,index_ans = makefunc.make_log_func(difficulty_level=1, base ="e", inner_function=f0 )   
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)

    #-------- exponential ---------------------------------------------------------------------------------------------------
    elif integrand_type == "exp" :
        #--- make coefficient --
        n_rad = rd.randrange(1,9,1)
        if sym.Mod(n_rad, 2)  == 0 :
            coff , sign_coff = makefunc.make_coefficient()
        elif sym.Mod(n_rad, 2)  == 1 :
            coff , sign_coff = makefunc.make_rational()
        #--- make answers
        if difficulty_level == 1:
            ans, base = makefunc.make_exponential_function(difficulty_level=1, base = "e",inner_function="x")
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)
        elif difficulty_level == 2:
            ans, base = makefunc.make_exponential_function(difficulty_level=2,inner_function="x")
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)
        elif difficulty_level == 3 :
            a0,b0 = 2,4
            while sym.gcd(a0,b0) != 1 :
                a0,sign_a_f = makefunc.make_coefficient()
                b0,sign_b_f = makefunc.make_coefficient()
            f0 = "%s*x + (%s)"%(a0,b0)
            ans, base = makefunc.make_exponential_function(difficulty_level=1, base = "e",inner_function=f0)
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)        
        elif difficulty_level == 4 :
            a0,b0 = 2,4
            while sym.gcd(a0,b0) != 1 :
                a0,sign_a_f = makefunc.make_coefficient()
                b0,sign_b_f = makefunc.make_coefficient()
            f0 = "%s*x + (%s)"%(a0,b0)
            ans, base = makefunc.make_exponential_function(difficulty_level=2, base = "e",inner_function=f0)
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)  


    #-------- Trigonometric functions -------------------------------------------------------------------------------
    elif integrand_type == "trig" :
        #--- make coefficient --
        n_rad = rd.randrange(1,9,1)
        if sym.Mod(n_rad, 2)  == 0 :
            coff , sign_coff = makefunc.make_coefficient()
        elif sym.Mod(n_rad, 2)  == 1 :
            coff , sign_coff = makefunc.make_rational()

        #--- make answers -----

        ##----- type cf(x) where f(x) = sin or cos or tan 
        if difficulty_level == 1:
            ans, type_index1, type_index2 = makefunc.make_trigonometric_functions(difficulty_level=1,trig_func_type=0,inner_function="x")
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)
            type_index = 1
        ##----- type cf(x) where f(x) = sin , cos, tan, csc , sec, cot
        elif difficulty_level == 2:
            ans ,type_index1 ,type_index2 = makefunc.make_trigonometric_functions(difficulty_level=2,trig_func_type=0,inner_function="x")
            n_rand = rd.randrange(1,9,1)
            if sym.Mod(n_rand,2) == 0 and (type_index2 >= 3) :
                  ans = ans.rewrite(sym.sin)
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)
            type_index = type_index2
        ##----- type f(ax+b) where f(x) = sin , cos, tan, csc , sec, cot
        elif difficulty_level == 3 :
            a0,b0 = 2,4
            while sym.gcd(a0,b0) != 1 :
                a0,sign_a_f = makefunc.make_coefficient()
                b0,sign_b_f = makefunc.make_coefficient()
            f0 = "%s*x + (%s)"%(a0,b0)
            ans,type_index1, type_index2 = makefunc.make_trigonometric_functions(difficulty_level=2,trig_func_type=0,inner_function=f0)
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans) 
            type_index = 1
        ##----- type f(x)+g(x) where f(x) and g(x) = sin , cos, tan, csc , sec, cot
        elif difficulty_level == 4 :
            ans ,type_index1 ,type_index2 = makefunc.make_trigonometric_functions(difficulty_level=3,trig_func_type=0,inner_function="x")
            ans = sym.sympify(sign_coff*coff)*sym.sympify(ans)
            type_index = type_index2
    #---- make problems ----
    x = sym.symbols("x")
    if integrand_type ==  "power" :
        integrand = sym.diff(ans,x)
        if num_exp == 1 :
            ans = sym.factor( sym.integrate( integrand , x) ) 
    elif integrand_type ==  "exp" :
        integrand = sym.powsimp( sym.diff(ans,x) , combine='all') 
    elif integrand_type ==  "trig":
        integrand = sym.trigsimp( sym.diff(ans,x) ) 
        if difficulty_level != 4 :
            if type_index == 3 :
                ans = sym.trigsimp( ans).rewrite(sym.tan) 
            elif type_index == 4 :
                ans = sym.trigsimp( ans).rewrite(sym.csc) 
            elif type_index == 5 :
                ans = sym.trigsimp( ans).rewrite(sym.sec) 
            elif type_index == 6 :
                ans = sym.trigsimp( ans).rewrite(sym.cot) 
        else :
            integrand = sym.factor( sym.diff(ans,x),deep=True,fraction=True) 
    else :
        integrand = sym.factor( sym.diff(ans,x) ) 

    ans = sym.latex(ans,ln_notation = True)
    tmp_coff = integrand.as_coefficients_dict()
    coff = tmp_coff[list(tmp_coff)[0]]

    #---- add bracket / append problems and answers ----
    if coff < 0 or len(integrand.as_ordered_terms()) >= 2:
        if str(sym.latex(integrand,ln_notation = True)).find('left') == -1 :
            integrand = "\\left( "+ sym.latex(integrand,ln_notation = True) + "\\right)"
        else :
            integrand = "\\left\{ "+ sym.latex(integrand,ln_notation = True) + "\\right\}"
    else :
        integrand = sym.latex(integrand,ln_notation = True) 

    #---- append q_list problems and answers ----
    tmp_list = [integrand,ans]
    q_list.append(tmp_list)
    return q_list
