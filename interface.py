import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    dbname = 'academia',
    user = 'postgres',
    password = 'admin',
    port = 5432
)

cursor = connection.cursor()

def historico_aluno():
    print("Digite o cpf do aluno desejado, ou 0 para cancelar:")
    cpf = input()
    if cpf == "0":
        return
    else:
        command = """SELECT * FROM TREINO WHERE ALUNOCPF='""" + cpf + """'"""
        cursor.execute(command)
        print("ID, DATA, CPFALUNO, CPFINSTRUTOR")
        print(cursor.fetchall())

def alunos_de_instrutor():
    print("Digite o cpf do instrutor desejado, ou 0 para cancelar")
    cpf = input()
    if cpf == "0":
        return
    else:
        command = """SELECT PNOME, MNOME, SNOME FROM ALUNO JOIN AUXILIA ON CPFALUNO = CPF WHERE CPFINSTRUTOR ='""" + cpf + """'"""
        cursor.execute(command)
        print(cursor.fetchall())

def todos_alunos():
    command = "SELECT * FROM ALUNO"
    cursor.execute(command)
    list = cursor.fetchall()
    print("PNOME, MNOME, SNOME, DATANASC, CPF, TELEFONE")
    print(list)

def todos_instrutores():
    command = "SELECT * FROM INSTRUTOR"
    cursor.execute(command)
    print("PNOME, MNOME, SNOME, CPF, SALARIO, TELEFONE")
    print(cursor.fetchall())

def progresso_aluno():
    print("Digite o cpf do aluno desejado, ou 0 para cancelar")
    cpf = input()
    if cpf == "0":
        return
    else:
        command = """SELECT NOME, MUSCULOFOCO, PESO, REPETICOES FROM USOEQUIPAMENTOS U JOIN TREINO T ON U.TREINOID = T.ID WHERE ALUNOCPF ='""" + cpf + """'"""
        cursor.execute(command)
        print("EQUIPAMENTO, MUSCOLO FOCO, PESO, REPETICOES")
        print(cursor.fetchall())

def horarios_aluno():
    print("Digite o cpf do aluno desejado, ou 0 para cancelar")
    cpf = input()
    if cpf == "0":
        return
    else:
        command = """SELECT SEGUNDA,TERCA,QUARTA,QUINTA,SEXTA FROM HORARIOS WHERE ALUNOCPF ='""" + cpf + """'"""
        cursor.execute(command)
        print("SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA")
        print(cursor.fetchall())

def horarios_alunos_instrutor():
    print("Digite o cpf do instrutor desejado, ou 0 para cancelar")
    cpf = input()
    if cpf == "0":
        return
    else:
        command = """SELECT SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA FROM INSTRUTOR JOIN
        AUXILIA ON CPFINSTRUTOR = CPF JOIN HORARIOS ON CPFALUNO = ALUNOCPF WHERE CPFINSTRUTOR ='""" + cpf + """'"""
        cursor.execute(command)
        print("SEGUNDA, TERCA, QUARTA, QUINTA, SEXTA")
        print(cursor.fetchall())

def pagamentos_alunos_instrutor():
    print("Digite o cpf do instrutor desejado, ou 0 para cancelar")
    cpf = input()
    if cpf == "0":
        return
    else:
        command = """SELECT CODIGO, VALOR, DATA, ALUNOCPF FROM INSTRUTOR JOIN
        AUXILIA ON CPFINSTRUTOR = CPF JOIN PAGAMENTO ON ALUNOCPF = CPFALUNO WHERE CPFINSTRUTOR ='""" + cpf + """'"""
        cursor.execute(command)
        print("CODIGO, VALOR, DATA, CPFALUNO")
        print(cursor.fetchall())

def print_menu():
    print("0. Sair")
    print("1. Consultar progresso de algum aluno")
    print("2. Consultar nomes dos alunos de um instrutor")
    print("3. Consultar historico de treinos de algum aluno")
    print("4. Consultar horários de algum aluno")
    print("5. Consultar horários dos alunos de algum instrutor")
    print("6. Consultar pagamentos dos alunos de algum instrutor")
    print("7. listar todos os dados dos alunos")
    print("8. listar todos os dados dos instrutores")

def main_loop():
    print_menu()
    user_input = input()
    match user_input:
        case "0":
            connection.close()
            cursor.close()
        case "1":
            progresso_aluno() # com join
            main_loop()
        case "2":
            alunos_de_instrutor() # com join
            main_loop()
        case "3":
            historico_aluno() # sem join
            main_loop()
        case "4":
            horarios_aluno() # sem join
            main_loop()
        case "5":
            horarios_alunos_instrutor() # com join
            main_loop()
        case "6":
            pagamentos_alunos_instrutor() # com join
            main_loop()
        case "7":
            todos_alunos() # sem join
            main_loop()  
        case "8":
            todos_instrutores() # sem join
            main_loop()    
   

print("Bem vindo ao banco de dados de uma academia.")
main_loop()