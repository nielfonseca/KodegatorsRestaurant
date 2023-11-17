
logins={}
# a criação do login
login = input('Digite um login: ')

while True:
    senha = input('Digite uma senha: ')
    csenha = input('Confirme sua senha: ')
    if len(senha) >= 4:
        if senha == csenha: 
            logins[login] = senha
            break
        else:
            print('Senhas incompativeis')
    else:
        print('Digite uma senha com 4 ou mais digitos')
print(logins)

# confirmação de login
