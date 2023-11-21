# Copie as suas células, cole em um bloco de notas e insira um colchete antes da primeira célula e um depois da última
# Em seguida, insira uma vírgula antes da segunda em diante
# Depois da vírgula e ao final de cada célula, insira uma aspas

# Insira aqui suas células
lista = ['exemplo 1'
, 'exemplo 2']

# Loop que vai pegar cada célula do texto para aplicar letra maiúscula em cada primeira letra das palavras da sua frase
for frase in lista:
    
    # Converte as primeiras letras de cada palavra da frase em maiúsculo
    frase = frase.title()
        
    # Printa a células do Excel inseridas, porém com a mudança feita
    print(f'{frase}')
