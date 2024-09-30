# Función para cifrar usando cifrado César
def cifrar(texto, desplazamiento):
    resultado = ""

    # Iterar sobre cada letra del texto
    for i in range(len(texto)):
        letra = texto[i]

        # Cifrar solo las letras2
        if letra.isalpha():
            ascii_offset = 65 if letra.isupper() else 97
            resultado += chr((ord(letra) - ascii_offset + desplazamiento) % 26 + ascii_offset)
        else:
            resultado += letra

    return resultado

# Función para descifrar usando cifrado César
def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)

# Programa principal
if __name__ == "__main__":
    opcion = input("Elige una opción: (1) Cifrar, (2) Descifrar: ")

    if opcion == '1':
        texto = input("Ingresa el texto a cifrar: ")
        desplazamiento = int(input("Ingresa el número de desplazamiento: "))
        texto_cifrado = cifrar(texto, desplazamiento)
        print("Texto cifrado:", texto_cifrado)

    elif opcion == '2':
        texto_cifrado = input("Ingresa el texto cifrado: ")
        desplazamiento = int(input("Ingresa el número de desplazamiento utilizado: "))
        texto_descifrado = descifrar(texto_cifrado, desplazamiento)
        print("Texto descifrado:", texto_descifrado)

    else:
        print("Opción no válida.")
