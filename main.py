# Input para receber o número a ser traduzido
valor = input ("Insira o valor a ser traduzido: ")

# Aqui iniciamos um loop que vai traduzir cada caractére individualmente para binário
for c in valor:
    v = ord(c)
    # Aqui temos a função f-string que formata o número int para uma string em binário
    print(c, v, f'{v:b}', sep='\t')
    # Outra opção é substituir f'{v:b}' por f'{v:08b}' para se ter um número binário com 8 dígitos.