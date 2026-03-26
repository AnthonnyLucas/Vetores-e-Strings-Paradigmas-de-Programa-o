# PARTE I - VETORES

# 1. Soma de elementos
def soma_elementos(lista):
    soma = 0  
    for n in lista:  
        soma += n    
    return soma      

print("1º QUESTAO - SOMA_DE_ELEMENTOS")
print(soma_elementos([1, 2, 3, 4]))   # esperado: 10
print()

#------------------------------------------------------------------------
# 2. Contar numeros pares
def contar_pares(lista):
    cont = 0           
    for n in lista:    
        if n % 2 == 0: 
            cont += 1  
    return cont        

print("2º QUESTAO - CONTAR_NUMEROS_PARES")
print(contar_pares([1, 2, 3, 4, 5, 6]))   # esperado: 3
print()

#----------------------------------------------------------------------
# 3. Maior numero
def maior_numero(lista):
    maior = lista[0]   
    for n in lista:    
        if n > maior:  
            maior = n 
    return maior       

print("3º QUESTAO - MAIOR_NUMERO")
print(maior_numero([3, 7, 2, 9, 5]))   # esperado: 9
print()

#-------------------------------------------------------------------
# 4. Contar elementos maiores que um valor
def contar_maiores(lista, x):
    cont = 0        
    for n in lista: 
        if n > x:   
            cont += 1
    return cont

print("4º QUESTAO - CONTAR_ELEMENTOS_MAIORES_QUE_UM_VALOR")
print(contar_maiores([1, 5, 8, 2, 10], 5))   # esperado: 2 
print()

#--------------------------------------------------------------------
# 5. Soma dos pares
def soma_pares(lista):
    soma = 0           
    for n in lista:    
        if n % 2 == 0: 
            soma += n  
    return soma

print("5º QUESTAO - SOMA_DOS_PARES")
print(soma_pares([1, 2, 3, 4, 5, 6]))   # esperado: 12 
print()

#----------------------------------------------------------------------
# 6. Verificar existencia de elemento
def verificar_existencia(lista, x):
    for n in lista:  
        if n == x:   
            return True 
    return False     
 
print("6º QUESTAO - VERIFICAR_EXISTENCIA_DE_ELEMENTO")
print(verificar_existencia([4, 7, 1, 9], 7))   # esperado: True
print()
 
#-------------------------------------------------------------------------------
# 7. Inverter lista 
def inverter_lista(lista):
    nova = []                              
    for i in range(len(lista) - 1, -1, -1):
        nova.append(lista[i]) 
    return nova
 
print("7º QUESTAO - INVERTER_LISTA")
print(inverter_lista([1, 2, 3, 4]))   # esperado: [4, 3, 2, 1]
print()

#------------------------------------------------------------------------------ 
# 8. Contar ocorrencias de X na lista
def contar_ocorrencias(lista, x):
    cont = 0        
    for n in lista:
        if n == x:
            cont += 1
    return cont
 
print("8º QUESTAO - CONTAR_OCORRENCIAS")
print(contar_ocorrencias([1, 2, 2, 3, 2, 4], 2))   # esperado: 3
print()

#----------------------------------------------------------------------------------
# 9. Soma dos valores positivos
def soma_positivos(lista):
    soma = 0        
    for n in lista:
        if n > 0:  
            soma += n
    return soma
 
print("9º QUESTAO - SOMA_DOS_VALORES_POSITIVOS")
print(soma_positivos([-1, 2, -3, 4, 5]))   # esperado: 11 (2+4+5)
print()

#----------------------------------------------------------------------------------------- 
# 10. Produto dos elementos
def produto_elementos(lista):
    produto = 1    
    for n in lista: 
        produto *= n  
    return produto
 
print("10º QUESTAO - PRODUTO_DOS_ELEMENTOS")
print(produto_elementos([1, 2, 3, 4]))   # esperado: 24 
print()
 

# PARTE II - STRINGS
 
# 11. Contar vogais
def contar_vogais(s):
    vogais = "aeiouAEIOU" 
    cont = 0
    for c in s:            
        if c in vogais:    
            cont += 1
    return cont
 
print("11º QUESTAO - CONTAR_VOGAIS")
print(contar_vogais("Programacao"))   # esperado: 5
print()

#-------------------------------------------------------------------------- 
# 12. Contar caracteres 
def contar_caracteres(s):
    cont = 0      
    for _ in s: 
        cont += 1
    return cont
 
print("12º QUESTAO - CONTAR_CARACTERES")
print(contar_caracteres("teste"))   # esperado: 5
print()

#----------------------------------------------------------------------- 
# 13. Verificar palindromo 
def verificar_palindromo(s):
    s = s.lower()    
    invertida = ""   
    for i in range(len(s) - 1, -1, -1):  
        invertida += s[i]  
    return s == invertida 
 
print("13º QUESTAO - VERIFICAR_PALINDROMO")
print(verificar_palindromo("arara"))   # esperado: True  
print(verificar_palindromo("casa"))    # esperado: False
print()

#-------------------------------------------------------------------------
# 14. Contar ocorrencias de um caractere na string
def contar_ocorrencias_char(s, c):
    cont = 0
    for char in s:   
        if char == c: 
            cont += 1
    return cont

print("14º QUESTAO - CONTAR_OCORRENCIAS_DE_UM_CARACTERE")
print(contar_ocorrencias_char("banana", 'a'))   # esperado: 3
print()

#--------------------------------------------------------------------------
# 15. Substituir caractere
def substituir_caractere(s, c1, c2):
    nova = ""         
    for char in s:   
        if char == c1: 
            nova += c2 
        else:
            nova += char
    return nova

print("15º QUESTAO - SUBSTITUIR_CARACTERE")
print(substituir_caractere("banana", 'a', 'o'))   # esperado: "bonono"
print()

#--------------------------------------------------------------------------------------------
# 16. Maiusculas e minusculas
def maiusculas_minusculas(s):
    mai = 0    
    min_ = 0   
    for c in s:
        if c.isupper():    
            mai += 1
        elif c.islower():
            min_ += 1
    return f"Maiusculas: {mai} | Minusculas: {min_}" 

print("16º QUESTAO - MAIUSCULAS_E_MINUSCULAS")
print(maiusculas_minusculas("AbCde"))   # esperado: Maiusculas: 2 | Minusculas: 3
print()

#------------------------------------------------------------------------------------------
# 17. Remover espacos
def remover_espacos(s):
    nova = ""      
    for c in s:    
        if c != ' ':  
            nova += c 
    return nova  

print("17º QUESTAO - REMOVER_ESPACOS")
print(remover_espacos("ola mundo"))   # esperado: "olamundo"
print()

#--------------------------------------------------------------------------------------------
# 18. Primeiro caractere
def primeiro_caractere(s):
    if s == "":   
        return None  
    return s[0] 

print("18º QUESTAO - PRIMEIRO_CARACTERE")
print(primeiro_caractere("python"))   # esperado: 'p'
print(primeiro_caractere(""))         # esperado: None