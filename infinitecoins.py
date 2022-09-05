from itertools import count


def makeChange(valor):
    """
    A função makeChange itera sobre o valor das moedas e retorna a lista de todas as possibilidades
    de representar o valor inserido usando as moedas de 25, 10, 5 e 1 centavo.
    """
    resultados = []
    soma = 0
    for q in count(0):
        for d in count(0):
            for n in count(0):
                soma = n * 5 + d * 10 + q * 25
                if soma < valor:
                    combinacao = [q, d, n, valor - soma]
                    resultados.append(combinacao)

                if n * 5 + d * 10 + q * 25 > valor:
                    break
            if d * 10 + q * 25 > valor:
                break
        if q * 25 > valor:
            break

    return resultados


if __name__ == "__main__":
    valor = int(input("Digite um valor: "))  # Recebe o valor que será decomposto em moedas
    print(makeChange(valor))  # Imprime todas as combinações, que formam o valor recebido, através das moedas.
