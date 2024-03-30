import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    palpite = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while palpite != numero_secreto:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número maior!")
        elif palpite > numero_secreto:
            print("Tente um número menor!")

    print("Parabéns! Você adivinhou o número em", tentativas, "tentativas.")

jogo_adivinhacao()
