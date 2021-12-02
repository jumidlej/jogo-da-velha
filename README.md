# Jogo da Velha

Essa aplicação possui um programa cliente e um programa servidor. O programa servidor irá se comunicar e jogar contra o programa cliente de forma automática. O programa servidor irá ganhar sempre que lhe for possível, se não for, tentará impedir o programa cliente de ganhar, e caso não seja possível, realizará uma jogada aleatória.

## O Funcionamento do Jogo

O jogo será gerido pelo programa servidor. Antes de cada partida, será perguntado se o programa cliente deseja começar a jogar. No final de cada partida, será perguntado se o programa cliente deseja jogar novamente.

O tabuleiro do jogo será uma lista com posições vazias que será preenchido a cada jogada.

A cada jogada, haverá uma verificação para saber se algum programa venceu a partida ou se deu 'velha'. 

O programa servidor irá jogar de forma aleatória se, na rodada atual, não houver possibilidade de vencer o jogo ou de impedir o programa cliente de vencer. Para isso, o programa irá verificar todos os locais do tabuleiro.

## O Protocolo da Aplicação

## Requisitos para o Funcionamento

* Python 3.8
* NumPy 1.20

## Comandos para rodar os programas

* python3 server.py
* python3 client.py
