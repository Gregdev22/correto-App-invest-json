
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
