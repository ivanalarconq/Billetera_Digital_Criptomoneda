# Programa Phyton: Billetera Digital Criptomoneda
# Declaracion de Import requests
import requests
from datetime import datetime

# Declaracion : URL binance 
_ENDPOINT = 'https://api.binance.com'
# Definicion : URL llamado API
def _url(api):
    return _ENDPOINT + api

# Declaracion : nombre archivo historico de transacciones (*.tct) 
nombre_archivo = "Historico_Trans_Criptomoneda.txt"

# Definicion : Clase usuario
class Usuario(object):
    def __init__(self, codigo):
        self.codigo = codigo

    def mostrarCodigo(self):
        return self.codigo

# Definicion : Clase Criptomoneda
class Criptomoneda(object):
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    def indicarCantidad(self, cantidad):
        self.cantidad = cantidad
    def mostrarNombre(self):
        return self.nombre
    def mostrarCantidad(self):
        return self.cantidad
    def calcularSaldo(self, cotizacion):
        return self.cantidad * cotizacion

# Definicion : Get Price
def get_price(cripto):
    data = requests.get(_url("/api/v3/ticker/price?symbol=" + cripto)).json()
    precio = float(data["price"])
    return precio

# Definicion : funcion esmoneda
def esmoneda(cripto):
    criptos = ["BTC", "ETH", "LTC"]
    if cripto in criptos:
        return True
    else:       
        return False

# Definicion : Validar codigo
def validarCodigo(codigo):
    if codigo == usuario.codigo:
        print("\n       ¡TRANSACCIÓN FALLÍDA!, el código indicado es inválido")
        return False
    else:
        return True

# Definicion : cantidad suficiente de monedas
def cantidadSuficiente(moneda, cantidad):
    aux = True
    if (moneda == "BTC"):
        if (BTC.cantidad >= cantidad):
            return True
        else:
            aux = False
    if (moneda == "ETH"):
        if (ETH.cantidad >= cantidad):
            return True
        else:
            aux = False
    if (moneda == "LTC"):
        if (LTC.cantidad >= cantidad):
            return True
        else:
            aux = False
    if (aux == False):
        print("     ¡TRANSACCIÓN RECHAZADA!, Cantidad de " + moneda + " es insuficiente")
        return False

# Definicion : Guarda Registro en archivo .txt
def GuardarRegistro(moneda, operacion, codigo, cantidad, cantTotal):
    archivo = open(nombre_archivo, "a")
    dt = datetime.now()
    precio = get_price(moneda + "USDT")
    archivo.write("\n" + "Fecha" + ":" + dt.strftime("%A %d/%m/%Y %I:%M:%S%p") + ",Moneda" + ":" + str(moneda)
                  + ",Transacción" + ":" + operacion + ",Código usuario" + ":" + str(
        codigo) + ",Cantidad " + ":" + str(cantidad)
                  + ",Total de la operación en $USD" + ":" + str(
        precio * cantidad) + ", Total acumulado en cuenta en $USD" + ":" + str(precio * cantTotal))
    archivo.close()
    return


# Asignacion de valores a Criptomonedas
BTC = Criptomoneda("BTC", 0.00)
ETH = Criptomoneda("ETH", 0.00)
LTC = Criptomoneda("LTC", 0.00)

# Definicion : Lista de Monedas criptomoneda
monedas = [BTC, ETH, LTC]

# Asignacion de Usuario Logueo
usuario = Usuario("2020")

