# Questao 6
import os
os.system("clear || cls")

list1=[1,3,6,9,12,15,18]
list2=[1,2,4,6,8,12,18]
list3=[]

for num in list1:
    if num not in list3:
        list3.append(num)

for num in list2:
    if num not in list3:
        list3.append(num)

print(f"- Lista 1: ",list1)
print(f"- Lista 2: ",list2)
list3.sort()
print(f"- Lista 3: ",list3)