# PA1
    DNA_SEQUENCE_1 = input("Enter the DNA Sequence 1")
    DNA_SEQUENCE_2 = input("Enter the DNA Sequence 2")

    with open('DNA_SEQUENCE_1.txt', 'r') as f:
        f.read()
    with open('DNA_SEQUENCE_2.txt', 'r') as f:
        f.read()

    def compare(list1, list2):
        score = 0
        if len(list1) == len(list2):
            for i in range(0,len(list1)):
                if list1[i] == list2[i]:
                    score += 1
                else:
                    pass
            return score

    score1 = 1
    score11 = 1
    score22 = 1
    if len(DNA_SEQUENCE_1) == len(DNA_SEQUENCE_2):
        score = compare(DNA_SEQUENCE_1, DNA_SEQUENCE_2)
        if score >= score1:
            score1 = score
            print(DNA_SEQUENCE_1)
            print(DNA_SEQUENCE_2)
            print("score =", score1,"chain = 0")
        else:
            pass

    for i1 in range(0,len(DNA_SEQUENCE_2)):
        DNA_SEQUENCE_11 = DNA_SEQUENCE_1 + '-'
        DNA_SEQUENCE_21 = '-' + DNA_SEQUENCE_2
        score111 = compare(DNA_SEQUENCE_11, DNA_SEQUENCE_21)
        if score111 >= score11:
            score11 = score111
            i11 = i1
            DNA_SEQUENCE_111 = DNA_SEQUENCE_11
            DNA_SEQUENCE_211 = DNA_SEQUENCE_21
                #print(DNA_SEQUENCE_11)
                #print(DNA_SEQUENCE_21)
                #print("score =",score11,",chain =",i1)
        else:
            pass

    for i2 in range(0,len(DNA_SEQUENCE_2)):
        DNA_SEQUENCE_12 = '-' + DNA_SEQUENCE_1
        DNA_SEQUENCE_22 = DNA_SEQUENCE_2 + '-'
        score222 = compare(DNA_SEQUENCE_12, DNA_SEQUENCE_22)
        if score222 >= score22:
            score22 = score222
            i22 = i2
            DNA_SEQUENCE_122 = DNA_SEQUENCE_12
            DNA_SEQUENCE_222 = DNA_SEQUENCE_22
                #print(DNA_SEQUENCE_12)
                #print(DNA_SEQUENCE_22)
                #print("score =",score22,",chain =",i)
        else:
            pass

    if score22 < score11:
        print(DNA_SEQUENCE_111)
        print(DNA_SEQUENCE_211)
        print("Score =",score11)
        print("Max chain =",i11)
    else:
        print(DNA_SEQUENCE_122)
        print(DNA_SEQUENCE_222)
        print("Score =",score22)
        print("Max chain =",i22)
