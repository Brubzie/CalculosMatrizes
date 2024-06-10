# Cálculo de Matrizes 2x2

Este é um projeto de cálculo de matrizes 2x2 implementado em Python, utilizando a biblioteca `numpy`. O programa oferece um menu interativo que permite ao usuário realizar várias operações matriciais, como adição, subtração, multiplicação, cálculo do determinante e inversão de matrizes. Além disso, o usuário pode alterar os valores das matrizes e continuar executando operações até decidir sair.

## Funcionalidades

- Adição de matrizes
- Subtração de matrizes
- Multiplicação de matrizes
- Cálculo do determinante de uma matriz
- Cálculo da inversa de uma matriz
- Alteração dos valores das matrizes A e B
- Interface de usuário interativa com menu de opções

## Pré-requisitos

- Python 3.x
- Biblioteca `numpy`

## Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Navegue até o diretório do projeto:
   ```bash
   cd CalculosMatrizes

3. Instale a biblioteca numpy (caso ainda não tenha):
    ```bash
    pip install numpy

## Uso

Execute o programa principal:
    ```bash
    python main.py

## Menu de Opções

1. Adição: Soma duas matrizes.
2 Subtração: Subtrai a matriz B da matriz A.
3. Multiplicação: Multiplica a matriz A pela matriz B.
4. Determinante: Calcula o determinante da matriz A.
5. Inversa: Calcula a inversa da matriz A.
6. Alterar Matrizes: Permite ao usuário inserir novos valores para as matrizes A e B.
7. Sair: Encerra o programa.

## Exemplo de Uso

~~~python
==================================================
                 Cálculo de Matrizes 2x2          
--------------------------------------------------
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Determinante
[5] Inversa
[6] Alterar Matrizes
[0] Sair
==================================================
~~~

Escolha uma das opções digitando o número correspondente e pressionando Enter.

## Alteração de Matrizes

Para alterar os valores das matrizes, selecione a opção [6] Alterar Matrizes e insira os novos valores conforme solicitado:

~~~python
Digite os novos valores para a Matriz A (2x2):
A[0][0]: 1
A[0][1]: 2
A[1][0]: 3
A[1][1]: 4

Digite os novos valores para a Matriz B (2x2):
B[0][0]: 5
B[0][1]: 6
B[1][0]: 7
B[1][1]: 8
~~~