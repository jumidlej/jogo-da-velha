import socket
from game import GameState
import time

# Cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind no endereco e porta
server_address = ('', 12000)
sock.bind(server_address)

# Fica ouvindo por conexoes
sock.listen(1)

while True:
    print('Aguardando a conexao do jogador')
    connection, client_address = sock.accept()

    try:
        print('Jogador chegou!')

        # Cria um tabuleiro de jogo vazio
        board = GameState()

        play_again = True
        while play_again:
            # Limpa o tabuleiro
            board.cleanBoard()

            # Pergunta se o jogador deseja iniciar o jogo
            connection.send("Deseja iniciar o jogo? (S/n) ".encode('utf-8'))
            data = connection.recv(1024)
            
            # Se sim, faz uma jogada, se não, envia o tabuleiro vazio
            if data.decode() not in ['S', 's']:
                # Faz uma jogada aleatoria
                board.serverMove('o')
            
            # Envia o tabuleiro para o jogador
            connection.sendall(board.save().encode('utf-8'))

            # Processa em loop
            while True:
                # Recebe a jogada do jogador
                data = connection.recv(1024)
                time.sleep(0.5)

                # Checa se a conexao do jogador foi terminada
                if not data:
                    print('Jogador se foi. :(')
                    break

                # Converte para string e restaura no tabuleiro
                board.restore(data.decode('utf-8'))

                # Verifica fim de jogo
                if board.checkGameVictory() or board.checkGameEnd():
                    connection.send("Game over! Deseja jogar novamente? (S/n) ".encode('utf-8'))
                    data = connection.recv(1024)
                    
                    if data.decode() not in ['S', 's']:
                        play_again = False
                    
                    break
                        
                # Faz outra jogada 
                board.serverMove('o')

                # Envia o tabuleiro para o jogador
                connection.sendall(board.save().encode('utf-8'))

    finally:
        # Clean up the connection
        connection.close()