import json
from pathlib import Path


ARQUIVO_ESTOQUE = Path(__file__).parent / "dados" / "estoque.json"


def carregar_estoque():
    with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def buscar_produto(produtos, codigo):
    for produto in produtos:
        if produto["codigoProduto"] == codigo:
            return produto
    return None


def realizar_movimentacao(produtos, proximo_id):
    print("\n=== NOVA MOVIMENTAÇÃO ===")

    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print("Código inválido.")
        return proximo_id

    produto = buscar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return proximo_id

    print(f"Produto: {produto['descricaoProduto']}")
    print(f"Estoque atual: {produto['estoque']}")

    tipo = input("Tipo (E = Entrada / S = Saída): ").strip().upper()

    if tipo not in ("E", "S"):
        print("Tipo de movimentação inválido.")
        return proximo_id

    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade inválida.")
        return proximo_id

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return proximo_id

    if tipo == "S" and quantidade > produto["estoque"]:
        print("Não é possível realizar a saída: estoque insuficiente.")
        return proximo_id

    if tipo == "E":
        produto["estoque"] += quantidade
        descricao = "Entrada de mercadoria"
    else:
        produto["estoque"] -= quantidade
        descricao = "Saída de mercadoria"

    movimentacao = {
        "id": proximo_id,
        "codigoProduto": produto["codigoProduto"],
        "descricaoProduto": produto["descricaoProduto"],
        "descricaoMovimentacao": descricao,
        "quantidade": quantidade
    }

    print("\nMovimentação realizada com sucesso!")
    print(f"ID: {movimentacao['id']}")
    print(f"Descrição: {movimentacao['descricaoMovimentacao']}")
    print(f"Produto: {produto['descricaoProduto']}")
    print(f"Quantidade movimentada: {quantidade}")
    print(f"Estoque final: {produto['estoque']}")

    return proximo_id + 1


def listar_estoque(produtos):
    print("\n=== ESTOQUE ATUAL ===")

    for produto in produtos:
        print(
            f"{produto['codigoProduto']} - "
            f"{produto['descricaoProduto']}: "
            f"{produto['estoque']} unidades"
        )


def main():
    dados = carregar_estoque()
    produtos = dados["estoque"]
    proximo_id = 1

    while True:
        print("\n=== CONTROLE DE ESTOQUE ===")
        print("1 - Nova movimentação")
        print("2 - Consultar estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = realizar_movimentacao(produtos, proximo_id)
        elif opcao == "2":
            listar_estoque(produtos)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
