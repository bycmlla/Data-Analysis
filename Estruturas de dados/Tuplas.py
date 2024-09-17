# sequência imutável
# tamanho fixo

tup = 4, 5, 6
print(tup)

nested_tup = (4,5,6), (7,8)
print(nested_tup)

converts = tuple([4,0,2])
print(converts)

tup_str = tuple('string')
print(tup_str)
print(tup_str[3])

# exemplo abaixo dá erro
tup_mod = tuple(['foo', [1,2], True])
# tup_mod[2] = False

# modificação in-place
tup_mod[1].append(3)

# se eu multiplico uma tupla por um inteiro, ele vai retornar a tupla repetidas vezes q indicou

tup_mult = ('foo', 'bar') * 4
print(tup_mult)

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))

