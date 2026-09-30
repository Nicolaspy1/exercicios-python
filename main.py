notas = []     # criei uma lista para ser a "memória" do código 

def calcular_notas(notas): # essa função vai pegar as notas, adicionar em forma de valores na lista e vai calcular a média devolvendo o resultado 
    while True:
        print("=="*30)

        pergunta = float(input("Digite o valor da nota: "))
        notas.append(pergunta)
        if len(notas) < 4:                   # condição que vai ler a lista, se ela tiver menos de 4 valores, o while roda mais uma vez, tiver mais ou 4, ele para 
            print("Próxima nota")
        else:
            break 
  
    media = sum(notas) / len(notas)
    return media                            # quando eu quero atribuir essa função à outra, preciso que o código entenda alguma resposta dessa função, o return serviu pra isso

def verificação (media):                    # função que pega a média passa logo acima e verifica em qual print se encaixa
    if media >= 7:
        print(f"Aprovado com média {media}")
    elif media > 5 and media < 6.9:
        print(f"Em Recuperação com média {media}")
    else:
        print(f"Reprovado com média {media}")


verificação(calcular_notas(notas))   # puxei a função e usei de parâmetro a função acima que usa a lista para basear seu return