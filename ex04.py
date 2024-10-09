from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TypeAlias

logging.basicConfig(level=logging.INFO, format="%(message)s")


@dataclass(frozen=True)
class Invoice:
    """Representa uma fatura com um estado e um valor."""

    state: str
    value: float


Invoices: TypeAlias = list[Invoice]


def calculate_percentage(invoices: Invoices) -> dict[str, float]:
    """Calcula a porcentagem do valor de cada fatura.

    Args:
        invoices (Invoices): Uma lista de objetos `Invoice`.

    Returns:
        (dict[str, float]): Um dicionário em que as chaves são o "estado" de cada fatura
        e os valores são a porcentagem do valor total.

    """
    total = sum(invoice.value for invoice in invoices)
    return {
        invoice.state: (invoice.value / total) * 100
        for invoice in invoices
        if isinstance(invoice.value, float)
    }


def main() -> None:
    """Calcular e imprimir a contribuição percentual de cada estado na lista de faturas.

    1. Inicializa uma lista de faturas, onde cada fatura é um dicionário que contém
    o estado e o valor da fatura.
    2. Em seguida, ela calcula a contribuição percentual de cada estado usando a função
    `calculate_percentage`
    3. Imprime os resultados.
    """
    invoices: Invoices = [
        Invoice("SP", 67_836.43),
        Invoice("RJ", 36_678.66),
        Invoice("MG", 29_229.88),
        Invoice("ES", 27_165.48),
        Invoice("Outros", 19_849.53),
    ]
    percentages = calculate_percentage(invoices)
    for state, percentage in percentages.items():
        logging.info("%10s: %.2f%%", state, percentage)
    logging.info("%10s: %.2f%%", "Total", sum(percentages.values()))


if __name__ == "__main__":
    main()
