"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será
a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem
que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o
número informado pertence ou não a sequência.
"""

from typing import Optional


def get_input() -> Optional[int]:
    """
    Solicita que o usuário insira um número e o retorna como um número inteiro.

    Returns:
        Optional[int]: O número inteiro inserido pelo usuário ou None se a entrada não for um número inteiro válido.
    """
    try:
        return int(input("Digite um número: "))
    except ValueError:
        print("Digite um número inteiro.")
        return None


def is_fibonacci(numero: int) -> bool:
    """
    Verificar se um determinado número é um número de Fibonacci.

    Um número de Fibonacci é um número que aparece na sequência de Fibonacci,
    em que cada número é a soma dos dois anteriores, começando em 0 e 1.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número for um número de Fibonacci, False caso contrário.
    """
    a, b = 0, 1
    while a < numero:
        if a == numero:
            return True
        a, b = b, a + b
    return a == numero


def main() -> None:
    """
    Função principal para determinar se um determinado número pertence à sequência de Fibonacci.
    1. Recupera a entrada do usuário usando a função `get_input`.
    2. Verifica se a entrada é válida (ou seja, não é None e não é negativa).
    3. Se a entrada for inválida, ele imprime uma mensagem apropriada e sai.
    4. Se a entrada for válida, ele verifica se o número faz parte da sequência de Fibonacci usando a função `is_fibonacci`.
    5. Imprime se o número pertence ou não à sequência de Fibonacci.
    """
    numero = get_input()
    if numero is None or numero < 0:
        print(f"{numero} não é um número válido para a sequência de Fibonacci.")
        return

    if not is_fibonacci(numero):
        print(f"{numero} não pertence à sequência de Fibonacci.")
        return

    print(f"{numero} pertence à sequência de Fibonacci.")


if __name__ == "__main__":
    main()
