#Printing the frequency of characters in a string in descending order

def Frequency_descending(string):
    dict1={}
    for i in string:
        dict1[i]=dict1.get(i,0) + 1
    dict1_sorted=sorted(dict1,key=dict1.get,reverse=True)
    for j in dict1_sorted:
        if(dict1[j]<10):
            print("%c = 0%d" %(j,dict1[j]))
        else:
            print(j,"=",dict1[j])

string=input()
string=string.lower()
Frequency_descending(string)
