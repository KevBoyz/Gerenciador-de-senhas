from time import sleep
from functions import *
import sqlite3 as sql

conn = sql.connect('passwords.db')
cursor = conn.cursor()
admin = 'admin'
fail = 0

def save():
    p_attribute = input(f'{cl("g")}Atributo: ')
    p_login = input(f'{cl("g")}Login: ')
    p_password = input(f'{cl("g")}Senha: ')
    print()
    cursor.execute("""
  INSERT INTO passwords (atribute, login, password)
  VALUES (?,?,?)
  """, (p_attribute, p_login, p_password))
    conn.commit()

    print(f'{cl("w")}Dados salvos')


def access():
    print(f'''{cl("o")}Senhas salvas
    ''')
    cursor.execute("""
            SELECT * FROM passwords;
            """)
    [print(f'{cl("g")}{a} {cl("w")}== {cl("p")}{l} {cl("w")}: {cl("b+")}{p}') for a, l, p in cursor.fetchall()]
    print()


def export():
    txt = open('data.txt', 'w')
    cursor.execute("""
                SELECT * FROM passwords;
                """)
    [txt.write(f'{a} == {l} : {p} | ') for a, l, p in cursor.fetchall()]
    print()
    print(f'{cl("g")}Dados exportados com sucesso para data.txt')


print(f'{cl("o")}[::] Insira a senha para prosseguir [::]')
print()

password(admin=admin, fail=0)

print(f'''{cl("g")}
 _   __              _   _                _  _   
| | / /             | | | |              | || |  
| |/ /   ___  _   _ | | | |  __ _  _   _ | || |_ 
|    \  / _ \| | | || | | | / _` || | | || || __|
| |\  \|  __/| |_| |\ \_/ /| (_| || |_| || || |_ 
\_| \_/ \___| \__, | \___/  \__,_| \__,_||_| \__|
               __/ |    Version 1.2 by KevBoyz                        
              |___/''')

menu()
while True:
    try:
        option = int(input(f'{cl("b")}>>> '))
        if option != 1 and option != 2 and option != 3:
            print(f'{cl("r")}Erro! Informe um numero válido')
        else:
            if option == 1:
                save()
            elif option == 2:
                access()
            elif option == 3:
                export()
    except:
        print(f'{cl("r")}Ocorreu um erro inesperado')
        sleep(0.8)