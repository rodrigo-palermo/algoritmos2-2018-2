"""Exercicio aula 2."""

num1 = 45
num2 = 50
num3 = 14


def media(num1, num2):
    """Calcula a média entre 2 números."""
    return (num1 + num2)/2


media = media(num1, num2)


def maiorDe3(num1, num2, num3):
    """Calcula o maior valor entre 3 números."""
    maior = num1
    if num2 > maior:
        maior = num2
    elif num3 > maior:
        maior = num3
    return maior


print("A média entre %.2f e %.2f é %.2f" % (num1, num2, media))
print("Entre %.2f, %.2f e %.2f, o maior é: %.2f" % (num1, num2, num3,
      maiorDe3(num1, num2, num3)))
