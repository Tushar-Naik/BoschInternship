
n=50
l=[]
def f(x):
    return (-5*(x**5))+(4*(x**4))-(12*(x**3))+(11*(x**2))-(2*x)+1

def g(x1,x2,k):
 i=x2-x1
 #print 'interval:',i
 b=i/2*((5.0**0.5)-1)
 #print b
 x3=x2-b;
 x4=x1+b;
 l.append([x1,x3,x4,x2,f(x3),f(x4)])
 if(n-k==0):
  return x3
 elif(i==0 or x3==x4):
  return x3
 else:
  if(f(x3)<f(x4)):
   return g(x1,x4,k+1)
  else:
   return g(x3,x2,k+1)

def write():
    x=open('golden_search_op.txt','a')
    x.write('x1\t\tx3\t\tx4\t\tx2\t\tf(x3)\t\tf(x4)\n')
    for l1 in l:
        x.write('\t'.join(map(str,l1)))
        x.write('\n')
    x.close()


    
    



        
    
