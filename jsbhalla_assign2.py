import csv
with open('Demographic_Statistics_By_Zip_Code.csv', 'r') as f: 
  reader = csv.reader(f)
  your_list = list(reader)

n=input("Enter Jurisdiction Name:")
i=1
y=len(your_list)
while(i<=y):
    if (n==your_list[i][0]):
        print(your_list[i][1:])
        break
    else:
        i+=1
        continue
        
k=1
l=len(your_list)
a=0
while(k<l)
    if(your_list[i][4]=='0'):
        a+=1
        k+=1
    else:
        k+=1
        continue
print(count,"times where Count male is zero")

j=1
x=len(your_list)
b=0
while(j<x):
    if(your_list[j][2]=='0'):
        b+=1
        j+=1
    else:
        j+=1
        continue
print(count1,"times where Count female is zero")