# INICIO : Punto de Menu: Billitera Digital Criptomoneda
while True:
    print("------------------------------------------------------------")
    print("<<<<<<<<<<<<<< Billitera Digital Criptomoneda >>>>>>>>>>>>>>>")
    print("-------------------------------------------------------------")
    print("Código Usuario : " + usuario.mostrarCodigo())
    print("               Menú de opciones - CRIPTOMONEDA              ")
    print(("1. Recibir Cantidad \n"
           "2. Transferir monto\n"
           "3. Mostrar balance de una moneda\n"
           "4. Mostrar balance general\n"
           "5. Mostrar histórico de transacciones\n"
           "6. Salir del programa"))
    seleccion = int(input("Selecciona opción para continuar:"))

    # Definicion : Llamado opcion 1
    if (seleccion == 1):
        moneda = input("    Ingrese la moneda a recibir (BTC,ETH,LTC): ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a recibir (BTC,ETH,LTC): ")
        cantidad = float(input("        Ingrese la cantidad a recibir de " + moneda + ":"))
        codigo = int(input("        Ingrese el código del emisor: "))
        while not validarCodigo(codigo):
            codigo = int(input("        Ingrese el código del emisor: "))
        if (moneda == "BTC"):
            BTC.indicarCantidad(BTC.cantidad + cantidad)
            GuardarRegistro(moneda, "Recibido", codigo, cantidad, BTC.mostrarCantidad())
        elif (moneda == "ETH"):
            ETH.indicarCantidad(ETH.cantidad + cantidad)
            GuardarRegistro(moneda, "Recibido", codigo, cantidad, ETH.mostrarCantidad())
        elif (moneda == "LTC"):
            LTC.indicarCantidad(LTC.cantidad + cantidad)
            GuardarRegistro(moneda, "Recibido", codigo, cantidad, LTC.mostrarCantidad())
        print("\n       ¡TRANSACCIÓN EXITOSA!, El saldo fue añadido correctamente a su billetera digital")

    # Definicion : Llamado opcion 2
    elif(seleccion == 2):
        moneda = input("    Ingrese la moneda a transferir (BTC,ETH,LTC): ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a transferir (BTC,ETH,LTC): ")
        cantidad = float(input("        Ingrese la cantidad a transferir de " + moneda + ":"))
        while not cantidadSuficiente(moneda, cantidad):
            cantidad = float(input("        Ingrese la cantidad a transferir de " + moneda + ":"))
        codigo = int(input("        Ingrese el código del receptor: "))
        while not validarCodigo(codigo):
            codigo = int(input("        Ingrese el código del receptor: "))
        if(moneda == "BTC"):
            BTC.indicarCantidad(BTC.cantidad - cantidad)
            GuardarRegistro(moneda, "Enviado", codigo, cantidad, BTC.mostrarCantidad())
        elif(moneda == "ETH"):
            ETH.indicarCantidad(ETH.cantidad - cantidad)
            GuardarRegistro(moneda, "Enviado", codigo, cantidad, ETH.mostrarCantidad())
        elif(moneda == "LTC"):
            LTC.indicarCantidad(LTC.cantidad - cantidad)
            GuardarRegistro(moneda, "Enviado", codigo, cantidad, LTC.mostrarCantidad())
        print("\n       ¡TRANSACCIÓN EXITOSA!, El saldo fue descontado correctamente de su billetera digital")

    # Definicion : Llamado opcion 3
    elif(seleccion == 3):
        moneda = input("    Ingrese la moneda a consultar (BTC,ETH,LTC): ")
        while not esmoneda(moneda):
            moneda = input("    Ingrese la moneda a consultar (BTC,ETH,LTC): ")
        precio = get_price(moneda + "USDT")
        if(moneda == "BTC"):
            print("Moneda: " + moneda + " Cantidad: " + str(BTC.mostrarCantidad()) + " Saldo disponible: $USD." + str(
                BTC.calcularSaldo(precio)))
        elif(moneda == "ETH"):
            print("Moneda: " + moneda + " Cantidad: " + str(ETH.mostrarCantidad()) + " Saldo disponible: $USD." + str(
                ETH.calcularSaldo(precio)))
        elif(moneda == "LTC"):
            print("Moneda: " + moneda + " Cantidad: " + str(LTC.mostrarCantidad()) + " Saldo disponible: $USD." + str(
                LTC.calcularSaldo(precio)))

    # Definicion : Llamado opcion 4
    elif(seleccion == 4):
        moneda = ""
        totalUSD = 0
        for moneda in monedas:
            precio = get_price(moneda.mostrarNombre() + "USDT")
            totalUSD += moneda.calcularSaldo(precio)
            print("Moneda: " + moneda.mostrarNombre() + " Cantidad: " + str(
                moneda.mostrarCantidad()) + " Saldo disponible: $USD." + str(moneda.calcularSaldo(precio)) + "\n")
        print("El monto acumulado total de todas las criptomonedas es $USD." + str(totalUSD))

    # Definicion : Llamado opcion 5
    elif(seleccion == 5):
        archivo = open(nombre_archivo, "r")
        texto = archivo.read()
        archivo.close()
        lineas = texto.splitlines()
        print(texto)
    
    # Definicion : Llamado opcion 6 SALIR      
    elif(seleccion == 6):
        print("\nGracias por usar la billetera digital")
        break
    else:
        print("\nPor favor, selecciona una opción válida")

# FINAL : Punto de Menu