import random

def squareMatrixMakerOnLength(length):
	infinity = 99999999999999999999
	squareMatrix = []
	rowVector = []
	while(len(squareMatrix)!=length):
		for index in range(0, length):
			rowVector.append(random.randint(0, infinity))
		squareMatrix.append(rowVector)
		rowVector = []
	return squareMatrix

def squareMatrixMakerOnList(listInput):
	squareMatrix = []
	rowVector = []
	listLength = len(listInput)
	length = int(listLength**(0.5))
	while(len(squareMatrix)!=length):
		for index in listInput[0:length]:
			rowVector.append(index)
		squareMatrix.append(rowVector)
		listInput = listInput[length:len(listInput)]
		rowVector = []
	return squareMatrix

def displayMatrix(matrix):
	for element in matrix:
		getRow = ''
		for subElement in element:
			getRow += str(subElement) + ' '
		print(getRow)

def makeDefaultSquareMatrix(length):
	defaultMatrix = []
	rowVector = []
	while(len(defaultMatrix)!=length):
		for index in range(0, length):
			rowVector.append(0)
		defaultMatrix.append(rowVector)
		rowVector = []
	return defaultMatrix

def addMatrices(matrixVector):
	matrixSum = makeDefaultSquareMatrix(len(matrixVector[0]))
	count = 0
	while(count != len(matrixVector)):
		for index in range(0,len(matrixSum)):
			for subIndex in range(0,len(matrixSum)):
				matrixSum[index][subIndex] += matrixVector[count][index][subIndex]
		count += 1
	return matrixSum

def matrixTransposer(matrix):
	transposeMatrix = makeDefaultSquareMatrix(len(matrix))
	for index in range(0, len(matrix)):
		for subIndex in range(0, len(matrix)):
			transposeMatrix[index][subIndex] = matrix[subIndex][index]
	return transposeMatrix

def matrixToVector(matrix):
	finalVector = []
	for rowVector in matrix:
		for index in rowVector:
			finalVector.append(index)
	return finalVector
	
# # def getMatrixCalc():
# matrixA = squareMatrixMakerOnList([1,4,7,2,5,8,3,6,9])
# # matrixA = squareMatrixMakerOnLength(3)
# matrixATranspose = matrixTransposer(matrixA)
# print(matrixToVector(matrixATranspose))
# # 	# matrixB = squareMatrixMaker(3)
# # 	# matrixO = makeDefaultMatrix(3)

# # 	displayMatrix(matrixA)
# displayMatrix(matrixATranspose)
# # 	# displayMatrix(matrixB)

# getMatrixCalc()