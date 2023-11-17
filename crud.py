import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='86275532',# senha feita quando clicou no projeto
    database='atividade',#nome do banco de dados
)
cursor = conexao.cursor() #pra iniciar o projeto
#CREATE

materia ="Ingês"
Notas = 8
Local= "instituto braga"
professor= "luara"
comando = f'INSERT INTO tarefas (materia, Notas, Local, professor) VALUES ("{materia}", {Notas}, "{Local}", "{professor}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


# mais um

materia ="Matemática"
Notas = 6
Local= "instituto braga"
professor= "vitor"
comando = f'INSERT INTO tarefas (materia, Notas, Local, professor) VALUES ("{materia}", {Notas}, "{Local}", "{professor}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#numero 3

materia ="português"
Notas = 4
Local= "instituto braga"
professor= "amélia"
comando = f'INSERT INTO tarefas (materia, Notas, Local, professor) VALUES ("{materia}", {Notas}, "{Local}", "{professor}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


# número 4

materia ="artes"
Notas = 10
Local= "instituto braga"
professor= "juliano"
comando = f'INSERT INTO tarefas (materia, Notas, Local, professor) VALUES ("{materia}", {Notas}, "{Local}", "{professor}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

#número 5

materia ="Física"
Notas = 7
Local= "instituto braga"
professor= "Carla"
comando = f'INSERT INTO tarefas (materia, Notas, Local, professor) VALUES ("{materia}", {Notas}, "{Local}", "{professor}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


#outras partes
'''
#READ
comando = f'SELECT * FROM tarefas'
cursor.execute(comando)
resultado = cursor.fetchall() 
print(resultado)

#UPDATE
materia = "inglês"
Notas = 6
Local = "instituto braga"
professor = "luara"
comando = f'UPDATE tarefas SET Notas = {Notas} WHERE materia = "{materia}"'
cursor.execute(comando)
conexao.commit()


#DELETE
materia= "inglês"
Notas= 8
Local="instituto braga"
professor="Luara"
comando = f'DELETE FROM tarefas WHERE materia = "{materia}"'
cursor.execute(comando)
conexao.commit() 
'''
cursor.close()
conexao.close()