def contar_listas(lista1, lista2, lista3):
    return sum(
        all(elem not in lista2 for elem in sublista) and all(elem in sublista for elem in lista3)
        for sublista in lista1
    )