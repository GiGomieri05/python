import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0
    
    while(not enforcou and not acertou):
        
        chute = pede_chute()
        
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)
    
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)




def imprime_mensagem_abertura():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
def carrega_palavra_secreta():
    arquivo = open("/Users/giova/OneDrive/Área de Trabalho/FACENS/python/jogos/lista_de_palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ").strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")# type: ignore
    print("   /               \       ")# type: ignore
    print("  /                 \      ")# type: ignore
    print("//                   \/\  ") # type: ignore
    print("\|   XXXX     XXXX   | /   ")# type: ignore
    print(" |   XXXX     XXXX   |/     ")# type: ignore
    print(" |   XXX       XXX   |      ")# type: ignore
    print(" |                   |      ")# type: ignore
    print(" \__      XXX      __/     ")# type: ignore
    print("   |\     XXX     /|       ")# type: ignore
    print("   | |           | |        ")# type: ignore
    print("   | I I I I I I I |        ")# type: ignore
    print("   |  I I I I I I  |        ")# type: ignore
    print("   \_             _/       ")# type: ignore
    print("     \_         _/         ")# type: ignore
    print("       \_______/           ")# type: ignore
    
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
        print(" |      \     ")# type: ignore
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")# type: ignore
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")# type: ignore
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")# type: ignore
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")# type: ignore
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")# type: ignore
        print(" |       |    ")
        print(" |      / \   ")# type: ignore

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()