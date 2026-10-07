# Desafio de Desenvolvimento - Python

Implementação dos três exercícios propostos no desafio.

## Requisitos

- Python 3.10 ou superior
- Não são necessárias bibliotecas externas.

## Estrutura

```text
desafio_python/
├── main.py
├── exercicio1_comissoes.py
├── exercicio2_estoque.py
├── exercicio3_juros.py
├── README.md
└── dados/
    ├── vendas.json
    └── estoque.json
```

## Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

Também é possível executar cada exercício separadamente:

```bash
python exercicio1_comissoes.py
python exercicio2_estoque.py
python exercicio3_juros.py
```

## Exercício 1 - Comissão

As regras aplicadas por venda são:

- abaixo de R$ 100,00: sem comissão;
- de R$ 100,00 até abaixo de R$ 500,00: 1%;
- a partir de R$ 500,00: 5%.

O programa lê `dados/vendas.json`, calcula a comissão de cada venda e soma os valores por vendedor.

Resultado esperado com os dados fornecidos:

```text
João Silva: R$ 461.59
Maria Souza: R$ 457.95
Carlos Oliveira: R$ 455.91
Ana Lima: R$ 452.58
```

## Exercício 2 - Estoque

O programa lê `dados/estoque.json` e permite:

- registrar entrada;
- registrar saída;
- gerar identificador sequencial para cada movimentação;
- informar a descrição da movimentação;
- impedir saída maior que o estoque disponível;
- consultar o estoque atual;
- informar o estoque final após a movimentação.

## Exercício 3 - Juros

O programa recebe o valor original e a data de vencimento.

A taxa utilizada é de 2,5% ao dia.

Para pagamentos em atraso, é aplicado:

```text
juros = valor × 0,025 × dias de atraso
```

O programa também informa o valor final com os juros.

## Observação

Os dados dos exercícios 1 e 2 estão separados em arquivos JSON para demonstrar a leitura de dados externos, em vez de manter os registros diretamente no código.