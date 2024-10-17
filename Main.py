from Produto import Produto
from DatabaseP import DatabaseP
import os
import time

class Main:
    def __init__(self):
        self.opcoes = {
            "1": self.opcao1,
            "2": self.opcao2,
            "3": self.opcao3,
            "0": self.sair
        }

    def mostrar_menu(self):
        os.system("clear")
        print("PROGRAMA DE CONTROLE\n====================")
        print("[1]-Cadastro de Produto\n[2]-Operações com Produto\n[3]-Listar Produtos Ativos\n[0]-Sair")

    def executar(self):
        while True:
            self.mostrar_menu()
            opcMenu = input("\n\nDigite a opção desejada....: ")
            acao = self.opcoes.get(opcMenu)

            if acao:
                acao()
            else:
                print("\n\nFavor digitar uma opção válida")
                time.sleep(3)
    
    def opcao1(self):
         p = Produto()
         p.cadastro()
         p.salvarProduto()
    
    def opcao2(self):
        p = Produto()
        p.pesquisa()
        p.operacaoProduto()
        
    def opcao3(self):
        dbDadosProduto = ["", "", 3]
        d = DatabaseP()
        d.operacaoProduto(dbDadosProduto)

    def sair(self):
        os.system("clear")
        print("\n\n=====================\n= Saindo do Sistema =\n=====================")
        time.sleep(4)
        os.system("clear")
        exit(0)


if __name__ == "__main__":
    menu = Main()
    menu.executar()


