# Questao 1
import os
os.system("clear || cls")

peso=float(input("Digite o peso dos peixes em kg: "))

if peso >50:
    execesso=peso-50
    multa=(peso-50)*4

else:
    execesso=0
    multa=0
os.system("clear || cls")
print("\tDados De Peixe\n")
print(f"- Quilos de peixe {peso:.2f} Kg")
print(f"- Multa: R$ {multa:.2f}")
print(f"- Quanto excedeu {execesso:.0f} Kg")
