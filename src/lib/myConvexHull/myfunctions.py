import numpy as np

def myConvexHull(dataFrame):
    convexHullSet = []

    farLeft = dataFrame[0]
    farRight = dataFrame[0]

    for point in dataFrame:
        if(point[0] < farLeft[0]):
            farLeft = point
        if(point[0] > farRight[0]):
            farRight = point

    # Rekursif untuk sisi atas
    convexHullSet.append(farLeft)
    dataFrameAbove = findPointAbove(dataFrame, farLeft, farRight)
    convexHullReccursiveAbove(dataFrameAbove, farLeft, farRight, convexHullSet)

    # Rekursive untuk sisi bawah
    convexHullSet.append(farRight)
    dataFrameBelow = findPointBelow(dataFrame, farLeft, farRight)
    convexHullReccursiveBelow(dataFrameBelow, farLeft, farRight, convexHullSet)


    answerSets = convertConvexHull(dataFrame, convexHullSet)
    arrayAnswer = np.array(answerSets)
    return arrayAnswer

# Fungsi rekursif untuk menyelesaikan convexHull
# Basis : jika sebelah kiri atau sebelah kanan garis sudah tidak ada lagi titik
def convexHullReccursiveAbove(dataFrame, leftPoint, rightPoint, convexHullSet):
    if dataFrame:
        farthestPoint = findFarAbove(dataFrame, leftPoint, rightPoint)

        # Rekursif untuk sisi atas sebelah kiri
        dataFrameAboveLeft = findPointAbove(
            dataFrame, leftPoint, farthestPoint)
        convexHullReccursiveAbove(
            dataFrameAboveLeft, leftPoint, farthestPoint, convexHullSet)

        convexHullSet.append(farthestPoint)

        # Rekursif untuk sisi atas sebelah kanan
        dataFrameAboveRight = findPointAbove(
            dataFrame, farthestPoint, rightPoint)
        convexHullReccursiveAbove(
            dataFrameAboveRight, farthestPoint, rightPoint, convexHullSet)


def convexHullReccursiveBelow(dataFrame, leftPoint, rightPoint, convexHullSet):
    if dataFrame:
        farthestPoint = findFarBelow(dataFrame, leftPoint, rightPoint)

        # Rekursif untuk sisi atas sebelah kanan
        dataFrameBelowRight = findPointBelow(
            dataFrame, farthestPoint, rightPoint)
        convexHullReccursiveBelow(
            dataFrameBelowRight, farthestPoint, rightPoint, convexHullSet)

        convexHullSet.append(farthestPoint)

        # Rekursif untuk sisi atas sebelah kiri
        dataFrameBelowLeft = findPointBelow(
            dataFrame, leftPoint, farthestPoint)
        convexHullReccursiveBelow(
            dataFrameBelowLeft, leftPoint, farthestPoint, convexHullSet)

# Fungsi mengembailkan point yang merupakan titik terjatuh pada sisi atas antara
# dua titik yang membentuk garis
def findFarAbove(dataFrame, leftPoint, rightPoint):
    distancePoint = (dataFrame[0][0] - leftPoint[0])*(rightPoint[1] - leftPoint[1]) - \
        (dataFrame[0][1] - leftPoint[1])*(rightPoint[0] - leftPoint[0])
    point = dataFrame[0]
    for data in dataFrame:
        d = (data[0] - leftPoint[0])*(rightPoint[1] - leftPoint[1]) - \
            (data[1] - leftPoint[1])*(rightPoint[0] - leftPoint[0])
        if (d < distancePoint):
            point = data
            distancePoint = d
    return point

# Fungsi mengembailkan point yang merupakan titik terjatuh pada sisi bawah antara
# dua titik yang membentuk garis
def findFarBelow(dataFrame, leftPoint, rightPoint):
    distancePoint = (dataFrame[0][0] - leftPoint[0])*(rightPoint[1] - leftPoint[1]) - \
        (dataFrame[0][1] - leftPoint[1])*(rightPoint[0] - leftPoint[0])
    point = dataFrame[0]
    for data in dataFrame:
        d = (data[0] - leftPoint[0])*(rightPoint[1] - leftPoint[1]) - \
            (data[1] - leftPoint[1])*(rightPoint[0] - leftPoint[0])
        if (d > distancePoint):
            point = data
            distancePoint = d
    return point


# Fungsi mengembalikan sets of point yang merupakan titik-titik yang berada di sisi atas
# antara dua titik yang memebentuk garis
def findPointAbove(dataFrame, leftPoint, rightPoint):
    sets = []
    for data in dataFrame:
        d = (data[0] - leftPoint[0])*(rightPoint[1] - leftPoint[1]) - \
            (data[1] - leftPoint[1])*(rightPoint[0] - leftPoint[0])
        if (d < 0):
            sets.append(data)
    return sets


# Fungsi mengembalikan sets of point yang merupakan titik-titik yang berada di sisi bawah
# antara dua titik yang memebentuk garis
def findPointBelow(dataFrame, leftPoint, rightPoint):
    sets = []
    for data in dataFrame:
        d = (data[0] - leftPoint[0])*(rightPoint[1] - leftPoint[1]) - \
            (data[1] - leftPoint[1])*(rightPoint[0] - leftPoint[0])
        if (d > 0):
            sets.append(data)
    return sets

# Fungsi mengembalikan numpy array of index dari dataFrame yang di input di awal
# Berdasarkan jawaban yang telah dicari sebelumnya
def convertConvexHull(dataFrame, convexHullSet):
    answerSets = []
    for i in range(len(convexHullSet)-1):
        for j in range(len(dataFrame)):
            if (dataFrame[j][0] == convexHullSet[i][0] and dataFrame[j][1] == convexHullSet[i][1]):
                leftSet = j
            if (dataFrame[j][0] == convexHullSet[i+1][0] and dataFrame[j][1] == convexHullSet[i+1][1]):
                rightSet = j
        answerSets.append([leftSet, rightSet])
    for j in range(len(dataFrame)):
        if (dataFrame[j][0] == convexHullSet[len(convexHullSet)-1][0] and dataFrame[j][1] == convexHullSet[len(convexHullSet)-1][1]):
            leftSet = j
        if (dataFrame[j][0] == convexHullSet[0][0] and dataFrame[j][1] == convexHullSet[0][1]):
            rightSet = j
    answerSets.append([leftSet, rightSet])
    return answerSets
