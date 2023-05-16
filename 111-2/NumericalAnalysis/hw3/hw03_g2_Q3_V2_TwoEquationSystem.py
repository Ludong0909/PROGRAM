import sympy as sym

def TwoEquationSystem(sympy_f1 ,sympy_f2 ,x0 ,y0 ,tolerance = 1e-6):

    # set function 
    # x, y are symbol and x0, y0 are values
    x, y = sym.symbols('x y')
    f1 = sym.lambdify((x, y), sympy_f1, 'numpy')
    fx1 = sym.lambdify((x, y), sym.diff(sympy_f1, x), 'numpy')
    fy1 = sym.lambdify((x, y), sym.diff(sympy_f1, y), 'numpy')
    f2 = sym.lambdify((x, y), sympy_f2, 'numpy')
    fx2 = sym.lambdify((x, y), sym.diff(sympy_f2, x), 'numpy')
    fy2 = sym.lambdify((x, y), sym.diff(sympy_f2, y), 'numpy')
    
    # set innitial number of iterate
    i = 0

    # calculate the result
    while (abs(f1(x0,y0))>tolerance and abs(f2(x0,y0))>tolerance):
        i += 1
        jacobian = fx1(x0,y0)*fy2(x0,y0)-fy1(x0,y0)*fx2(x0,y0)  # Jacobian Matrix
        deltax = (-f1(x0,y0)*fy2(x0,y0)+f2(x0,y0)*fy1(x0,y0))/jacobian
        deltay = (-f2(x0,y0)*fx1(x0,y0)+f1(x0,y0)*fx2(x0,y0))/jacobian
        x0 += deltax
        y0 += deltay
        print('current ans: ', x0, y0, ' ,iteration: ' ,i)
    return (x0,y0)  # return x0, y0 after iterate

# set target functions
# set x, y to the symbol of function
x, y = sym.symbols('x y')
f1 = x**2+2*x+2*y**2-26
f2 = 2*x**3-y**2+4*y-19

# set tolerance
TOL = 0.0001

# use defined function TwoEquationSystem to get the result 
sol = TwoEquationSystem(f1,f2,1,1,TOL)
print(sol)

sol2 = TwoEquationSystem(f1,f2,-1,-1,TOL)
print(sol2)