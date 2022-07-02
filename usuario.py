from basededados import BaseDeDados

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


