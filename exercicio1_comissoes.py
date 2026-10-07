import json
from pathlib import Path


ARQUIVO_VENDAS = Path(__file__).parent / "dados" / "vendas.json"


def calcular_comissao(valor):
    """Calcula a comissão de uma venda conforme as regras do desafio."""
    if valor < 100:
        return 0.0
    if valor < 500:
        return valor * 0.01
    return valor * 0.05


def carregar_vendas():
    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def calcular_comissoes(vendas):
    """Retorna o total de comissão acumulado por vendedor."""
    comissoes = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = float(venda["valor"])
        comissao = calcular_comissao(valor)

        comissoes[vendedor] = comissoes.get(vendedor, 0.0) + comissao

    return comissoes


def main():
    dados = carregar_vendas()
    comissoes = calcular_comissoes(dados["vendas"])

    print("\n=== COMISSÃO DOS VENDEDORES ===")

    for vendedor, comissao in comissoes.items():
        print(f"{vendedor}: R$ {comissao:.2f}")


if __name__ == "__main__":
    main()
