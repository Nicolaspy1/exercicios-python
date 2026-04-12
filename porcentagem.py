
compras = float(input("Digite o valor bruto: "))
try:
    if compras > 500:
        quinze_porcento = compras - (compras * 15) / 100
        desconto = compras - quinze_porcento
        print(f"valor do desconto: {desconto:.2f}, total a pagar: {quinze_porcento:.2f}")

    elif compras > 200 and compras < 500:
        dez_porcento = compras - (compras * 10) / 100
        desconto = compras - dez_porcento
        print(f"valor do desconto: {desconto:.2f}, total a pagar: {dez_porcento:.2f}")

    elif compras < 200:
        compras + 0
        print(f"valor do desconto: 0,00 , total a pagar: {compras:.2f}")

    else:
        print(f"Erro")
except ValueError:
    print("Digite somente números")

