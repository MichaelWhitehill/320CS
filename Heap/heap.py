import sys
import math

# BEGIN DO NOT MODIFY

db = False
swap_count = 0
heapify_call_count = 0


def reset_counts():
    global swap_count
    swap_count = 0
    global heapify_call_count
    heapify_call_count = 0

    
def swap(A, i, j):
    global swap_count
    swap_count += 1
    A[i], A[j] = A[j], A[i]

    
def count_heapify():
    global heapify_call_count
    heapify_call_count += 1

    
def current_counts():
    return {'swap_count': swap_count, 'heapify_call_count': heapify_call_count}


def readNums(filename):
    """Reads a text file containing whitespace separated numbers.
    Returns a list of those numbers."""
    with open(filename) as f:
        lst = [int(x) for line in f for x in line.strip().split() if x]
        if db:
            print("List read from file {}: {}".format(filename, lst))
        return lst

    
# heaps here are complete binary trees allocated in arrays (0 based)
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1

# END DO NOT MODIFY

def heapify(A, i, n=None):
    """Ensure that the tree rooted at element i in the list A is a heap,
    assuming that the trees rooted at elements left(i) and right(i) are already
    heaps. Obviously, if left(i) or right(i) are >= len(A), then element i simply does
    not have those out-of-bounds children. In order to implement an in-place heap sort,
    we will sometimes need to consider the tail part of A as out-of-bounds, even though
    elements do exist there. So instead of comparing with len(A), use the parameter n to
    determine if the child "exists" or not. If n is not provided, it defaults to None,
    which we check for and then set n to len(A).

    Since the (up to) two child trees are already heaps, we just need to find the right
    place for the element at i. If it is smaller than both its children, then nothing
    more needs to be done, it's already a min heap. Otherwise you should swap the root
    with the smallest child and recursively heapify that tree.

    ***NEW***
    If you determine that the element at i should swap with one of its children nodes,
    MAKE SURE you do this by calling the swap function defined above.
    """
    count_heapify()  # This should be the first line of the heapify function, don't change.
    if n is None:
        n = len(A)
    if not(i < n):
        # if asked to heapify an element not below n (the conceptual size of the heap), just return
        # because no work is required
        return
    # Your code here
    minimum_index = i
    minimum_value = A[i]
    if left(i) < n:
        if A[left(i)] < minimum_value:
            minimum_index = left(i)
            minimum_value = A[minimum_index]
    if right(i) < n:
        if A[right(i)] < minimum_value:
            minimum_index = right(i)
            minimum_value = A[minimum_index]
    if minimum_index != i:
        swap(A, i, minimum_index)
        heapify(A, minimum_index, n)
    else:
        return

def buildHeap(A):
    """Turn the list A (whose elements could be in any order) into a
    heap. Call heapify on all the internal nodes, starting with
    the last internal node, and working backwards to the root."""
    for i in range(parent(len(A) -1), -1, -1):
        heapify(A, i)
    


def heapExtractMin(A):
    """Extract the min element from the heap A. Make sure that A
    is a valid heap afterwards. Return the extracted element.
    This operation should perform approximately log_2(len(A))
    comparisons and swaps (heapify calls and swap calls).
    Your implementation should not perform O(n) (linear) work."""
    A[0], A[len(A)-1] = A[len(A)-1], A[0]  # swap start and end
    ret_val = A.pop()
    if len(A) > 0:
        heapify(A, 0)
    return ret_val


def sift_up(A,i):
    if i == 0:
        return
    if A[i] < A[parent(i)]:
        swap(A, parent(i), i)
        sift_up(A, parent(i))

def sift_down (A, i, n):
    if i >= n:
        return


def heapInsert(A, v):
    """Insert the element v into the heap A. Make sure that A
    is a valid heap afterwards.
    This operation should perform approximately log_2(len(A))
    comparisons and swaps (swap calls).
    Your implementation should not perform O(n) (linear) work.
    MAKE SURE you swap elements by calling the swap function defined above."""
    A.append(v)
    sift_up(A, len(A) -1)




def heapSort(A):
    """Sort the list A (in place) using the heap sort algorithm, into descending order.
    Start by using buildHeap.
    For example, if A = [4, 2, 1, 3, 5]. After calling heapSort(A), then A should be [5, 4, 3, 2, 1].
    """
    buildHeap(A)
    for i in range(0, len(A)):
        swap(A, 0, len(A)-(i+1))
        heapify(A, 0, len(A) - (i+1))



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
                print("{:^{width}}".format(A[idx], width=width),
                      width * (2 ** (height - i + 1) - 1) * " ", sep='', end='')
    print()


def shuffled_list(length, seed):
    A = list(range(10, length + 10))
    import random
    r = random.Random(seed) # pseudo random, so it is repeatable
    r.shuffle(A)
    return A


def report_counts_on_basic_ops(A, loop_extracts=1, loop_inserts=1):
    original_len = len(A)
    print("\nREPORT on list of len: {}".format(original_len))
    reset_counts()
    buildHeap(A)
    print("buildHeap(A):           \t", current_counts())
    # printHeap(A)

    reset_counts()
    m = heapExtractMin(A)
    print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    reset_counts()
    heapInsert(A, m)
    print("heapInsert(A, {}):       \t".format(m), current_counts())

    for i in range(loop_extracts):
        reset_counts()
        m = heapExtractMin(A)
        print("heapExtractMin(A) => {}:\t".format(m), current_counts())

    import random
    r = random.Random(0)
    for i in range(loop_inserts):
        reset_counts()
        new_number = r.randrange(0, original_len // 8)
        heapInsert(A, new_number)
        print("heapInsert(A, {}):       \t".format(new_number), current_counts())


def main():
    global db
    if len(sys.argv) > 2:
        db = True
    
    A = shuffled_list(10, 0)
    report_counts_on_basic_ops(A)

    A = shuffled_list(400, 0)
    report_counts_on_basic_ops(A)

    A = shuffled_list(10000, 0)
    report_counts_on_basic_ops(A)

    A = shuffled_list(100000, 0)
    report_counts_on_basic_ops(A, 3, 3)

    heapSort(A)
    print(str(A))

if __name__ == "__main__":
    main()
