n = str(input("enter the string: "))
print("orignal string: ",n)

y=len(n)
reversed_str = ""
 
for i in range(y):
 x=n[y-1-i]    
 reversed_str += x

print("reversed string:",reversed_str)