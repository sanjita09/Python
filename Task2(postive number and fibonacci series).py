#Printing the positive numbers in a list
lists=list(map(int,input().split(",")))
list1=[]
for i in lists:
    if i > 0:
        list1.append(i)
print(list1)

#printing the fibonacci numbers
num=int(input("Enter the count of the numbers to be printed in the fibonacci sequence(Enter a value greater than 0)"))
i=-1
j=1
count=0
while count<=num:
    k=i+j
    print(k,end=",")
    i=j
    j=k
    count=count+1
    

        
    
