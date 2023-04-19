#x^2+2x-3=0
def square(a,b,c):
    d=(b*b-4*a*c)**0.5
    x1=(-b-d)/2*a
    x2=(-b+d)/2*a
    return x1,x2

print(square(1,2,-3))
