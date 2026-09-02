# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:02:36 2026

@author: EGLOBAL
"""

"""
CRUZANDO, INVERTENDO E ORGANIZANDO DICIONÁRIOS
===============================================

Uma aula passo a passo com o Campeonato de Games entre Amigos

Da inversão simples até a inversão de um dicionário de dicionários
Nível: Iniciante • Linguagem: Python • Pré-requisito: noções de dicionário simples
"""

from pprint import pprint

print("=" * 80)
print("🎮 CRUZANDO, INVERTENDO E ORGANIZANDO DICIONÁRIOS")
print("=" * 80)

print("""
🎯 Objetivo desta aula:
- Partir de 3 dicionários simples sobre os jogadores de um campeonato
- Inverter um deles (chave ↔ valor)
- Juntar os 3 num único dicionário de dicionários
- Fazer consultas nesse dicionário de dicionários
- Inverter o próprio dicionário de dicionários
""")

print("\n" + "=" * 80)
print("PARTE 1 — O CENÁRIO: CAMPEONATO DE GAMES ENTRE AMIGOS")
print("=" * 80)

print("""
🎮 A situação:
Um grupo de amigos organizou um campeonato de um jogo online. Cada jogador tem:
- código de inscrição (J1, J2, J3...)
- apelido (nick) escolhido para jogar
- time
- pontuação acumulada no campeonato

As informações estão espalhadas em TRÊS dicionários separados.
""")

# =====================================================================
# DICIONÁRIOS DE PARTIDA
# =====================================================================

print("\n--- DICIONÁRIO 1: dApelido (código → apelido) ---")
dApelido = {
    'J1': 'ShadowFox',
    'J2': 'LunaStar',
    'J3': 'TrovaoAzul',
    'J4': 'GatoNinja',
    'J5': 'AguiaDourada'
}
pprint(dApelido)

print("\n--- DICIONÁRIO 2: dTime (código → time) ---")
dTime = {
    'J1': 'Fenix',
    'J2': 'Trovão',
    'J3': 'Fenix',
    'J4': 'Trovão',
    'J5': 'Fenix'
}
pprint(dTime)

print("\n--- DICIONÁRIO 3: dPontos (código → pontuação) ---")
dPontos = {
    'J1': 1200,
    'J2': 1050,
    'J3': 1500,
    'J4': 860,
    'J5': 900
}
pprint(dPontos)

print("\n" + "=" * 80)
print("PARTE 2 — REVISÃO RELÂMPAGO: INVERTENDO UM DICIONÁRIO SIMPLES")
print("=" * 80)

print("""
🔁 Relembrando:
Inverter um dicionário significa trocar chave → valor por valor → chave.

