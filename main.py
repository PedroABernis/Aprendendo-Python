from financeiro import GerenciadorFinanceiro

def formatar_moeda(valor: float) -> str:
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"

def ler_valor(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Valor inválido. Digite apenas números (ex.: 150,50).")
            continue
        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue
        return valor


def ler_texto(mensagem: str) -> str:
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Este campo não pode ficar vazio.")


def exibir_menu():
    print("\n" + "=" * 40)
    print("      CONTROLE FINANCEIRO PESSOAL")
    print("=" * 40)
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Listar movimentações")
    print("4 - Consultar saldo atual")
    print("5 - Exibir resumo financeiro")
    print("6 - Encerrar aplicação")
    print("-" * 40)


def registrar_receita(gerenciador):
    print("\n--- Registrar receita ---")
    descricao = ler_texto("Descrição: ")
    valor = ler_valor("Valor (R$): ")
    categoria = ler_texto("Categoria: ")
    gerenciador.registrar_receita(descricao, valor, categoria)
    print("Receita registrada com sucesso!")


def registrar_despesa(gerenciador):
    print("\n--- Registrar despesa ---")
    descricao = ler_texto("Descrição: ")
    valor = ler_valor("Valor (R$): ")
    categoria = ler_texto("Categoria: ")
    gerenciador.registrar_despesa(descricao, valor, categoria)
    print("Despesa registrada com sucesso!")


def listar_movimentacoes(gerenciador):
    print("\n--- Movimentações ---")
    movimentacoes = gerenciador.listar()
    if not movimentacoes:
        print("Nenhuma movimentação registrada.")
        return

    print(f"{'Nº':<4}{'Tipo':<10}{'Descrição':<25}{'Valor':>15}  {'Categoria'}")
    print("-" * 70)
    for i, m in enumerate(movimentacoes, start=1):
        print(
            f"{i:<4}{m.tipo:<10}{m.descricao[:24]:<25}"
            f"{formatar_moeda(m.valor):>15}  {m.categoria}"
        )


def consultar_saldo(gerenciador):
    print("\n--- Saldo atual ---")
    print(f"Saldo: {formatar_moeda(gerenciador.saldo())}")


def exibir_resumo(gerenciador):
    print("\n--- Resumo financeiro ---")
    print(f"Total de receitas:       {formatar_moeda(gerenciador.total_receitas())}")
    print(f"Total de despesas:       {formatar_moeda(gerenciador.total_despesas())}")
    print(f"Saldo atual:             {formatar_moeda(gerenciador.saldo())}")
    print(f"Total de movimentações:  {gerenciador.total_movimentacoes()}")


def main():
    gerenciador = GerenciadorFinanceiro()

    acoes = {
        "1": registrar_receita,
        "2": registrar_despesa,
        "3": listar_movimentacoes,
        "4": consultar_saldo,
        "5": exibir_resumo,
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "6":
            print("\nEncerrando a aplicação. Até logo!")
            break
        elif opcao in acoes:
            acoes[opcao](gerenciador)
        else:
            print("Opção inválida. Escolha um número de 1 a 6.")


if __name__ == "__main__":
    main()