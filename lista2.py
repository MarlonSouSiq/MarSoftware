"""
Função para definir triangulo, isso é um docstring
"""

def triangulo(x,y,z):
    if x==y and x==z and y==z:
        tri="equilatero"
    elif (x==y and x!=z) or (x==z and x!=y) or (y==z and y!=x):
        tri="Isosceles"
    elif (x!=y and x!=z and y!=z):
        tri="Escaleno"
    return tri

def num_mul_10(num):
    for x in range(1,11) :
        print(f' Numero é : { x*num} ')
    return ""    
      


"""
Função recebe um dicionario com aluno e nota
"""

def aprovados(alunos):
    for nome,nota in alunos.items():
        if nota >=6:
            print(f' Aluno {nome} Aprovado')
        else:
            print(f' Aluno {nome} Reprovado')

"""
Acrescenta os status dentro do dicionario com um sub dicionario
"""

def aprovados1(alunos):
    if not alunos:
        return "Dicioanrio vazio"
    soma_das_notas_turma=0
    for nome,nota in alunos.items():
        if nota >=6:
            alunos[nome]={"Nota":nota,"Status":"Aprovado"}
        else:
            alunos[nome]={"Nota":nota,"Status":"Reprovado"}
        soma_das_notas_turma= soma_das_notas_turma + nota
    print(soma_das_notas_turma/len(alunos))
        
    return alunos

"""
Ordenar uma lista
"""
def ordenar_lista(lista):
    #pessoas_ordenadas=sorted(lista, key=lambda x:x["Idade"]) # x é uma apelido p dicioario
    pessoas_ordenadas=sorted(lista, key=lambda x:x["Idade"],reverse=True) # x é uma apelido p dicioario
    return pessoas_ordenadas

pessoas= [
    {"Nome": "Marcelo","Idade":18},
    {"NoNe": "Matheus","Idade":22},
    {"Nome": "Arthur","Idade":9}
     ]
#print(ordenar_lista(pessoas))    


#lista_alunos={"Matheus":8, "Arthur":7, "Alessandra":5}
#lista_alunos={}
#print(aprovados1(lista_alunos))


def num_pares(lista):
    pares=[]
    par=0
    impares=0
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
            par+=1
        else:
            impares+=1
    print(f'Temos {par} números pares e {impares} impares')
    return(pares)   

lista=[3,4,6,7,9,10,12]
#print(num_pares(lista))

"""
Ver texto nas 3 ultimas posições
"""
def verifica_string(lista):
    for x in lista:
        last3=x[-3:]
        if last3=="com":
            print(f' O texto : {x} é um email')
        else:
            print(f' O texto : {x} não é email')

lista=['marlonsousiq@gmail.com',
       'Turma da monica',
       'marlonsousiq@outlook.com',
       'Mickey']

#print(verifica_string(lista))

"""
Verfica se as ultimas letras são iguais com endswith
return[email for email in emails if email.endswith(f"@{dominio_desejado}")]:::::: è um list comprehension

"""

def dsa_filtra_emails_por_dominio(emails,dominio_desejado="gmail.com"):
    return[email for email in emails if email.endswith(f"@{dominio_desejado}")]


lista=['marlonsousiq@gmail.com',
       'turmadamonica@outlook.com',
       'marlonsousiq@outlook.com',
       'mickey@gmail.com']

#print(dsa_filtra_emails_por_dominio(lista))
#print(dsa_filtra_emails_por_dominio(lista,"outlook.com"))

"""
O seguinte poderia fazer com funçaõ lambda, list comprehension
frase_modificadas=list(map(lambda f: f.upper() + "EM PYTHON", frases))
"""

def modifica_string(lista):
    lista_modificada=[]
    for frase in lista:
        lista_pas=frase.upper() + " - EM PYTHON"
        lista_modificada.append(lista_pas)
    return(lista_modificada)

lista=[
    "Hoje é um novo dia",
    "Graças a Deus",
    "Senhor, estou aqui"
]
#print(modifica_string(lista))


import random
def aposta():
    tentativa=0
    numescolhido=random.randint(1,10)
    while(tentativa < 3):
        numapostado=int(input(f'Entre com um número. Faltam {tentativa -3} chances: '))
        if numapostado>numescolhido:
            print("O numero é menor")
        elif numapostado<numescolhido:
            print("O número é maior")
        else:
            print("Voce acertou")
        tentativa += 1
    print("Acabou o jogo")


aposta()
        
