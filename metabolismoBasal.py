# importando biblioteca
from time import sleep


# criando funções
def imc(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        return f'IMC = {imc:.1f}. Você está abaixo do peso.'
    if 18.5 < imc < 24.9:
        return f'IMC = {imc:.1f}. Você está com o peso normal.'
    if 25 < imc < 29.9:
        return f'IMC = {imc:.1f}. Você está com sobrepeso.'
    if 30 < imc < 34.9:
        return f'IMC = {imc:.1f}. Você está com obesidade de grau 1.'
    if 35 < imc < 39.9:
        return f'IMC = {imc:.1f}. Você está com obesidade de grau 2.'
    if imc > 40:
        return f'IMC = {imc:.1f}. Você está com obesidade de grau 3.'

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[1;31mERRO! Digite um valor valido por favor.\033[m')
            continue
        else:
            return float(n)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[1;31mERRO! Digite um valor válido por favor.\033[m')
            continue
        else:
            return int(n)

def basalFeminino(peso, altura, idade):
    basal = 665.1 + (9.56 * peso) + (1.8 * altura) - (4.7 * idade)
    return f'\033[1;33m{basal:.1f}kcal\033[m'

def basalMasculino(peso, altura, idade):
    basal = 66.5 + (13.75 * peso) + (5.0 * altura) - (6.8 * idade)
    return f'\033[1;33m{basal:.1f}kcal\033[m'

def mostrarLinha():
    print('\033[1;29m---\033[m' * 15)

def menu():
    print('''\033[1;29m       -            \033[1;34mMENU\033[m            -            \033[m
\033[1;34m[ 1 ]\033[m - \033[1;29mIMC\033[m
\033[1;34m[ 2 ]\033[m - \033[1;29mTaxa de metabolismo basal feminina\033[m
\033[1;34m[ 3 ]\033[m - \033[1;29mTaxa de metabolismo basal masculina\033[m
\033[1;34m[ 4 ]\033[m - \033[1;29mSair\033[m ''')
    op = leiaInt('\033[1;29m >>> OPÇÃO: \033[m')
    while op < 1 or op > 4:
        print('\033[1;31mOPÇÂO INVALIDA! Tente novamente por favor.\033[m')
        op = leiaInt('\033[1;29m >>> OPÇÃO: \033[m')
    return op

# Cores
vermelho = '\033[1;31m'
verde = '\033[1;32m'
azul = '\033[1;34m'
ciano = '\033[1;36m'
magenta = '\033[1;35m'
amarelo = '\033[1;33m'
preto = '\033[1;30m'
cinza = '\033[1;37m'
parar = '\033[m'


# Programa Principal
while True:

    # criando interface e configurando botões
    mostrarLinha()
    opcao = menu()
    if opcao == 1:
        mostrarLinha()
        peso = leiaFloat('\033[1;34mPESO: \033[m')
        altura = leiaFloat('\033[1;34mALTURA: \033[m')
        mostrarLinha()
        print(f'\033[1;29;40m{imc(peso, altura)}\033[m')
    elif opcao == 2:
        mostrarLinha()
        peso = leiaInt('\033[1;34mPESO (em quilos): \033[m')
        altura = leiaInt('\033[1;34mALTURA (em centímetros): \033[m')
        idade = leiaInt('\033[1;34mIDADE: \033[m')
        mostrarLinha()
        print(f'\033[1;29;40mSua taxa de metabolismo basal é de {basalFeminino(peso, altura, idade)}\033[m')
    elif opcao == 3:
        mostrarLinha()
        peso = leiaInt('\033[1;34mPESO (em quilos): \033[m')
        altura = leiaInt('\033[1;34mALTURA (em centímetros): \033[m')
        idade = leiaInt('\033[1;34mIDADE: \033[m')
        mostrarLinha()
        print(f'\033[1;29;40mSua taxa de metabolismo basal é de {basalMasculino(peso, altura, idade)}\033[m')
    else:
        mostrarLinha()
        break

# encerrando programa
print('\033[1;37mEncerrando Programa...\033[m')
sleep(1)
print('\033[1;37mPrograma encerrado.\033[m')
print('\033[1;36m          <<< Volte Sempre >>> \033[m')
