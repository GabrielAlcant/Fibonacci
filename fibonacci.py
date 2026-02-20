import matplotlib.pyplot as plt


def fibonacci(n, contador):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci
    utilizando recursão.

    Parâmetros:
    n (int): posição do termo na sequência
    contador (list): lista usada para contar linhas executadas

    Retorno:
    int: valor do termo de Fibonacci
    """

    # Contabiliza uma linha executada a cada chamada da função
    contador[0] += 1

    # Caso base
    if n <= 1:
        return n

    # Chamada recursiva
    return fibonacci(n - 1, contador) + fibonacci(n - 2, contador)


# ==========================
# Bateria de Testes
# ==========================

valores_n = list(range(1, 11))  # Testes de n = 1 até 10
linhas_executadas = []

for n in valores_n:
    contador = [0]  # Inicializa contador
    resultado = fibonacci(n, contador)
    linhas_executadas.append(contador[0])

    print(f"Fibonacci({n}) = {resultado} | Linhas executadas = {contador[0]}")


# ==========================
# Plot do Gráfico de Desempenho
# ==========================

plt.figure()
plt.plot(valores_n, linhas_executadas, marker='o')
plt.xlabel("Valor de n")
plt.ylabel("Quantidade de linhas executadas")
plt.title("Desempenho da função recursiva Fibonacci")
plt.grid(True)
plt.show()