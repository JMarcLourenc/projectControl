from DatabaseC import DatabaseC
import os
import time


class Cliente:
    def __init__(self):
        os.system("clear")
        print("O P E R A Ç Õ E S   C O M   C L I E N T E S\n===========================================")
        

    def cadastro(self):
        print("C A D A S T R O\n= = = = = = = =")

        #Entrada de Dados para Cadastro do Cliente
        self.nomeClient = input("Nome.........: ").upper()
        self.dataNascClient = input("Data nasc....: ").zfill(8)[:8]
        self.dataNascClie = '{}-{}-{}'.format(self.dataNascClient[4:], self.dataNascClient[2:4], self.dataNascClient[:2])  #Mascara para data
        self.cpfClient = input("CPF..........: ").zfill(11)[:11]
        self.endClient = input("Endereço.....: ").upper()
        self.complementClient = input("Complemento..: ").upper()
        self.bairroClient = input("Bairro.......: ").upper()
        self.cidadeClient = input("Cidade.......: ").upper()
        self.ufClient = input("UF...........: ").upper().zfill(2)[:2]
        self.cepClient = input("CEP..........: ").upper().zfill(8)[:8]
        self.ativoClient = input("Cliente Ativo s/n..: ").upper()

        if self.ufClient != "":
            self.ufClient = self.ufClient
        else:
            self.ufClient = "SP"

    def salvarCliente(self):
        print("\n[1]-Salvar e cadastrar o Fone\n[2]-Apenas salvar e retornar ao menu principal\n[0]-Sair sem salvar")
        self.opcao = int(input("\nDigite a opção desejada........: "))
        self.dbDadosCliente = [self.nomeClient, self.dataNascClie, self.cpfClient, self.endClient, self.complementClient, self.bairroClient, self.cidadeClient, self.ufClient, self.cepClient, self.ativoClient, self.opcao]

        match self.opcao:
            case 1:
                #Envio dos Dados digitados
                dc = DatabaseC()
                dc.salvar(self.dbDadosCliente)
                dc.cadastro_fone_clientes(dc.id_Cliente_Atual)

            case 2:
                #Envio dos Dados digitados
                dc = DatabaseC()
                dc.salvar(self.dbDadosCliente)

            case 0:
                os.system("clear")
                print("Você esta saindo sem salvar")
                time.sleep(4)

            case _:
                print("\n\nFavor digitar uma opção válida")
                time.sleep(3)