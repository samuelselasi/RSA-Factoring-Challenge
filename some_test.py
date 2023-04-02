from sympy import factorint

n = 3141592653589793238462643383279502884197169399375105820974944592

factors = factorint(n)

p, q = factors.keys()

print(f"The factors of {n} are {p} and {q}")
