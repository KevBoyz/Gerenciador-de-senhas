import os


def cl(color):
    colors = {
        "r": '\033[31m',
        "g": '\033[32m',
        "o": '\033[33m',
        "b": '\033[34m',
        "p": '\033[35m',
        "b+": '\033[36m',
        "w": '\033[38m'
    }
    return colors[color]


def menu():
    print(f'''{cl("g")}
     _   __              _   _                _  _   
    | | / /             | | | |              | || |  
    | |/ /   ___  _   _ | | | |  __ _  _   _ | || |_ 
    |    \  / _ \| | | || | | | / _` || | | || || __|
    | |\  \|  __/| |_| |\ \_/ /| (_| || |_| || || |_ 
    \_| \_/ \___| \__, | \___/  \__,_| \__,_||_| \__|
                   __/ |    Version 1.3 by KevBoyz                        
                  |___/

{cl("g")}[1] {cl("b")}Salvar senha {cl("g")}         
[2] {cl("b")}Senhas existentes {cl("g")}    
[3] {cl("b")}Exportar senhas
''')


def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')
    menu()

