def jogar():

    import random

    print("****************************")
    print("****Jogo da Adivinhação*****")
    print("****************************")


    num_secreto = round(random.randrange(101))
    total_chance = 0
    pontos = 1000

    print('Selecione a dificuldade')
    print('(1) Facil (2) Medio (3) Dificil')

    nivel = int(input('Defina o nível: '))

    if nivel == 1:
        total_chance = 19
    elif nivel == 2:
        total_chance = 9
    else:
        total_chance = 4

    for rodada in range(1, total_chance):
        print('Tentativa: {} de {}'.format(rodada, total_chance+1))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Digite apenas numeros entre 1 e 100")
            continue

        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto
        
        if acertou:
            print("Você acertou e conseguiu {}!".format(pontos))
            break
        else:
            if maior:
                print("Muito alto, o numero é menor")
            elif menor:
                print("Muito baixo, o numeor é maior")
            lost_pontos = abs(num_secreto - chute)
            pontos = pontos - lost_pontos

    print("Fim de jogo, resposta {}". format(num_secreto))

if __name__ == "__main__":
    jogar()