# 1. Write a function with the following signature: pythagoreanTheorem(length_a, length_b).
    import math
    def pythagoreanTheorem(length_a, length_b):
        length_h = math.sqrt(pow(length_a,2) + pow(length_b,2))
        return length_h
    print(pythagoreanTheorem(2, 3))
    print(pythagoreanTheorem(3, 4))
    print(pythagoreanTheorem(4, 5))
    
    3.605551275463989
    5.0
    6.4031242374328485

# 2. Write a function with the following signature: list_mangler(list_in).
    def list_mangler(list_in):
        for i, val in enumerate(list_in):
            if val % 2 == 0:
                list_in[i] = val * 2
            else:
                list_in[i] = val * 3
        return list_in
    print(list_mangler([1, 3, 5, 7]))
    print(list_mangler([2, 4, 6, 8]))
    print(list_mangler([11, 14, 17, 20]))
    
    [3, 9, 15, 21]
    [4, 8, 12, 16]
    [33, 28, 51, 40]
In the program, use the loop for traversing the array number, use if and else to determine whether each number is odd or even, then do the corresponding operation, and finally output the result.

# 3. Write a function with the following signature: grade_calc(grades_in, to_drop).


# 4. Write a function with the following signature: odd_even_filter(numbers).
    def odd_even_filter(numbers):
        ev_li = []
        od_li = []
        for i in numbers:
            if (i % 2 == 0):
                ev_li.append(i)
            else:
                od_li.append(i)
        print("Even lists:", ev_li)
        print("Odd lists:", od_li)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd_even_filter(numbers)
    numbers = [3, 9, 43, 7]
    odd_even_filter(numbers)
    numbers = [71, 39, 98, 79, 5, 89, 50, 90, 2, 56]
    odd_even_filter(numbers)

    Even lists: [2, 4, 6, 8]
    Odd lists: [1, 3, 5, 7, 9]
    Even lists: []
    Odd lists: [3, 9, 43, 7]
    Even lists: [98, 50, 90, 2, 56]
    Odd lists: [71, 39, 79, 5, 89]
