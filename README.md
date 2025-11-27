🎮 Sobre o Projeto

Este projeto é uma versão simplificada do famoso jogo Termo (ou Wordle), desenvolvida em Python, totalmente jogável pelo terminal.
O objetivo é adivinhar a palavra secreta em até 6 tentativas, recebendo feedback colorido sobre cada letra:

Verde → Letra correta no lugar correto

Amarelo → Letra existe na palavra, mas em outra posição

Cinza → Letra não faz parte da palavra

O projeto é ideal para entender conceitos como funções, laços, condicionais e manipulação de strings.

📌 Funcionalidades Principais
✔️ Sorteio automático da palavra secreta

O jogo escolhe aleatoriamente uma palavra da lista disponível.

✔️ Validação do chute

O jogo só aceita palavras com o mesmo número de letras da palavra secreta.

✔️ Comparação letra a letra

O programa destaca cada letra com cores ANSI, facilitando visualização.

✔️ Sistema de tentativas

O jogador tem 6 chances para acertar a palavra.

✔️ Loop de repetição

Após cada partida, o jogador pode escolher jogar novamente.

🧠 Como o jogo funciona
1. Escolha da palavra

A função sortear_palavra() utiliza random.choice() para selecionar uma palavra aleatória.

2. Entrada do usuário

O jogador informa uma palavra do mesmo tamanho que a secreta.

3. Comparação das palavras

A função comparar_palavras() analisa cada letra:

Se a letra está correta e no lugar certo, fica verde.

Se a letra existe, mas está no lugar errado, fica amarela.

Se não existe na palavra, fica cinza.

O resultado colorido aparece no terminal.

4. Vitória ou derrota

Se acertar antes das 6 tentativas → vitória 🎉

Se acabar as tentativas → o jogo revela a palavra secreta ❌

5. Jogar novamente

O jogador escolhe se deseja recomeçar.

🖥️ Como Executar
Pré-requisitos

Python 3 instalado

Passos
# 1. Baixar o arquivo
git clone https://github.com/pedrohoppe88/Jogo_do_termo

# 2. Acessar o diretório
cd jogo_do_termo

# 3. Executar o jogo
python termo.py
