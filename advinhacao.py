print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
chute = input("Digite o seu número: ")
print("Você digitou ", chute)

if numero_secreto == int(chute):
    print("Parabéns, você acertou!")
else:
    print("Você errou...")

print("Fim do Jogo!!")