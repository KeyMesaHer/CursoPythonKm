from pathlib import Path

base = Path.home()
guia = Path(base,"Europa", "España", Path("Barcelona", 'Sagrada_Familia.txt'))
#guia2 = guia.with_name("La_Pedrera.txt")
print(guia.parent.parent.parent)#Antecesor más inmediato de una archivo en una ruta

guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob('**/*.txt'):
    print(txt)

guia = Path('Europa', 'España', 'Barcelona', 'Sagrada_Familia.txt')
en_europa = guia.relative_to(Path('Europa'))
en_espana = guia.relative_to(Path('Europa', 'España'))
print(en_europa)
print(en_espana)

