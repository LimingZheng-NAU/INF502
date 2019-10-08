# PA1
Description: 

        * First of all, I first wrote a function to compare sequence similarity, that is, using a loop to traverse the strings separately to calculate how many letters in the two sequences are the same, that is, how many points there are.
        * Second, I set the user to input two sequences, write two DNA sequence files, and the following program to read.
        * Third, the movement of each DNA character sequence is realized by looping, and the previous comparison function is used to calculate the score for each movement, and the score obtained each time is compared to obtain the maximum value.
        * Finally, print out the two sequences after the maximum value is obtained, the maximum score and the number of shifts.Sets the exception handling when the lengths of the two DNA sequences entered are inconsistent. 
   
Code:

        def compare(str1, str2):
            score = 0
            if len(str1) == len(str2):
                for i in range(0, len(str1)):
                    if str1[i] == str2[i]:
                        score += 1
                    else:
                        pass
                return score

        DNA_SEQUENCE_11 = input("Enter the DNA Sequence 1")
        DNA_SEQUENCE_22 = input("Enter the DNA Sequence 2")
        with open('DNA_SEQUENCE_1.txt', 'w') as f:
            f.write(DNA_SEQUENCE_11)
        with open('DNA_SEQUENCE_2.txt', 'w') as f:
            f.write(DNA_SEQUENCE_22)

        try:

            if len(DNA_SEQUENCE_11) == len(DNA_SEQUENCE_22):
                with open('DNA_SEQUENCE_1.txt', 'r') as f:
                    DNA_SEQUENCE_13 = DNA_SEQUENCE_11 = f.read()
                with open('DNA_SEQUENCE_2.txt', 'r') as f:
                    DNA_SEQUENCE_24 = DNA_SEQUENCE_22 = f.read()

            score1 = 0
            for i1 in range(0,len(DNA_SEQUENCE_22)):
                DNA_SEQUENCE_11 = '-' + DNA_SEQUENCE_11
                DNA_SEQUENCE_22 = DNA_SEQUENCE_22 + '-'
                score11 = compare(DNA_SEQUENCE_11, DNA_SEQUENCE_22)
                if score11 >= score1:
                    score1 = score11
                    i11 = i1 + 1
                    DNA_SEQUENCE_15 = DNA_SEQUENCE_11
                    DNA_SEQUENCE_26 = DNA_SEQUENCE_22
                if i1 == len(DNA_SEQUENCE_22):
                    break

            score2 = 0
            for i2 in range(0,len(DNA_SEQUENCE_24)):
                DNA_SEQUENCE_13 = DNA_SEQUENCE_13 + '-'
                DNA_SEQUENCE_24 = '-' + DNA_SEQUENCE_24
                score22 = compare(DNA_SEQUENCE_13, DNA_SEQUENCE_24)
                if score22 >= score2:
                    score2 = score22
                    i22 = i2 + 1
                    DNA_SEQUENCE_17 = DNA_SEQUENCE_13
                    DNA_SEQUENCE_28 = DNA_SEQUENCE_24
                if i2 == len(DNA_SEQUENCE_24):
                    break

            if score1 == score2:
                print("Please look the Shift DNA_SEQUENCE 1 txt file and Shift DNA_SEQUENCE 2 txt file to check two shift DNA sequences")
                print("SEQUENCE_1->", DNA_SEQUENCE_15)
                print("SEQUENCE_2->", DNA_SEQUENCE_26)
                print("Max Score =", score1, "\nShifting sequence 1 by", i11)
                print("SEQUENCE_1->", DNA_SEQUENCE_17)
                print("SEQUENCE_2->", DNA_SEQUENCE_28)
                print("Max Score =", score2, "\nShifting sequence 2 by", i22)
                with open('Shift DNA_SEQUENCE 1.txt', 'w') as f:
                    f.writelines(DNA_SEQUENCE_15 + "\n")
                    f.writelines(DNA_SEQUENCE_26 + "\n")
                with open('Shift DNA_SEQUENCE 2.txt', 'w') as f:
                    f.writelines(DNA_SEQUENCE_17 + "\n")
                    f.writelines(DNA_SEQUENCE_28 + "\n")
            elif score1 > score2:
                print("Please look the Shift DNA_SEQUENCE txt file to check two shift DNA sequences")
                print("SEQUENCE_1->", DNA_SEQUENCE_15)
                print("SEQUENCE_2->", DNA_SEQUENCE_26)
                print("Max Score =", score1, "\nShifting sequence 1 by", i11)
                with open('Shift DNA_SEQUENCE.txt', 'w') as f:
                    f.writelines(DNA_SEQUENCE_15 + "\n")
                    f.writelines(DNA_SEQUENCE_26 + "\n")
            elif score2 > score1:
                print("Please look the Shift DNA_SEQUENCE txt file to check two shift DNA sequences")
                print("SEQUENCE_1->", DNA_SEQUENCE_17)
                print("SEQUENCE_2->", DNA_SEQUENCE_28)
                print("Max Score =", score2, "\nShifting sequence 2 by", i22)
                with open('Shift DNA_SEQUENCE.txt', 'w') as f:
                    f.writelines(DNA_SEQUENCE_17 + "\n")
                    f.writelines(DNA_SEQUENCE_28 + "\n")

        except (TypeError):
            print("Please input two same length of DNA sequence")  
     
Example:

        Example 1:  
        Enter the DNA Sequence 1: TGACAGATCGA  
        Enter the DNA Sequence 2: ACCGTAGCGAT  
        Result:  
        SEQUENCE_1-> TGACAGATCGA-  
        SEQUENCE_2-> -ACCGTAGCGAT  
        Max Score = 5   
        Shifting sequence 2 by 1  

        Example 2:    
        Enter the DNA Sequence 1: TACCGGCTA     
        Enter the DNA Sequence 2: AACGTAGCT      
        Result:  
        SEQUENCE_1-> ----TACCGGCTA   
        SEQUENCE_2-> AACGTAGCT----  
        Max Score = 3     
        Shifting sequence 1 by 4   
        SEQUENCE_1-> TACCGGCTA-   
        SEQUENCE_2-> -AACGTAGCT    
        Max Score = 3     
        Shifting sequence 2 by 1      

        Example 3:  
        Enter the DNA Sequence 1: GCCTACTTACG    
        Enter the DNA Sequence 2: AACGATCGGAT    
        Result:   
        SEQUENCE_1-> GCCTACTTACG---  
        SEQUENCE_2-> ---AACGATCGGAT  
        Max Score = 4   
        Shifting sequence 2 by 3  

        Example 4:     
        Enter the DNA Sequence 1: ACTAGC   
        Enter the DNA Sequence 2: ACCGT   
        Result:   
        Please input two same length of DNA sequence

