def roots(a, b, c):
    sqrt = (b**2 - 4*a*c)**0.5
    r1 = (-b + sqrt)/(2*a)
    r2 = (-b - sqrt)/(2*a)
    return f"{r1}, {r2}"

def value_y(a,b,c,x):
    y=a*x**2+b*x+c
    return y

def to_string(a, b, c):
    if b > 0:
        b=f"+ {b}x"
    if c > 0:
        c =f"+ {c}"
    return f"f(x)= {a}x {b} {c}"

def derivation(a, b):
    return f"2{a}x + {b}"
