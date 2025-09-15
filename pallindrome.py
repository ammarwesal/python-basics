def palindrome():
 x=str(input("enter the string: "))
 
 for i in range(0,len(x)//2):
     if x[i]!=x[len(x)-1-i]:
      return False
 return True      
      
     
result=palindrome()
if result:
    print("palindrome")
else:
    print("no")