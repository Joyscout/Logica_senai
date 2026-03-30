# Questao 4
import os
os.system('cls || clear')

n1=int(input("digite o numero: "))
n2=int(input("\ndigite o numero: "))
print()
maior=max(n1,n2)
menor=min(n1,n2)
for i in range(menor, maior+1):
    print(i,end='-')

