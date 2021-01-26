#School Administration

import csv

def School_Administration(list1):
    with open("info.csv","a",newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(['NAME','AGE','CONTACT-NO.','EMAIL-ID'])
        writer.writerow(list1) 

if __name__ == '__main__':
    temp=True
    student=1
    while(temp):
        list1=list(input("Enter the student #{} details in the format(Name Age ContactNo. Email-Id):".format(student)).split())
        for i in list1:
            print(i)
        check=input("Verify the above details.Confirm with yes/no")
        check.lower()
        if check=='yes':
            School_Administration(list1)
            temp1=input("Do you want to continue (yes/no)")
            temp1.lower()
            if temp1=='no':
                temp=False
        else:
            continue
