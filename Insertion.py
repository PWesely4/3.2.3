x=0
def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def insertionsort(array):
    global x
    for i in range(0, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            print(j)
            x += 1
            swap(array, j-1, j)
            j -= 1

if __name__ == "__main__":
    array = [12, 5, 11, 6, -3, -4, -11, 6, 3, 4, 1, -2, -8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8, 12, 5, 11, 6, -3, -4, -11, 6, 3, 4, 1, -2, -8, 15, 25, -2, 0, 3, -4, 27, 13, 15, 10, 8]
    insertionsort(array)
    print(array)
    print(x)