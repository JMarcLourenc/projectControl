from DatabaseP import DatabaseP
import os
import time


class Produto:
    def __init__(self):
        os.system("clear")
        print("O P E R A Ç Õ E S   C O M   P R O D U T O S\n===========================================")
        

    def cadastro(self):
        print("C A D A S T R O\n= = = = = = = =")

        #Entrada de Dados para Cadastro do Produto
        self.descricaoProdut = input("Descrição.........: ").upper()
        self.custoProdut = float(input("Valor custo.......: "))
        self.porcentagemLucr = float(input("% de lucro........: "))
        self.estoqueProdut = int(input("Estoque produto...: "))
        self.minimoEstoqueProdut = int(input("Mínimo em Estoque.: "))
        self.ativoProdut = input("Produto Ativo s/n..: ").upper()
 

    def salvarProduto(self):
        self.opcoesSalvar = int(input("\n[1]-Salvar e Cadastrar Novo Produto\n[2]-Apenas Salvar e sair\n[0]-Sair sem Salvar\n\nDigite a opção desejada.....: "))
        self.dbDadosProduto = [self.descricaoProdut, self.custoProdut, self.porcentagemLucr, self.estoqueProdut, self.minimoEstoqueProdut, self.ativoProdut, self.opcoesSalvar]
        
        match self.opcoesSalvar:
            case 1:
                #Envio dos Dados digitados
                d = DatabaseP()
                d.salvar(self.dbDadosProduto)
            case 2:
                #Envio dos Dados digitados
                d = DatabaseP()
                d.salvar(self.dbDadosProduto)
            case 0:
                os.system("clear")
                print("Você esta saindo sem salvar")
                time.sleep(4)
            case _:
                print("\n\nFavor digitar uma opção válida")
                time.sleep(3)


    def pesquisa(self):
        print("L O C A L I Z A R\n= = = = = = = = =")
        
        #Entrada de Dado para pesquisa
        self.idProdut = int(input("ID Produto........: "))

    def alterarProduto(self):
        print("\nMudar o Status do produton\n=================================")
        #Dado(s) a ser(em) alterados
        self.ativoProdut = input("Produto Ativo s/n..: ").upper()
        if self.ativoProdut == "N":
            self.ativoProdut = 0
        
 
    def operacaoProduto(self):
        self.opcoesProduto = int(input("\n\n[1]-Alterar Status do Produto\n[2]-Apagar Produto\n[0]-Sair sem Salvar\n\nDigite a opção desejada.....: "))
        

        match self.opcoesProduto:
            case 1:
                p = Produto()
                p.alterarProduto()

                self.dbDadosProduto = [self.idProdut, p.ativoProdut, self.opcoesProduto]
                d = DatabaseP()
                d.operacaoProduto(self.dbDadosProduto)
            case 2:
                self.dbDadosProduto = [self.idProdut, "", self.opcoesProduto]
                #Envio do Dados a ser pesquisado
                d = DatabaseP()
                d.operacaoProduto(self.dbDadosProduto)
            case 0:
                os.system("clear")
                print("Você esta saindo sem salvar")
                time.sleep(4)
            case _:
                print("\n\nFavor digitar uma opção válida")
                time.sleep(3)