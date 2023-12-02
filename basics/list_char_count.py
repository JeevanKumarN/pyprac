string=input("enter the comma separated integers : ")

l1=string.split(",")
count=0
for x in l1:
    if (x=="4"):
        count+=1
print(count)