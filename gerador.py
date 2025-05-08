import random
import string

def password_generator(Len_pass=8):   #parametro escolhido len, tamanho, maioria dos sites usando 8 caracteres
    if Len_pass < 3:
        return "A senha deve ter pelo menos 3 caracteres."

    ascii_options = string.ascii_letters #criação da variável ascii
    number_options = string.digits       #criação da variável number
    punt_options = string.punctuation    #criação da variável pontuação
    all_options = ascii_options + number_options + punt_options

    # Garantir pelo menos um de cada tipo
    password_user = [
        random.choice(ascii_options),
        random.choice(number_options),
        random.choice(punt_options)
    ]

    # Preencher o restante da senha com aleatórios
    for _ in range(Len_pass - 3):
        password_user.append(random.choice(all_options))

    # Embaralhar os caracteres para não ficarem previsíveis
    random.shuffle(password_user)

    # Juntar em uma string final
    return ''.join(password_user)

# Parte de entrada do usuário
choice_user = input("Quantos dígitos tem a senha? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida!")
    quit()

response = password_generator(Len_pass=choice_user)
print(f"Senha gerada:\n{response}")
