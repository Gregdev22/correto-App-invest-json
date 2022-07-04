import json

class BaseDeDados():

    def __init__(self):
        with open("dados.json", "r") as file:
            dados_dict_json = file.read()  # --> Aqui é um arquivo json
            self.dados = json.loads(dados_dict_json)  # --> Aqui é um dicionario python
            print(self.dados.keys()) # --> Mostra as chaves do dicionario

    def verificar_usuario(self):
        self.id = input("Insira o id do usuario")
        if self.id in self.dados.keys():
            print(f'Exibindo dados do usuario de id {self.id}.')
            # Chamar uma função de carregar dados do usuario e/ou de alterar dados do usuario
        else:
            # Rodar ALGUMAS funções da classe BaseDeDados
            self.inserir_dados_usuario()
            self.adicionar_inv()

    def inserir_dados_usuario(self):

        self.nome = input("Insira seu nome")
        self.sobrenome = input("Insira seu sobrenome")
        self.email = input("Insira seu email")
        self.senha = input("Insira seu senha")
        # ---> Como eu chamo o id passado na função verificar usuario ?
        # R= Tive que trocar 'id' por 'self.id'. O self.id fica disponivel para uso de todas as funções da classe.

    def adicionar_inv(self):
        tipo_inv = input("insira RF ou RV")
        if tipo_inv == "RF":
            self.carteira = {}
            renda_fixa_nome = input("Insira o nome da renda fixa: CB, LCI, LCA, TESOURO")
            renda_fixa_indexador = input("Insira o indexador: IPCA, CDI, PRE")
            renda_fixa_valor = input("Insira a valor investido")
            self.dict_renda_fixa = {"tipo":tipo_inv, "nome":renda_fixa_nome,"indexador":renda_fixa_indexador,"valor":renda_fixa_valor}
            # Como adiciono um dicionario a UM dicionario? R= abaixo.
            self.carteira.update(self.dict_renda_fixa)
            self.dict_dados_usuario = {
                "Nome": self.nome,
                "Sobrenome": self.sobrenome,
                "Email": self.email,
                "id": self.id,
                "CARTEIRA": self.carteira
            }
            print(self.dict_dados_usuario)
            self.dados[self.id] = (self.dict_dados_usuario)
            print(self.dados)

            dados_json = json.dumps(self.dados, indent=True)
            with open("dados.json", "w+") as file:
                file.write(dados_json)
        else:
            self.carteira = {}
            renda_variavel_tipo = input("Insira o tipo da renda variavel: Acao, FII ou ETF")
            renda_variavel_papel = input("Insira o nome do papel")
            renda_variavel_valor = input("Insira a valor investido")
            self.dict_renda_variavel = {"Inv":tipo_inv, "tipo":renda_variavel_tipo,"papel":renda_variavel_papel, "valor":renda_variavel_valor}
            self.carteira.update(self.dict_renda_variavel)
            self.dict_dados_usuario = {
                "Nome": self.nome,
                "Sobrenome": self.sobrenome,
                "Email": self.email,
                "id": self.id,
                "CARTEIRA": self.carteira
            }
            print(self.dict_dados_usuario)
            self.dados[self.id] = (self.dict_dados_usuario)
            print(self.dados)

            dados_json = json.dumps(self.dados, indent=True)
            with open("dados.json", "w+") as file:
                file.write(dados_json)



