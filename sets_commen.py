def mynew():
    # Input for set1
    input1 = input("Enter elements for set1 (comma separated): ")
    set1 = set(input1.split(","))
    
    # Input for set2  
    input2 = input("Enter elements for set2 (comma separated): ")
    set2 = set(input2.split(","))
    
    print("Set 1:", set1)
    print("Set 2:", set2)
    
    set3 = set1.intersection(set2)
    print("Intersection:", set3)
            
mynew()