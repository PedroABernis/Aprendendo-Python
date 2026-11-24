# 💰 Controle Financeiro (Terminal)

Projeto desenvolvido em **Python** com o objetivo de **praticar lógica de programação**. É um sistema de controle financeiro pessoal executado inteiramente pelo terminal, sem interface gráfica, onde é possível registrar receitas e despesas, consultar movimentações e acompanhar o saldo.

## 📋 Funcionalidades

- Registrar receitas (descrição, valor e categoria)
- Registrar despesas (descrição, valor e categoria)
- Listar todas as movimentações em formato de tabela
- Consultar o saldo atual (`Saldo = Receitas - Despesas`)
- Exibir um resumo financeiro (total de receitas, total de despesas, saldo e quantidade de movimentações)
- Validação das entradas (campos vazios, valores inválidos, zero e negativos)
- Valores exibidos no padrão brasileiro (`R$ 1.234,56`)

## 🗂️ Estrutura do projeto

```
controle_financeiro/
├── main.py         # menu e interação com o usuário
├── financeiro.py   # regras de negócio (classes e cálculos)
└── README.md
```

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Exibe o menu, lê os dados digitados e mostra os resultados |
| `financeiro.py` | Guarda as movimentações, valida os dados e calcula totais e saldo |

A lógica foi separada da interface para que as regras de negócio possam ser reaproveitadas no futuro (por exemplo, em uma interface gráfica ou em uma API).

## ▶️ Como executar

**Pré-requisito:** Python 3.9 ou superior. Não é necessário instalar nenhuma biblioteca externa.

```bash
# 1. Clone o repositório
git clone <https://github.com/PedroABernis/Aprendendo-Python>

# 2. Entre na pasta do projeto
cd controle_financeiro

# 3. Execute
python main.py
```

No Linux/Mac, use `python3 main.py` se necessário. No PyCharm, basta abrir o `main.py` e clicar em **Run**.

## 🖥️ Exemplo de uso

```
========================================
      CONTROLE FINANCEIRO PESSOAL
========================================
1 - Registrar receita
2 - Registrar despesa
3 - Listar movimentações
4 - Consultar saldo atual
5 - Exibir resumo financeiro
6 - Encerrar aplicação
----------------------------------------
Escolha uma opção: 3

--- Movimentações ---
Nº  Tipo      Descrição                          Valor  Categoria
----------------------------------------------------------------------
1   Receita   Salario                      R$ 3.000,50  Trabalho
2   Despesa   Mercado                        R$ 450,25  Alimentacao
```

## 🧠 Conceitos praticados

- Estruturas de repetição (`while`) e condicionais (`if / elif / else`)
- Funções e organização do código em módulos
- Classes e objetos (programação orientada a objetos)
- `dataclass` para modelar dados
- Listas e dicionários (menu com dicionário de ações)
- Tratamento de exceções (`try / except`)
- Validação de entrada de dados
- Formatação de textos com *f-strings*
- Separação de responsabilidades (regras de negócio x interface)

## ✅ Requisitos atendidos

| Requisito | Descrição |
|---|---|
| RF01 | Menu principal |
| RF02 | Registrar receita |
| RF03 | Registrar despesa |
| RF04 | Listar movimentações |
| RF05 | Consultar saldo |
| RF06 | Resumo financeiro |
| RF07 | Encerramento da aplicação |

## ⚠️ Limitações desta versão

- Os dados ficam apenas na memória: ao encerrar o programa, as movimentações são perdidas.
- Não é possível editar ou excluir uma movimentação já registrada.
- As movimentações não possuem data.

## 🚀 Melhorias futuras

- [ ] Salvar os dados em arquivo (JSON ou CSV) ou em banco de dados (SQLite)
- [ ] Adicionar data às movimentações e filtrar por período
- [ ] Permitir editar e excluir movimentações
- [ ] Resumo por categoria
- [ ] Interface gráfica
- [ ] Testes automatizados

## 👨‍💻 Autor

Desenvolvido por **Pedro Bernis** como projeto de estudo.
