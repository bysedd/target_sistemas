"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

from collections import deque
from textwrap import dedent


def reverse_string(original_string: str) -> str:
    """
    Inverte os caracteres de uma string.

    Args:
        original_string (str): A string a ser invertida.

    Returns:
        str: A string invertida.
    """
    # return original_string[::-1]  # Alternativa mais simples.
    reversed_chars: deque[str] = deque()
    for i in range(len(original_string)):
        reversed_chars.appendleft(original_string[i])

    return "".join(reversed_chars)


def main() -> None:
    """
    Função principal que demonstra a inversão de uma determinada cadeia de caracteres.

    Essa função:
    1. Define uma string de várias linhas.
    2. Retira qualquer espaço em branco à esquerda ou à direita da string.
    3. Imprime a string original.
    4. Imprime a versão invertida da string usando a função `reverse_string`.
    """
    string = dedent("""
    Códigos escrevo sem parar,
    Pra ver a aprovação chegar,
    Se me aprovarem, vou comemorar,
    Um dev na Target? Que lugar pra brilhar!
    """)
    print(f"String invertida: {reverse_string(string)}")


if __name__ == "__main__":
    main()
