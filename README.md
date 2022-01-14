# Checkers

## Execução

Para iniciar o jogo, basta executar o arquivo game.py, a tela do jogo irá abrir em outra janela.
Caso queira fechar o jogo, basta pressionar a tecla ESC ou fechar a janela do jogo, o programa irá terminar junto.
Para mover as peças, basta arrastar a peça desejada e movê-la para a região pretendida. Caso o movimento da peça seja inválido, a mesma voltará para o lugar inicial.

Para executar os testes é preciso executar o seguinte comando:
python -m unittest test_file_example.py

## Biblioteca utilizada

A biblioteca principal utilizada para o desenvolvimento do jogo foi o Pygame. Através dessa biblioteca conseguimos abrir a tela para o jogo, registrar as ações dos jogadores e utilizar inúmeros módulos que a biblioteca nos oferece.

A documentação completa da biblioteca pode ser encontrada no link https://www.pygame.org/docs/

## Funcionamento 

Quem começa jogando é o jogador 1 (peças vermelhas), e a cada movimento de peça o turno é alternado.
O turno é exibido no canto inferior esquerdo da tela, abaixo do tabuleiro.
Caso um dos jogadores fique sem peças, o outro jogador vence. Imprimindo o vencedor no canto inferior direito da tela.
