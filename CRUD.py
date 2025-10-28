import sqlite3


connect = sqlite3.connect("produtos")
cursor = connect.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS produto(
                   id int primary key,
                   nome varchar(255),
                   valor double
               )
               '''
)

id1 = int(input("Digite o id do produto:"))
nome = input("Digite o nome do produto: ")
valor = int(input("Digite o valor do produto: "))

cursor.execute("INSERT INTO produto (id,nome,valor) VALUES (?,?,?)",(id1,nome,valor))


cursor.execute("SELECT * FROM produto")
produtos = cursor.fetchall()
print(produtos)


atualizandoProduto = "Maria"
valorAtualizado = 15

cursor.execute("UPDATE produto set nome=?, valor = ? where id=?",(atualizandoProduto,valorAtualizado,3))


cursor.execute("SELECT * FROM produto")
produtosAt = cursor.fetchall()
print(produtosAt)


cursor.execute("DELETE FROM produto where id = 11")

cursor.execute("SELECT * FROM produto")
produtosAt = cursor.fetchall()
print(produtosAt)

connect.commit()
connect.close()

