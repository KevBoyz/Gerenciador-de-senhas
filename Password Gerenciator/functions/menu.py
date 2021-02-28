def clr(color):
    colors = {
        "red": '\033[31m',
        "green": '\033[32m',
        "orange": '\033[33m',
        "blue": '\033[34m',
        "purple": '\033[35m',
        "blue+": '\033[36m',
        "white": '\033[38m'
    }
    return colors[color]

def title(txt):
    print(f'''{clr("white")}{'-'*40}
{txt:^40}
{'-'*40}''')


def menu():
    title('Menu Principal')
    print(f'''{clr("green")} 1 - {clr("blue")}Salvar senha
{clr("green")} 2 - {clr("blue")}Conferir senhas salvas
{clr("green")} 3 - {clr("blue")}Exportar senhas em formato txt
{clr("white")}{'-'*40}''')
