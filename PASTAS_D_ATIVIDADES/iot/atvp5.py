# Questao 5
import os
os.system("clear || cls")

dias=int(input("Digite a qauntidade de dias percorrido com o carro: "))
km=float(input("\nDigite a quantidade de kilometros rodados (em km): "))

din_dias=dias*60
din_km=km*(km*0.15)
total=din_dias+din_km
os.system("clear || cls")
print("\tDados De Peixe\n")
print(f"- Dias percorrido: {dias} ")
print(f"- Kilometros percorrido: {km:.2f} km")
print(f"- Quanto deve pagar: R$ {total:.2f} ")
