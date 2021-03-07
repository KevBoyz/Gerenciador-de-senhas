# KeyVault
## Clonando o projeto

`git clone https://github.com/KevBoyz/KeyVault.git`

##Executando o arquivo principal

`cd KeyVault\KeyVault`

`start python main.py`

## Função
KeyVault é um gerenciador de senhas simples, salva informações de login em um banco de dados
sqlite3. Os dados podem ser acessados pelo programa ou exportados para um arquivo de texto
## Requisitos
Python 3.8 ou superior

Modulo **sqlite3**, para instalar -> `pip install sqlite3`

Plugin _Database Navigator_, instale-o em seu Framework
## Como ultilizar
O programa vem com um sismples sistema de segurança, onde
uma senha principal dever ser inserida para acessa-lo.
Por padrão a senha e 'admin', você pode mudar a senha 
alterando o valor da variavel admin.
Na exportação os dados são enviados para data.txt,
arquivo presente na mesma pasta que o programa principal
