import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

'''Crie uma tabela chamada "alunos"''' 
#cursor.execute('CREATE TABLE alunos(id INTEGER PRIMARY KEY, nome VARCHAR(100), idade INT, curso VARCHAR(100))')
'''Insira pelo menos 5 registros de alunos'''
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Valentina",27,"Engenharia")')
'''a) Selecionar todos os registros da tabela "alunos".'''
#dados = cursor.execute('SELECT * FROM alunos')
#for info in dados:
#    print(info)
'''b) Selecionar o nome e a idade dos alunos com mais de 20 anos.'''
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
#for info in dados:
#    print(info)
'''c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.'''
#dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
#for info in dados:
    #print(info)
"""d) Contar o número total de alunos na tabela"""
#cursor.execute('SELECT * FROM alunos')
#print(len(cursor.fetchall()))

'''4. a) Atualize a idade de um aluno específico na tabela'''
#cursor.execute('UPDATE alunos SET idade=28 where id=1')
'''b) Remova um aluno pelo seu ID.'''
#cursor.execute('DELETE FROM alunos where id=2')
'''5. Criar uma Tabela e Inserir Dados'''
#cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY, nome VARCHAR(100), idade VARCHAR(100), saldo INT)')
#cursor.execute('INSERT INTO clientes(id,nome,idade,saldo) VALUES(4,"Caio",23,600)')
'''6 a) Selecione o nome e a idade dos clientes com idade superior a
30 anos'''
#dados=cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
#for info in dados:
#    print(info)
'''b) Calcule o saldo médio dos clientes'''
#saldos = cursor.execute('SELECT AVG(saldo) FROM CLIENTES')
#print(cursor.fetchall())
'''c) Encontre o cliente com o saldo máximo.'''
#cursor.execute('SELECT nome, MAX(saldo) FROM clientes')
#print(cursor.fetchall())

'''d) Conte quantos clientes têm saldo acima de 1000'''
#cursor.execute('SELECT * FROM clientes where saldo > 1000')
#print(len(cursor.fetchall()))

'''7 a) Atualize o saldo de um cliente específico.'''
#cursor.execute('UPDATE clientes SET saldo = 5000 WHERE id=4')
'''b) Remova um cliente pelo seu ID.'''
#cursor.execute('DELETE FROM clientes WHERE id=1')
'''8. Junção de Tabelas'''
#cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente_id INT, produto VARCHAR(50), valor INT, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')
#cursor.execute('INSERT INTO compras(id,cliente_id,produto,valor) VALUES(7,1,"pão",5)')
#cursor.execute('SELECT nome FROM clientes WHERE id IN (SELECT cliente_id FROM compras)')
#print(cursor.fetchall())




conexao.commit()
conexao.close

