# 1. Jogo da Velha
Este projeto foi desenvolvido em Python como atividade avaliativa da matéria de Redes de Computadores I, ministrada pelo professor Jorge Lima na Universidade Estadual de Santa Cruz.
O projeto consiste em uma aplicação que possui um programa cliente e um programa servidor. O programa servidor irá se comunicar e jogar o jogo da velha contra o programa cliente de forma automática. O protocolo de transporte utilizado para comunicação foi o TCP pois garante a entrega de todos os dados que estão sendo enviados, logo, ao fazer uma jogada é garantido que a resposta a essa escolha esteja disponível para ambos jogadores.

## 2. O Funcionamento do Jogo: Cliente e Servidor 

O jogo será gerido pelo programa servidor. Antes de cada partida, será perguntado ao programa cliente se ele deseja começar a partida. No final de cada partida, será perguntado ao programa cliente se ele deseja jogar novamente.

## 2.1 GameState 

A implementação do jogo foi feita a partir da Classe GameState, que guarda o estado do tabuleiro do jogo. O tabuleiro do jogo será inicializado como uma lista com posições vazias e será preenchido a cada jogada do servidor ou do cliente. Existem funções auxiliares para executar as jogadas, verificar se alguém venceu o jogo e limpar o tabuleiro quando necessário.

A cada jogada, haverá uma verificação para saber se algum programa, cliente ou servidor, venceu a partida ou se deu 'velha'. 

O programa servidor só irá jogar de forma aleatória se, na rodada atual, não houver possibilidade de vencer o jogo ou de impedir o programa cliente de vencer. Para isso, o programa irá verificar todos os locais do tabuleiro.

## Lista de funções utilizadas:

## 2.1.1 __init__  
Construtor. Inicializa o tabuleiro 3x3 vazio.

## 2.1.2 save
Salva os dados do tabuleiro para uma string.

## 2.1.3 restore
Restaura os dados do tabuleiro a partir de uma string.

## 2.1.4 move
Faz uma jogada no tabuleiro, nas posições dadas.

## 2.1.5 serverMove
Faz uma jogada no tabuleiro, em uma das posições vazias.

## 2.1.6 checkGameVictory
Verifica se o jogo foi vencido por alguma das peças.

## 2.1.7 checkGameEnd
Verifica se ainda existem locais vazios no tabuleiro.

## 3. O Protocolo da Aplicação

Assim que o programa cliente se conecta com o programa servidor, o programa servidor pergunta se o cliente deseja ser o primeiro a efetuar uma jogada. A partir disso, o servidor envia o tabuleiro vazio ou com a primeira jogada efetuada. Então, sempre que o programa cliente receber uma nova jogada do servidor, ele verificará se é um tabuleiro ou uma pergunta que indica o fim do jogo (Deseja jogar novamente?). Se for um tabuleiro, o cliente verificará se a jogada efetuada pelo servidor venceu o jogo, caso o servidor tenha vencido, o cliente reenviará o tabuleiro recebido pelo servidor. Se o servidor não venceu, o cliente enviará o tabuleiro com uma nova jogada efetuada por ele. Se o cliente tiver recebido a pergunta: Deseja jogar novamente?, ele responderá com 'S' ou 'N'.

Sempre que o servidor receber uma jogada do cliente, ele verificará se o jogo acabou, se tiver acabado, ele enviará a pergunta: Deseja jogar novamente?. Se o jogo não acabou, o servidor irá efetuar uma jogada e enviar para o cliente.

<img src="/protocolo.drawio.png" alt="Protocolo da aplicação"/>

Para essa aplicação, o protocolo escolhido foi o TCP, pois é mais confiável e, para o bom funcionamento do jogo, dados não podem ser perdidos.

## 4. Requisitos para o Funcionamento

* Sistema operacional Linux
* Python 3.8
* NumPy 1.20

## 5. Comandos para Executar os Programas

* python3 server.py
* python3 client.py

## 6. Screenshots

Abaixo estão algumas Screenshots  de interface do jogo e mensagens que podem ser apresentadas.
Nas imgens abaixo os dois jogadores já se conectaram e fizeram sua primeira jogada:
