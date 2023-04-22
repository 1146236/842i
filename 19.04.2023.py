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

print(square(3,5,4))

#narmin
#parabolanin yerlesmesi, parabolanin tepe noqtesinin yerlesmesi
#y=a(x-m)**2+n
def square(a, b, c):
    d = (b**2-4*a*c)
    x1 = (-b-d**0.5)/2*a
    x2 = (-b+d**0.5)/2*a
    m = -b/2*a
    n = 4*a*c-b**2/4*a

    if a>0 :
        print("parabolanin qollari yuxari yonelib")

    elif a<0 :
        print("parabolanin qollari asagi yonelib")
    
    if c>0 :
        print("parabola y oxunu musbetde kesir")

    elif c<0 :
        print("parabola y oxunu menfide kesir")

    if m>0 and n>0 :
        print("tepe noqtesi 1ci rubdedir")

    elif m<0 and n>0 :
        print("tepe noqtesi 2ci rubdedir")
    
    elif m<0 and n<0 :
        print("tepe noqtesi 3cu rubdedir")

    elif m>0 and n<0 :
        print("tepe noqtesi 4cu rubdedir") 
        
    print(x1, x2)
    print(m, n)
square(3, 5, 4)
