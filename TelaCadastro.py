import sqlite3

# Declaração de Variáveis
fimloop1 = 0
fimloop2 = 0

# Início do Programa
print("Olá, bem vindo a tela de login da FEMA!")
initchoice = int(input("Digite 1 para fazer login e 2 para se cadastrar: "))

# Início da Lógica do Login
if initchoice == 1:
    while fimloop1 == 0:

        # Coleta de Dados
        ra = int(input("Digite seu RA: "))
        senha = str(input("Digite sua senha: "))

        # Verificação de Segurança
        try:
            conn = sqlite3.connect("FemaDB.db")
            cursor = conn.cursor()

            cursor.execute(f"SELECT ra, senha FROM alunos WHERE ra = {ra}")
            result = cursor.fetchone()
            
            # Resultado da verificação
            if result:
                ra_db, senha_db = result
                
                # if de entrada positiva
                if ra == ra_db and senha == senha_db:
                    cursor.execute(f"SELECT nome FROM alunos WHERE ra = {ra}")
                    nome = cursor.fetchone()
                    nomeformatado = ''.join(map(str, nome[0]))

                    print(f"Você está logado como: {nomeformatado}")
                    
                    logchoice = int(input("Digite 1 para conferir suas matérias e 2 para sair: "))
                    
                    if logchoice == 1:

                        # Realizando a consulta do curso do aluno dentro da DB
                        cursor.execute(f"SELECT curso FROM alunos WHERE ra = {ra}")
                        curso_aluno = cursor.fetchall()
                        cformatado = ''.join(map(str, curso_aluno[0]))

                        # Selecionando as matérias do curso, baseando-se na consulta acima
                        cursor.execute(f"SELECT materia1, materia2, materia3, materia4, materia5, materia6, materia7 FROM cursos WHERE nome_curso = '{cformatado}'")
                        materias = cursor.fetchall()

                        # Printando as materias de maneira organizada e limpa para o usuário
                        print("Suas matérias são: ")
                        for materia in materias:
                            mformatada = '\n'.join(map(str, materias[0]))
                            print(mformatada)

                        # Finalizando
                        print(f"\nSeja bem vindo a FEMA {nomeformatado}! Finalizando conexão.")
                        fimloop1 = 1

                    # IF 
                    elif logchoice == 2:
                        print("Finalizando.")
                        conn.close()
                        fimloop1 = 1
                    
                    else:
                        print("Comando inválido, finalizando.")
                        conn.close()
                        fimloop1 = 1

            # Entrada negativa
            else:
                print("RA ou senha inválidos. Tente novamente!")


        # Tratamento de Erros
        except sqlite3.Error as error:
            print("Ocorreu um erro: ", error)