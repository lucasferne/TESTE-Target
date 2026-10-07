def mostrar_menu():
    print("\n" + "=" * 40)
    print("        DESAFIO DE DESENVOLVIMENTO TARGET")
    print("=" * 40)
    print("1 - Exercício 1: Comissão de vendedores")
    print("2 - Exercício 2: Movimentação de estoque")
    print("3 - Exercício 3: Cálculo de juros")
    print("0 - Sair")
    print("=" * 40)


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            from exercicio1_comissoes import main as executar
            executar()
        elif opcao == "2":
            from exercicio2_estoque import main as executar
            executar()
        elif opcao == "3":
            from exercicio3_juros import main as executar
            executar()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
