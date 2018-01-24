from PreferenceEntity import PreferenceEntity as Entity
import copy
from random import shuffle


def create_set(size):
    list_of_numbers = []
    set1 = []
    set2 = []
    for i in range(0, size):
        list_of_numbers.append(i)
    for i in range(0, size):
        shuffle(list_of_numbers)
        set1.append(Entity(i, copy.copy(list_of_numbers)))
        shuffle(list_of_numbers)
        set2.append(Entity(i, copy.copy(list_of_numbers)))
    return set1, set2


s1, s2 = create_set(100)
