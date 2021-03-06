import numpy as np
from random import *

class GameState:
    """
    Classe que representa o estado do jogo da velha.
    """

    # -------------------------------------------------
    def __init__(self):
        """
        Construtor. Inicializa o tabuleiro 3x3 vazio.
        """
        self.board = [[''] * 3 for n in range(3)]

    # -------------------------------------------------
    def save(self):
        """
        Salva os dados do tabuleiro para uma string.

        Gera uma string com as peças do tabuleiro separadas por
        ponto-e-vírgula (';'), de forma que o estado do jogo possa
        ser comunicado via socket.

        Retorno
        ----------
        data: str
            String de texto com os dados do tabuleiro separados por
            ponto-e-vírgula (';'), prontos para serem comunicados.     
        """
        return ';'.join([';'.join(x) for x in self.board])

    # -------------------------------------------------
    def restore(self, data):
        """
        Restaura os dados do tabuleiro a partir de uma string.

        Lê uma string com as peças do tabuleiro separadas por
        ponto-e-vírgula (';'), de forma que o estado do jogo possa ser
        comunicado via socket.

        Parâmetros
        ----------
        data: str
            String de texto com os dados do tabuleiro separados por um
            ponto-e-vírgula (';'), prontos para serem atualizados neste
            objeto.
        """
        self.board = np.reshape(data.split(';'), (3,3)).tolist()

    # -------------------------------------------------
    def print(self):
        """
        Imprime o tabuleiro em um formato visual.
        """
        print("+---+---+---+")
        for row in self.board:
            print('|{}|{}|{}|'.format(row[0].center(3, ' '), row[1].center(3, ' '), row[2].center(3, ' ')))
            print("+---+---+---+")

    # -------------------------------------------------
    def move(self, row, col, piece):
        """
        Faz uma jogada no tabuleiro, nas posições dadas.

        Parâmetros
        ----------
        row: int
            Número da linha no tabuleiro, no intervalo [0,2].
        col: int
            Número da coluna no tabuleiro, no intervalo [0,2].
        piece: str
            Letra com o símbolo jogado, entre as opções 'o' e 'x'.        
        """

        # Valida os parâmetros de entrada
        if row < 0 or row > 2:
            raise RuntimeError('Número de linha inválido: {}'.format(row))
        if col < 0 or col > 2:
            raise RuntimeError('Número de coluna inválido: {}'.format(col))
        piece = piece.lower()
        if piece != 'x' and piece != 'o':
            raise RuntimeError('Peça inválida: {}'.format(piece))

        # Verifica se a posição jogada está vazia
        if self.board[row][col] != '':
            raise RuntimeError('Posição do tabuleiro já preenchida: {}x{}'.format(row, col))

        # Faz a jogada
        self.board[row][col] = piece

    # -------------------------------------------------
    def serverMove(self, piece):
        """
        Faz uma jogada no tabuleiro, em uma das posições vazias.

        Parâmetros
        ----------
        piece: str
            Letra com o símbolo jogado, entre as opções 'o' e 'x'.
        """
        # Faz uma jogada para vencer nas linhas nesta rodada, se possível
        for row in range(3):
            qtdO = 0
            qtdX = 0
            for col in range(3):
                if self.board[row][col] == 'o':
                    qtdO += 1
                if self.board[row][col] == 'x':
                    qtdX += 1
            if qtdO == 2 and qtdX == 0:
                self.board[row][0] = 'o'
                self.board[row][1] = 'o'
                self.board[row][2] = 'o'
                return

        # Faz uma jogada para vencer nas colunas nesta rodada, se possível
        for col in range(3):
            qtdO = 0
            qtdX = 0
            for row in range(3):
                if self.board[row][col] == 'o':
                    qtdO += 1
                if self.board[row][col] == 'x':
                    qtdX += 1
            if qtdO == 2 and qtdX == 0:
                self.board[0][col] = 'o'
                self.board[1][col] = 'o'
                self.board[2][col] = 'o'
                return

        # Faz uma jogada para vencer na diagonal nesta rodada, se possível
        qtdO = 0
        qtdX = 0
        for col in range(3):
            if self.board[col][col] == 'o':
                qtdO += 1
            if self.board[col][col] == 'x':
                qtdX += 1
        if qtdO == 2 and qtdX == 0:
            self.board[0][0] = 'o'
            self.board[1][1] = 'o'
            self.board[2][2] = 'o'
            return

        # Faz uma jogada para vencer na diagonal nesta rodada, se possível
        qtdO = 0
        qtdX = 0
        for col in range(3):
            if self.board[col][2-col] == 'o':
                qtdO += 1
            if self.board[col][2-col] == 'x':
                qtdX += 1
        if qtdO == 2 and qtdX == 0:
            self.board[0][2] = 'o'
            self.board[1][1] = 'o'
            self.board[2][0] = 'o'
            return

        # Impede o X de ganhar nas linhas nesta rodada, se possível
        for row in range(3):
            empty_row = -1
            empty_col = -1
            qtdX = 0
            for col in range(3):
                if self.board[row][col] == '':
                    empty_row = row
                    empty_col = col
                if self.board[row][col] == 'x':
                    qtdX += 1
            if qtdX == 2 and empty_row >= 0:
                self.move(empty_row, empty_col, 'o')
                return

        # Impede o X de ganhar nas colunas nesta rodada, se possível
        for col in range(3):
            empty_row = -1
            empty_col = -1
            qtdX = 0
            for row in range(3):
                if self.board[row][col] == '':
                    empty_row = row
                    empty_col = col
                if self.board[row][col] == 'x':
                    qtdX += 1
            if qtdX == 2 and empty_row >= 0:
                self.move(empty_row, empty_col, 'o')
                return

        # Impede o X de ganhar na diagonal
        qtdX = 0
        empty_row = -1
        empty_col = -1
        for col in range(3):
            if self.board[col][col] == '':
                empty_row = col
                empty_col = col
            if self.board[col][col] == 'x':
                qtdX += 1
        if qtdX == 2 and empty_row >= 0:
            self.move(empty_row, empty_col, 'o')
            return

        # Impede o X de ganhar na diagonal
        qtdX = 0
        empty_row = -1
        empty_col = -1
        for col in range(3):
            if self.board[col][2-col] == '':
                empty_row = col
                empty_col = 2-col
            if self.board[col][2-col] == 'x':
                qtdX += 1
        if qtdX == 2 and empty_row >= 0:
            self.move(empty_row, empty_col, 'o')
            return

        # Cria uma lista com as posições vazias
        options = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    options.append((row, col))

        # Faz uma permutação aleatória nessa lista
        shuffle(options)

        # Faz a jogada na primeira posição da lista
        if len(options) > 0:
            row = options[0][0]
            col = options[0][1]
            self.move(row, col, piece)

    # -------------------------------------------------
    def checkGameVictory(self):
        """
        Verifica se o jogo foi vencido por alguma das peças.

        """
        qtdX = 0
        qtdO = 0
        over = False

        # Verifica vitórias nas linhas
        for row in range(3):
            qtdX = 0
            qtdO = 0
            for col in range(3):
                if self.board[row][col] == 'o':
                  qtdO += 1
                if self.board[row][col] == 'x':
                  qtdX += 1
            if qtdX == 3 or qtdO == 3:
              over = True

        # Verifica vitória nas colunas

        for col in range(3):
            qtdX = 0
            qtdO = 0
            for row in range(3):
                if self.board[row][col] == 'o':
                  qtdO += 1
                if self.board[row][col] == 'x':
                  qtdX += 1
            if qtdX == 3 or qtdO == 3:
              over = True

        qtdX = 0
        qtdO = 0

        # Verifica vitória nas diagonais
        for col in range(3):
            if self.board[col][col] == 'o':
                qtdO += 1
            if self.board[col][col] == 'x':
                qtdX += 1
        if qtdX == 3 or qtdO == 3:
            over = True

        qtdX = 0
        qtdO = 0

        # Verifica vitória nas diagonais
        for col in range(3):
            if self.board[col][2-col] == 'o':
                qtdO += 1
            if self.board[col][2-col] == 'x':
                qtdX += 1
        if qtdX == 3 or qtdO == 3:
            over = True
        
        return over

    # -------------------------------------------------
    def checkGameEnd(self):
        """
        Verifica se ainda existem locais vazios no tabuleiro.

        """
        for row in range(3):
                for col in range(3):
                    if self.board[row][col] == '':
                        return False
        return True

    # -------------------------------------------------
    def cleanBoard(self):
        """
        Reseta o tabuleiro, colocando todas as suas posições como vazias.

        """
        self.board = [[''] * 3 for n in range(3)]