Isso só funciona de forma direta e simples quando os valores NÃO se repetem.
Quando os valores se repetem, é preciso agrupar em listas.
""")

print("\n--- Por que dá para inverter o dApelido sem problema? ---")
print("""
Porque cada apelido pertence a um único jogador — nenhum valor se repete.
Então cada apelido pode virar uma chave nova, com segurança.
""")

print("\n--- OBJETIVO: dCodigoPorApelido (apelido → código) ---")
dCodigoPorApelido = {}

for codigo, apelido in dApelido.items():
    dCodigoPorApelido[apelido] = codigo
    print(f"Passo {codigo}: {apelido} → {codigo}")
    print(f"  dCodigoPorApelido = {dCodigoPorApelido}")

print("\n✅ RESULTADO FINAL:")
pprint(dCodigoPorApelido)

print("\n" + "=" * 80)
print("PARTE 3 — JUNTANDO OS 3 DICIONÁRIOS NUM DICIONÁRIO DE DICIONÁRIOS")
print("=" * 80)

print("""
🧠 Analogia do dia a dia:
Imagine uma ficha de inscrição do campeonato: em vez de ter 3 fichários 
separados (um só com apelidos, outro só com times, outro só com pontos), 
você organiza tudo numa ÚNICA ficha por jogador, com todos os campos juntos.
""")

print("\n--- OBJETIVO: dJogadores (código → {apelido, time, pontos}) ---")
dJogadores = {}

print("\nProcessando jogadores:")
for codigo in dApelido:
    apelido = dApelido.get(codigo)
    time = dTime.get(codigo)
    pontos = dPontos.get(codigo)
    
    # Monta o dicionário interno com os 3 dados juntos
    dJogadores[codigo] = {
        'apelido': apelido,
        'time': time,
        'pontos': pontos
    }
    print(f"✅ {codigo} cadastrado: {dJogadores[codigo]}")

print("\n🎯 RESULTADO FINAL:")
pprint(dJogadores)

print("\n--- VISUALIZAÇÃO TABELAR ---")
print("-" * 70)
print(f"{'Código':<8} {'Apelido':<15} {'Time':<10} {'Pontos':<8}")
print("-" * 70)
for codigo, dados in dJogadores.items():
    print(f"{codigo:<8} {dados['apelido']:<15} {dados['time']:<10} {dados['pontos']:<8}")
print("-" * 70)

print("\n" + "=" * 80)
print("PARTE 4 — FAZENDO CONSULTAS NO DICIONÁRIO DE DICIONÁRIOS")
print("=" * 80)

print("""
🔑 Regra de ouro:
Sempre pense em DOIS níveis: primeiro a chave externa (o código do jogador), 
depois a chave interna (o campo que você quer, como 'apelido', 'time' ou 'pontos').
""")

print("\n--- 4.1 CONSULTA DIRETA COM .get() ENCADEADO ---")
print("\nQual é o apelido do jogador J3?")
apelido_j3 = dJogadores.get('J3', {}).get('apelido', 'não encontrado')
print(f"Apelido de J3: {apelido_j3}")

print("\nE se o jogador não existir?")
apelido_j99 = dJogadores.get('J99', {}).get('apelido', 'não encontrado')
print(f"Apelido de J99: {apelido_j99}")

print("\n--- 4.2 PERCORRENDO TODOS OS JOGADORES ---")
print("\nLista completa:")
for codigo, dados in dJogadores.items():
    print(f"{codigo}: {dados['apelido']} | Time: {dados['time']} | Pontos: {dados['pontos']}")

print("\n--- 4.3 FILTRO: JOGADORES COM MAIS DE 1000 PONTOS ---")
print("\nJogadores com mais de 1000 pontos:")
for codigo, dados in dJogadores.items():
    if dados['pontos'] > 1000:
        print(f" {codigo}: {dados['apelido']} ({dados['pontos']} pts)")

print("\n--- 4.4 FILTRO: JOGADORES DO TIME FENIX ---")
print("\nJogadores do time Fenix:")
for codigo, dados in dJogadores.items():
    if dados['time'] == 'Fenix':
        print(f" {codigo}: {dados['apelido']}")

print("\n" + "=" * 80)
print("PARTE 5 — O GRANDE DESAFIO: INVERTENDO O DICIONÁRIO DE DICIONÁRIOS")
print("=" * 80)

print("""
🧠 A grande sacada desta aula:
Inverter um dicionário de dicionários significa: escolher UM CAMPO de 
dentro do dicionário interno e promovê-lo a nova chave externa.

E a pergunta que decide tudo: esse campo escolhido tem valores únicos 
entre os jogadores, ou valores repetidos?

