input_str = input("Enter tuple elements (comma-separated): ")
tuple1 = tuple(map(int, input_str.split(',')))
print("Original tuple:", tuple1)

temp_list=list(tuple1)

for i in range (len(temp_list)):
    for j in range(i+1,len(temp_list)):
        if temp_list[i]>temp_list[j]:
            temp_list[i],temp_list[j]=temp_list[j],temp_list[i]
          
        
tuple2=tuple(temp_list)
print("sorted tuple",tuple2)
print(tuple2[-2])