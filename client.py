import socket
import sys
from game import GameState

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('', 5000)
print('Conectando ao servidor {} na porta {}'.format(server_address[0], server_address[1]))
sock.connect(server_address)

# Cria um tabuleiro de jogo vazio
board = GameState()

try:
    while True:
        # Variável que verifica o fim do jogo
        gameOver = False

        # Recebe a jogada do servidor
        data = sock.recv(1024)
        board.restore(data.decode('utf-8'))

        # Mostra a jogada do servidor
        print('O servidor jogou:')
        board.print()

        # Verifica se o servidor venceu o jogo
        if board.checkGameVictory():
            print('O servidor venceu.')
            gameOver = True
        elif board.checkGameEnd():
            print('Velha!')
            gameOver = True

        # Se o servidor venceu o jogo, pergunta se deseja jogar novamente
        if gameOver:
            restart = input('Deseja jogar novamente? (S/N) ')
            # Se sim, limpa o jogo
            if restart == 'S':
                board.cleanBoard()
                gameOver = False
            # Se não, encerra a conexão
            else:
                break

        else:
            print('Faça a sua jogada:')
            print('------------------')

            nok = True
            while nok:
                row = int(input('Digite a linha: '))
                col = int(input('Digite a coluna: '))

                nok = False
                try:
                    board.move(row, col, 'x')
                except:
                    nok = True
                    print('Linha ou coluna inválida. Tente novamente.')
                
            # Verifica se o jogador venceu o jogo
            if board.checkGameVictory():
                board.print()
                print('O jogador venceu.')
                gameOver = True
            elif board.checkGameEnd():
                board.print()
                print('Velha!')
                gameOver = True

            if gameOver:
                restart = input('Deseja jogar novamente? (S/N) ')
                if restart == 'S':
                    board.cleanBoard()
                    gameOver = False
                else:
                    break

        # Envia o tabuleiro para o servidor
        sock.sendall(board.save().encode('utf-8'))

finally:
    print('Encerrando o cliente')
    sock.close()