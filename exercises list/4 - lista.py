# Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota

notas = [2, 5, 7, 9]

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / len(notas)

print(f'maior {maior_nota}, menor {menor_nota}, média {media}')

if media > 7:
    print('APROVADO')
else:
    prova_final = 6
    notas.append(prova_final)

    media_final = sum(notas) / len(notas)

    if media_final > 7:
        print(f'Média final: {media_final}: APROVADO')
    else:
        print(f'Média final: {media_final}: REPROVADO')

print(notas)