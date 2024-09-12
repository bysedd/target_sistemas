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

from typing import TypeAlias

Fatura: TypeAlias = dict[str, str | float]


def calculate_percentage(invoices: list[Fatura]) -> dict[str, float]:
    """
    Calcula o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

    Args:
        invoices (list[Fatura]): Uma lista de dicionários contendo o estado e o valor faturado.

    Returns:
        dict[str, float]: Um dicionário contendo o estado e o percentual de representação.
    """
    total: float = sum(
        invoice["valor"] for invoice in invoices if isinstance(invoice["valor"], float)
    )
    for invoice in invoices:
        if isinstance(invoice["valor"], float):
            invoice["percentual"] = (invoice["valor"] / total) * 100
    return {
        invoice["estado"]: invoice["percentual"]
        for invoice in invoices
        if isinstance(invoice["estado"], str)
        and isinstance(invoice["percentual"], float)
    }


def main() -> None:
    """
    Função principal para calcular e imprimir a contribuição percentual de cada estado na lista de faturas.

    A função inicializa uma lista de faturas, onde cada fatura é um dicionário que contém o estado e o valor da fatura.
    Em seguida, ela calcula a contribuição percentual de cada estado usando a função `calculate_percentage` e imprime os resultados.
    """
    invoices: list[Fatura] = [
        {"estado": "SP", "valor": 67_836.43},
        {"estado": "RJ", "valor": 36_678.66},
        {"estado": "MG", "valor": 29_229.88},
        {"estado": "ES", "valor": 27_165.48},
        {"estado": "Outros", "valor": 19_849.53},
    ]
    percentages = calculate_percentage(invoices)
    for state, percentage in percentages.items():
        print(f"{state:>10}: {percentage:.2f}%")


if __name__ == "__main__":
    main()
