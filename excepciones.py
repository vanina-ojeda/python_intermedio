#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
try:
    numero_1 = float(input("ingrese primer numero:"))
    numero_2 = float(input("ingrese segundo numero:"))
    resultado = numero_1 / numero_2
    print(f"el resultado de la division entre los dos numeros es: {resultado}")
except ZeroDivisionError:
    print("error : no se puede dividir utilizando el cero ")


#Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
try:
    num = 93
    text = "hola"
    resultado = num + text
    print(f"el resultado de la suma es: {resultado }")
except TypeError:
    print("error : no se puede sumar un numero con una cadena de texro")

#Escribe un programa que intente acceder a una clave que no existe en un
#diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

try:
    ingredientes = {"harina": 300,"manteca":150,"azucar":120,"huevo":1}
    cantidad = ingredientes["almidon_maiz"]
    print(f"la candidad del ingediente es:{cantidad}")
except KeyError:
    print("error: el ingrediente mencionado no se encuentra en la lista ")


#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
#embargo, también intenta crear el archivo si no existe.

try:
    with open("recetas.txt","r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("error: el archivo no existe")
    with open("recetas.txt" , "w") as archivo:
        archivo.write("archivo de recetas creado50")

#Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
#captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.

try:
    num_1 = float(input("ingrese primer numero"))
    num_2 = float(input("engrese segundo numero"))
    resultado = num_1 / num_2
    print(f"el resultado de la division es:{resultado}")
except ZeroDivisionError:
    print("error no puede dividirse por cero")
except ValueError:
    print("error: debe ingresar un numero valido")