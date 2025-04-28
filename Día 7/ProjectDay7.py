class Persona: #nombre, apellido
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona): #numero de cuenta, balance (saldo de la cuenta)
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'''Cliente:{self.nombre} {self.apellido}
         Información de la cuenta: {self.numero_cuenta}
         Total: {self.balance}'''

    def depositar(self, monto):
        self.balance += monto
        print('Deposito realizado exitosamente')


    def retirar(self, monto):
        if  monto <= self.balance:
            self.balance -= monto
            print('Saldo insuficiente')
        else:
            print('Retiro exitoso!')



def crear_cliente():
    nombre_cliente = input('Ingrese su nombre: ')
    apellido_cliente = input('Ingrese su apellido: ')
    numero_cuenta_cliente = input('Ingrese su número de cuenta: ')
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_cuenta_cliente)
    return cliente


def inicio():
    client = crear_cliente()
    print(client)

    menu = 0

    while menu != 'S':
        menu = input('Elije: Depositar (D), Retirar (R), o Salir (S): ')
        print(menu)

        if menu == 'D':
            monto = int(input("Cantidad a depositar: "))
            client.depositar(monto)
        elif menu == 'R':
            retiro = int(input("Cantidad a retirar: "))
            client.retirar(monto)
        print(client)

inicio()

