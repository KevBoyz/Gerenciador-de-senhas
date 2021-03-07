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
    print()
    print(f'''{cl("g")}[1] {cl("b")}Salvar senha {cl("g")}         
[2] {cl("b")}Senhas existentes {cl("g")}    
[3] {cl("b")}Exportar senhas''')



