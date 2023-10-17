import random

def jogar():
    
    boas_vindas()

    randoniza_palavra()
    
    letras_certas = ["_" for letra in palavra]
    
    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_certas)
    
    while not enforcou and not acertou:
        
        chute = input("Diga uma letra: ")
        chute = chute.strip().upper()
        
        if chute in palavra:
            index = 0
            for letra in palavra:
                if chute == letra:
                    letras_certas[index] = letra
                index +=1
        else:
            erros +=1
            
        enforcou = erros == 6
        acertou = "_" not in letras_certas
        print(letras_certas)
        
    if acertou:
        print("Acertou boy!!")
    else:
        print("Erro, mato o buneco :(")
    print("Fim de jogo")    
if __name__ == "__main__":
    jogar()
    
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