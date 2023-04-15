#################################################################
# FILE : ex3.py
# WRITER : Dana Aviran , dana.av , 211326608
# EXERCISE : intro2cs2 ex3 2022
# SITES I USED : https://www.pythonpool.com/check-if-number-is-prime-in-python/
#################################################################

def input_list():
    w_continue = True  # a boolean to continue the while loop
    lst1 = []  # the list of inputs we create
    sum_of_inputs = 0  # the sum of all the inputs
    input_0 = input()
    if input_0 == "":
        lst1 = [0]
        return lst1
    else:
        lst1 = [float(input_0)]
        sum_of_inputs = float(input_0)
    while w_continue:
        input_1 = input()
        if input_1 != "":  # if the input is not empty (false)
            input_1 = float(input_1)  # we convert it to float
            lst1.append(input_1)  # we add the new input to the list
            sum_of_inputs += input_1  # we add the new input to the sum
            w_continue = True  # we put in this boolean True
        else:
            w_continue = False  # we put in this boolean False
    lst1.append(sum_of_inputs)  # we append the sum to the list
    return lst1


def inner_product(vec_1, vec_2):
    len_vec_1 = len(vec_1)  # lengths of vectors
    len_vec_2 = len(vec_2)
    i = 0
    multiply = 1  # the variable in which we put the multiply of values
    sum_vec = 0  # the variable in which we sum the multiplies we got
    if len_vec_1 == len_vec_2:  # if the length of vectors the same
        if len_vec_1 != 0:  # and not zero
            while i < len_vec_1:  # while of calculation
                multiply = vec_1[i] * vec_2[i]
                sum_vec += multiply
                i += 1
        else:  # if the lengths of vectors zero
            return 0
    else:  # if the lengths of vectors isn't the same
        return None
    return sum_vec


def sequence_monotonicity(sequence):
    if len(sequence) == 0 or len(sequence) == 1:  # self explanatory
        return [True, True, True, True]
    else:
        i = 1
        check_value = sequence[0]  # the value from the list we are checking
        is_up = True  # boolean values
        is_very_up = True
        is_down = True
        is_very_down = True
        while i < len(sequence) and (is_up or is_down):
            if is_up:  # if the list might be going up
                if check_value > sequence[i]:  # if we find it's not going up
                    is_up = False  # we put the False value in the booleans
                    is_very_up = False
                elif check_value == sequence[i]:  # we find it's not sharply up
                    is_very_up = False  # we put the False value in the boolean
            if is_down:  # if the list might be going down
                if check_value < sequence[i]:  # if we find it's not going down
                    is_down = False  # we put the False value in the booleans
                    is_very_down = False
                elif check_value == sequence[i]:  # we find it's not sharp down
                    is_very_down = False  # we put the False value
            check_value = sequence[i]  # we update the check_value
            i += 1  # we update the index
    return [is_up, is_very_up, is_down, is_very_down]


def monotonicity_inverse(def_bool):
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 1, 1, 1):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 1, 1, 0):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 1, 0, 0):
        return [0, 1, 2, 3]
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 0, 0, 0):
        return [0, 1, 1, 2]
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (0, 0, 0, 0):
        return [1, 2, 1, 3]
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (0, 0, 0, 1):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (0, 0, 1, 1):
        return [10, 9, 8, 7]
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (0, 1, 1, 1):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (0, 0, 1, 0):
        return [10, 10, 9, 8]
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (0, 1, 0, 1):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 0, 1, 1):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 0, 1, 0):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 0, 0, 1):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (0, 1, 1, 0):
        return False
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 0, 1, 0):
        return [1, 1, 1, 1]
    if (def_bool[0], def_bool[1], def_bool[2], def_bool[3]) == (1, 1, 0, 1):
        return False


def is_prime(n):  # I use a helping function, from lab 3
    i = 2
    if n == 1:
        return False
    while i < (n ** 0.5) + 1:  # try to do it as efficient I can
        if n != i and n % i == 0:  # because the number is not a prime
            return False
        i += 1
    return True


def primes_for_asafi(n):
    if n == 0:
        return []
    i = 2
    list_of_primes = []
    count_primes = 0  # counting the number of primes
    while count_primes < n:  # we check all the numbers until there are n
        if is_prime(i):  # we call the helper function
            list_of_primes.append(i)  # we add the prime to the list
            count_primes += 1
        i += 1  # index up by one
    return list_of_primes


def sum_of_vectors(vec_lst):
    if not vec_lst:  # if there isn't any lists inside, return None
        return None
    elif not vec_lst[0]:  # if the length of first list is 0 return empty lst
        return []
    else:
        num_of_lists = len(vec_lst)  # number of lists in total
        length = len(vec_lst[0])     # number of values in each list
        i = 0
        new_lst = []  # the new list we create
        while i < length:  # while there are more values in each list
            j = 0
            sum_of_values = 0  # we want to sum the values of the same index
            while j < num_of_lists:  # while there are more lists
                sum_of_values += vec_lst[j][i]  # we sum the values
                j += 1  # index up by one
            new_lst.append(sum_of_values)  # we insert the sum in the new list
            i += 1  # index up by one
        return new_lst


def num_of_orthogonal(vectors):
    num_of_vectors = len(vectors)  # checking the number of vectors
    i = 0
    j = 0
    counter = 0
    while i < num_of_vectors:  # while there are still vectors to check
        j = i + 1  # makes sure we compare vectors that weren't compared before
        while j < num_of_vectors:  # while there still vectors to compare with
            if inner_product(vectors[i], vectors[j]) == 0:  # if it equals zero
                counter += 1  # the vectors are vertical so we add 1 to counter
            j += 1
        i += 1
    return counter  # we return the amount of vertical vectors

