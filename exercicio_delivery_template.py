"""
EXERCÍCIO PRÁTICO — Aplicativo de Delivery "Tá na Hora"
=========================================================

Este arquivo é um TEMPLATE: contém a assinatura de cada função já pronta,
com uma explicação (docstring) do que ela deve fazer.

Sua tarefa: substituir cada "pass" pelo código que resolve o problema.

Regras:
- NÃO mude o nome das funções.
- NÃO mude a ordem nem o nome dos parâmetros.
- Você pode (e deve) criar variáveis auxiliares dentro de cada função.

Se travar em algum tópico, releia a parte correspondente da apostila.
"""
from pprint import pprint
# # =====================================================================
# # DADOS DE PARTIDA (não precisa mexer aqui)
# # =====================================================================
# dNomeEntregador = {
#     "E1": "Marcos", "E2": "Juliana", "E3": "Renato",
#     "E4": "Patricia", "E5": "Felipe"
# }

# dVeiculo = {
#     "E1": "Moto", "E2": "Bike", "E3": "Moto",
#     "E4": "Carro", "E5": "Moto"
# }

# dEntregas = {
#     "E1": 120, "E2": 45, "E3": 98,
#     "E4": 60, "E5": 150
# }

# dTaxaPorVeiculo = {
#     "Moto": 8.50, "Bike": 5.00, "Carro": 12.00
# }

# Observação importante antes de começar:
# - Os NOMES dos entregadores NÃO se repetem.
# - Os VEÍCULOS se repetem (vários entregadores usam Moto, por exemplo).


# =====================================================================
# BLOCO 1 — CRUZAMENTO, FREQUÊNCIA E AGRUPAMENTO
# =====================================================================

def obter_taxa_por_entregador(dVeiculo, dTaxaPorVeiculo):
    """
    Para cada entregador, descubra o veículo que ele usa (em dVeiculo).
    Em seguida, use esse veículo para descobrir a taxa correspondente
    (em dTaxaPorVeiculo). Monte um novo dicionário relacionando cada
    entregador à sua taxa.

    Parâmetros:
        dVeiculo (dict): código -> veículo
        dTaxaPorVeiculo (dict): veículo -> taxa em R$

    Retorno:
        dict no formato {código_do_entregador: taxa_em_reais}
    """
    # Escreva seu código aqui
    
    dEntregadorTaxa = dict()
    for (entregador,veiculo) in dVeiculo.items():
        taxa = dTaxaPorVeiculo[veiculo]
        dEntregadorTaxa[entregador] = taxa
    return dEntregadorTaxa
        


def contar_entregadores_por_veiculo(dVeiculo):
    """
    Conte quantos entregadores usam cada tipo de veículo.

    Parâmetros:
        dVeiculo (dict): código -> veículo

    Retorno:
        dict no formato {veículo: quantidade_de_entregadores}
    """
    # Escreva seu código aqui

    dQntVeiculos = dict()
    for (entregador,veiculo) in dVeiculo.items():
        qnt = dQntVeiculos.get(veiculo,0)
        dQntVeiculos[veiculo] = qnt +1
    return dQntVeiculos

def agrupar_entregadores_por_veiculo(dVeiculo):
    """
    Agrupe os CÓDIGOS dos entregadores de acordo com o veículo que usam.
    
    Parâmetros:
        dVeiculo (dict): código -> veículo

    Retorno:
        dict no formato {veículo: [lista de códigos de entregadores]}
    """
    # Escreva seu código aqui

    dVeiculoEntregador = {}
    for (entregador,veiculo) in dVeiculo.items():
        codigo = dVeiculoEntregador.get(veiculo,[])
        codigo.append(entregador)
        dVeiculoEntregador[veiculo] = codigo
    return dVeiculoEntregador
        




# =====================================================================
# BLOCO 2 — INVERSÃO DE DICIONÁRIOS
# =====================================================================

def inverter_nomes(dNomeEntregador):
    """
    Os nomes dos entregadores não se repetem entre si. Inverta o
    dicionário dNomeEntregador, trocando código por nome.

    Parâmetros:
        dNomeEntregador (dict): código -> nome

    Retorno:
        dict no formato {nome: código_do_entregador}
    """
    # Escreva seu código aqui

    dInvertido = {}
    for (codigo, nome) in dNome


def inverter_veiculos_com_nomes(dVeiculo, dNomeEntregador):
    """
    O tipo de veículo se repete entre vários entregadores. Inverta
    dVeiculo, mas em vez de guardar os códigos, guarde os NOMES dos
    entregadores (use dNomeEntregador para converter cada código em
    nome antes de guardar na lista).

    Parâmetros:
        dVeiculo (dict): código -> veículo
        dNomeEntregador (dict): código -> nome

    Retorno:
        dict no formato {veículo: [lista de nomes de entregadores]}
    """
    # Escreva seu código aqui

    pass


# =====================================================================
# BLOCO 3 — DICIONÁRIO DE DICIONÁRIOS E CONSULTAS
# =====================================================================

def montar_cadastro_entregadores(dNomeEntregador, dVeiculo, dEntregas):
    """
    Junte os três dicionários originais num único dicionário de
    dicionários, um "cadastro completo" por entregador.

    Parâmetros:
        dNomeEntregador (dict): código -> nome
        dVeiculo (dict): código -> veículo
        dEntregas (dict): código -> entregas no mês

    Retorno:
        dict no formato:
        {código: {'nome': ..., 'veiculo': ..., 'entregas': ...}}
    """
    # Escreva seu código aqui

    pass


