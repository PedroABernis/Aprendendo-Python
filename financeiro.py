from dataclasses import dataclass

RECEITA = "Receita"
DESPESA = "Despesa"

@dataclass
class Movimentacao:
    tipo: str        # "Receita" ou "Despesa"
    descricao: str
    valor: float
    categoria: str

class GerenciadorFinanceiro:
    """Guarda as movimentações e calcula totais e saldo."""

    def __init__(self):
        self._movimentacoes: list[Movimentacao] = []

    def _registrar(self, tipo, descricao, valor, categoria):
        descricao = descricao.strip()
        categoria = categoria.strip()
        if not descricao:
            raise ValueError("A descrição não pode ser vazia.")
        if not categoria:
            raise ValueError("A categoria não pode ser vazia.")
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        mov = Movimentacao(tipo, descricao, valor, categoria)
        self._movimentacoes.append(mov)
        return mov

    def registrar_receita(self, descricao, valor, categoria):
        return self._registrar(RECEITA, descricao, valor, categoria)

    def registrar_despesa(self, descricao, valor, categoria):
        return self._registrar(DESPESA, descricao, valor, categoria)

    def listar(self):
        return list(self._movimentacoes)

    def total_receitas(self):
        return sum(m.valor for m in self._movimentacoes if m.tipo == RECEITA)

    def total_despesas(self):
        return sum(m.valor for m in self._movimentacoes if m.tipo == DESPESA)

    def saldo(self):
        # Saldo = Receitas - Despesas
        return self.total_receitas() - self.total_despesas()

    def total_movimentacoes(self):
        return len(self._movimentacoes)