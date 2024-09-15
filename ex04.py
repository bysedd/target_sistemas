"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
•	    SP – R$67.836,43
•	    RJ – R$36.678,66
•	    MG – R$29.229,88
•	    ES – R$27.165,48
•	Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
"""

from dataclasses import dataclass


@dataclass
class Fatura:
    estado: str
    valor: float


def calculate_percentage(invoices: list[Fatura]) -> dict[str, float]:
    """
    Calculate the percentage of each invoice value relative to the total value of all invoices.

    Args:
        invoices (list[Fatura]): A list of Fatura objects, where each object contains an 'estado' (state) and 'valor' (value) attribute.

    Returns:
        dict[str, float]: A dictionary where the keys are the 'estado' of each invoice and the values are the percentage of the total value.

    Raises:
        ValueError: If any invoice's 'valor' is not a float.
    """
    if not all(isinstance(invoice.valor, float) for invoice in invoices):
        raise ValueError("O valor de cada fatura deve ser um número real.")

    total = sum(invoice.valor for invoice in invoices)
    return {invoice.estado: (invoice.valor / total) * 100 for invoice in invoices}


def main() -> None:
    """
    Função principal para calcular e imprimir a contribuição percentual de cada estado na lista de faturas.

    A função inicializa uma lista de faturas, onde cada fatura é um dicionário que contém o estado e o valor da fatura.
    Em seguida, ela calcula a contribuição percentual de cada estado usando a função `calculate_percentage` e imprime os resultados.
    """
    invoices: list[Fatura] = [
        Fatura("SP", 67_836.43),
        Fatura("RJ", 36_678.66),
        Fatura("MG", 29_229.88),
        Fatura("ES", 27_165.48),
        Fatura("Outros", 19_849.53),
    ]
    percentages = calculate_percentage(invoices)
    for state, percentage in percentages.items():
        print(f"{state:>10}: {percentage:.2f}%")


if __name__ == "__main__":
    main()
