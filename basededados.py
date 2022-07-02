class BaseDeDados():
    def __init__(self):
        self.dados = {}

    def inserir_dados_usuario(self):

        self.carteira = {}
        self.nome = input("Insira seu nome")
        self.sobrenome = input("Insira seu sobrenome")
        self.email = input("Insira seu email")
        self.senha = input("Insira seu senha")
        self.id = input("Insira seu id")
        self.dict_dados_usuario = {
            "Nome":self.nome,
            "Sobrenome":self.sobrenome,
            "Email":self.email,
            "id":self.id
        }
        self.dados.update(self.dict_dados_usuario)

    def adicionar_inv(self):
        tipo_inv = input("insira RF ou RV")
        if tipo_inv == "RF":
            self.carteira = {}
            renda_fixa_nome = input("Insira o nome da renda fixa: CB, LCI, LCA, TESOURO")
            renda_fixa_indexador = input("Insira o indexador: IPCA, CDI, PRE")
            renda_fixa_valor = input("Insira a valor investido")
            self.dict_renda_fixa = {"tipo":tipo_inv, "nome":renda_fixa_nome,"indexador":renda_fixa_indexador,"valor":renda_fixa_valor}
            #self.dict_renda_fixa.update({"tipo":tipo_inv, "nome":renda_fixa_nome,"indexador":renda_fixa_indexador,"valor":renda_fixa_valor})
            # Como adiciono um dicionarios ao dicionario carteira da classe usuario? R= abaixo.
            self.carteira.update(self.dict_renda_fixa)
            self.dict_carteira = {"Carteira": self.carteira}
            self.dados.update(self.dict_carteira)  # esse dicionario deve ficar separado das demais info do usuario
            print(self.carteira)
            print(self.dados)
        else:
            self.carteira = {}
            renda_variavel_tipo = input("Insira o tipo da renda variavel: Acao, FII ou ETF")
            renda_variavel_papel = input("Insira o nome do papel")
            renda_variavel_valor = input("Insira a valor investido")
            self.dict_renda_variavel = {"Inv":tipo_inv, "tipo":renda_variavel_tipo,"papel":renda_variavel_papel, "valor":renda_variavel_valor}
            # Como adiciono um dicionarios ao dicionario carteira da classe usuario? R= abaixo.
            self.carteira.update(self.dict_renda_variavel)
            self.dict_carteira = {"Carteira": self.carteira}
            self.dados.update(self.dict_carteira) # esse dicionario deve ficar separado das demais info do usuario
            print(self.carteira)
            print(self.dados)



