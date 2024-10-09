from __future__ import annotations

import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_input() -> int | None:
    """Solicita que o usuário insira um número e o retorna como um número inteiro.

    Returns:
        (int | None): O número inteiro inserido pelo usuário ou None se a entrada
        não for um número inteiro válido.

    """
    try:
        return int(input("Digite um número: "))
    except ValueError:
        logging.exception(
            "Entrada inválida. Certifique-se de inserir um número inteiro.",
        )
        return None


def is_fibonacci(numero: int) -> bool:
    """Verificar se um determinado número é um número de Fibonacci.

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
    """Verifica se um determinado número pertence à sequência de Fibonacci.

    1. Recupera a entrada do usuário usando a função `get_input`.
    2. Verifica se a entrada é válida (ou seja, não é None e não é negativa).
    3. Se a entrada for inválida, ele imprime uma mensagem apropriada e sai.
    4. Se a entrada for válida, ele verifica se o número faz parte da sequência de
       Fibonacci.
    5. Imprime se o número pertence ou não à sequência de Fibonacci.
    """
    numero = get_input()
    if numero is None or numero < 0:
        logging.info("%s não é um número válido para a sequência de Fibonacci.", numero)
        return

    if not is_fibonacci(numero):
        logging.info("%d não pertence à sequência de Fibonacci.", numero)
        return

    logging.info("%d pertence à sequência de Fibonacci.", numero)


if __name__ == "__main__":
    main()
