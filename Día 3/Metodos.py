#metodos de string: mayuscula, minuscula, separar
texto = "Este es el texto de Keissy"
resultado = texto.upper()
resultado2 = texto.lower()
resultado3 = texto[2].upper()
resultado4 = texto.split()
resultado5 = texto.split("t")
print(resultado, resultado2, resultado3)
print(resultado4, resultado5)

#Metodo join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)

#metodo find
resultado6 = texto.find("texto")
print(resultado6)

#Metodo replace
resultado7 = texto.replace("Keissy", "todos")
print(resultado7)