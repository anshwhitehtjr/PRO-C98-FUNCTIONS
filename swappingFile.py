file1 = "sample1.txt"
file2 = "sample2.txt"


def swapFileData():
    with open(file1, "r") as a:
        dataA = a.read()
    with open(file2, "r") as a:
        dataB = a.read()

    with open(file1, "w") as a:
        a.write(dataB)

    with open(file2, "w") as a:
        a.write(dataA)


swapFileData()
