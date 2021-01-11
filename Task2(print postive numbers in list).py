#Printing the positive numbers in a list
lists=list(map(int,input().split(",")))
list1=[]
for i in lists:
    if i > 0:
        list1.append(i)
print(list1)
        
    
