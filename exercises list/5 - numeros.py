# Desenvolva um programa que leia um número inteiro qualquer e que apresete o número informado, seguido do seu antecessor e do seu sucessor
# Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado com duas casas decimais

notas = []

for i in range(4):
    numero = int(input('digite um número: '))
    notas.append(numero)
    
media_final = sum(notas) / len(notas)

print('antecessor: ', notas[0] - 1, 'sucessor: ', notas[0] + 1)
print(f'numero: {notas[0]}.00')
print(f'média: {media_final}')




