# Wallets
    import os

    Wallets = {}
    Wallets[("Wallet 1")] = input("First number:")
    Wallets[("Wallet 2")] = input("Second number:")
    Wallets[("Wallet 3")] = input("Third number:")
    Wallets[("Wallet 4")] = input("Fourth number:")
    Wallets[("Wallet 5")] = input("Fifth number:")
    print(Wallets)

    def print_main_window():
        os.system('clear')
        print("Choose an option as follows: ")
        print("[1] The fattest wallet has $ value in it.")
        print("[2] The skinniest wallet has $ value in it.")
        print("[3] All together, these wallets have $ value in them.")
        print("[4] All together, the total value of these wallets is worth $ dimes.")
        print("[5] EXIT")

    def Fattest(Wallets):
        Wallets = max(Wallets.values())
        return Wallets

    def Skinniest(Wallets):
        Wallets = min(Wallets.values())
        return Wallets

    def Together(Wallets):
        Wallets = sum((int(v) for v in Wallets.values()))
        return Wallets

    def Exchange(Wallets):
        Dimes = 10*sum((int(v) for v in Wallets.values()))
        return Dimes

    while (True):
        print_main_window()
        option = int(input("Your option: "))
        os.system('clear')
        if (option == 1):
            print("The fattest wallet has $",Fattest(Wallets),"value in it")
        elif (option == 2):
            print("The skinniest wallet has $",Skinniest(Wallets),"value in it")
        elif (option == 3):
            print("All together, these wallets have $",Together(Wallets),"value in them")
        elif (option == 4):
            print("All together, the total value of these wallets is worth $",Exchange(Wallets),"dimes")
        elif (option == 5):
            break
# Periodic Table
    import os

    Symbol = ['H','He','Li','Be','B','C']
    Name = ['Hydrogen','Helium','Lithium','Berylium','Boron','Carbon']
    AtomicNumber = ['1','2','3','4','5','6']
    Row = ['1','1','2','2','2','2']
    Column = ['1','18','1','2','13','14']
    PeriodicTable = {}
    for i in range(0, len(Symbol)):
        PeriodicTable[Symbol[i]] = [Name[i], AtomicNumber[i], Row[i], Column[i]]
    print("PeriodicTable={'Symbol':['Name','Atomic_Number','Row','Column']}=",PeriodicTable)

    def print_main_window():
        os.system('clear')
        print("Choose an option as follows: ")
        print("[1] Enter element's symbol:")
        print("[2] Select Element's property:")
        print("[3] Enter new element's symbol:")
        print("[4] Enter element's symbol to change the attributes of an element:")
        print("[5] EXIT")

    while (True):
        print_main_window()
        option = int(input("Your option: "))
        os.system('clear')
        if (option == 1):
            key = input("Enter the symbol:")
            print("Name, Atomic_Number, Row, Column:", PeriodicTable.get(key))
        elif (option == 2):
            def print_window():
                os.system('clear')
                print("Choose an property number: ")
                print("[1] Name")
                print("[2] Atomic Number")
                print("[3] Row")
                print("[4] Column")
                print("[5] EXIT")
            while (True):
                print_window()
                option = int(input("Your option: "))
                os.system('clear')
                if (option == 1):
                    print(Symbol,":Symbol Name are:",Name)
                elif (option == 2):
                    print(Symbol,":Symbol Atomic Number are:",AtomicNumber)
                elif (option == 3):
                    print(Symbol,":Symbol Row are:",Row)
                elif (option == 4):
                    print(Symbol,":Symbol Column are:",Column)
                elif (option == 5):
                    break
        elif (option == 3):
            NewSymbol = input("Enter new element's symbol:")
            property = input("Enter new element's property=['Name','Atomic_Number','Row','Column']=")
            Property = property.split(',')
            PeriodicTable[NewSymbol] = Property
            print("PeriodicTable={'Symbol':['Name','Atomic_Number','Row','Column']}=",PeriodicTable)
        elif (option == 4):
            NewSymbol = input("Enter element's symbol:")
            property = input("Enter the element's new property=['Name','Atomic_Number','Row','Column']=:")
            Property = property.split(',')
            PeriodicTable[NewSymbol] = Property
            print("PeriodicTable={'Symbol':['Name','Atomic_Number','Row','Column']}=",PeriodicTable)
        elif (option == 5):
            break
