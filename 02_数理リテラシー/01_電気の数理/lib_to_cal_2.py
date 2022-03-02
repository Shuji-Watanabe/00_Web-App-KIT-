########### Be used librarys ############
import math
import re as Re
from sympy import *


########### Class cal_log ###########
class cal_log:
    def __init__(self,form_log):
        self.a = sympify(form_log,evaluate = False)
        self.term = list( Add.make_args( expand(self.a) ) )
        self.tmp =[] ; self.info_01 = []
        for self.term_i in self.term :
            self.prim = list(self.term_i.primitive())
            self.num_rational = 1 ; self.num_iirational = 1
            for self.num in self.prim:
                if isinstance(self.num,Integer) or isinstance(self.num,Rational):
                    self.num_rational   = self.num_rational * self.num
                elif isinstance(num,Float):
                    self.num_rational   = self.num_rational * simplify(self.num,rational = True)
                else:
                    self.num_iirational = self.num_iirational * simplify( log(E**self.num))

            self.num_rational   = simplify(self.num_rational,rational = True)
            self.num_iirational = self.term_i/self.num_rational

            if fraction(self.num_iirational)[1] != 1:
                self.antilog = E**fraction(self.num_iirational)[0]
                self.base    = E**fraction(self.num_iirational)[1]
                self.info_01.append([self.num_rational,self.antilog,self.base])
            else :
                self.rational_num = self.num_rational
                self.info_01.append([self.rational_num,E,E])
        
                
    def get_info(self):
        return self.info_01
    
    def simplify(self):
        self.num = 0
        for self.num_00 in self.info_01:
            if self.num_00[2] == E :
                self.num += self.num_00[0]
            else:
                self.factor_num_00_i = factorint(self.num_00[1])
                self.num_01_keys     = list( factorint(self.num_00[1]).keys() )
                for self.n_key in self.num_01_keys:
                    self.num += self.num_00[0]*self.factor_num_00_i[self.n_key] * log(self.n_key)/log(self.num_00[2])
                
        return self.num

    def convert_to_tex(self):
        self.x = 0 ; self.ans = 'X00'
        for self.num in self.info_01:
            self.x += self.num[0]*log(self.num[1],self.num[2])
            if  self.num[1]  == E and self.num[0] >= 0 :
                self.ans += r"+ %s "%( latex(self.num[0]) ) 
            elif self.num[1] == E and self.num[0] < 0 :
                self.ans += r" %s "%( latex(self.num[0]) ) 
            elif self.num[1] != E and self.num[0] >= 0:
                self.ans += r"+ %s \cdot \log_{%s}\left( %s \right)"%( latex(self.num[0]),latex(self.num[2]),latex(self.num[1]) )
            else:
                self.ans += r" %s \cdot \log_{%s}\left( %s \right)"%( latex(self.num[0]),latex(self.num[2]),latex(self.num[1]) )

        self.ans = self.ans.replace("X00+ ","").replace("X00","")
        return self.ans


############ classsignifigant_figure ############
class sig_fig:
    def __init__(self,val):
        self.val_org = str(val)
        self.val_01  = Re.sub("\s","",str(val))
        self.val_01  = self.val_01.replace("**","^").split("*")
        self.num_part="1";self.sim_part = "1";self.tmp_sigdig=[]
        for i in range(len(self.val_01)):
            self.val_sym = sympify(self.val_01[i], evaluate = False)
            if isinstance(self.val_sym,Float) or isinstance(self.val_sym,Integer) or isinstance(self.val_sym,Pow):
                self.tmp_sigdig.append(len(str(self.val_01[i]).replace(".","")))
                self.num_part += "*" + str(self.val_01[i])
            else:
                self.sim_part += "*" + str(self.val_01[i])
 
        self.sigdig     = min(self.tmp_sigdig)
        self.index_val  = math.floor(math.log10(sympify(self.num_part)))
            
        self.num_part   = sympify(self.num_part)
        self.sim_part   = sympify(self.sim_part)
        
        if self.sigdig == 1:
            self.style_set  = r"%1" + str(self.sigdig-1) + "d"
        else:
            self.style_set  = r"%1." + str(self.sigdig-1) + "f"
        self.style_set += "*10^{%s}"  

    def num(self):
        a = (self.sigdig,self.index_val)            
        return a
    
    def cov_tex(self,tex_return=True):
        self.num_part_result = self.style_set%(self.num_part*10**(-self.index_val),self.index_val)
        self.sym_part_result = sympify(str(self.sim_part).replace("1.0*",""))
        if tex_return :
            self.sym_part_result = sympify(str(self.sym_part_result).replace("*",""))
        else:
            self.num_part_result = self.num_part_result.replace("^","**")
            self.num_part_result = self.num_part_result.replace("{","(")
            self.num_part_result = self.num_part_result.replace("}",")")
            self.num_part_result = sympify(self.num_part_result)
        self.num_part_result = self.num_part_result.replace("*","\\times")
        return self.num_part_result,self.sym_part_result
