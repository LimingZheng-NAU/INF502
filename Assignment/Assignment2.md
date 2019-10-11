# 1. Write a function with the following signature: pythagoreanTheorem(length_a, length_b).
    import math
    def pythagoreanTheorem(length_a, length_b):
        length_h = math.sqrt(pow(length_a,2) + pow(length_b,2))
        return length_h
    
    print(pythagoreanTheorem(2, 3))
    3.605551275463989
    print(pythagoreanTheorem(3, 4))
    5.0
    print(pythagoreanTheorem(4, 5))
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
    [3, 9, 15, 21]
    print(list_mangler([2, 4, 6, 8]))
    [4, 8, 12, 16]
    print(list_mangler([11, 14, 17, 20]))
    [33, 28, 51, 40]]
    
In the program, use the loop for traversing the array number, use if and else to determine whether each number is odd or even, then do the corresponding operation, and finally output the result.

# 3. Write a function with the following signature: grade_calc(grades_in, to_drop).
    def average(num):
        nums = 0
        for i in range(len(num)):
            nums += num[i]
        return nums / len(num)

    def jude(score):
        if (score <= 60):
            print('F')
        elif (score <= 70):
            print('D')
        elif (score <= 80):
            print('C')
        elif (score <= 90):
            print('B')
        else:
            print('A')
        return score

    def grade_calc(grades_in, to_drop):
        for i in range(to_drop):
            G = min(grades_in)
            grades_in.remove(G)
            jude(average(grades_in))
        return grades_in

    grade_calc([100,95,85,75],1)
    A
    grade_calc([86,76,66,56],2)
    B
    grade_calc([98,88,78,68],3)
    A

In this program, it is mainly composed of three parts, one is responsible for calculating the average value of the array, and the other is for determining which level the average score belongs to. The last one mainly deletes the smaller value in the input array, and calls the other two parts to obtain the result. 

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
    Even lists: [2, 4, 6, 8]
    Odd lists: [1, 3, 5, 7, 9]   
    numbers = [3, 9, 43, 7]
    odd_even_filter(numbers)
    Even lists: []
    Odd lists: [3, 9, 43, 7]
    numbers = [71, 39, 98, 79, 5, 89, 50, 90, 2, 56]
    odd_even_filter(numbers)
    Even lists: [98, 50, 90, 2, 56]
    Odd lists: [71, 39, 79, 5, 89]

In this program, loops and judgment statements(if and else) are used to determine whether the values in the array are even or odd, which are stored in two small arrays, one is even list, the other is odd list, then output the two arrys.
