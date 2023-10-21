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

def maximumSubsequence(arr, n):
	max = 0
	memo = [0 for x in range(n)]

	# Initialize maximumSubsequence values for all indexes
	for i in range(n):
		memo[i] = arr[i][0]

	# bottom up manner
	for i in range(1, n):
		for j in range(i):
			if (arr[i][1] > arr[j][1] and arr[i][2] > arr[j][2] and
				memo[i] < memo[j] + arr[i][0]):
				memo[i] = memo[j] + arr[i][0]

	# Find maximum of all 
	for i in range(n):
		if max < memo[i]:
			max = memo[i]

	return max

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

    m = generate_all(matrix)
    n = len(m)
    result_max= maximumSubsequence(m, n)
    print(result_max)





# while True:
#     try:
#         setnumber=int(input())
#     except:
#         break

#     matrix=[]

#     for i in range(setnumber):
#         aux=input().split()
#         aux[0]=int(aux[0])
#         aux[1]=int(aux[1])
#         aux[2]=int(aux[2])
#         matrix.append(aux)
    
#     result_subsequence = max_height_increasing_subsequence(generate_all(matrix))
#     print(result_subsequence)
