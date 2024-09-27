def calculapuntos_relajado(clientes_nogustan, listaingredientes):
    return sum(all(elem not in listaingredientes for elem in sublista) for sublista in clientes_nogustan)