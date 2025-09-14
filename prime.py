x=int(input("enter any integer: "))
if x<=1:
    is_prime =False
else:
    is_prime =True
    
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
          is_prime=False
          
if is_prime ==True:
 print("prime")
else:
 print("not prime")