
a = 0
b = 0.4
n = 10000000000
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

