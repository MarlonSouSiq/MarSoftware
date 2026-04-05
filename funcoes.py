def dsa_saudacao(nome, saudacao="ola"):  # saudação com valor padrao ola, se chamar na função sobescreve
    print(f" {saudacao} {nome}")
          

def dsa_soma_numeros(*args):   # com *args quando não souber o numeo de argumentos que virá
    total=0
    for numeros in args:
        total += numeros
    return total

def dsa_exibe_info(**kwargs):  # argumento é um dicionario qualquer
    print("\n Infornmação da pessoa\n")
    for chave, valor in kwargs.items():
        print(f' - {chave}: {valor}')
    

dsa_saudacao("Maria")
dsa_saudacao("Maria","Oi")  
print (dsa_soma_numeros(1,2,3,4))

dsa_exibe_info(nome="Carla", Profissao="Engenheira",Hobby="Leitura")
dsa_exibe_info(nome="Jose", Profissao="Gerente")