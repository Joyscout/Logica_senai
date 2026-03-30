@dataclass
class Carro1:
   marca: str
   ano: int
   placa: str
   dtaquisicao: str
   
@dataclass
class Carro2:
   marca: str
   ano: int
   placa: str
   dtaquisicao: str
   
print("===CARRO 1===\n")
Carro_1 = Carro1(
    marca=str(input("Digite a marca do 1º carrao: ")),
    ano=int(input("Digite o ano do 1º carrao: ")),
    placa=str(input("Digite a placa do 1º carrao: ")),
    dtaquisicao=str(input("Digite a data que tu adiquiriu seu carro: "))
    )
print("\n===CARRO 2===\n")

Carro_2 = Carro2(
    marca=str(input("Digite a marca do 2º carrao: ")),
    ano=int(input("Digite o ano de criação do 2º carrao: ")),
    placa=str(input("Digite a placa do 2º carrao: ")),
    dtaquisicao=str(input("Digite a data que tu adiquiriu seu carro: "))
    )
print("\n=== DADOS DO CARRO 1===\n")
print("carro 1\n")
print(f"Marca: {Carro_1.marca}, Ano: {Carro_1.ano}, Placa: {Carro_1.placa}, Data de aquisição: {Carro_1.dtaquisicao}")
print("\n=== DADOS DO CARRO 2===\n")
print("carro 1\n")
print(f"Marca: {Carro_2.marca}, Ano: {Carro_2.ano}, Placa: {Carro_2.placa}, Data de aquisição: {Carro_2.dtaquisicao}")