❓ Pergunta-guia:
- SIM, os valores são únicos → Caso A: Reindexação simples (1 para 1)
- NÃO, os valores se repetem → Caso B: Inversão com agrupamento (listas)
""")

print("\n" + "-" * 80)
print("CASO A — REINDEXAR PELO APELIDO (campo com valores únicos)")
print("-" * 80)

print("""
Objetivo: criar dPorApelido, onde a chave passa a ser o apelido, 
e o valor é um dicionário com o restante das informações.
""")

print("De: dJogadores[código] → {apelido, time, pontos}")
print("Para: dPorApelido[apelido] → {codigo, time, pontos}")

dPorApelido = {}

for codigo, dados in dJogadores.items():
    apelido = dados['apelido']
    
    # Monta o novo dicionário interno, trocando 'apelido' por 'codigo'
    dPorApelido[apelido] = {
        'codigo': codigo,
        'time': dados['time'],
        'pontos': dados['pontos']
    }
    print(f"Passo {codigo}: {apelido} → {dPorApelido[apelido]}")

print("\n✅ RESULTADO FINAL:")
pprint(dPorApelido)

print("\n--- VISUALIZAÇÃO TABELAR ---")
print("-" * 70)
print(f"{'Apelido':<15} {'Código':<8} {'Time':<10} {'Pontos':<8}")
print("-" * 70)
for apelido, dados in dPorApelido.items():
    print(f"{apelido:<15} {dados['codigo']:<8} {dados['time']:<10} {dados['pontos']:<8}")
print("-" * 70)

print("\n" + "-" * 80)
print("CASO B — AGRUPAR PELO TIME (campo com valores repetidos)")
print("-" * 80)

print("""
Objetivo: criar dPorTime, onde a chave passa a ser o time, 
e o valor é a LISTA de apelidos dos jogadores daquele time.
""")

print("\n--- PRIMEIRO, VAMOS VER O QUE ACONTECE SE FIZERMOS DO JEITO ERRADO ---")
print("""
ATENÇÃO: este código tem um problema de propósito, para mostrarmos o erro!
""")

dErrado = {}

print("\nExecução do código ERRADO (sobrescrevendo valores):")
for codigo, dados in dJogadores.items():
    time = dados['time']
    dErrado[time] = dados['apelido']  # ⚠️ vai SOBRESCREVER quando o time repetir!
    print(f"Passo {codigo}: time={time}, apelido={dados['apelido']}")
    print(f"  dErrado atual: {dErrado}")

print("\n⚠️ RESULTADO DO CÓDIGO ERRADO — DADOS PERDIDOS!")
print("Perdemos 'ShadowFox' e 'TrovaoAzul' (sobrescritos dentro de 'Fenix')")
print("e perdemos 'LunaStar' (sobrescrita dentro de 'Trovão')")
pprint(dErrado)

print("\n--- AGORA, A FORMA CORRETA: AGRUPANDO COM setdefault() ---")

dPorTime = {}

print("\nExecução do código CORRETO:")
for codigo, dados in dJogadores.items():
    time = dados['time']
    apelido = dados['apelido']
    
    # setdefault garante uma lista para cada time,
    # e o append adiciona o apelido sem apagar os anteriores
    dPorTime.setdefault(time, []).append(apelido)
    print(f"Passo {codigo}: time={time}, apelido={apelido}")
    print(f"  dPorTime['{time}'] = {dPorTime.get(time, [])}")

print("\n✅ RESULTADO FINAL — NINGUÉM FOI PERDIDO!")
pprint(dPorTime)

print("\n--- QUADRO-RESUMO: Caso A vs. Caso B ---")
print("""
┌─────────────────────┬────────────────────────┬────────────────────────┐
│                     │   Caso A — reindexar   │   Caso B — agrupar    │
│                     │   (apelido)            │   (time)              │
├─────────────────────┼────────────────────────┼────────────────────────┤
│ Os valores do campo │   Não                  │   Sim                 │
│ se repetem?         │                        │                        │
├─────────────────────┼────────────────────────┼────────────────────────┤
│ Técnica usada       │   Atribuição direta    │   setdefault(chave,   │
│                     │                        │   []).append(valor)   │
├─────────────────────┼────────────────────────┼────────────────────────┤
│ Formato do novo     │   Um dicionário com    │   Uma lista de        │
│ valor               │   o restante dos dados │   valores             │
├─────────────────────┼────────────────────────┼────────────────────────┤
│ Risco do jeito      │   Nenhum (não há       │   Sobrescrita e       │
│ ingênuo             │   repetição)           │   perda de dados      │
└─────────────────────┴────────────────────────┴────────────────────────┘
""")

print("\n" + "=" * 80)
print("PARTE 6 — FECHANDO O CICLO: O MAPA COMPLETO DA JORNADA")
print("=" * 80)

print("""
🗺️ O caminho que percorremos nesta aula:

1) Começamos com 3 dicionários simples (dApelido, dTime, dPontos),
   todos usando o código do jogador como chave.

2) Invertemos o dApelido (valores únicos) para descobrir o código
   a partir do apelido.

3) Juntamos os 3 dicionários num único dicionário de dicionários:
   dJogadores.

4) Fizemos consultas em dJogadores: acesso direto, percorrendo tudo,
   e filtrando por condições.

5) Invertemos o próprio dJogadores, escolhendo um campo interno para
   virar a nova chave: apelido (único → reindexação) e time (repetido → 
   agrupamento).
""")

print("""
✅ Pergunta-guia que serve para a vida toda (guarde esta!):

Sempre que for inverter algo — um dicionário simples OU um campo de
dentro de um dicionário de dicionários — pergunte-se:

"Esse valor (ou campo) pode se repetir entre diferentes registros?"

