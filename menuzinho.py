import pandas as pd


medicos_autorizados = {
    'Thabata Andes': 'esqueciasenha',
    'Luiz Carlos': 'souomelhor'
}

def verifica_login():
    nome_medico = input("Digite seu nome de usuário: ")
    senha_medico = input("Digite sua senha: ")

    if nome_medico in medicos_autorizados and medicos_autorizados[nome_medico] == senha_medico:
        print(f'Login bem-sucedido! Seja bem-vindo/a {nome_medico}')
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False



def verifica_resposta(msg,opcoes,msg_erro=None):
    resp = input(msg)
    while resp not in opcoes:
        print('Opção inválida!')
        if msg_erro:
            print(msg_erro) 
        resp = input(msg)
    return resp

def pega_indice(msg):
    opcoes = pacientes['Nome']
    nomes_pacientes = verifica_resposta(msg,opcoes,'\n'.join(opcoes))
    local = indices[nomes_pacientes]
    return local

def create():
    
    for key in pacientes.keys():
        info = input(f'Diga o/a novo/a {key}: ')
        pacientes[key].append(info)
    print('Paciente computado com sucesso:')
    print(pd.DataFrame(pacientes))
    return create

def remove():
    local = pega_indice('Qual paciente você quer remover?: ')
    for key in pacientes.keys():
        pacientes[key].pop(local)
    print('Paciente removido com sucesso:')
    print(pd.DataFrame(pacientes))
    return remove

def update():
    local = pega_indice('Qual paciente você quer atualizar?: ')
    for key in pacientes.keys():
        info = input(f'Diga o novo {key}: ')
        pacientes[key][local] = info
    print('Paciente atualizado com sucesso:')
    print(pd.DataFrame(pacientes))
    return update

def read():
    
    local = pega_indice('Qual paciente você quer ver?: ')
    for key in pacientes.keys():
        print(pacientes[key][local])
    return read


def cria_indices(): 
    pacientes_hospital = pacientes['Nome']
    global indices
    indices = {pacientes_hospital[i] : i for i in range(len(pacientes_hospital))}
    return


while True:
    if verifica_login():
        break

print("Sistema de gerenciamento de pacientes...")

pacientes = {
    'Nome' : ['Danilo Elias de Assis Neto','Beatriz Dantas Sampaio','Zion Hughes','Mael Rodrigues','Melissa Trinidad'],
    'Sexo' : ['Masculino','Feminino','Masculino','Masculino','Feminino'],
    'Idade' : ['13','5','10','8','6'],
    'Altura' : [172,130,170,130,100],
    'Último Procedimento' : ['Biópsia','Eletroencefalograma','Cirurgia Cardíaca','Radiografia','Exame de urina']
}



cria_indices() 

while True:
    opcoes = ['Cadastrar','Remover','Atualizar','Ler','Sair']
    opcao = verifica_resposta('O que deseja fazer hoje?: ',opcoes,'\n'.join(opcoes))
    if opcao == opcoes[0]:
        create()
        cria_indices()
    elif opcao == opcoes[1]:
        remove()
        cria_indices()
    elif opcao == opcoes[2]:
        update()
    elif opcao == opcoes[3]:
        read()
    else:
        print('Beijo me liga')
        break