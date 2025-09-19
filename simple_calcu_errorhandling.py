try:
    x=float(input("emter the 1st number: "))
    z=str(input("entr th operator(+,-,*,/): "))
    y=float(input("eneter the 2nd number: "))
    if z=="+":
        ans=x+y
        print(ans)
    elif z=="-":
        ans=x-y
        print(ans)
    elif z=="*":
        ans=x*y
        print(ans)
    elif z=="/":
        ans=x/y
        print(ans)
    else:
        print("Wrong operator! Please use +, -, *, or /")
        
except ValueError:
    print("Error: Please enter valid numbers!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")