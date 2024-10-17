import mysql.connector
import time
import os



class DatabaseP:
    def __init__(self):

        #Acesso ao Banco de Dados
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '@dm!n!23A2015',
            database = 'project_control'
        )

    def salvar(self,DatabaseP): 
        #Variaveis recebidas
        self.descProduto = DatabaseP[0]
        self.custProduto = float(DatabaseP[1])
        self.porcLucro = float(DatabaseP[2])
        self.estProduto = int(DatabaseP[3])
        self.minEstoqueProduto = int(DatabaseP[4])
        self.ativProduto = bool(DatabaseP[5])
        self.opcaoSalvamento =  int(DatabaseP[6])

        cursor = self.conexao.cursor()

        #Query de ação do Banco de Dados (Adicão de dados)
        query = "INSERT INTO produtos (descricaoProduto, custoProduto, porcentagemProduto, estoqueProduto, minimoEstoqueProduto, ativoProduto) VALUES (%s, %s, %s, %s, %s, %s)"

        cursor.execute(query, (self.descProduto, self.custProduto, self.porcLucro, self.estProduto, self.minEstoqueProduto, self.ativProduto))
        self.conexao.commit()
        self.conexao.close()

        if self.opcaoSalvamento == 1:
            from Main import Main
            Main.opcao1(self)

    def operacaoProduto(self,DatabaseP):   
        #Variaveis recebidas
        self.idProduto = DatabaseP[0]
        self.ativProduto = bool(DatabaseP[1])
        self.operaProdutos = int(DatabaseP[2])


        if self.operaProdutos == 1:
            cursor = self.conexao.cursor()

            #Query de ação do Banco de Dados (Aleração de registro de acordo com o ID)
            query = "UPDATE produtos SET ativoProduto = %s WHERE id_produto = %s" %(self.ativProduto, self.idProduto)

            cursor.execute(query)
            
            self.conexao.commit()
            self.conexao.close()

            
        elif self.operaProdutos == 2:
            cursor = self.conexao.cursor()

            #Query de ação do Banco de Dados (Deleção de registro de acordo com o ID)
            query = "DELETE FROM produtos WHERE id_produto = %s" %(self.idProduto)

            cursor.execute(query)
            
            self.conexao.commit()
            self.conexao.close()

        elif self.operaProdutos == 3:
            cursor = self.conexao.cursor()

            #Query de ação do Banco de Dados (Deleção de registro de acordo com o ID)
            query = "SELECT id_produto, descricaoProduto, estoqueProduto FROM produtos WHERE ativoProduto = '1'"
            
            cursor.execute(query)
            relatP = cursor.fetchone()

            #Geração do relatório dos protudos ativos em tela
            os.system("clear")
            print("  Cod  |           Descrição            | Estoque \n==================================================")
            print(f"{str(relatP[0]).center(7)}| {relatP[1].ljust(30)} |{str(relatP[2]).center(9)}")
            
            #Loop de repetição de uma variável enquanto ela existir dentro do Banco de Dados
            for relatP in cursor:
                print(f"{str(relatP[0]).center(7)}| {relatP[1].ljust(30)} |{str(relatP[2]).center(9)}")
    
            time.sleep(6)
            self.conexao.close()    #Fechamento da conexão com o Banco de Dados

            



        


    


