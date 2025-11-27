import random

# CORES ANSI
VERDE = '\033[92m'
AMARELO = '\033[93m'
CINZA = '\033[90m'
RESET = '\033[0m'

# LISTA DE PALAVRAS
palavras = ["canto", "verde", "lapis", "plano", "bravo"]

# FUNÇÃO: SORTEAR PALAVRA
def sortear_palavra():
    return random.choice(palavras)

# FUNÇÃO: MOSTRAR RESULTADO COLORIDO

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

# FUNÇÃO PRINCIPAL DO JOGO

def jogar():
    palavra_secreta = sortear_palavra()
    tamanho = len(palavra_secreta)

    print("\n=== JOGO TERMO ===")
    print(f"Adivinhe a palavra com {tamanho} letras!")
    print("Você tem 6 tentativas.\n")

    tentativas = 6

    for tentativa in range(1, tentativas + 1):

        chute = input(f"Tentativa {tentativa}/{tentativas}: ").lower()

        # validação do tamanho
        if len(chute) != tamanho:
            print(f"A palavra deve ter {tamanho} letras!\n")
            continue

        resultado = comparar_palavras(chute, palavra_secreta)
        print(resultado + "\n")

        if chute == palavra_secreta:
            print("🎉 PARABÉNS! Você acertou a palavra!")
            return  # encerra a função

    # se não acertou
    print(f"❌ Você perdeu! A palavra era: {palavra_secreta}")

# LOOP PARA JOGAR VÁRIAS VEZES
while True:
    jogar()

    print("\nDeseja jogar novamente?")
    opcao = input("Digite S para SIM ou N para NÃO: ").lower()

    if opcao != "s":
        print("\nObrigado por jogar! Até a próxima!")
        break
