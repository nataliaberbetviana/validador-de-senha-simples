# Importa a biblioteca para manipulação de strings e a biblioteca para operações aleatórias.
import string
import random

# Pede ao usuário para digitar uma senha
senha = input("Digite sua senha: ")

# Define as funções de validação
def tamanho_da_senha(senha):
    return len(senha) >= 8

def senha_tem_numeros (senha):
    for caractere in senha:
        if caractere in string.digits:
            return True
    return False
def senha_tem_maiusculas(senha):
    for caractere in senha:
        if caractere in string.ascii_uppercase:
            return True
    return False
def senha_tem_minusculas(senha):
    for caractere in senha:
        if caractere in string.ascii_lowercase:
            return True
    return False
def senha_tem_caracteres(senha):
    for caractere in senha:
        if caractere in string.punctuation:
            return True
    return False
def senha_tem_repeticao(senha):
    for caractere in senha:
        contador_caractere = senha.count(caractere)
        if contador_caractere > 2:
            return False
    return True

# Lógica principal para validar a senha e dar o feedback ao usuário
if senha_tem_numeros(senha) and senha_tem_maiusculas(senha) and senha_tem_caracteres(senha) and tamanho_da_senha(senha) and senha_tem_repeticao(senha) and senha_tem_minusculas(senha):
    print("Sua senha atende aos nossos critérios de segurança!")
else:
    print("Sua senha não atende aos nossos critérios de segurança")
    if not tamanho_da_senha(senha):
        print("- Precisa ter pelo menos 8 caracteres!")
    if not senha_tem_numeros(senha):
        print("- Precisa ter pelo menos um número!")
    if not senha_tem_maiusculas(senha):
        print("- Precisa ter ao menos uma letra maiuscula!")
    if not senha_tem_caracteres(senha):
        print("- Precisa ter ao menos um caractere especial!")
    if not senha_tem_minusculas(senha):
        print("- Precisa ter ao menos uma letra minuscula!")
    if not senha_tem_repeticao(senha):
        print("- Você não pode repetir mais do que duas vezes o mesmo caractere!")