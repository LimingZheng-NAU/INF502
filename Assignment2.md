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

# 3. Write a function with the following signature: grade_calc(grades_in, to_drop).


# 4. Write a function with the following signature: odd_even_filter(numbers).

