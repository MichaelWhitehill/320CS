import sys
import math

db = False


# provided
def readNums(filename):
    """Reads a text file containing whitespace separated numbers.
    Returns a list of those numbers"""
    with open(filename) as f:
        lst = [int(x) for line in f for x in line.strip().split() if x]
        if db:
            print("List read from file {}: {}".format(filename, lst))
        return lst


# provided
# heaps here are complete binary trees allocated in arrays (0 based)
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1


def heapify(A, i, n=None):
    """Build a Min Heap at i
    Bubbling smallest of Parent Child1 Child2 up
    and if a swap occurred descending into the changed sub heap.
    A[i] is "almost a heap" (except root i),
    Make A[i] a heap
    n needed for heap sort,
    where the heap is left part of the array 
    and sorted is right part"""
    if n is None:
        n = len(A)
    if right(i) < n:
        heapify(A, right(i), None)
    if left(i) < n:
        heapify(A, left(i), None)

    if left(i) < n and right(i) < n:
        smallest_child = "right"
        if A[right(i)] > A[left(i)]:
            smallest_child = "left"

        if smallest_child is "right":
            if A[right(i)] < A[i]:
                A[i], A[right(i)] = A[right(i)], A[i]  # Swap
                heapify(A, right(i), n)


        if smallest_child is "left":
            if A[left(i)] < A[i]:
                A[i], A[left(i)] = A[left(i)], A[i]  # Swap
                heapify(A, left(i), n)
    elif left(i) < len(A) and A[left(i)] < A[i]:
        A[i], A[left(i)] = A[left(i)], A[i]  # Swap
        heapify(A, left(i), n)

    else:
        return


def sift_up(A,i):
    if i == 0:
        return
    if A[i] < A[parent(i)]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        sift_up(A, parent(i))


def buildHeap(A):
    """Build a Min heap A from an unsorted array"""
    heapify(A, 0)


def heapExtractMin(A):
    """extract min from heap, and re-heapify A,
    return min"""
    min = A[0]
    A[0] = A[len(A)-1]
    A.pop(len(A)-1)
    heapify(A, 0)
    return min


def heapInsert(A, v):
    """add v to end of array
    bubble v up until heap property holds"""
    A.append(v)
    sift_up(A, len(A)-1)


def heapSort(A):
    """use a heap to build REVERSE sorted array from the end"""
    newArr = []
    while(A):
        newArr.append(heapExtractMin(A))
    newArr.reverse()
    A += newArr

def printHeap(A):
    height = int(math.log(len(A), 2))
    width = len(str(max(A)))
    for i in range(height + 1):
        print(width * (2 ** (height - i) - 1) * " ", end="")
        for j in range(2 ** i):
            idx = 2 ** i - 1 + j
            if idx >= len(A):
                print()
                break
            if j == 2 ** i - 1:
                print("{:^{width}}".format(A[idx], width=width))
            else:
                print("{:^{width}}".format(A[idx], width=width), width * (2 ** (height - i + 1) - 1) * " ", sep='',
                      end="")
    print()


# provided
def main():
    testA = []
    heapInsert(testA, 5)
    heapInsert(testA, 7)
    heapInsert(testA, 3)
    heapInsert(testA, 1)
    printHeap(testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)
    m = heapExtractMin(testA)
    print("min:", m, "testA:", testA)

    global db
    if len(sys.argv) > 2:
        db = True
    A = readNums(sys.argv[1])
    if db: print("Input:", A)
    buildHeap(A)
    if db: print("heap:", A)
    x = heapExtractMin(A)
    print("min", x)
    if db: print("heap:", A)
    heapInsert(A, 0)
    if db: print("heap:", A)
    x = heapExtractMin(A)
    print("min", x)
    if db: print("heap:", A)
    x = heapExtractMin(A)
    print("min", x)
    if db: print("heap:", A)
    heapSort(A)
    print("reverse sorted A:", A)

if __name__ == "__main__":
    main()
