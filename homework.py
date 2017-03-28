# ------homework---------
def getMNMatrix(line, row):
	matrix = [ [0 for i in range(row)] for j in range(line) ]
	index = 1
	for i in range(line):
		j = 0;
		for j in range(row) :
			matrix[i][j] = index
			index += 1
			j += 1
	return matrix

def convertMatrix(matrix_2d):
	re = []
	for i in range(len(matrix_2d)) :
		re.extend(matrix_2d[i])
	return re

matrix_2d = getMNMatrix(2, 4)
print(matrix_2d)

matrix_1d = convertMatrix(matrix_2d)
print(matrix_1d)


a = raw_input("Enter a: ")
b = raw_input("Enter b: ")
print "a + b as strings: ", a + b  # + everywhere is ok since all are strings
a = int(a)
b = int(b)
c = a + b
print "a + b as integers: ", c



def sumMatrix(A):
	sum, i, j = 0, 0, 0
	while i < len(A):
		j = 0
		while j < len(A[i]):
			sum += A[i][j]
			A[i][j] = sum
			j += 1
		i += 1
	return A

A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
print(A)
B = sumMatrix(A)
print(B)
