import csv
from operator import itemgetter

vencedores = []

with open("winners.csv", encoding="utf-8") as arq:
    linhas = csv.DictReader(arq)
    for linha in linhas:
        vencedores.append(linha)


def titulo(texto):
    print()
    print(texto)
    print("="*40)


def top10_pilotos():
    titulo("Top 10 Pilotos com Maior Número de Vitórias")
    pilotos = list(set([x['Winner'] for x in vencedores]))
    vitorias = [0] * len(pilotos)
 
    for vencedor in vencedores:
        indice = pilotos.index(vencedor['Winner'])
        vitorias[indice] += 1

    juntos = sorted(zip(vitorias, pilotos), reverse=True)
    vitorias2, pilotos2 = zip(*juntos)

    print("Nº Nome do Piloto........... Vitórias")
    print("-------------------------------------")

    for num, (vitoria, piloto) in enumerate(zip(vitorias2, pilotos2), start=1):
        print(f"{num:2d} {piloto:25s} {vitoria:5d}")
        if num == 10:
            break


def compara_equipes():
    titulo("Compara 2 Equipes")

    equipe1 = input("1ª Equipe: ")
    equipe2 = input("2ª Equipe: ")
    conta1 = 0
    conta2 = 0

    for vencedor in vencedores:
        if equipe1 in vencedor['Car']:
            conta1 += 1
        elif equipe2 in vencedor['Car']:
            conta2 += 1

    print("-"*40)
    print(f"{equipe1} - {conta1} vitórias")
    print(f"{equipe2} - {conta2} vitórias")


def top5_vitorias():
    titulo("Vencedores com menor tempo")

    vencedores3 = []
    for vencedor in vencedores:
        if len(vencedor['Time']) > 1 and len(vencedor['Time']) < 11:
            vencedor['Time'] = "0:" + vencedor["Time"]
        vencedores3.append(vencedor)

    vencedores2 = sorted(vencedores3, key=itemgetter("Time"))

    print("Nº Nome do Piloto........... Tempo...... Grande Prêmio.. Data......")
    num = 0
    for vencedor in vencedores2:
        if vencedor['Time'] == "":
            continue
        num = num + 1
        print(
            f"{num:2d} {vencedor['Winner']:25s} {vencedor['Time']} {vencedor['Grand Prix']:15s} {vencedor['Date']}")
        if num == 5:
            break


def pesquisa_piloto():
    titulo("Pesquisa por Piloto")

    piloto = input("Nome do Piloto:").upper()

    print("Grande Prêmio....... Data...... Equipe.............")

    for vencedor in vencedores:
        if piloto in vencedor['Winner'].upper():
            print(f"{vencedor['Grand Prix']:20s} {vencedor['Date']} {vencedor['Car']}")


def novos_vencedores():
    titulo("Novos Vencedores dos Últimos Anos")

    venc_ate_2021 = set([x['Winner'] for x in vencedores if x['Date'] <= '2021'])
    venc_2022 = set([x['Winner'] for x in vencedores if '2022' in x['Date']])
    venc_2023 = set([x['Winner'] for x in vencedores if '2023' in x['Date']])
    venc_2024 = set([x['Winner'] for x in vencedores if '2024' in x['Date']])

    print(f"Novos Vencedores de 2022: {', '.join(venc_2022.difference(venc_ate_2021))}")
    print(f"Novos Vencedores de 2023: {', '.join(venc_2023.difference(venc_ate_2021))}")
    print(f"Novos Vencedores de 2024: {', '.join(venc_2024.difference(venc_ate_2021))}")

# ------------------------------------------------------ Programa Principal
while True:
    titulo("Fórmula 1: Vencedores de Corridas")
    print("1. Top 10 pilotos com maior número de vitórias")
    print("2. Compara Equipes")
    print("3. Top 5 vitórias com menor tempo")
    print("4. Pesquisa por Piloto")
    print("5. Novos vencedores dos últimos anos")
    print("6. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top10_pilotos()
    elif opcao == 2:
        compara_equipes()
    elif opcao == 3:
        top5_vitorias()
    elif opcao == 4:
        pesquisa_piloto()
    elif opcao == 5:
        novos_vencedores()
    else:
        break
