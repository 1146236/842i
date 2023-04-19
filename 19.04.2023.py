#x^2+2x-3=0
def square(a,b,c):
    d=b*b-4*a*c
    if(d<0):
        x="Heqiqi koku yoxdur"  
        result=x      
    elif(d==0):
        x=(-b-d**0.5)/2*a
        result=x
    else:
        x1=(-b-d**0.5)/2*a
        x2=(-b+d**0.5)/2*a
        result=x1,x2    
    return result

print(square(3,4,5))

# Ramazan
# (c-b*x)**0.5=a*x
a=int(input("Enter the first index:"))
b=int(input("Enter the second index:"))
c=int(input("Enter the third index:"))
def func (a,b,c):
    D=b**2-4*a*c
    if D==0:
        x=(-b-D**0.5)/2*a
        result=x
    if D<0:
        x="Heqiqi koku yoxdur."
        result=x
    if (c-b*x1 or x2)==0:  #Kok altindadi deye
        x==0
        result=x
    else:
        x1=int((-b-D**0.5)/2*a)
        x2=int((-b+D**0.5)/2*a)
        result=x1,x2
    return result

print(func(a,b,c))
