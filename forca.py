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
            
        enforcou = erros == 6
        acertou = "_" not in letras_certas
        print(letras_certas)
        
    if acertou:
        print("Acertou boy!!")
    else:
        print("Erro, mato o buneco :(")   


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
        

if __name__ == "__main__":
    jogar()