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

# Leman
def faktroial(n): #Factorial
    p=1
    for i in range(1 ,n+1):
        p=p*i
    print(p)
faktroial(6)
