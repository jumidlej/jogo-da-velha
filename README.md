# Jogo da Velha

Essa aplicação possui um programa cliente e um programa servidor. O programa servidor irá se comunicar e jogar o jogo da velha contra o programa cliente de forma automática.

## O Funcionamento do Jogo

O jogo será gerido pelo programa servidor. Antes de cada partida, será perguntado ao programa cliente se ele deseja começar a partida. No final de cada partida, será perguntado ao programa cliente se ele deseja jogar novamente.

A implementação do jogo foi feita a partir da Classe GameState, que guarda o estado do tabuleiro do jogo. O tabuleiro do jogo será inicializado como uma lista com posições vazias e será preenchido a cada jogada do servidor ou do cliente. Existem funções auxiliares para executar as jogadas, verificar se alguém venceu o jogo e limpar o tabuleiro quando necessário.

A cada jogada, haverá uma verificação para saber se algum programa, cliente ou servidor, venceu a partida ou se deu 'velha'. 

O programa servidor só irá jogar de forma aleatória se, na rodada atual, não houver possibilidade de vencer o jogo ou de impedir o programa cliente de vencer. Para isso, o programa irá verificar todos os locais do tabuleiro.

## O Protocolo da Aplicação

Assim que o programa cliente se conecta com o programa servidor, o programa servidor pergunta se o cliente deseja ser o primeiro a efetuar uma jogada. A partir disso, o servidor envia o tabuleiro vazio ou com a primeira jogada efetuada. Então, sempre que o programa cliente receber dados do servidor, ele verificará se é um tabuleiro ou uma pergunta que indica o fim do jogo (Deseja jogar novamente?). Se for um tabuleiro, o cliente verificará se a jogada efetuada pelo servidor venceu o jogo, caso o servidor tenha vencido, o cliente enviará a mensagem: O servidor venceu!. Se o servidor não venceu, o cliente enviará o tabuleiro com uma nova jogada efetuada por ele. Se o cliente tiver recebido a pergunta: Deseja jogar novamente?, ele responderá com 'S' ou 'N'.

Sempre que o servidor receber uma jogada do cliente, ele verificará se o cliente venceu o jogo, se tiver vencido, ele enviará a pergunta: Deseja jogar novamente?. Se o cliente não venceu, o servidor irá efetuar uma jogada e enviar para o cliente. Se a jogada efetuada pelo servidor vencer o jogo, o servidor ainda sim enviará o tabuleiro para o cliente para que ele possa ser mostrado, e esperará a resposta: O servidor venceu!. Após isso, irá perguntar ao cliente se ele deseja jogar novamente. Se sim, irá perguntar também se ele deseja ser o primeiro a efetuar uma jogada, se não, a conexão será perdida e o servidor voltará a esperar uma conexão.

<img src="/protocolo.drawio.png" alt="Protocolo da aplicação"/>

Para essa aplicação, o protocolo escolhido foi o TCP, pois é mais confiável e, para o bom funcionamento do jogo, dados não podem ser perdidos.

## Requisitos para o Funcionamento

* Python 3.8
* NumPy 1.20

## Comandos para Executar os Programas

* python3 server.py
* python3 client.py
