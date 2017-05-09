import getpass

letras_descobertas=[]
palavra_secreta = getpass.getpass('Qual a palavra secrete? ')
palavra_secreta = list(palavra_secreta)
acertou = False

for i in range(0, len(palavra_secreta)) :
    letras_descobertas.append('-')

while acertou == False :
    letra = str(input('Digite uma letra: '))

    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_descobertas[i] = letra

        print(letras_descobertas[i])

    acertou = True

    for x in range (0, len(letras_descobertas)):
        if letras_descobertas[x] == 'x':
            acertou = False

