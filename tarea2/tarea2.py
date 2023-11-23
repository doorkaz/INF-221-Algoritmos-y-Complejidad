###############################################################################
# overlap:
#   Calcula la cantidad de elementos que son interseccion entre dos intervalos
# inputs:
#   interval1: intervalo de numeros a comparar con interval2
#   interval2: intervalo de numeros a comparar con interval1
#
# return:
#   Numero de elementos en la interseccion de ambos intervalos
#   
###############################################################################

def overlap(interval1, interval2):
    a1, b1 = interval1
    a2, b2 = interval2

    # Calcula el punto de inicio y fin del intervalo de superposicion
    start = max(a1, a2)
    end = min(b1, b2)

    # Verifica si existe superposicion
    if start <= end:
        return end - start + 1 # Por ejemplo, para el intervalo [5,13] hay 13-5+1 elementos.
    else:
        return 0



###############################################################################
# superposicion_mitad:
#   Busca la maxima interseccion que pueden tener los intervalos divididos de la izq y la derecha
# inputs:
#   arr_izq: lista de intervalos
#   arr_der: lista de intervalos
#
# return:
#   olap: Maxima superposicion
#   
###############################################################################
def superposicion_mitad(arr_izq, arr_der):
    if len(arr_izq) == 0 or len(arr_der) == 0:
        return 0

    minc = arr_der[0][0]
    maxb = 0
    olap = 0

    for i in range(0, len(arr_izq)):
        if maxb < arr_izq[i][1]:
            maxb = arr_izq[i][1]

    for j in range(0, len(arr_der)):
        current_overlap = overlap([minc, maxb], arr_der[j])
        olap = max(olap, current_overlap)

    return olap


###############################################################################
# encontrar_superposicion:
#   Entrega la maxima cantidad de intersecciones que pueden tener los intervalos en el arreglo "arr".
# inputs:
#   arr: Arreglo con todos los intervalos en los que se quiere buscar el maximo numero de intersecciones
#
# return: maxima cantidad de coincidencias de elementos entre los intervalos de arr. 
#   
###############################################################################
def encontrar_superposicion(arr):
    if len(arr) == 0 or len(arr) == 1:
        return 0

    mitad = len(arr) // 2
    arr_izq = arr[0:mitad]
    arr_der = arr[mitad:]

    # Se divide el problema en problemas mas pequeños
    max_izq = encontrar_superposicion(arr_izq)
    max_der = encontrar_superposicion(arr_der)
    max_mitad = superposicion_mitad(arr_izq, arr_der)

    return max(max_izq, max_der, max_mitad)

# Se piden los datos por consola y se formatean para que se almacene como un array de intervalos.
# Ademas, se utiliza el try y except para detectar el EOF
while True:
    try:
        setnumber=int(input())
    except:
        break
    
    # Logica para ir almacenando las entradas. 
    numeros = list(map(int, input().split()))
    array_intervalos = [numeros[i:i+2] for i in range(0, len(numeros), 2)]
    
    resultado = encontrar_superposicion(array_intervalos)
    print(resultado)
