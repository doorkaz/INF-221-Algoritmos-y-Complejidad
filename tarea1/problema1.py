def generate_all(matrix):
    def rotations(matrix):
        m = []
        m.append([matrix[0], matrix[2], matrix[1]])
        m.append([matrix[1], matrix[0], matrix[2]])
        m.append([matrix[1], matrix[2], matrix[0]])
        m.append([matrix[2], matrix[1], matrix[0]])
        m.append([matrix[2], matrix[0], matrix[1]])
        return m


    for i in range(len(matrix)):
        m = rotations(matrix[i])
        matrix.extend(m)

    matrices_unicas = list(set(tuple(matriz) for matriz in matrix))
    sorted_matrix = sorted(matrices_unicas, key=lambda matriz: matriz[1])

    return sorted_matrix


def modified_LIS(matriz):
    def buscar_subsecuencia(subsecuencia, i):
        if i == len(matriz):
            return subsecuencia, sum(arr[0] for arr in subsecuencia)

        skip, skip_sum = buscar_subsecuencia(subsecuencia, i + 1)
        if not subsecuencia or (matriz[i][1] > subsecuencia[-1][1] and matriz[i][2] > subsecuencia[-1][2]):
            
            select, select_sum = buscar_subsecuencia(subsecuencia + [matriz[i]], i + 1) #Se busca en la subsecuencia concatenada con el arreglo de la matriz
            
            if select_sum > skip_sum:
                
                return select, select_sum
            else:
                
                return skip, skip_sum
        else:
            return skip, skip_sum

    subsequence, sum_of_subsequence = buscar_subsecuencia([], 0)
    return subsequence, sum_of_subsequence

while True:
    try:
        setnumber=int(input())
    except:
        break

    matrix=[]

    for i in range(setnumber):
        aux=input().split()
        aux[0]=int(aux[0])
        aux[1]=int(aux[1])
        aux[2]=int(aux[2])
        matrix.append(aux)
    result_subsequence, result_sum = modified_LIS(generate_all(matrix))
    print(result_sum)
