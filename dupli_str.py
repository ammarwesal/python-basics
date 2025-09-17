def mynew():
    y=[]
    c={}
    x=str(input("enter the string: "))
    for i in range(len(x)):
        if x[i] not in y:  # Only process if not already in y
            count = 1
            for j in range(i+1,len(x)):
                if x[i]==x[j]:
                    count += 1
            if count > 1:  # Only add if duplicate found
                y.append(x[i])
                c[x[i]] = count  # Store count in dictionary
        
    print("Duplicates and counts:")    
    for char in y:
        print(f"'{char}': {c[char]} times")
            
mynew()