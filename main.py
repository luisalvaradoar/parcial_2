def traza_maxima(M):
	diagonales = []
	for k in range(len(M) - 1):
		dk = []
		i = 0
		j = k
		while(True):
			dk.append(M[i][j])
			i += 1
			j += 1
			if j == len(M):
				diagonales.append(dk)
				break

	for k in range(len(M) - 1):
		dk = []
		i = k
		j = 0
		while(True):
			dk.append(M[i][j])
			i += 1
			j += 1
			if i == len(M):
				diagonales.append(dk)
				break
	diagonal_principal = diagonales[0]
	diagonales.remove(diagonal_principal)

	sumas = []
	for d in diagonales:
		if len(d) == 2:
			sumas.append(sum(d))
		else:
			for i in range(len(d) - 1):
				for j in range(i + 2, len(d) + 1):
					sumas.append(sum(d[i:j]))

	sumas.remove(sum(diagonal_principal))
	return(max(sumas))

def main():
	entrada = open("input.txt", "r")
	salida = open("output.txt", "w")

	T = int(entrada.readline())
	for t in range(T):
		tam = int(entrada.readline())
		matriz = []

		for i in range(tam):
			fila = entrada.readline().replace('\n','').split(' ')
			fila_int = []
			for f in fila:
				fila_int.append(int(f))
			
			matriz.append(fila_int)

		resultado = traza_maxima(matriz)
		salida.write("Caso #{}: {}\n".format(t + 1, resultado))

	entrada.close()
	salida.close()

main()