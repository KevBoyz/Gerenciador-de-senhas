from time import sleep
from functions import *
import sqlite3 as sql

conn = sql.connect('passwords.db')
cursor = conn.cursor()
admin = 'admin'
fail = 0

def save():
    p_attribute = input(f'{clr("green")}Atributo: ')
    p_login = input(f'{clr("green")}Login: ')
    p_password = input(f'{clr("green")}Senha: ')


    cursor.execute("""
  INSERT INTO passwords (atribute, login, password)
  VALUES (?,?,?)
  """, (p_attribute, p_login, p_password))
    conn.commit()

    print()
    print(f'{clr("white")}Dados salvos')


def access():
    print(f'''{clr("orange")}Senhas salvas
    ''')
    cursor.execute("""
            SELECT * FROM passwords;
            """)
    [print(f'{clr("green")}{a} {clr("white")}== {clr("purple")}{l} {clr("white")}: {clr("blue+")}{p}') for a, l, p in cursor.fetchall()]
    print()


def export():
    txt = open('data.txt', 'w')
    cursor.execute("""
                SELECT * FROM passwords;
                """)
    [txt.write(f'{a} == {l} : {p} | ') for a, l, p in cursor.fetchall()]
    print()
    print(f'{clr("green")}Dados exportados com sucesso para data.txt')


print(f'{clr("orange")}[::] Insira a senha para prosseguir [::]')
print()
while True:
    passw = str(input(f'{clr("green")}>>> '))
    if passw == admin:
        if admin == 'admin':
            print(f'{clr("red")}Aviso! Você está ultilizando a senha padrão!')
            print('Troque a imediatamente para sua segurança')
        break
    else:
        print(f'{clr("red")}Senha incorreta!')
        fail += 1
        if fail > 3:
            print(f'{clr("red")}Senha errada varias vezes, espere 10 segundos e tente novamente')
            sleep(10)
        continue


print(f'''{clr("green")}
 _   __              _   _                _  _   
| | / /             | | | |              | || |  
| |/ /   ___  _   _ | | | |  __ _  _   _ | || |_ 
|    \  / _ \| | | || | | | / _` || | | || || __|
| |\  \|  __/| |_| |\ \_/ /| (_| || |_| || || |_ 
\_| \_/ \___| \__, | \___/  \__,_| \__,_||_| \__|
               __/ |    Version 1.1 by KevBoyz                        
              |___/''')

menu()
while True:
    try:
        option = int(input(f'{clr("blue")}>>> '))
        if option != 1 and option != 2 and option != 3:
            print(f'{clr("red")}Erro! Informe um numero válido')
        else:
            if option == 1:
                sleep(0.4)
                save()
            elif option == 2:
                sleep(0.5)
                access()
            elif option == 3:
                sleep(0.4)
                export()
    except:
        print(f'{clr("red")}Ocorreu um erro inesperado')
        sleep(0.8)