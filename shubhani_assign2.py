import csv
with open('Demographic_Statistics_By_Zip_Code.csv', 'r') as f: #put the filename as  the first paramter
  reader = csv.reader(f)
  your_list = list(reader)
#print(your_list)

y=input("enter jurisdiction name:")
for i in range(len(your_list)):
    if y==your_list[i][0]:
        print(your_list[i][0:])



print("number of jurisdiction where count male is zero")
count=0
for i in range(len(your_list)):
    if(your_list[i][4]=='0'):
        count=count+1
print(count)


print("number of jurisdiction where count male is zero")
flag=0
for i in range(len(your_list)):
    if(your_list[i][2]=='0'):
        flag=flag+1
print(flag)

#print("remove allyour_list[0][j] columns except jurisdiction name,count male and count female")
#for j in range (0,46):
#    if((your_list[0][j]!='JURISDICTION') and (your_list[0][j]!='COUNT MALE') and (your_list[0][j]!='COUNT FEMALE')):
#        your_list[0].pop(j)
#print(your_list[0][0:])
