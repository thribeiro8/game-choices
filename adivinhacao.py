"""
Programa: Criação de Sistema em Python
Tema: Jogo de Advinhação
Autor: Thomas Ribeiro
Data: 12/01/2022
"""
import random

def jogar():
    print(35 * '*')
    print('Bem vindo(a) ao Jogo de Advinhação!')
    print(35 * '*')

    numero_secreto = random.randrange(1, 101)
    quantidade_de_tentativas = 0
    pontos = 1000

    print('Nível de dificuldade? (1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina um nível: '))
    if nivel == 1:
        quantidade_de_tentativas = 20
    elif nivel == 2:
        quantidade_de_tentativas = 10
    else:
        quantidade_de_tentativas = 5

    for rodada in range(1, quantidade_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, quantidade_de_tentativas))

        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou {}'.format(chute))

        if chute < 1 or chute > 100:
            continue

        acertou = chute == numero_secreto
        maior_palpite = chute > numero_secreto
        menor_palpite = chute < numero_secreto

        if acertou:
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            print('Você Errou!')
            if maior_palpite:
                print('Você chutou um número maior!')
            elif menor_palpite:
                print('Você chutou um número menor!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print('Fim de jogo!')

if __name__ == '__main__':
    jogar()