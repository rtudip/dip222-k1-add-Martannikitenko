import pandas
import sys

reg_name=''

region=[]
with open("data.txt","r") as f:
    for line in f:
        row=line.rstrip().split(",")
        region.append(row)
#1970
info_list = region
#minvalue = 999999999
#for x in range(len(info_list)):
#    if int(x) > 0:
#        #print(x)
#        i=info_list[x][6]
#        try:
#            if int(i) < minvalue:
#                minvalue = int(i)
#        except ValueError:
#              flag = False
#Latvia = 253
#telco = 2
#https: 135
#org 35

value = 0
for x in range(len(info_list)):
    if info_list[x][4] == "Latvia" and ".org" in info_list[x][3]:
        #print(info_list[x][7])
        value = value +1
print(value)