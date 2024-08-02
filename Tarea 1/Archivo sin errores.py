# Escriba un programa Python para crear dos cadenas de una cadena dada.
# Cree la primera cadena usando los caracteres que ocurren solo una vez y
# cree la segunda cadena con caracteres repetidos.

lista_repetido = []
lista_uno = []


def cadena():
    texto = input("ingrese el texto: ")
    for i in texto:
        contador = texto.count(i)
        if contador > 1:
            lista_repetido.append(i)
        for letra in lista_repetido:
            if lista_repetido.count(letra) > 1:
                lista_repetido.remove(letra)
    for i in texto:
        cont = texto.count(i)
        if cont == 1:
            lista_uno.append(i)

    print("caracteres repetidos: ", lista_repetido, "\n"
          "caracteres únicos: ", "\n", lista_uno)  # error 1, 2


cadena()  # error 3
