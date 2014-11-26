"""
" This is an implementation of Fourth order Runga-Kutta
" on y' = ty + y + t^2
"
" The general algoritm is as follows
" for each step
"   f_1(y_k, t_k)
"   f_2(y_k + h/2*f_1, t_k + h/2)
"   f_3(y_k + h/2*f_2, t_k + h/2)
"   f_4(y_k + h*f_3, t_k + h)
"   y_[k+1] = y_k + h/6*(f_1 + 2*f_2 + 2*f_3 + f_4)
"   t_k = t_k + h
"""


a = 0
b = 0.4
n = 2
h = (b - a) / n

t = [0]
y = [2]


for k in range(0, n):
    F_1 = t[k]*y[k] + y[k] + t[k]**2
    F_2 = (t[k] + h/2)*(y[k] + h/2*F_1) + (y[k] + h/2*F_1) + (t[k] + h/2)**2
    F_3 = (t[k] + h/2)*(y[k] + h/2*F_2) + (y[k] + h/2*F_2) + (t[k] + h/2)**2
    F_4 = (t[k] + h)*(y[k] + h*F_3) + (y[k] + h*F_3) + (t[k] + h)**2
    y.append(y[k] + h/6*(F_1 + 2*F_2 + 2*F_3 + F_4))
    t.append(t[k] + h)


print(y[n])

