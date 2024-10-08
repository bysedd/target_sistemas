from __future__ import annotations

import json
from pathlib import Path
from typing import TypeAlias

from icecream import ic

Invoices: TypeAlias = list[dict[str, int | float]]


def load_data() -> Invoices:
    """Carrega dados de um arquivo JSON localizado no diretório `data`.

    Returns:
        Invoices: Os dados carregados a partir do arquivo “dados.json”.

    """
    data_dir = Path(__file__).parent / "data"
    with Path(data_dir / "dados.json").open() as f:
        data: Invoices = json.load(f)
    return data


def calculate_statistics(invoices: Invoices) -> dict[str, float]:
    """Calcula várias estatísticas a partir de uma lista de faturamentos.

    Args:
        invoices (Invoices): Uma lista de dicionários em que cada dicionário representa
                             uma fatura e contém uma chave de “valor” com um valor
                             numérico.

    Returns:
        (dict[str, float]): Um dicionário que contém as seguintes estatísticas:
            - "menor_faturamento": O menor valor da fatura.
            - "maior_faturamento": O maior valor da fatura.
            - "dias_acima_media": O número de dias com valores de fatura acima da média
              mensal.

    """
    invoice_values = [f["valor"] for f in invoices if f["valor"] > 0]
    monthly_average = sum(invoice_values) / len(invoice_values)
    days_above_average = sum(1 for f in invoice_values if f > monthly_average)
    minimum_invoice = min(invoice_values)
    maximum_invoice = max(invoice_values)
    return {
        "menor_faturamento": minimum_invoice,
        "maior_faturamento": maximum_invoice,
        "dias_acima_media": days_above_average,
    }


def main() -> None:
    """Carregar dados, calcular estatísticas e exibir os resultados.

    Essa função executa as seguintes etapas:
    1. Carrega os dados usando a função `load_data`.
    2. Calcula estatísticas sobre os dados carregados usando a função
       `calculate_statistics`.
    3. Exibe as estatísticas calculadas usando a função `ic`.
    """
    data = load_data()
    statistics = calculate_statistics(data)
    ic(statistics)


if __name__ == "__main__":
    main()
