import random
import time
from functions import *
from classes import Matrix, Point

# INPUT


print("Pilih metode input: ")
print("[1]. Input melalui file .txt")
print("[2]. Input melalui CLI")
inputMethod = int(input("> "))

# INPUT via file .txt 

if (inputMethod == 1):
    # BUKA FILE
    try:
        lines = []
        filename = "test.txt"
        with open(filename, "r") as file:
            for line in file:
                lines.append(line.strip())
    except Exception as e:
        print(f"Gagal membuka file {file}.")

    # PROSES INPUT
    buffer_size = int(lines[0])

    matrixSize = lines[1].split(" ")
    matrixCol = int(matrixSize[0])
    matrixRow = int(matrixSize[1])
    matrix = Matrix(matrixRow, matrixCol, "")
    for i in range(matrixRow):
        currentLine = lines[2 + i]
        currentRow = currentLine.split(" ")
        for j in range(matrixCol):
            matrix.el[i][j] = currentRow[j]

    nSequence = int(lines[2 + matrixRow])
    sequences = ["" for i in range(nSequence)]
    sequenceRewards = [0 for i in range(nSequence)]
    for i in range(nSequence):
        sequences[i] = lines[3 + matrixRow + (i * 2)]
        sequenceRewards[i] = lines[4 + matrixRow + (i * 2)]

# INPUT via CLI

else:
    nTokenUnik = int(input("Jumlah token unik: "))

    tokens = input("Token: ").split(" ")

    buffer_size = int(input("Ukuran buffer: "))

    matrixSize = input("Ukuran matriks: ").split(" ")
    matrixCol = int(matrixSize[0])
    matrixRow = int(matrixSize[1])
    matrix = Matrix(matrixRow, matrixCol, "")
    for i in range(matrixRow):
        for j in range(matrixCol):
            random_int = random.randint(0, nTokenUnik - 1)
            matrix.el[i][j] = tokens[random_int]

    nSequence = int(input("Jumlah sequence: "))
    maxSequenceSize = int(input("Ukuran maksimal sequence: "))
    sequences = ["" for i in range(nSequence)]
    sequenceRewards = [0 for i in range(nSequence)]
    for i in range(nSequence):
        current_sequence_length = random.randint(2, maxSequenceSize)

        for j in range(current_sequence_length):
            random_int = random.randint(0, nTokenUnik - 1)
            sequences[i] += tokens[random_int] + (" " if j != current_sequence_length - 1 else "")
        
        sequenceRewards[i] = random.randint(1, 10)

    # DISPLAY MATRIX
    print("\n-- Matrix --")
    for i in range(matrixRow):
        for j in range(matrixCol):
            print(matrix.el[i][j], end = " ")
        print("")
    # DISPLAY SEQUENCE
    print("-- Sequence --")
    for i in range(nSequence):
        print(f"{sequences[i]} ({sequenceRewards[i]} poin)")
    print("--------------\n")


# PROSES


waktu_awal = time.time()
gerakan = searchMatrix(matrix, buffer_size)

# konversi path ke dalam bentuk token
listofPath = []
for i in gerakan:
    listofPath.append(i.path)

listofPathT = [["" for i in range(buffer_size)] for j in range(len(listofPath))]
for i in range(len(listofPath)):
    for j in range(len(listofPath[i])):
        listofPathT[i][j] = str(pointToToken(listofPath[i][j], matrix))

# konversi token ke poin
sequences_split = [sequence.split(" ") for sequence in sequences]
pointList = []
for n in range(len(listofPathT)):
    point = 0
    for i in range(len(sequences_split)):
        cnt = sum(sequences_split[i] == listofPathT[n][j:j + len(sequences_split[i])] for j in range(len(listofPathT) - len(sequences_split[i]) + 1))

        if cnt > 0:
            point += int(sequenceRewards[i]) * cnt
    pointList.append(point)

max_point = max(pointList)
max_index = pointList.index(max_point)
waktu_akhir = time.time()
waktu_total = waktu_akhir - waktu_awal  

# OUTPUT

print(max_point)
if (max_point != 0):
    for i in listofPathT[max_index]:
        print(i, end = " ")
    print("")
    
    for j in listofPath[max_index]:
        j.display_point()
    print("")

    # WAKTU EKSEKUSI
    print(f"{waktu_total * 1000} ms\n\n")

    inp = str(input("Apakah anda ingin menyimpan solusi? y/n\n"))
    if inp == "y":
        with open("hasil.txt", "w") as file:
            file.write(f"{str(max_point)}\n")

            for i in listofPathT[max_index]:
                file.write(f"{i} ")
            file.write("\n")

            for j in listofPath[max_index]:
                file.write(f"{j.y + 1}, {j.x + 1}\n")
            file.write("\n\n")

            # WAKTU EKSEKUSI
            file.write(f"{waktu_total * 1000} ms\n")