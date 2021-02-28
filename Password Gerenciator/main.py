from time import sleep
from functions import *
import sqlite3 as sql


conn = sql.connect('passwords.db')
cursor = conn.cursor()

admin = 'admin'

def save():
  global temp_info
  p_domain = input(f'{clr("green")}Dominio: ')
  p_password = input(f'{clr("green")}Senha: ')

  cursor.execute("""
  INSERT INTO passwords (domain, password)
  VALUES (?,?)
  """, (p_domain, p_password))
  conn.commit()

  print()
  print(f'{clr("white")}Dados salvos')

def access():
    print(f'{clr("purple")}Senhas salvas no programa')
    print()
    cursor.execute("""
            SELECT * FROM passwords;
            """)
    for d, p in cursor.fetchall():
        print(f'{clr("green")}{d:<10} == {p:^10}')
    print()


def export():
    txt = open('data.txt', 'w')
    cursor.execute("""
                SELECT * FROM passwords;
                """)
    for d, p in cursor.fetchall():
        txt.write(f'{d} == {p}')
    print(f'{clr("green")}Dados exportados com sucesso')
    print('para o arquivo data.txt')

# Inicio do programa

title('Insira a senha para prosseguir')
while True:
    passw = str(input(f'{clr("green")}>>> '))
    sleep(0.4)
    if passw == admin:
        sleep(0.6)
        break
    else:
        print(f'{clr("red")}Senha incorreta!')
        sleep(0.4)
        continue


while True:
    menu()
    try:
        option = int(input('>>> '))
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