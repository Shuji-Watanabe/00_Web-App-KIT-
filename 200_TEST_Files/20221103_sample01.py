import streamlit as st
import sympy as sym

st.title("べき関数関係")
Contents_list=["基本公式","例題","基本問題","標準問題"]
Contents_tab =[]
Contents_tab = st.tabs(Contents_list)
Contents_num = 0


#######   Contents 01 main   #################
with Contents_tab[Contents_num]:
    st.markdown( f"### {Contents_num+1:02}. {Contents_list[Contents_num]}") 
    with st.container():
            """
            $$
                \\int
                \,
                x^{\,\\alpha}
                \,
                dx
                =
                \\left\{
                    \\begin{align*}
                        &\\quad 
                            \\frac{1}{\\alpha+1} x^{\\alpha+1}+C 
                            \\quad :\\quad  \\alpha \\ne -1 \\ \\text{のとき}
                        \\\\
                        &\\phantom{a}
                        \\\\
                        &\\quad \\ln|x| +C
                            \\quad :\\quad \\alpha = -1 \\ \\text{のとき}
                    \\end{align*}
                \\right.
            $$
            """
#######   Contents 02 main   #################
Contents_num += 1
with Contents_tab[Contents_num]:
    st.markdown( f"### {Contents_num+1:02}. {Contents_list[Contents_num]}") 
    

