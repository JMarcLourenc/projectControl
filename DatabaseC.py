import mysql.connector
import time
import os

class DatabaseC:
    def __init__(self):

        #Acesso ao Banco de Dados
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '@dm!n!23A2015',
            database = 'project_control'
        )

        
    def salvar(self,DatabaseC): 
        #Variaveis recebidas
        self.nomeCliente = DatabaseC[0]
        self.dataNascCliente = DatabaseC[1]
        self.cpfCliente = DatabaseC[2]
        self.endCliente = DatabaseC[3]
        self.complementoCliente = DatabaseC[4]
        self.bairroCliente = DatabaseC[5]
        self.cidadeCliente = DatabaseC[6]
        self.ufCliente = DatabaseC[7]
        self.cepCliente = DatabaseC[8]
        self.ativoCliente = bool(DatabaseC[9])
        self.opcaoSalvamento =  int(DatabaseC[10])

        cursor = self.conexao.cursor() # Criação de um cursor para os comandos MySQL

        #Query de ação do Banco de Dados (Adicão de dados)
        query = "INSERT INTO clientes (nomeCliente, dataNascCliente, cpfCliente, endCliente, complementoCliente, bairroCliente, cidadeCliente, ufCliente, cepCliente, ativoCliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(query, (self.nomeCliente, self.dataNascCliente, self.cpfCliente, self.endCliente, self.complementoCliente, self.bairroCliente, self.cidadeCliente, self.ufCliente, self.cepCliente, self.ativoCliente))
        self.conexao.commit()

        if self.opcaoSalvamento == 1:
            cursor.execute("SELECT id_Cliente FROM clientes WHERE nomeCliente = %s and cpfCliente = %s",(self.nomeCliente,self.cpfCliente,))         # execução do comando Select do MySQL 
            
            resultado = cursor.fetchall()

            self.id_Cliente = resultado[0]     #Obtenção de dado da Tupla
        
            self.id_Cliente_Atual = self.id_Cliente

            return(self.id_Cliente_Atual)


        elif self.opcaoSalvamento == 2:
            pass
    

    def cadastro_fone_clientes(self, db_Id_Cliente_Atual):
        os.system("clear")
        self.dbRetorno = db_Id_Cliente_Atual
        
        print("Fone Cliente\n==============================================")
        self.foneClient = input("Fone.........: ").zfill(11)[:11]  

        self.menuSalveFoneCliente=int(input("\n[1]-Salvar e Cadastrar outro Fone\n[2]-Apenas Salvar e ir para Cadostro de e-mails\n[3]-Apenas Salvar e sair\n[0]-Sair sem Salvar\n\nDigite a opção desejada.....: ")) 
        self.dadosFones = [self.foneClient, self.dbRetorno[0], self.menuSalveFoneCliente]
        match self.menuSalveFoneCliente:
            case 1:
                DatabaseC.salvar_cadastro_fone_cliente(self,self.dadosFones)
            case 2:
                DatabaseC.salvar_cadastro_fone_cliente(self,self.dadosFones)
            case 3:
                DatabaseC.salvar_cadastro_fone_cliente(self,self.dadosFones)
            case 0:
                os.system("clear")
                print("Você esta saindo sem salvar")
                time.sleep(4)
            case _:
                print("\n\n\nFavor digitar uma opção válida")
                time.sleep(5)
    

    def salvar_cadastro_fone_cliente(self,dbDadosFonesClientes):
        # Declaração de Variáveis
        #---------------------------------------------------
        self.dbFoneCliente = dbDadosFonesClientes[0]
        self.db_Id_Cliente_Atual = dbDadosFonesClientes[1]
        self.opcFone = dbDadosFonesClientes[2]

        cursor = self.conexao.cursor()  # Criação de um cursor para os comandos MySQL

        query = "INSERT INTO fonesClientes (foneCliente, cliente_id) VALUES (%s, %s)"  # Query para adição de registro
        cursor.execute(query,(self.dbFoneCliente,self.db_Id_Cliente_Atual))
        self.conexao.commit()
       
        if self.opcFone == 1:
            id_Cliente_Atual = [self.db_Id_Cliente_Atual]
            dc = DatabaseC()
            dc.cadastro_fone_clientes(id_Cliente_Atual)
        elif self.opcFone == 2:
            id_Cliente_Atual = [self.db_Id_Cliente_Atual]
            dc = DatabaseC()
            dc.cadastro_emails_cliente(id_Cliente_Atual)
        else:
            self.conexao.close()
            

    def cadastro_emails_cliente(self,db_Id_Cliente_Atual):
        os.system("clear")
        self.dbRetorno = db_Id_Cliente_Atual
        print("E-mails Cliente\n==============================================")
        self.emailClient = input("E-mails......: ").lower()


        self.menuSalveEmailCliente=int(input("\n[1]-Salvar e Cadastrar outro E-mail\n[2]-Apenas Salvar e sair\n[0]-Sair sem Salvar\n\nDigite a opção desejada.....: ")) 
        self.dadosEmail = [self.emailClient, self.dbRetorno[0], self.menuSalveEmailCliente]
        match self.menuSalveEmailCliente:
            
            case 1:
                DatabaseC.salvar_cadastro_emails_cliente(self,self.dadosEmail)
            case 2:
                DatabaseC.salvar_cadastro_emails_cliente(self,self.dadosEmail)
            case 0:
                os.system("clear")
                print("Você esta saindo sem salvar")
                time.sleep(4)
            case _:
                print("\n\n\nFavor digitar uma opção válida")
                time.sleep(5)
        

    def salvar_cadastro_emails_cliente(self, dbDadosEmailClientes):
        # Declaração de Variáveis
        #---------------------------------------------------
        self.dbEmailCliente = dbDadosEmailClientes[0]
        self.db_Id_Cliente_Atual = dbDadosEmailClientes[1]
        self.opcEmail = dbDadosEmailClientes[2]

        cursor = self.conexao.cursor()  # Criação de um cursor para os comandos MySQL
    

        query = "INSERT INTO emailsClientes (emailCliente, cliente_id) VALUES (%s, %s)"  # Query para adição de registro
        cursor.execute(query,(self.dbEmailCliente,self.db_Id_Cliente_Atual))
        self.conexao.commit()
        
        if self.opcEmail == 1:
            id_Cliente_Atual = [self.db_Id_Cliente_Atual]
            dc = DatabaseC()
            dc.cadastro_emails_cliente(id_Cliente_Atual)
        else:
            self.conexao.close()
