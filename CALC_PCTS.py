

# ==========================================
# CALCULADORA INDUSTRIAL - CONSECANA SP
# ATR / ART / ART DO CALDO / PUREZA / FIBRA
# ==========================================

def calcular_atr_art():
    fator = 0.915

    valor = float(input("Digite o valor: "))
    tipo = input("O valor informado é ATR ou ART? ").strip().upper()

    if tipo == "ATR":
        art = valor / fator
        print(f"ART = {art:.2f}")

    elif tipo == "ART":
        atr = valor * fator
        print(f"ATR = {atr:.2f}")

    else:
        print("Erro: digite apenas ATR ou ART.")


def calcular_art_caldo():
    pol_caldo = float(input("Digite o Pol do caldo: "))
    ar_caldo = float(input("Digite o AR do caldo: "))

    art = (pol_caldo / 0.95) + ar_caldo

    print(f"ART do caldo = {art:.2f}")


def calcular_pureza():
    pol = float(input("Digite o Pol do caldo: "))
    brix = float(input("Digite o Brix do caldo: "))

    if brix == 0:
        print("Erro: Brix não pode ser zero.")
        return

    pureza = (pol / brix) * 100

    print(f"Pureza = {pureza:.2f} %")


def calcular_fibra_consecana_sp():
    print("\nCálculo da Fibra % Cana - CONSECANA SP")
    print("Fórmula: Fibra % cana = [(100 x PBS) - (PBU x B)] / [5 x (100 - B)]\n")

    pbs = float(input("Digite o PBS - peso do bolo seco (g): "))
    pbu = float(input("Digite o PBU - peso do bolo úmido (g): "))
    brix = float(input("Digite o Brix do caldo (%): "))

    if brix >= 100:
        print("Erro: o Brix deve ser menor que 100.")
        return

    fibra = ((100 * pbs) - (pbu * brix)) / (5 * (100 - brix))

    print(f"Fibra % Cana = {fibra:.2f} %")


def main():
    while True:
        print("\n===== MENU DE CÁLCULOS =====")
        print("1 - Conversão ATR / ART")
        print("2 - Cálculo de ART do caldo")
        print("3 - Cálculo de Pureza (Pol / Brix)")
        print("4 - Cálculo de Fibra % Cana - CONSECANA SP")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            calcular_atr_art()

        elif opcao == "2":
            calcular_art_caldo()

        elif opcao == "3":
            calcular_pureza()

        elif opcao == "4":
            calcular_fibra_consecana_sp()

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

    ##end