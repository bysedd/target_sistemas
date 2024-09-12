"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json
from pathlib import Path
from typing import TypeAlias

from icecream import ic

Number: TypeAlias = int | float
Data: TypeAlias = list[dict[str, Number]]


def load_data() -> Data:
    """
    Carrega dados de um arquivo JSON localizado no diretório 'data' relativo à localização do script.

    Returns:
        Data: Os dados carregados a partir do arquivo “dados.json”.
    """
    data_dir = Path(__file__).parent / "data"
    with open(data_dir / "dados.json") as f:
        data: Data = json.load(f)
    return data


def calculate_statistics(invoices: Data) -> dict[str, Number]:
    """
    Calcula várias estatísticas a partir de uma lista de faturamentos.

    Args:
        invoices (Data): Uma lista de dicionários em que cada dicionário representa uma fatura
                         e contém uma chave de “valor” com um valor numérico.

    Returns:
        dict[str, Number]: Um dicionário que contém as seguintes estatísticas:
            - "menor_faturamento": O menor valor da fatura.
            - "maior_faturamento": O maior valor da fatura.
            - "dias_acima_media": O número de dias com valores de fatura acima da média mensal.
    """
    invoice_values = [f["valor"] for f in invoices if f["valor"] > 0]
    media_mensal = sum(invoice_values) / len(invoice_values)
    dias_acima_media = sum(1 for f in invoice_values if f > media_mensal)
    menor_faturamento = min(invoice_values)
    maior_faturamento = max(invoice_values)
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media,
    }


def main() -> None:
    """
    Função principal para carregar dados, calcular estatísticas e exibir os resultados.

    Essa função executa as seguintes etapas:
    1. Carrega os dados usando a função `load_data`.
    2. Calcula estatísticas sobre os dados carregados usando a função `calculate_statistics`.
    3. Exibe as estatísticas calculadas usando a função `ic`.
    """
    data = load_data()
    statistics = calculate_statistics(data)
    ic(statistics)


if __name__ == "__main__":
    main()
