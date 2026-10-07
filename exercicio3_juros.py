from datetime import date, datetime


TAXA_DIARIA = 0.025


def calcular_juros(valor, data_vencimento, data_atual=None):
    """
    Calcula os juros simples de 2,5% ao dia sobre o valor original.
    """
    if data_atual is None:
        data_atual = date.today()

    if data_atual <= data_vencimento:
        return 0, 0.0, valor

    dias_atraso = (data_atual - data_vencimento).days
    juros = valor * TAXA_DIARIA * dias_atraso
    valor_final = valor + juros

    return dias_atraso, juros, valor_final


def main():
    print("\n=== CÁLCULO DE JUROS ===")

    try:
        valor = float(input("Valor original: R$ ").replace(",", "."))
        data_texto = input("Data de vencimento (dd/mm/aaaa): ")
        data_vencimento = datetime.strptime(
            data_texto, "%d/%m/%Y"
        ).date()
    except ValueError:
        print("Valor ou data inválidos.")
        return

    if valor < 0:
        print("O valor não pode ser negativo.")
        return

    data_atual = date.today()

    dias_atraso, juros, valor_final = calcular_juros(
        valor,
        data_vencimento,
        data_atual
    )

    print(f"\nData de hoje: {data_atual.strftime('%d/%m/%Y')}")

    if dias_atraso == 0:
        print("O pagamento não está atrasado.")
        print("Juros: R$ 0,00")
        print(f"Valor final: R$ {valor:.2f}")
        return

    print(f"Dias de atraso: {dias_atraso}")
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Juros: R$ {juros:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")


if __name__ == "__main__":
    main()
