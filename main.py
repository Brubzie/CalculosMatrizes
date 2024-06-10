import numpy as np

class Matriz:
    def __init__(self, matriz):
        self.matriz = np.array(matriz)

    def adicionar(self, outra):
        return self.matriz + outra.matriz

    def subtrair(self, outra):
        return self.matriz - outra.matriz

    def multiplicar(self, outra):
        return np.dot(self.matriz, outra.matriz)

    def determinante(self):
        return np.linalg.det(self.matriz)

    def inversa(self):
        return np.linalg.inv(self.matriz)


class Menu:
    def __init__(self):
        self.menu = [
            "=" * 50,
            "Cálculo de Matrizes 2x2".center(50),
            "-" * 50,
            "[1] Adição",
            "[2] Subtração",
            "[3] Multiplicação",
            "[4] Determinante",
            "[5] Inversa",
            "[6] Alterar Matrizes",
            "[0] Sair",
            "=" * 50,
        ]
        self.opcoes = {
            1: self.adicionar,
            2: self.subtrair,
            3: self.multiplicar,
            4: self.determinante,
            5: self.inversa,
            6: self.alterar_matrizes,
            0: self.sair
        }
        self.A = Matriz([[1, 2], [3, 4]])
        self.B = Matriz([[5, 6], [7, 8]])
        self.continuar = True

    def exibir(self):
        for linha in self.menu:
            print(linha)

    def executar(self):
        while self.continuar:
            self.exibir()
            op = None
            while op not in self.opcoes:
                try:
                    op = int(input("\nOpção: "))
                    if op not in self.opcoes:
                        raise ValueError
                except (TypeError, ValueError):
                    print("Opção inválida! Tente novamente.")
            
            self.opcoes[op]()

    def adicionar(self):
        resultado = self.A.adicionar(self.B)
        print("Resultado da Adição:\n", resultado)

    def subtrair(self):
        resultado = self.A.subtrair(self.B)
        print("Resultado da Subtração:\n", resultado)

    def multiplicar(self):
        resultado = self.A.multiplicar(self.B)
        print("Resultado da Multiplicação:\n", resultado)

    def determinante(self):
        det_A = self.A.determinante()
        print("Determinante da Matriz A:", det_A)

    def inversa(self):
        try:
            inv_A = self.A.inversa()
            print("Inversa da Matriz A:\n", inv_A)
        except np.linalg.LinAlgError:
            print("A matriz não é inversível.")

    def alterar_matrizes(self):
        print("Digite os novos valores para a Matriz A (2x2):")
        nova_A = []
        for i in range(2):
            linha = []
            for j in range(2):
                while True:
                    try:
                        valor = float(input(f"A[{i}][{j}]: "))
                        linha.append(valor)
                        break
                    except ValueError:
                        print("Entrada inválida! Digite um número.")
            nova_A.append(linha)
        self.A = Matriz(nova_A)

        print("Digite os novos valores para a Matriz B (2x2):")
        nova_B = []
        for i in range(2):
            linha = []
            for j in range(2):
                while True:
                    try:
                        valor = float(input(f"B[{i}][{j}]: "))
                        linha.append(valor)
                        break
                    except ValueError:
                        print("Entrada inválida! Digite um número.")
            nova_B.append(linha)
        self.B = Matriz(nova_B)

    def sair(self):
        self.continuar = False
        print("Saindo...")

if __name__ == "__main__":
    menu = Menu()
    menu.executar()
