"""
1)	Observe o trecho de código abaixo:
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""

from icecream import ic


def calculate_sum() -> int:
    """
    Calcular a soma de todos os números inteiros de 1 até o índice definido.

    Returns:
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
    """
    Função principal que calcula a soma usando a função calculate_sum e imprime o resultado.
    """
    soma = calculate_sum()
    ic(soma)


if __name__ == "__main__":
    main()
