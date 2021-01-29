import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou ", chute)

    if (chute < 1 or chute > 10):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Parabéns, você acertou!")
        break
    else:
        if(menor):
            print("O número informado é menor do que o número secreto.")
        elif(maior):
            print("O número informado é maior do que o número secreto.")
    print("")
print("Fim do Jogo o número secreto era: {} !!".format(numero_secreto))