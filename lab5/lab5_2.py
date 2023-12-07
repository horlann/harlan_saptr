import openpyxl
import numpy as np


def getMatrixOutOfSheet(sheet):
    matrix = []


    for row in sheet.iter_rows(values_only = True):
        matrix.append(row)


    return np.array(matrix)




def chistStrat(workbook):
    payMatrix = getMatrixOutOfSheet(workbook.worksheets[0])
    print(payMatrix)

    numberOfRows = payMatrix.shape[0]
    numberOfColumns = payMatrix.shape[1]


    min = []
    max = []


    for row in range(numberOfRows):
        minValue = 100000

        print(numberOfRows)
        print(numberOfColumns)


        for column in range(numberOfColumns):
            if payMatrix[row, column] < minValue:
                minValue = payMatrix[row, column]
           
        min.append(minValue)


    for column in range(numberOfColumns):
        maxValue = -100000
        for row in range(numberOfRows):
            if payMatrix[row, column] > maxValue:
                maxValue = payMatrix[row, column]
           
        max.append(maxValue)


    index = np.argmax(min)
    maxmin = min[index]


    index = np.argmin(max)
    minmax = max[index]


    print(f'min A:{min}')
    print(f'max B:{max}\n')
    print(f'Нижня ціна гри:{maxmin}')
    print(f'Верхня ціна гри:{minmax}\n')
    if(maxmin != minmax):
        print("Сідлової точки не існує, отже рівноваги в чистих стратегіях немає")
    else:
        print(f'Сідлова точка:{minmax}')


# =============================================================================================================


filePath = '/Users/admin/Univer/3kurs/saptr/code/lab5/task_2.xlsx'


workbook = openpyxl.load_workbook(filePath)


chistStrat(workbook)


workbook.close()