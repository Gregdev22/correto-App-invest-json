import json
from random import randint

class BaseDeDados():

    def __init__(self):
        with open("dados.json", "r") as file:
            dados_dict_json = file.read()  # --> Aqui é um arquivo json
            self.dados = json.loads(dados_dict_json)  # --> Aqui é um dicionario python
            #print(self.dados.keys()) # --> Mostra as chaves do dicionario

    def verificar_usuario(self):
        self.id = input("Insira o id do usuario")
        senha = input("Insira sua senha")
        # --> Confere se o id está no dicionario e a senha do usuario está correta.
        if self.id not in self.dados.keys() or senha not in self.dados[self.id]['senha']:
            print("senha ou usuario invalido")
            self.verificar_usuario() # --> Retorna para a função.
        else:
            print(f'usuario {self.dados[self.id]["Nome"]} {self.dados[self.id]["Sobrenome"]} logado.')
            self.visualizar_usuario()  # Chamar uma função de carregar dados do usuario e/ou de alterar dados do usuario
            # self.dados[self.id]['senha'] # -- lOCALIZAÇÃO DA CHAVE 'senha' dentro do dicionario.
            # usuario = Usuario()
            # usuario.adicionar_renda_fixa()


    def cadastrar_usuario(self):

        self.id = randint(1,30)
        while str(self.id) in self.dados.keys():
            variavel = ("Usuario ja existe")
        else:
            pass
        self.carteira = {}
        self.nome = input("Insira seu nome")
        self.sobrenome = input("Insira seu sobrenome")
        self.email = input("Insira seu email")
        self.senha = input("Insira seu senha")
        self.dict_dados_usuario = {
        "Nome": self.nome,
        "Sobrenome": self.sobrenome,
        "Email": self.email,
        "id": self.id,
        "CARTEIRA": self.carteira,
        "senha":self.senha
        }
        self.dados[self.id] = (self.dict_dados_usuario)
        dados_json = json.dumps(self.dados, indent=True)
        with open("dados.json", "w+") as file:
            file.write(dados_json)
        print('Usuario cadastrado com sucesso.')
        # ---> Como eu chamo o id passado na função verificar usuario ?
        # R= Tive que trocar 'id' por 'self.id'. O self.id fica disponivel para uso de todas as funções da classe.

    def visualizar_usuario(self):
        dados_usuario_logado = {
        "Nome": self.dados[self.id]["Nome"],
        "Sobrenome": self.dados[self.id]["Sobrenome"],
        "Email": self.dados[self.id]["Email"],
        "id": self.dados[self.id]["id"],
        "CARTEIRA": self.dados[self.id]["CARTEIRA"],
        }
        #print(self.dados[self.id])
        print(dados_usuario_logado)

class Usuario():
    # Aqui eu tenho que importar da base de dados salva em json.

    def mostrar_usuario(self):
        print(self.id,self.nome, self.sobrenome, self.email)

    def adicionar_renda_fixa(self):
        self.dict_renda_fixa = {}
        renda_fixa = input("Insira a renda fixa")
        self.dict_renda_fixa.update({"CDB":renda_fixa})
        # Como adiciono um dicionarios ao dicionario carteira da classe usuario? R= abaixo.
        self.carteira.update({"RF":self.dict_renda_fixa})

    # def adicionar_inv(self):
    #     tipo_inv = input("insira RF ou RV")
    #     if tipo_inv == "RF":
    #         self.carteira = {}
    #         renda_fixa_nome = input("Insira o nome da renda fixa: CB, LCI, LCA, TESOURO")
    #         renda_fixa_indexador = input("Insira o indexador: IPCA, CDI, PRE")
    #         renda_fixa_valor = input("Insira a valor investido")
    #         self.dict_renda_fixa = {"tipo":tipo_inv, "nome":renda_fixa_nome,"indexador":renda_fixa_indexador,"valor":renda_fixa_valor}
    #         # Como adiciono um dicionario a UM dicionario? R= abaixo.
    #         self.carteira.update(self.dict_renda_fixa)
    #         self.dict_dados_usuario = {
    #             "Nome": self.nome,
    #             "Sobrenome": self.sobrenome,
    #             "Email": self.email,
    #             "id": self.id,
    #             "CARTEIRA": self.carteira
    #         }
    #         #print(self.dict_dados_usuario)
    #         self.dados[self.id] = (self.dict_dados_usuario)
    #         #print(self.dados)
    #
    #         dados_json = json.dumps(self.dados, indent=True)
    #         with open("dados.json", "w+") as file:
    #             file.write(dados_json)
    #     else:
    #         self.carteira = {}
    #         renda_variavel_tipo = input("Insira o tipo da renda variavel: Acao, FII ou ETF")
    #         renda_variavel_papel = input("Insira o nome do papel")
    #         renda_variavel_valor = input("Insira a valor investido")
    #         self.dict_renda_variavel = {"Inv":tipo_inv, "tipo":renda_variavel_tipo,"papel":renda_variavel_papel, "valor":renda_variavel_valor}
    #         self.carteira.update(self.dict_renda_variavel)
    #         self.dict_dados_usuario = {
    #             "Nome": self.nome,
    #             "Sobrenome": self.sobrenome,
    #             "Email": self.email,
    #             "id": self.id,
    #             "CARTEIRA": self.carteira
    #         }
    #         #print(self.dict_dados_usuario)
    #         self.dados[self.id] = (self.dict_dados_usuario)
    #         #print(self.dados)
    #
    #         dados_json = json.dumps(self.dados, indent=True)
    #         with open("dados.json", "w+") as file:
    #             file.write(dados_json)