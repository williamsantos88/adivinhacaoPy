print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
chute = int(input("Digite o seu número: "))
print("Você digitou ", chute)

acertou = chute == numero_secreto
menor = chute < numero_secreto
maior = chute > numero_secreto

if (acertou):
    print("Parabéns, você acertou!")
else:
    if(menor):
        print("O número informado é menor do que o número secreto.")
    elif(maior):
        print("O número informado é maior do que o número secreto.")

print("Fim do Jogo!!")