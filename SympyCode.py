
""" #1 """

from sympy import solve, Symbol 

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

expr1 = 3*x + 5*y - 5
expr2 = 10*x - 3*y - 15
expr3 = 4*y + 10*z - 19 

solve((expr1, expr2, expr3), dict=True)



""" #2 """

from sympy import solve, Symbol 

x = Symbol('x')
expr1 = x**2 - 16
solve((expr1), dict=True)




""" #3 """

from sympy import solve
x = Symbol('x')
expr = x**2 + 10*x - 5
solve(expr, dict=True)




""" #4 """

from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
plot(x**2 + 5)


from sympy.plotting import plot
from sympy import Symbol
x = Symbol('x')
plot(x**3 + 10*x + 5)


from sympy.plotting import plot
from sympy import Symbol
a = Symbol('a')
plot(a**7 - 5*a)


