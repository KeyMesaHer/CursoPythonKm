from collections import Counter, defaultdict
from collections import defaultdict
from collections import namedtuple


'''numeros = [9, 8, 7, 4, 3, 5, 2, 4, 2, 6]
frase = 'Al pan pan y al vino vino'
print(Counter(numeros))
print(Counter('missisipi'))
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,])
print(serie.most_common())
'''

'''mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)'''

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)

print(ariel.altura)
print(ariel.peso)
print(ariel.nombre)
print(ariel[2])
