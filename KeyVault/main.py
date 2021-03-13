from time import sleep
from functions import *
import sqlite3 as sql
import os

conn = sql.connect('passwords.db')
cursor = conn.cursor()
fail = 0
admin = 'admin'

os.system('cls') if os.name == 'nt' else os.system('clear')


class Passwords:

    def save(self, service='undefined', login='undefined', password='undefined'):
        cursor.execute("""
          INSERT INTO passwords (service, login, password)
          VALUES (?,?,?)
          """, (service, login, password))
        conn.commit()
        return print('''
Dados Salvos''')

    def access(self):
        print()
        cursor.execute('SELECT * FROM passwords;')
        [print(f'{cl("g")}{s} {cl("w")}== {cl("p")}{l} {cl("w")}: {cl("b+")}{p}') for s, l, p in cursor.fetchall()]
        print()

    def export(self):
        txt = open('data.txt', 'w')
        cursor.execute('SELECT * FROM passwords;')
        [txt.write(f'{s} = {l} : {p} \n') for s, l, p in cursor.fetchall()]


passwords = Passwords()

print(f'{cl("o")}[::] Insira a senha para prosseguir [::]')
print()

password(admin=admin, fail=0)

menu()
while True:
    try:
        option = int(input(f'{cl("b")}>>> '))
        if option != 1 and option != 2 and option != 3:
            print(f'{cl("r")}Erro! Informe um numero válido')
        else:
            if option == 1:
                s = input(f'{cl("g")}Serviço: ')
                l = input(f'{cl("g")}Login: ')
                p = input(f'{cl("g")}Senha: ')

                passwords.save(s, l, p)
                stop = input(f'{cl("g")}>>> ')
                clear()

            elif option == 2:
                passwords.access()
                stop = input(f'{cl("b")}>>> ')
                clear()

            elif option == 3:
                passwords.export()
                print(f'{cl("g")}Dados exportados para data.txt')
                open_file = str(input('Deseja abrir o arquivo? (S/N) ')).lower()
                if open_file:
                    os.system('start data.txt')
                stop = input(f'{cl("g")}>>> ')
                clear()
    except:
        print(f'{cl("r")}Ocorreu um erro inesperado')
        sleep(0.8)
        stop = input(f'{cl("r")}>>> ')