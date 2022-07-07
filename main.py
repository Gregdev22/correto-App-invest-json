from usuario import Usuario
from basededados import BaseDeDados
import json
from random import randint

u1=BaseDeDados()
print(u1.dados.keys())
#u1.verificar_usuario()

print('Bem vindo ao AppInvest Json \n')
resposta = input(' Já é cadastrado ? (S/N)')
if resposta == "S":
    usuario = BaseDeDados()
    usuario.verificar_usuario() # --> Quando responde S e o id de usuario não existe no dicionario, ele executa o else de verificar usuario.
    #print(usuario.dados["1"]) #--> Exibiu os dados do usuario de id "1". usuario.dados é um dicionario de todos os dados de todos usuarios.
else:
    usuario = BaseDeDados()
    usuario.cadastrar_usuario()
    # usuario.adicionar_inv()
    # usuario.visualizar_usuario()



