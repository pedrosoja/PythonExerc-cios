#Python Code
#Jogo da Forca

#Escolha uma palavra
palavra_secreta = 'Pindamonhagaba'
palavra_secreta = list(palavra_secreta)

letras_descobertas = []
acertou = False

for i in range(0, len(palavra_secreta)) :
    letras_descobertas.append('-')

while acertou == False :
    letra = str(input('Digite uma letra: '))
    linha = ''

    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_descobertas[i] = letra

        linha += letras_descobertas[i]
    print(linha)

    acertou = True

    for x in range (0, len(letras_descobertas)):
        if letras_descobertas[x] == '-':
            acertou = False

print('Parabéns, Você conseguiu!!!!')