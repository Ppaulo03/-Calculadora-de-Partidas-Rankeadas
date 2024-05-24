def get_saldo(vitorias: int, derrotas:int) -> int:
    return vitorias - derrotas

def get_level(vitorias: int) -> str:
    if vitorias < 10: return "Ferro"
    elif vitorias <= 20: return "Bronze"
    elif vitorias <= 50: return "Prata"
    elif vitorias <= 80: return "Ouro"
    elif vitorias <= 90: return "Diamante"
    elif vitorias <= 100: return "Lendário"
    else: return "Imortal"

while True:
    vitorias = input("Digite a quantidade de vitórias: ")
    if not vitorias.isdigit():
        print("Digite um número inteiro positivo para as vitórias", end="\n\n")
        continue
    derrotas = input("Digite a quantidade de derrotas: ")
    if not derrotas.isdigit():
        print("Digite um número inteiro positivo para as derrotas", end="\n\n")
        continue

    vitorias = int(vitorias)
    derrotas = int(derrotas)

    saldo = get_saldo(vitorias, derrotas)
    nivel = get_level(saldo)

    print(f"O Herói tem de saldo de **{saldo}** está no nível de **{nivel}**", end="\n\n")