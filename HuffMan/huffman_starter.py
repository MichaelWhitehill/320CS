import math
import sys
import pprint


def file_character_frequencies(file_name):
    # Suggested helper
    char_dict = {}

    with open(file_name) as file:
        for line in file:
            for current_char in line:
                if current_char in char_dict:
                    char_dict[current_char] = char_dict[current_char] + 1
                else:
                    char_dict[current_char] = 1
    priority_tuples = []
    for key in char_dict:
        priority_tuples.append(PriorityTuple((char_dict[key], key)))
    buildHeap(priority_tuples)
    printHeap(priority_tuples)
    return priority_tuples


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one like this: PriorityTuple((x, y, z)) # note the doubled parens"""
    def __lt__(self, other):
        return self[0] < other[0]

    def __gt__(self, other):
        return self[0] > other[0]

    def __le__(self, other):
        return self[0] <= other[0]

    def __ge__(self, other):
        return self[0] >= other[0]

    def __format__(self, format_spec):
        return self[1]


def huffman_codes_from_frequencies(frequencies):
    while len(frequencies) > 1:
        smaller = heapExtractMin(frequencies)
        bigger = heapExtractMin(frequencies)
        addition = PriorityTuple((bigger[0] + smaller[0], smaller, bigger))
        heapInsert(frequencies, addition)
    code_dict = {}
    build_huffman_dict(code_dict, frequencies[0], '')
    pprint.pprint(code_dict)

    return code_dict


def build_huffman_dict(code_dict, tuple, current_string):
    if len(tuple) == 2:
        code_dict[tuple[1]] = current_string
        build_huffman_dict(code_dict, tuple[1], current_string+"1")
    if len(tuple) == 3:
        build_huffman_dict(code_dict, tuple[1], current_string+"0")
        build_huffman_dict(code_dict, tuple[2], current_string+"1")






def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    #freqs = file_character_frequencies(file_name)
    #return huffman_codes_from_frequencies(freqs)
    freq = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freq)


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))




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


def main():
    """Provided to help you play with your code."""
    frequencies = file_character_frequencies(sys.argv[1])
    # pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    encode_file_using_codes(sys.argv[1], codes)
    decode_file_using_codes(sys.argv[1]+"_encoded", codes)
    # pprint.pprint(codes)


if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()
db = False