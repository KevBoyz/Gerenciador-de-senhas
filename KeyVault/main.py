from time import sleep
from functions import *
import sqlite3 as sql
import os

conn = sql.connect('database.db')
cursor = conn.cursor()
fail = 0
admin = 'admin'

os.system('cls') if os.name == 'nt' else os.system('clear')


def save(log=False):
    if log:
        cursor.execute('INSERT INTO security_log (date) VALUES (?)', [get_time()])
        conn.commit()
        return
    s = input(f'{cl("g")}Serviço: ')
    l = input(f'{cl("g")}Login: ')
    p = input(f'{cl("g")}Senha: ')
    cursor.execute('INSERT INTO passwords (service, login, password) VALUES (?,?,?)', (s, l, p))
    conn.commit()
    print('''
Dados salvos''')
    stop = input(f'{cl("g")}>>> ')
    clear()


def access(log=False):
    if log:
        print()
        cursor.execute('SELECT * FROM security_log;')
        [print(f'{cl("b+")}{i} : {d}') for i, d in cursor.fetchall()]
        print()
        return
    print()
    cursor.execute('SELECT * FROM passwords;')
    [print(f'{cl("g")}{s} {cl("w")}== {cl("p")}{l} {cl("w")}: {cl("b+")}{p}') for s, l, p in cursor.fetchall()]
    print()
    stop = input(f'{cl("g")}>>> ')
    clear()


def export():
    txt = open('data.txt', 'w')
    cursor.execute('SELECT * FROM passwords;')
    [txt.write(f'{s} = {l} : {p} \n') for s, l, p in cursor.fetchall()]
    stop = input(f'{cl("g")}>>> ')
    clear()


print(f'{cl("o")}[::] Insira a senha para prosseguir [::]')
print()

password(admin=admin, fail=0)
save(log=True)

menu()
while True:
    try:
        option = int(input(f'{cl("b")}>>> '))
        if option != 1 and option != 2 and option != 3 and option != 4 and option != '':
            print(f'{cl("r")}Erro! Informe um numero válido')
        else:
            if option == 1:
                save()
            elif option == 2:
                access()
            elif option == 3:
                export()
                print(f'{cl("g")}Dados exportados para data.txt')
                open_file = str(input('Deseja abrir o arquivo? (S/N) ')).lower()
                if open_file:
                    os.system('start data.txt')
            elif option == 4:
                while True:
                    clear_sysrq()
                    security_menu()
                    option = int(input(f'{cl("b")}>>> '))
                    if option != 1 and option != 2:
                        print(f'{cl("r")}Erro! Informe um numero válido')
                    else:
                        if option == 1:
                            access(log=True)
                            stop = input(f'{cl("g")}>>> ')
                            continue
                        elif option == 2:
                            clear()
                            break
    except:
        print(f'{cl("r")}Ocorreu um erro inesperado')
        sleep(0.8)
        stop = input(f'{cl("r")}>>> ')