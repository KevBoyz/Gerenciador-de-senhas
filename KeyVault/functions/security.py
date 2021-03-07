from time import sleep

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

def password(admin, fail):
    while True:
        passw = str(input(f'{cl("g")}>>> '))
        if passw == admin:
            if admin == 'admin':
                print(f'{cl("r")}Aviso! Você está ultilizando a senha padrão!')
                print('Troque a imediatamente para sua segurança')
            break
        else:
            print(f'{cl("r")}Senha incorreta!')
            fail += 1
            if fail > 3:
                print(f'{cl("r")}Senha errada varias vezes, espere 10 segundos e tente novamente')
                sleep(10)
            continue
