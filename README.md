# 📚 Vetores e Strings — Paradigmas de Programação

> Lista de exercícios da disciplina **Paradigmas de Programação**  
> UFRPE — Unidade Acadêmica de Belo Jardim | Prof. Denini Gabriel

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Requisitos](#requisitos)
- [Como Executar](#como-executar)
- [Exercícios](#exercícios)
  - [Parte I — Vetores](#parte-i--vetores)
  - [Parte II — Strings](#parte-ii--strings)
- [Exemplos de Saída](#exemplos-de-saída)
- [Guia de Modificação](#guia-de-modificação)
- [Decisões de Implementação](#decisões-de-implementação)
- [Autor](#autor)

---

## Sobre o Projeto

Este repositório contém a solução da **Lista de Exercícios — Vetores e Strings**, desenvolvida para a disciplina de Paradigmas de Programação da UFRPE-UAB.

O objetivo da lista é praticar a implementação de funções que manipulam **listas (vetores)** e **strings** em Python, com foco em lógica de programação e construção manual de algoritmos — sem depender de funções prontas da linguagem onde o enunciado assim exige.

Todas as soluções foram implementadas como **funções puras**: recebem parâmetros, processam os dados e retornam o resultado, sem efeitos colaterais ou dependência de estado externo.

---

## Estrutura do Repositório

```
📦 vetores-e-strings/
├── 📄 lista_vetores_strings_comentado.py   # Código principal com todas as soluções comentadas
├── 📄 guia_lista_vetores_strings.txt       # Guia de uso e modificação para cada questão
└── 📄 README.md                            # Este arquivo
```

---

## Requisitos

- **Python** `3.6+`
- Nenhuma biblioteca externa necessária — apenas a biblioteca padrão do Python.

Para verificar sua versão do Python:

```bash
python --version
# ou
python3 --version
```

---

## Como Executar

**1. Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/vetores-e-strings.git
cd vetores-e-strings
```

**2. Execute o arquivo principal:**

```bash
python lista_vetores_strings_comentado.py
```

**3. A saída no terminal seguirá o formato:**

```
QUESTAO-1/SOMA_DE_ELEMENTOS
10

QUESTAO-2/CONTAR_NUMEROS_PARES
3

...
```

---

## Exercícios

### Parte I — Vetores

| # | Nome da Função | Descrição | Entrada | Saída |
|---|---|---|---|---|
| 1 | `soma_elementos(lista)` | Soma todos os elementos da lista | `[1, 2, 3, 4]` | `10` |
| 2 | `contar_pares(lista)` | Conta quantos números são pares | `[1, 2, 3, 4, 5, 6]` | `3` |
| 3 | `maior_numero(lista)` | Retorna o maior valor da lista | `[3, 7, 2, 9, 5]` | `9` |
| 4 | `contar_maiores(lista, x)` | Conta elementos estritamente maiores que X | `[1, 5, 8, 2, 10], 5` | `2` |
| 5 | `soma_pares(lista)` | Soma apenas os números pares | `[1, 2, 3, 4, 5, 6]` | `12` |
| 6 | `verificar_existencia(lista, x)` | Verifica se X existe na lista | `[4, 7, 1, 9], 7` | `True` |
| 7 | `inverter_lista(lista)` | Retorna a lista em ordem inversa (sem `reverse()`) | `[1, 2, 3, 4]` | `[4, 3, 2, 1]` |
| 8 | `contar_ocorrencias(lista, x)` | Conta quantas vezes X aparece na lista | `[1, 2, 2, 3, 2, 4], 2` | `3` |
| 9 | `soma_positivos(lista)` | Soma apenas os valores positivos | `[-1, 2, -3, 4, 5]` | `11` |
| 10 | `produto_elementos(lista)` | Retorna o produto de todos os elementos | `[1, 2, 3, 4]` | `24` |

---

### Parte II — Strings

| # | Nome da Função | Descrição | Entrada | Saída |
|---|---|---|---|---|
| 11 | `contar_vogais(s)` | Conta vogais (maiúsculas e minúsculas) | `"Programacao"` | `5` |
| 12 | `contar_caracteres(s)` | Conta caracteres sem usar `len()` | `"teste"` | `5` |
| 13 | `verificar_palindromo(s)` | Verifica se a string é palíndromo (case-insensitive) | `"arara"` | `True` |
| 14 | `contar_ocorrencias_char(s, c)` | Conta ocorrências de um caractere na string | `"banana", 'a'` | `3` |
| 15 | `substituir_caractere(s, c1, c2)` | Substitui todas as ocorrências de c1 por c2 | `"banana", 'a', 'o'` | `"bonono"` |
| 16 | `maiusculas_minusculas(s)` | Conta letras maiúsculas e minúsculas separadamente | `"AbCde"` | `Maiusculas: 2 \| Minusculas: 3` |
| 17 | `remover_espacos(s)` | Remove todos os espaços da string | `"ola mundo"` | `"olamundo"` |
| 18 | `primeiro_caractere(s)` | Retorna o primeiro caractere, ou `None` se vazia | `"python"` | `'p'` |

---

## Exemplos de Saída

Ao executar o arquivo, a saída completa esperada no terminal é:

```
QUESTAO-1/SOMA_DE_ELEMENTOS
10

QUESTAO-2/CONTAR_NUMEROS_PARES
3

QUESTAO-3/MAIOR_NUMERO
9

QUESTAO-4/CONTAR_ELEMENTOS_MAIORES_QUE_UM_VALOR
2

QUESTAO-5/SOMA_DOS_PARES
12

QUESTAO-6/VERIFICAR_EXISTENCIA_DE_ELEMENTO
True

QUESTAO-7/INVERTER_LISTA
[4, 3, 2, 1]

QUESTAO-8/CONTAR_OCORRENCIAS
3

QUESTAO-9/SOMA_DOS_VALORES_POSITIVOS
11

QUESTAO-10/PRODUTO_DOS_ELEMENTOS
24

QUESTAO-11/CONTAR_VOGAIS
5

QUESTAO-12/CONTAR_CARACTERES
5

QUESTAO-13/VERIFICAR_PALINDROMO
True
False

QUESTAO-14/CONTAR_OCORRENCIAS_DE_UM_CARACTERE
3

QUESTAO-15/SUBSTITUIR_CARACTERE
bonono

QUESTAO-16/MAIUSCULAS_E_MINUSCULAS
Maiusculas: 2 | Minusculas: 3

QUESTAO-17/REMOVER_ESPACOS
olamundo

QUESTAO-18/PRIMEIRO_CARACTERE
p
None
```

---

## Guia de Modificação

Para testar as funções com entradas diferentes, basta alterar os valores nos `print()` ao final do arquivo.

**Exemplo — alterando a questão 1:**

```python
# Valor atual
print(soma_elementos([1, 2, 3, 4]))   # saída: 10

# Modificado
print(soma_elementos([10, 20, 30]))   # saída: 60
```

**Exemplo — alterando a questão 15:**

```python
# Valor atual
print(substituir_caractere("banana", 'a', 'o'))   # saída: bonono

# Modificado
print(substituir_caractere("hello", 'l', 'r'))    # saída: herro
```

> 📄 Para um guia completo com exemplos e cuidados para cada função individualmente, consulte o arquivo [`guia_lista_vetores_strings.txt`](./guia_lista_vetores_strings.txt).

---

## Decisões de Implementação

Algumas escolhas de implementação merecem destaque:

**Sem funções prontas onde o enunciado exige**  
As questões 7 (inverter lista) e 12 (contar caracteres) foram implementadas manualmente, sem o uso de `list.reverse()`, slicing `[::-1]` ou `len()`, respeitando o enunciado original.

**Funções puras**  
Nenhuma função modifica a entrada original. Em `inverter_lista`, por exemplo, uma nova lista é criada — a original permanece intacta. O mesmo vale para as funções de string como `substituir_caractere` e `remover_espacos`.

**Palíndromo case-insensitive**  
A questão 13 converte a string para letras minúsculas antes da verificação, garantindo que `"Ana"` e `"ana"` sejam corretamente identificadas como palíndromos.

**Produto inicializado em 1**  
Na questão 10, o acumulador começa em `1` (elemento neutro da multiplicação) e não em `0`, pois `0` zeraria qualquer produto.

**Tratamento de string vazia na questão 18**  
A função `primeiro_caractere` verifica explicitamente se a string é vazia antes de acessar o índice `[0]`, evitando um `IndexError`.

---

## Autor

Desenvolvido como atividade avaliativa da disciplina de **Paradigmas de Programação**.  
UFRPE — Unidade Acadêmica de Belo Jardim | Prof. Denini Gabriel.
