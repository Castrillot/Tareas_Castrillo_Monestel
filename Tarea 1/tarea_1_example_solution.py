def operation_selector(num1, num2, op):
    # Verificar que num1 y num2 sean números enteros
    if not isinstance(num1, int) or isinstance(num1, bool):
        return (-50, None)  # Error -50: num1 no es entero

    if not isinstance(num2, int) or isinstance(num2, bool):
        return (-50, None)  # Error -50: num2 no es entero

    # Verificar que op sea de tipo string
    if not isinstance(op, str):
        return (-60, None)  # Error -60: op no es un string

    # Verificar que op sea una de las opciones permitidas
    if op not in ['+', '-', '*', '&']:
        return (-70, None)  # Error -70: no es una operación valida

    # Realizar la operación según el carácter op
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '&':
        result = num1 & num2

    return (0, result)  # Código de éxito 0: operación realizada con éxito
# print(operation_selector(2, 9.8, '+'))  # (0, 9)


def calculo_promedio(lista_valores):
    # Verificar que todos los elementos de la lista sean números
    for valor in lista_valores:
        if isinstance(valor, str) or isinstance(valor, bool):
            return (-80, None)  # Error -80: verificar numeros de lista

    # Verificar que el tamaño de la lista no sea mayor a 10 elementos
    if len(lista_valores) > 10:
        return (-90, None)  # Error -90: lista con mas de 10 elementos

    # Calcular el promedio
    if not lista_valores:
        return (0, 0)  # Si la lista está vacía, el promedio es 0

    promedio = sum(lista_valores) / len(lista_valores)
    return (0, promedio)  # Código de éxito 0: operación realizada con éxito
# print(calculo_promedio([1,False, 3, 4, 5]))  # (0, 3.0)
