import csv
with open('Demographic_Statistics_By_Zip_Code.csv', 'r') as f: #put the filename as as the first paramter
  reader = csv.reader(f)
  your_list = list(reader)

#As the user types a Jurisdiction Name all the attributes should show

n=input("Enter Jurisdiction Name:")
i=1
y=len(your_list)
while(i<=y):
    if (n==your_list[i][0]):
        print(your_list[i][1:])
        break
    else:
        i=i+1
        continue



#Remove all the columns except Jurisdiction Name,count female,count male



# Count how many Jurisdiction are there where Count male is zero #hint access it by your_list[1][4]

i=1
y=len(your_list)
count=0
while(i<y):
    if(your_list[i][4]=='0'):
        count=count+1
        i=i+1
    else:
        i=i+1
        continue
print(count,"times where Count male is zero")


#Count how many Jurisdiction are there where Count female is zero #hint access it by your_list[1][2]

j=1
x=len(your_list)
count1=0
while(j<x):
    if(your_list[j][2]=='0'):
        count1=count1+1
        j=j+1
    else:
        j=j+1
        continue
print(count1,"times where Count female is zero")
