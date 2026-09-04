#Dictionaries
#
#Ejercicio 41

# students = {}
# amount = int(input("\n¿Cuántos estudiantes quieres registrar? > "))

# for i in range(amount):
#     id = int(input(f"\nCodigo del estudiante {i + 1} > "))
#     name = input(f"\nNombre del estudiante {i + 1} > ")
#     students[id] = name

# print("Listado de estudiantes")
# for i in students:
#     print(f"\n{i} -> {students[i]}")


#Ejercicio 42
#
# contacts = {}

# amount = int(input("\n¿Cuántos contactos quieres registrar? > "))

# for i in range(amount):
#     name = input(f"\nNombre del contacto {i + 1} > ")
#     phone = input(f"\nTeléfono del contacto {i + 1} > ")
#     contacts[name] = phone

# search = input("\nBuscar contacto > ")
# if search in contacts:
#     print(f"\n{search} -> {contacts[search]}")
# else:
#     print("\nNo se encontró el contacto")


#Ejercicio 43
#
# products = {}
# amount = int(input("\n¿Cuántos productos quieres registrar? > "))

# for i in range(amount):
#     name = input(f"\nNombre del producto {i + 1} > ")
#     quantity = float(input(f"\nCantidad de {name} > "))
#     products[name] = quantity

# search = input("\nBuscar producto > ")
# if search in products:
#     print(f"\n{search} -> {products[search]}")
# else:
#     print("\nNo se encontró el producto")


#Ejercicio 44
#
bypieces = {}

phrase = input("\nIngresa una frase > ").lower()

words = phrase.split()
for word in words:
    if word in bypieces:
        bypieces[word] += 1
    else:
        bypieces[word] = 1
print("\nContador de palabras")
for word in bypieces:
    print(f"\n{word} -> {bypieces[word]}")
