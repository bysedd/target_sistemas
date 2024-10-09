from icecream import ic


def calculate_sum() -> int:
    """Calcular a soma de todos os números inteiros de 1 até o índice definido.

    Returns :
        int: A soma de todos os números inteiros.
    """
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k += 1
        soma += k

    return soma


def main() -> None:
    """Calcula a soma usando a função `calculate_sum` e imprime o resultado."""
    soma = calculate_sum()
    ic(soma)


if __name__ == "__main__":
    main()
