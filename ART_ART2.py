

## cálculo de ATR / ART

# entrada de dados
valor = float(input("Digite o valor: "))
tipo = input("O valor informado é ATR ou ART? ").upper()

# cálculo
if tipo == "ATR":
    ART = valor / 0.915
    print(f"ART = {ART:.2f}")

elif tipo == "ART":
    ATR = valor * 0.915
    print(f"ATR = {ATR:.2f}")

else:
    print("Tipo inválido. Digite ATR ou ART.")


    