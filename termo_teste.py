import random

VERDE = '\033[92m'
AMARELO = '\033[93m'
CINZA = '\033[90m'
RESET = '\033[0m'


def comparar_palavras(chute, palavra_secreta):
    resultado = ""
    
    for i in range(len(palavra_secreta)):
        if chute[i] == palavra_secreta[i]:
            resultado += VERDE + chute[i] + RESET
        elif chute[i] in palavra_secreta:
            resultado += AMARELO + chute[i] + RESET
        else:
            resultado += CINZA + chute[i] + RESET

    return resultado


def gerar_palavra():
    return random.choice(['canto', 'verde', 'lapis', 'plano', 'bravo'])


def play():
    palavra_secreta = gerar_palavra()
    tamanho = len(palavra_secreta)
    
    print("\n=== JOGO TERMO ===")
    print(f"Adivinhe a palavra com {tamanho} letras!")
    print("Você tem 6 tentativas.\n")
    
    max_tentativas = 6
    
    for tentativa in range(1, max_tentativas + 1):

        chute = input(f"Tentativa {tentativa}/{max_tentativas}: ").lower()
        
        if len(chute) != tamanho:
            print(f"Palavra deve ter {tamanho} letras. Tente novamente.\n")
            continue
        
        resultado = comparar_palavras(chute, palavra_secreta)
        print("Resultado:", resultado, "\n")
        
        if chute == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra!")
            break
        
    else:
        print(f"Fim de jogo! A palavra era: {palavra_secreta}")


# LOOP DO JOGO
while True:
    play()

    print("\nDeseja jogar novamente?")
    opcao = input("Digite S para SIM ou N para NÃO: ").lower()

    if opcao != "s":
        print("\nObrigado por jogar! Até a próxima!")
        break
