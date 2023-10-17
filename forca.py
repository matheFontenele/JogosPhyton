import random

def jogar():
    
    boas_vindas()
    palavra = randoniza_palavra()
    letras_certas = inicia_chute(palavra)
    print(letras_certas)

    enforcou = False
    acertou = False
    erros = 0
    
    
    
    while not enforcou and not acertou:
        
        chute = input("Diga uma letra: ")
        chute = chute.strip().upper()
        
        if chute in palavra:
            chute_correto(chute, letras_certas, palavra)
        else:
            erros +=1
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_certas
        print(letras_certas)
        
    if acertou:
        voce_venceu()
    else:
        voce_perdeu(palavra)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def boas_vindas():
    print("****************************")
    print("********Jogo da Forca*******")
    print("****************************")
    
def randoniza_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].upper()
    return palavra

def inicia_chute(palavra):
    return ["_" for letra in palavra]

def chute_correto(chute, letras_certas, palavra):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras_certas[index] = letra
        index +=1

def voce_venceu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def voce_perdeu(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == "__main__":
    jogar()