#######   Contents 03 main   #################
Contents_num += 1
with Contents_tab[Contents_num]:
    st.markdown( f"### {Contents_num+1:02}. {Contents_list[Contents_num]}") 

    class get_expr_info01:
        def __init__(self : str,function_str):
            import sympy as sym
            self.f = sym.sympify(function_str)
            self.str = function_str

        def get_coeff_polynomial(self,symbol="x"):
            """
            Get coefficients of polynomial
            """
            import sympy as sym
            val_symbol = sym.symbols(str(symbol))
            expanded_function = self.f.expand()
            coefficients_of_x = dict(expanded_function.as_coefficients_dict())
            
            term_list = []
            for cof_key in coefficients_of_x.keys():
                exponent = list(sym.integrals.meijerint._exponents(cof_key,val_symbol))
                if not exponent:
                    exponent = ['0']
                term = [ str(coefficients_of_x[cof_key]), str(exponent[0])]
                term_list.append([term[0],term[1]])
            term_list = sorted(term_list, key=lambda x: x[1],reverse=True)
            return str(symbol), term_list

        def get_bracket_info(self):
            """
            Get brackets and their structure in an expression
            output : dict
                     "log((x+3)(x+2))"
                     -> {'Lv0Num0': '(x+3)', 'Lv0Num1': '(x+2)', 'Lv0Num2': 'log(Lv0Num0Lv0Num1)', 'Lv1Num0': '(Lv0Num0Lv0Num1)', 'Lv1Num1': 'logLv1V0'}
            **** restraction of orignal expr from output ****
            list_keys_rev = list(tmp_val_dict.keys())
            list_keys_rev.reverse()
            print(list_keys_rev)
            for i in list_keys_rev:
                out_form_str = out_form_str.replace(i,tmp_val_dict[i]) 
            print(out_form_str)
            """
            import re
            tmp_str=self.str
            level=0
            output_dict = {}
            while len(re.findall('\([^\(\)]+\)',tmp_str)) > 0 :
                num = 0
                for i in re.findall('\([^\(\)]+\)',tmp_str):
                    val_name = f'Lv{level}Num{num}'
                    output_dict[val_name] = i
                    tmp_str = tmp_str.replace(i,val_name,1)
                    num += 1
                val_name = f'Lv{level}Num{num}'
            output_dict[val_name] = tmp_str
            level += 1
            return output_dict

    def get_coeff_monomial(monomial_expr):
        "monomial_expr : sympy format"
        coefficient_of_expr_dict = dict(monomial_expr.as_coefficients_dict())
        expr = list(coefficient_of_expr_dict.keys())[0] 
        coefficient_of_expr = coefficient_of_expr_dict[expr]
        if coefficient_of_expr > 0 :
            coefficient_of_expr_sign = "+"
        elif coefficient_of_expr < 0 :
            coefficient_of_expr_sign = "-"
        else :
            st.error("Error : get_coeff_monomial")
            st.stop() 
        return coefficient_of_expr_sign,coefficient_of_expr,expr

    def get_last_key(dict_val):
        """
        Get the last key of a dictionary type variable.
        """
        dict_val_last_key = list(dict_val.keys())[len(dict_val)-1]
        return dict_val_last_key
    
    def convert_str_brac_to_vbrac_logarithm(get_bracket_info_output_list):
        """
         convert log(x) to log|x|
         input : Use get_bracket_info of get_expr_info01.
        """
        import re 
        dict_val = get_bracket_info_output_list
        dict_val_keys_list = list(dict_val.keys())
        dict_val_keys_list_rev = dict_val_keys_list
        dict_val_keys_list_rev.reverse()
        if dict_val[dict_val_keys_list_rev[0]].count('log') == 1:
            n=0
            for i in dict_val_keys_list_rev:
                if n == 0 :
                    out_form_str = "\\log\\left|" 
                    out_form_str += re.sub('log',"",dict_val[i] ) 
                    out_form_str += "\\right|"
                elif n == 1:
                    out_form_str = out_form_str.replace(i,dict_val[i])
                    out_form_str = re.sub('["\(","\)"]',"",out_form_str)
                else :
                    out_form_str = out_form_str.replace(i,dict_val[i]) 
                n+=1
        else :
            out_form_str = "error"
        return out_form_str
    # --- convert to sympy data and latex data
    def convert_str_to_sympy_latex (tmp_list):
        """
        Converts coefficients and exponents of power functions (str type) to sympy and latex formats
        outfile : list[dict] 
                  Ex. [{"sympy":*,"latex":*}]
        """
        output_list_dict_list = []
        for i in tmp_list:
            if sym.sympify(i[0]) == 1 :
                tmp_coff_sym = 1
                tmp_exponent_sym = sym.sympify(i[1])
                tmp_coff_latex = ""
                tmp_exponent_latex = sym.latex(tmp_exponent_sym)
            elif sym.sympify(i[0]) < 0 :
                tmp_coff_sym = sym.sympify(i[0])
                tmp_exponent_sym = sym.sympify(i[1])
                tmp_coff_latex = "\\left( " +  sym.latex(tmp_coff_sym) + "\\right)"
                tmp_exponent_latex = sym.latex(tmp_exponent_sym)
            else :
                tmp_coff_sym = sym.sympify(i[0])
                tmp_exponent_sym = sym.sympify(i[1])
                tmp_coff_latex =  sym.latex(tmp_coff_sym) 
                tmp_exponent_latex = sym.latex(tmp_exponent_sym)
            output_list_dict_list.append(\
                                            {\
                                            "sympy":[tmp_coff_sym,tmp_exponent_sym]\
                                            ,"latex":[tmp_coff_latex,tmp_exponent_latex]\
                                            }
                                        )
        return output_list_dict_list


    ####  展開 + 基本の不定積分　タイプ　Q1-001 #### 
    q_num = "Q1-001"
    with st.container():
        st.button("問題の更新",key="test")
        ###======  input data 
        import ast 
        Q_data_file_text = open('00_問題データ.txt', 'r', encoding='UTF-8')
        # st.write(Q_data_file_text.read())
        # ORG_f_list_dict = ast.literal_eval( Q_data_file_text.read() )
        ORG_f_list_dict = {
                            "Q1-001-memo":"展開して積分するタイプの問題",
                            "Q1-001":["(4*x**5 - x - 1)/x**2",
                                    "(2*x-1)/( 3*sqrt(x) )",
                                    "( x**3-4*x+3 )/x**2"
                                    ,"( x-2 )*( x+1 )"]
                             }
        # ORG_f_list_dict = ast.literal_eval( Q_data_file_text )
        f_list  = ORG_f_list_dict[q_num]


        
        ###======  make ans  ======
        import random as rd
        function_str = rd.choice(f_list)
        function_sym = sym.sympify(function_str,evaluate=None)
        symbol_func_str, function_sym_info = get_expr_info01(function_sym).get_coeff_polynomial()
        symbol_func_sym = sym.symbols(symbol_func_str)


        ### ---- line 0
        display_str_l00 = sym.latex(function_sym)

        ### ---- line 1 
        display_str_l01 = sym.latex(function_sym.expand())
        ### ---- data check display_str_l01
        # f"""$${display_str_l01}$$"""

        ### ---- line 2 
        display_str_l02_list = convert_str_to_sympy_latex (function_sym_info)
        display_str_l02 = ""
        for i in range(len(display_str_l02_list)):
            if i == 0 :
                display_str_l02 += '\\int\\, '
            else :
                display_str_l02 += ' + \\int\\, '
            if display_str_l02_list[i]["sympy"][0] == 1 :
                display_str_l02 += ""
            elif display_str_l02_list[i]["sympy"][0] < 0 :
                display_str_l02 += display_str_l02_list[i]["latex"][0] + "\\cdot "
            else :
                display_str_l02 += display_str_l02_list[i]["latex"][0] + "\\cdot "
            display_str_l02 += f'{symbol_func_str}^{{ { display_str_l02_list[i]["latex"][1] }  }}'
            display_str_l02 += f'\\, d{symbol_func_str}'

        ###--check data--
        # for i in display_str_l02_list :
        #     f"""
        #         $
        #         { i["latex"][0] } 
        #         \\cdot
        #         {symbol_func_str}
        #         ^{{ {i["latex"][1]}  }}
        #         $
        #      """

        ### ---- line 3
        display_str_l03_list = []
        for i in display_str_l02_list:
            tmp_func_sym = symbol_func_sym**i["sympy"][1]
            tmp_integrated_f_sym = sym.integrate(tmp_func_sym,symbol_func_sym)
            tmp_integrated_f_latex = sym.latex(tmp_integrated_f_sym)
            # st.write(f"Expression_sym=${str(tmp_integrated_f_sym)}$ , Expression_latex=${str(tmp_integrated_f_latex)}$ ")
            if tmp_integrated_f_latex.count("log") == 1 :
                # st.markdown(f"expression = ${tmp_integrated_f_latex}$")
                tmp_integrated_f_str = str(tmp_integrated_f_sym)
                tmp_info_log = get_expr_info01(tmp_integrated_f_str).get_bracket_info()
                tmp_integrated_f_latex = convert_str_brac_to_vbrac_logarithm(tmp_info_log)
            display_str_l03_list.append(\
                                    {"sympy":[i["sympy"][0],tmp_integrated_f_sym]\
                                    ,"latex":[i["latex"][0],tmp_integrated_f_latex]\
                                    }\
                                )
          
        ### ---- data check  display_str_l03_list
        # for i in display_str_l03_list:
        #     f"""
        #         $$
        #         \\int\\, {i["latex"][0]} \\, d{symbol_func_str}
        #         =
        #         {i["latex"][1]} +C
        #         $$
        #      """
        display_str_l03 = ""
        for i in range(len(display_str_l02_list)):
            if i == 0 :
                display_str_l03 += ''
            else :
                display_str_l03+= '+'
            if display_str_l02_list[i]["sympy"][0] == 1 :
                display_str_l03 += ""
            else :
                display_str_l03 += display_str_l02_list[i]["latex"][0] + "\\cdot"
            display_str_l03 += f'\\int\\,  {symbol_func_str}^{{ { display_str_l02_list[i]["latex"][1] }  }}'
            display_str_l03 += f'\\, d{symbol_func_str}'

        ### ---- line 4
        display_str_l04 = ""
        for i in range(len(display_str_l03_list)):
            if i == 0 :
                display_str_l04 += ''
            else :
                display_str_l04+= '+'
            if display_str_l03_list[i]["sympy"][0] == 1 :
                display_str_l04 += ""
            else :
                display_str_l04 += display_str_l03_list[i]["latex"][0] + " \\cdot "
            tmp_symbol, tmp_coeff =get_expr_info01(display_str_l03_list[i]["sympy"][1]).get_coeff_polynomial()
            
            if sym.sympify(tmp_coeff[0][0]) < 0 :
                display_str_l04 += "\\left(" + display_str_l03_list[i]["latex"][1] + "\\right)"
            else :
                display_str_l04 += display_str_l03_list[i]["latex"][1]
        display_str_l04 += '+C'

        ### ---- line 5
        display_str_l05_list = []
        display_str_l05 = 0
        for i in range(len(display_str_l03_list)):
            tmp_term_sym = display_str_l03_list[i]["sympy"][0]*display_str_l03_list[i]["sympy"][1]

            # display_str_l05 += tmp_term_sym
            sign,coeff,expr = get_coeff_monomial(tmp_term_sym)
            # st.write(f"sign=${sign}$,coeff=${coeff}$,expr=${expr}$")
            tmp_term_latex = sym.latex(expr)
            
            if tmp_term_latex.count("log") == 1 :
                # st.markdown(f"expression_sym = ${str(tmp_term_sym)}$")
                tmp_info_log = get_expr_info01(str(expr)).get_bracket_info()
                # st.markdown(f"{tmp_info_log}")
                tmp_term_latex = convert_str_brac_to_vbrac_logarithm(tmp_info_log)
                # st.write(f"coeff = ${coeff}$, is coeff 1 or -1? = {coeff == 1 or coeff == -1}")
                if coeff == -1:
                    tmp_term_latex = "-" + tmp_term_latex
                else :
                    tmp_term_latex = sym.latex(sym.sympify(coeff)) + tmp_term_latex
                # st.markdown(f"tmp_term_latex = {tmp_term_latex}")
            else :
                tmp_term_latex = sym.latex(tmp_term_sym)

            if i == 0 :
                display_str_l05 = tmp_term_latex
            else :
                if sign == "+" :
                    display_str_l05 += "+" + tmp_term_latex
                elif sign == "-" :
                    display_str_l05 += tmp_term_latex
                else :
                    st.error("stop : line 5")
                    st.stop
            display_str_l05_list.append({"sympy":tmp_term_sym,"latex":tmp_term_latex})
        
        
        display_str_l05 += "+C"
        # display_str_l05 = display_str_l05.replace("(","|").replace(")","|")
    ### ---- display : results
    f"""
        ###### 次の不定積分を求めなさい．ただし，積分定数は$~C~$とすること．
        （１）  $\\displaystyle \\int\\, {display_str_l00} \\, d{symbol_func_str} $
    """
    
    with st.expander("（１）の解答・解説"):
        f"""
            $$
            \\begin{{align*}}
                &\\int\\, {display_str_l00} \\, d{symbol_func_str}
                    \\\\
                    &=
                    \\int\\, \\left( {display_str_l01}\\right) \\, d{symbol_func_str} 
                    \\\\
                    &=
                    {display_str_l02}
                    \\\\
                    &=
                    {display_str_l03}
                    \\\\
                    &=
                    {display_str_l04}
                    \\\\
                    &=
                    {display_str_l05}
                    \\\\
            \\end{{align*}}
            $$
        """

