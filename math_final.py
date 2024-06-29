import math
print('WELCOME TO SRIJON\'S CALCULATOR')
a=int(input('Enter the value of a'))
b=int(input('Enter the value of b'))
c=int(input('Enter the value of c'))
def show_result(x,y,z):
    d=pow(b,2)-(4*a*c)
    e=(-b+pow(d,0.5))/(2*a)
    f=(-b-pow(d,0.5))/(2*a)
    if d>0:
        return 'Congrats your results are', e,f
    elif d==0:
        return 'WOW! Both values are', e,f
    else:
        return 'LOL. Give proper value' 
    
print(show_result(a,b,c))
