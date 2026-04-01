

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

    #END




## cálculo de ART a partir de Pol do caldo e AR

# entrada de dados
pol_caldo = float(input("Digite o Pol do caldo: "))
ar_caldo = float(input("Digite o AR do caldo: "))

# cálculo
ART = (pol_caldo / 0.95) + ar_caldo

# saída
print(f"ART = {ART:.2f}")

#END



