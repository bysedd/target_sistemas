import logging
from collections import deque
from textwrap import dedent

logging.basicConfig(level=logging.INFO, format="%(message)s")


def reverse_string(original_string: str) -> str:
    """Inverte os caracteres de uma string.

    Args:
        original_string (str): A string a ser invertida.

    Returns:
        str: A string invertida.

    """
    reversed_chars: deque[str] = deque()
    for i in range(len(original_string)):
        reversed_chars.appendleft(original_string[i])

    return "".join(reversed_chars)


def main() -> None:
    """Inverte de uma determinada cadeia de caracteres.

    Essa função:
    1. Define uma string de várias linhas.
    2. Retira qualquer espaço em branco à esquerda ou à direita da string.
    3. Imprime a versão invertida da string usando a função `reverse_string`.
    """
    string = dedent("""
    Códigos escrevo sem parar,
    Pra ver a aprovação chegar,
    Se me aprovarem, vou comemorar,
    Um dev na Target? Que lugar pra brilhar!
    """)
    logging.info("String invertida: %s", reverse_string(string))


if __name__ == "__main__":
    main()
