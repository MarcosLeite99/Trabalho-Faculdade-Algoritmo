import sqlite3
connect = sqlite3.connect("Gestão de Estoque")
cursor = connect.cursor()
cursor.execute('''
    Create table if not exist product(
               id int primary key,
               nome varchar (255),
               quantidade int, 
               validade varchar(255))
               
''')
cursor.commit()
print('''
Bem Vindo Ao Sistema de Gestão de Estoque!!!
    Menu:
      1-adicionar produto
      2-remover produto
      3-consultar
      0-Voltar ao Menu Inicial

      ''')
opcaomenu = input("Digite uma opção do Menu")