Se a resposta for NÃO → inversão simples, direta, 1 para 1.
Se a resposta for SIM → inversão com agrupamento, usando lista 
(se possível, com setdefault).
""")

print("\n" + "=" * 80)
print("DESAFIO FINAL — CLÍNICA VETERINÁRIA AuMiau")
print("=" * 80)

print("""
Agora é sua vez de repetir a jornada inteira, sozinho(a), só que com um
cenário diferente. Tente resolver cada etapa.
""")

# =====================================================================
# DADOS DO DESAFIO FINAL
# =====================================================================

dNome = {
    'PET01': 'Rex',
    'PET02': 'Mimi',
    'PET03': 'Bidu',
    'PET04': 'Fifi',
    'PET05': 'Thor'
}

dEspecie = {
    'PET01': 'Cachorro',
    'PET02': 'Gato',
    'PET03': 'Cachorro',
    'PET04': 'Gato',
    'PET05': 'Cachorro'
}

dPeso = {
    'PET01': 12,
    'PET02': 4,
    'PET03': 9,
    'PET04': 3,
    'PET05': 15
}

print("\n--- DADOS INICIAIS ---")
print("dNome:")
pprint(dNome)
print("\ndEspecie:")
pprint(dEspecie)
print("\ndPeso:")
pprint(dPeso)

print("\n" + "-" * 80)
print("ETAPA 1 — Inverta o dicionário dNome")
print("-" * 80)

print("\n✅ RESOLUÇÃO:")
dCodigoPorNome = {}

for codigo, nome in dNome.items():
    dCodigoPorNome[nome] = codigo

print("dCodigoPorNome:")
pprint(dCodigoPorNome)

print("\n" + "-" * 80)
print("ETAPA 2 — Monte o dicionário de dicionários dPets")
print("-" * 80)

print("\n✅ RESOLUÇÃO:")
dPets = {}

for codigo in dNome:
    dPets[codigo] = {
        'nome': dNome.get(codigo),
        'especie': dEspecie.get(codigo),
        'peso': dPeso.get(codigo)
    }

print("dPets:")
pprint(dPets)

print("\n--- VISUALIZAÇÃO TABELAR ---")
print("-" * 60)
print(f"{'Código':<8} {'Nome':<10} {'Espécie':<12} {'Peso (kg)':<10}")
print("-" * 60)
for codigo, dados in dPets.items():
    print(f"{codigo:<8} {dados['nome']:<10} {dados['especie']:<12} {dados['peso']:<10}")
print("-" * 60)

print("\n" + "-" * 80)
print("ETAPA 3 — Faça 2 consultas")
print("-" * 80)

print("\n--- CONSULTA 1: Pets com peso maior que 10 kg ---")
print("\n✅ RESOLUÇÃO:")
print("Pets com mais de 10 kg:")
for codigo, dados in dPets.items():
    if dados['peso'] > 10:
        print(f" {codigo}: {dados['nome']} ({dados['peso']} kg)")

print("\n--- CONSULTA 2: Pets da espécie 'Cachorro' ---")
print("\n✅ RESOLUÇÃO:")
print("Pets da espécie Cachorro:")
for codigo, dados in dPets.items():
    if dados['especie'] == 'Cachorro':
        print(f" {codigo}: {dados['nome']}")

print("\n" + "-" * 80)
print("ETAPA 4 — Inverta o dicionário de dicionários")
print("-" * 80)

print("\n--- Reindexação pelo nome (valores únicos) ---")
print("\n✅ RESOLUÇÃO:")
dPorNome = {}

for codigo, dados in dPets.items():
    nome = dados['nome']
    dPorNome[nome] = {
        'codigo': codigo,
        'especie': dados['especie'],
        'peso': dados['peso']
    }

print("dPorNome:")
pprint(dPorNome)

print("\n--- Agrupamento pela espécie (valores repetidos) ---")
print("\n✅ RESOLUÇÃO:")
dPorEspecie = {}

for codigo, dados in dPets.items():
    especie = dados['especie']
    dPorEspecie.setdefault(especie, []).append(dados['nome'])

print("dPorEspecie:")
pprint(dPorEspecie)

print("\n" + "=" * 80)
print("GABARITO DOS MINITESTES")
print("=" * 80)

print("""
Miniteste da Parte 4:
print(dJogadores.get('J4', {}).get('time', '?'))

✅ Resposta correta: alternativa (b) Trovão

O código J4 existe em dJogadores, então o primeiro .get() retorna o
dicionário interno de J4. Dentro dele, a chave 'time' vale 'Trovão'.
O apelido (a) e o próprio código (c) não são o que foi pedido, e o
valor padrão '?' (d) só apareceria se J4 não existisse.
""")

print("\n" + "=" * 80)
print("🎉 FIM DA AULA")
print("=" * 80)

