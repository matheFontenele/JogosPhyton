def jogar():
    print("****************************")
    print("********Jogo da Forca*******")
    print("****************************")

    palavra = "banana"
    
    letras_certas = ["_", "_", "_", "_", "_", "_"]
    
    enforcou = False
    acertou = False
    
    while not enforcou and not acertou:
        
        chute = input("Diga uma letra: ")
        chute = chute.strip()
        
        index = 0
        for letra in palavra:
            if chute.upper() == letra.upper():
                letras_certas[index] = letra.upper()
                print(letras_certas)
            index = index+1
        print("jogando...")

    print("Fim de jogo")    
if __name__ == "__main__":
    jogar()