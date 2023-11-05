#Gabriel Campos Amaral Ribeiro
#10/06/2023

from PIL import Image, ImageFilter

# Abre a imagem
antes = Image.open('teste.png')

# Aplica o filtro de desfoque
#O numero 10 indica a taxa de desfoque
depois = antes.filter(ImageFilter.BoxBlur(0))

# Salva a imagem resultante
depois.save('teste02.png')

print('Sucesso')
