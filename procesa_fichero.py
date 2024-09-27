def procesa_fichero(rutafichero):

    numclientes = 0
    numlinea = 0
    # with open(carpeta + nombrearchivo, 'r') as archivo:
    #     for linea in archivo:
    #         print(linea.strip())  # Procesa cada línea (se usa .strip() para eliminar saltos de línea)
    
    with open(rutafichero, 'r') as archivo:
        numclientes = int(archivo.readline())
            


    #TABLA DE INGREDIENTES
    # CLIENTE | Lista de ingredientes que le gustan | Lista de ingredientes que no le gustan

    #Se declara la tabla numero de clientes (numclientesx2)    
    tablagustos = [[None] * 2 for _ in range(numclientes)]

    with open(rutafichero, 'r') as archivo:
        #Se desecha la primera linea
        archivo.readline()
        for linea in archivo:
            datos = linea.strip().split()
            #Si los datos solo tienen un elemento, no se hace nada, en otro caso, se procesa
            if len(datos) > 1:
                #Desechamos el primer elemento:
                del datos[0]
                #Hay que procesar la linea. Si i es par, son ingredientes que gustan, impar, no gustan
                tablagustos[numlinea//2][numlinea%2] = datos
            numlinea = numlinea + 1
            #print(datos)  # Procesar o almacenar los datos 


    elementos = [item for sublist1 in tablagustos for sublist2 in sublist1 for item in (sublist2 if isinstance(sublist2, list) else [sublist2])]
    elementos = [e for e in elementos if e is not None]
    elementos_unicos = set(elementos)
    lista_ingredientes = list(elementos_unicos)
    
    
    return lista_ingredientes, tablagustos