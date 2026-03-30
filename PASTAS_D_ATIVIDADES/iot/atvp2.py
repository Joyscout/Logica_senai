# Questao 2
import os
os.system("clear || cls")

salario=float(input("Digite o seu salario: "))

if salario <=280:
    percentual=1.20
    salario_reajustado=salario*percentual
    valor_aumentado=salario_reajustado-salario
    

elif salario >280 or salario<=700:
    percentual=1.15
    salario_reajustado=salario*percentual
    valor_aumentado=salario_reajustado-salario


elif salario >700 or salario<=1500:
    percentual=1.10
    salario_reajustado=salario*percentual
    valor_aumentado=salario_reajustado-salario
   

elif salario >1500:
    percentual=1.05
    salario_reajustado=salario*percentual
    valor_aumentado=salario_reajustado-salario
  

else:
    os.system("clear || cls")
    print("Valor invalido")

os.system("clear || cls")
print("\tTabela de Dados \n")
print(f"- Salario antes do reajusto: R$ {salario:.2f} ")
print(f"- Percentual: 20%")
print(f"- Valor de aumento: R$ {valor_aumentado:.2f}")
print(f"- Novo Salario: R$ {salario_reajustado:.2f}")