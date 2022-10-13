import streamlit as st
import random as rd
import sympy as sym

def make_coefficient(n_range=10, difficulty_level=1):
    cof = 0 # coefficient
    #   integer only
    if difficulty_level == 1:
        cof = 0
        while cof == 0 :
            cof = rd.randrange(1,n_range,1)
        tmp_index = rd.randrange(1,4,1)
        sign_cof = (-1)**tmp_index
            
    # difficulty_level = 2
    #   nth root　   
    ### difficulty_level = 3
    #   exponential
    ### difficulty_level = 4
    #   logarithm
    return cof , sign_cof

def make_rational(difficulty_level=1):
    #   integer only
    if difficulty_level == 1 :
        a , sign_a = make_coefficient(10,1)
        b , sign_b = make_coefficient(10,1)
        c = sym.Rational(a, b)
        while c.is_integer :
            a , sign_a = make_coefficient(10,1)
            b , sign_b = make_coefficient(10,1)
            c = sym.Rational(a, b)     
        sign_c = sign_a*sign_b
    ### difficulty_level = 2
    #   nth root　   
    ### difficulty_level = 3
    #   exponential
    ### difficulty_level = 4
    #   logarithm

    return c , sign_c

def make_power_func(n_range, difficulty_level=1,inner_function="x"):
    """
    make_power_func return power function c*x^a or c*
    difficulty_level=1 : c f(x) or f(cx)
    difficulty_level=2 : f(ax+b)
    """
    a = 0
    c = 0
    tmp = 0
    x = sym.symbols("x")
    f = sym.sympify(inner_function)
    if difficulty_level == 1:
        while a ==0  :
            a=rd.randrange(-n_range,n_range,1)
        func = sym.Pow(f,a)/a
        index_brack = 0
        num_exp = a
    elif difficulty_level == 2:
        b = 0
        while b ==0  :
            a=rd.randrange(-n_range,n_range,1)
            b=rd.randrange(-n_range,n_range,1)
            c=rd.randrange(-n_range,n_range,1)
        cof = sym.Rational(c,b)
        func = cof*sym.Pow(f,a)
        if a*c >= 0 :
            index_brack = 0
        else :
            index_brack = 1
        num_exp = a

    elif difficulty_level == 3 :
        b=0 ; e=0
        while b*e == 0  :
            a=rd.randrange(-n_range,n_range,1)
            b=rd.randrange(-n_range,n_range,1)
            c=rd.randrange(-n_range,n_range,1)
            d=rd.randrange(-n_range,n_range,1)
            e=rd.randrange(-3,3,1)
        d2 = rd.randrange(1,9,1)
        if sym.Mod(d2,3) != 1 :
            d = 1
        cof = sym.Rational(c,b)
        num_exp = sym.Rational(d,e)
        func = cof*sym.Pow(f,num_exp)
        if c*b >= 0 :
            index_brack = 0
        else :
            index_brack = 1
    return func , index_brack , num_exp

def make_log_func(difficulty_level=1, base = "e",inner_function="x"):
    """
    difficulty_level = 1
      > base is e (Euler's number)
    difficulty_level = 2
      > base is a in (2,3,5,7)
    difficulty_level = 3
      > a (positive real number)
        a = base
    """
    #   base = Euler's number e
    e = sym.E
    x = sym.symbols("x")
    u = sym.sympify(inner_function)
    if difficulty_level == 1 :
        base  = e
        log_func = sym.log(u,base)        
    #   base = natural number
    elif difficulty_level == 2 :
        base_list = {1:2,2:3,3:5,4:7}
        base  = rd.randrange(1,len(base_list),1)
        log_func = sym.log(u,base_list[base])
        base  = str( base )
    return log_func ,  base 

def make_exponential_function(difficulty_level=1, base = "e",inner_function="x"):
    """
    difficulty_level = 1
      > base is e (Euler's number)
    difficulty_level = 2
      > base is a in (2,3,5,7)
    difficulty_level = 3
      > a (positive real number)
        a = base
    """
    e = sym.E
    x = sym.symbols("x")
    u = sym.sympify(inner_function)
    #   base = Euler's number e
    if difficulty_level == 1 :
        exp_func = sym.exp( u )
        base  = str(e)        

    #   base = natural number
    elif difficulty_level == 2 :
        base_list = {1:2,2:3,3:5,4:7}
        base_num  = rd.randrange(1,len(base_list),1)
        exp_func = sym.Pow(base_list[base_num],u)
        base  = str( base_list[base_num])
        if sym.Mod( rd.randrange(1,9,1),2) == 0:
            exp_func = sym.simplify(exp_func/sym.log(base_list[base_num]))
        else :
            exp_func = exp_func
    return exp_func, base 

def make_trigonometric_functions(difficulty_level=1,trig_func_type = 0,inner_function="x"):
    """
    trigonometric function type
      > 1:sin(x) 2:cos(x) 3:tan(x) 4:csc(x) 5:sec(x) 6:cot(x)
    difficulty_level = 1
      > f(x) in sin, cos, tan
    difficulty_level = 2
      > f(x) in sin, cos, tan, csc, sec, tan
    difficulty_level = 3
      > f(x) + f(x) 
        f(x) in sin, cos, tan, csc, sec, tan
        g(x) in sin, cos, tan, csc, sec, tan
    """
    x = sym.symbols("x")
    u = sym.sympify(inner_function)
    f_list = {\
                1:sym.sin(u),2:sym.cos(u),3:sym.tan(u),\
                4:sym.csc(u),5:sym.sec(u),6:sym.cot(u),\
             }
    f_num01 = rd.randrange(1,3,1)
    f_num02 = rd.randrange(1,6,1)
    
    f_01 = f_list[f_num01]
    f_02 = f_list[f_num02]

    if trig_func_type == 0 :
        # sin, cos, tan
        if difficulty_level == 1 :
            trig_func = f_01
        # sin, cos, tan, csc, sec, tan
        elif difficulty_level == 2 :
            trig_func = f_02
        # f(x) + g(x)
        elif difficulty_level == 3 :
            trig_func = f_01 + f_02
    else :
        trig_func = f_list[trig_func_type]

    return trig_func,f_num01,f_num02
