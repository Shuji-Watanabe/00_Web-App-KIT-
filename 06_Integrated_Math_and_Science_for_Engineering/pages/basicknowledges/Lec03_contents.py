def fundamental_theorem_of_calculus():
    strs=\
    """
    ###### 微分積分学の基本定理（第二定理）
    区間$~\\big[a,\\ b \\big]~$で定義された連続関数$~f(x)~$の任意の原始関数を$~F(x)~$とするとき
    $$
      \\int_{a}^{b} f(x) dx = F(b)-F(a)
    $$
    が成り立つ．  
    $\\phantom{a}$  
    ###### 微分積分学の基本定理（第二定理）の気持ち
    区間$~\\big[a,\\ b\\big]~$で定義された連続関数$~f(x)~$の定積分（リーマン積分）は
    $$
        \\int_{a}^{b} f(x) dx 
        =
        \\lim_{n \\to \\infty}
        \\sum_{k=1}^{n} f\\big( c_i \\big) \\Delta x
    $$
    によって定義されている．しかし，関数$~f(x)~$の原始関数$~F(x)~$がわかるのであれば，
    和の極限を考える必要はなく$~F(b)-F(a)~$の計算によって求められることを意味している．
    しかし，関数$~f(x)~$の原始関数がわからなければ，和の極限として求めなくてはならない．
      
    $\\phantom{a}$  

    ###### 不定積分と原始関数
    ある微分可能な関数を$~F(x)~$とし，定数を$~C~$とすると
    $$
        \\frac{d}{dx}\\Big\{ F(x) + C \\Big\} 
        =
        \\frac{d}{dx}\\Big\{ F(x) \\Big\} 
    $$
    であることから，関数$~f(x)~$に対して，
    $$
        \\frac{d}{dx}\\Big\{ F(x) \\Big\} = f(x)
    $$
    となる関数$~F(x)~$が無数に存在することがわかる．
    $~F(x)~$は関数$~f(x)~$の原始関数であると．

    関数$~f(x)~$の任意の原始関数を表す記号を
    $$
      \\int f(x) dx
    $$
    とし，これを$~f(x)~$の不定積分という．
    無数にある原始関数の中の任意の１つを$~F(x)~$，任意の定数（積分定数）を$~C~$とすると，
    $$
      \\int f(x) dx = F(x) + C
    $$
    と表すことができる．
    """
    return strs

def integral_calculus_formulas():
    strs =\
    """
    ##### 不定積分の性質
    - 被積分関数の和について
        $$ 
            \\int 
                \\Big\{
                    f(x) + g(x)
                \\Big\}dx 
            =
            \\int f(x) dx
            +
            \\int g(x) dx
        $$
    - 被積分関数の定数倍
        $$
            \\int c f(x) dx = c \\int f(x) dx
        $$
    - 導関数と不定積分
        $$
            \\int \\frac{d}{dx} \\Big\{ f(x) \\Big\} dx = f(x) 
          \\quad \\text{または} \\quad
            \\frac{d}{dx} \\Big\{ \\int f(x)  dx \\Big\} = f(x) 
        $$ 
    - 合成関数の不定積分（置換積分）
        $$
            \\int f\\Big( g(x) \\Big) dx  
            =
            \\int f\\big( u \\big) \\cdot \\frac{1}{\\frac{du}{dx} } du  
        $$
        ここで$~u=g(x)~$である．
        ※ 同じ結論に至るが，教科書と説明が異なるので注意する．
    $\\phantom{x}$  
    
    ##### 初等関数の不定積分
    - べき関数の不定積分
        - $\\alpha \\ne -1 $のとき
            $$
                \\int x^{\\alpha} dx = \\frac{1}{\\alpha + 1} x^{\\alpha + 1} + C
            $$
        - $\\alpha = -1 $のとき
            $$
                \\int x^{-1} dx = \\ln|x| + C
            $$  
    - 指数関数の不定積分  
        $$
            \\int e^{x} dx = e^x + C
        $$
        $$
            \\int a^{x} dx = \\frac{a^x}{\\ln a} + C
        $$  
    - 三角関数の不定積分
        - 必要最低限
            $$
                \\int \\cos x dx = \\sin x + C
            $$
            $$
                \\int \\sin x dx = -\\cos x + C
            $$    
            $$
                \\int \\frac{1}{\\cos^2 x} dx = \\int \\sec^2 x dx =\\tan x + C
            $$    
            $$
                \\int \\frac{1}{\\sin^2 x} dx = \\int \\csc^2 x dx =-\\cot x + C = - \\frac{1}{\\tan x} + C
            $$   
        - より高みを目指して
            $$
                \\int \\sec x \\tan x dx = \\sec x + C
            $$
            $$
                \\int \\sec x \\cot x dx = -\\csc x + C
            $$
    - 分数関数の不定積分
        - 必要最低限   
            $$
                \\int \\frac{1}{\\sqrt{1+x^2}} dx = \\ln \\Big| x + \\sqrt{1 + x^2} \\Big| + C
            $$   
        - より高みを目指して
            $$
                \\int \\frac{1}{\\sqrt{1-x^2}} dx = \\sin^{-1} x + C
            $$
            $$
                \\int \\frac{1}{1+x^2} dx = \\tan^{-1} x + C
            $$ 
            $$
                \\int \\frac{1}{x\\sqrt{x^2-1}} dx = \\sec^{-1} + C
            $$    
    $\\phantom{a}$ 
    """
    return strs