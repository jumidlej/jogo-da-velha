import socket
import sys
from game import GameState

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('', 12000)
print('Conectando ao servidor {} na porta {}'.format(server_address[0], server_address[1]))
sock.connect(server_address)

# Cria um tabuleiro de jogo vazio
board = GameState()

try:
    # Recebe a pergunta do servidor
    data = sock.recv(1024)
    answer = input(data.decode())

    # Envia resposta para o servidor
    sock.send(answer.encode('utf-8'))

    while True:
        # Recebe a jogada do servidor
        data = sock.recv(1024)
        if data.decode('utf-8') != "Game over! Deseja jogar novamente? (S/N) ":
            board.restore(data.decode('utf-8'))

            # Mostra a jogada do servidor
            print('O servidor jogou:')
            board.print()

            # Verifica se o servidor venceu o jogo
            if board.checkGameVictory() or board.checkGameEnd():
                sock.sendall(board.save().encode('utf-8'))
            else:
                print('Faça a sua jogada:')
                print('------------------')

                nok = True
                while nok:
                    row = input('Digite a linha [1,3]: ')
                    while row not in ['1', '2', '3']:
                        print('Valor inválido. Tente novamente!')
                        row = input('Digite a linha [1,3]: ')

                    col = input('Digite a coluna [1,3]: ')
                    while col not in ['1', '2', '3']:
                        print('Valor inválido. Tente novamente!')
                        col = input('Digite a coluna [1,3]: ')

                    nok = False
                    try:
                        board.move(int(row)-1, int(col)-1, 'x')
                    except:
                        nok = True
                        print('Linha ou coluna inválida. Tente novamente.')

                board.print()
                # Envia o tabuleiro para o servidor
                sock.sendall(board.save().encode('utf-8'))
        else:
            # Responde se deseja jogar novamente
            answer = input(data.decode())
            if answer != 'S':
                break

            # Envia resposta para o servidor
            sock.send(answer.encode('utf-8'))

            data = sock.recv(1024)

            # Responde se deseja iniciar o jogo
            answer = input(data.decode())

            # Envia resposta para o servidor
            sock.send(answer.encode('utf-8'))

finally:
    print('Encerrando o cliente')
    sock.close()