def swap(a, b):
    return b, a


def bubblesort(l: list):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if (l[j] > l[j + 1]):
                l[j], l[j + 1] = swap(l[j], l[j + 1])
        print(i+1, end="-> ")
        print(l)
    return l


def selectionsort(l: list):
    for i in range(len(l)):
        min = i
        for j in range(i + 1, len(l)):
            if (l[j] < l[min]):
                min = j
        l[i], l[min] = swap(l[i], l[min])
        print(i+1, end="-> ")
        print(l)
    return l


def insertionsort(l: list):
    for i in range(len(l)):
        j = i
        while (j > 0):
            if(l[j - 1] > l[j]):
                l[j], l[j - 1] = swap(l[j], l[j - 1])
                j -= 1
            else:
                break
        print(i+1, end="-> ")
        print(l)
    return l


print("Before Bubble Sort")
l = [11, 4, 7, 5, 10, 9, 13, 1]
l = bubblesort(l)
print("After Bubble Sort")
print(l)
print("----------------------------------\n")
print("Before Selection Sort")
l = [11, 4, 7, 5, 10, 9, 13, 1]
l = selectionsort(l)
print("After Selection Sort")
print(l)
print("----------------------------------\n")
print("Before Insertion Sort")
l = [11, 4, 7, 5, 10, 9, 13, 1]
l = insertionsort(l)
print("After Insertion Sort")
print(l)
print("----------------------------------")