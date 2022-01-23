"""
Programa: Criação de Sistema em Python
Tema: Escolha de Jogos
Autor: Thomas Ribeiro
Data: 17/01/2022
"""
import forca
import adivinhacao

def escolhe_jogo():
    print(35 * '*')
    print('Escolha o seu jogo!')
    print(35 * '*')

    print('(1) Forca (2) Advinhação')

    jogo = int(input('Qual jogo você quer jogar? '))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()
    else:
        print('Opção inválida!')

if __name__ == '__main__':
    escolhe_jogo()