def consultar_campo(dCadastro, codigo, campo):
    """
    Consulte um campo específico de um entregador dentro do cadastro,
    de forma segura (sem quebrar o programa se o código ou o campo
    não existirem).

    Parâmetros:
        dCadastro (dict): dicionário de dicionários dos entregadores
        codigo (str): código do entregador buscado
        campo (str): nome do campo desejado ('nome', 'veiculo' ou
                     'entregas')

    Retorno:
        o valor do campo pedido, ou a string 'Não encontrado' se o
        código ou o campo não existirem
    """
    # Escreva seu código aqui

    pass


def listar_todos_entregadores(dCadastro):
    """
    Percorra o cadastro inteiro e IMPRIMA uma linha para cada
    entregador, exatamente neste formato:
    "<código>: <nome> | Veículo: <veiculo> | Entregas: <entregas>"

    Parâmetros:
        dCadastro (dict): dicionário de dicionários dos entregadores

    Retorno:
        Esta função não precisa retornar nada (apenas imprimir)
    """
    # Escreva seu código aqui

    pass


def listar_entregadores_acima_de(dCadastro, minimo):
    """
    Procure, no cadastro, os entregadores que fizeram MAIS entregas
    do que o valor mínimo informado.

    Parâmetros:
        dCadastro (dict): dicionário de dicionários dos entregadores
        minimo (int): valor mínimo de entregas (não incluído)

    Retorno:
        list com os códigos dos entregadores que atendem à condição
    """
    # Escreva seu código aqui

    pass


def listar_entregadores_por_veiculo(dCadastro, veiculo):
    """
    Procure, no cadastro, os entregadores que usam um determinado
    tipo de veículo.

    Parâmetros:
        dCadastro (dict): dicionário de dicionários dos entregadores
        veiculo (str): tipo de veículo procurado (ex: 'Moto')

    Retorno:
        list com os códigos dos entregadores que usam esse veículo
    """
    # Escreva seu código aqui

    pass


# =====================================================================
# BLOCO 4 — INVERTENDO O DICIONÁRIO DE DICIONÁRIOS
# =====================================================================
# Antes de começar, lembre-se da pergunta-guia:
# "O campo que eu quero promover a nova chave tem valores únicos, ou
#  valores repetidos entre os entregadores?"
# Único -> reindexação simples (Caso A). Repetido -> agrupamento (Caso B).

def reindexar_por_nome(dCadastro):
    """
    Crie um novo dicionário de dicionários, trocando a chave externa:
    em vez do código, a chave passa a ser o NOME do entregador (campo
    com valores únicos). O restante das informações deve continuar
    disponível no dicionário interno.

    Parâmetros:
        dCadastro (dict): dicionário de dicionários dos entregadores

    Retorno:
        dict no formato:
        {nome: {'codigo': ..., 'veiculo': ..., 'entregas': ...}}
    """
    # Escreva seu código aqui

    pass


def agrupar_cadastro_por_veiculo(dCadastro):
    """
    Crie um novo dicionário, agrupando os NOMES dos entregadores de
    acordo com o veículo que usam (campo com valores repetidos).

    Parâmetros:
        dCadastro (dict): dicionário de dicionários dos entregadores

    Retorno:
        dict no formato {veiculo: [lista de nomes de entregadores]}
    """
    # Escreva seu código aqui

    pass


# =====================================================================
# COMO TESTAR SUAS FUNÇÕES
# =====================================================================
# Depois de preencher cada função acima, descomente as linhas abaixo
# (uma de cada vez, ou todas juntas) e rode este arquivo para conferir
# se os resultados fazem sentido com os dados originais.
# Nenhum resultado esperado é mostrado aqui de propósito — teste com
# atenção e compare com o que você já sabe sobre os dados de partida!

# =====================================================================
# DADOS DE PARTIDA (não precisa mexer aqui)
# =====================================================================
dNomeEntregador = {
    "E1": "Marcos", "E2": "Juliana", "E3": "Renato",
    "E4": "Patricia", "E5": "Felipe"
}

dVeiculo = {
    "E1": "Moto", "E2": "Bike", "E3": "Moto",
    "E4": "Carro", "E5": "Moto"
}

dEntregas = {
    "E1": 120, "E2": 45, "E3": 98,
    "E4": 60, "E5": 150
}

dTaxaPorVeiculo = {
    "Moto": 8.50, "Bike": 5.00, "Carro": 12.00
}

print("1.taxa_por_entregador")
pprint(obter_taxa_por_entregador(dVeiculo, dTaxaPorVeiculo))
print("2. Quantidade de entregadores por veículo")
pprint(contar_entregadores_por_veiculo(dVeiculo))
print("3. entregadores por veículo")
pprint(agrupar_entregadores_por_veiculo(dVeiculo))
print("4. dicionário por nome de entregador")
pprint(inverter_nomes(dNomeEntregador))
print("5. dicionário por veículo e lista de entregadores")
pprint(inverter_veiculos_com_nomes(dVeiculo, dNomeEntregador))
print("6. cadastro completo por entregador")
dCadastro = montar_cadastro_entregadores(dNomeEntregador, dVeiculo, dEntregas)
pprint(dCadastro)
print("7. consulta veiculo / entregador existente")
pprint(consultar_campo(dCadastro, "E3", "veiculo"))
print("8. consulta veiculo / entregador inexistente")
pprint(consultar_campo(dCadastro, "E99", "nome"))  # deve dar 'Não encontrado'
print("9. Exibe cadastro de entregadores")
listar_todos_entregadores(dCadastro)
print("10. Eentregadores acima de 90")
pprint(listar_entregadores_acima_de(dCadastro, 90))
print("11. Eentregadores de moto")
pprint(listar_entregadores_por_veiculo(dCadastro, "Moto"))
print("12. Cadastro por nome")
pprint(reindexar_por_nome(dCadastro))
print("13. Cadastro por veiculo")
pprint(agrupar_cadastro_por_veiculo(dCadastro))
