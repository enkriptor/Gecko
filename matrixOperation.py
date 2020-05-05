import random

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

def makeDefaultSquareMatrix(length):
	defaultMatrix = []
	rowVector = []
	while(len(defaultMatrix)!=length):
		for index in range(0, length):
			rowVector.append(0)
		defaultMatrix.append(rowVector)
		rowVector = []
	return defaultMatrix


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