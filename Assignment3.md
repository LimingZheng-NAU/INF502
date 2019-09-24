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
            break
        elif (option == 2):
            print("The skinniest wallet has $",Skinniest(Wallets),"value in it")
            break
        elif (option == 3):
            print("All together, these wallets have $",Together(Wallets),"value in them")
            break
        elif (option == 4):
            print("All together, the total value of these wallets is worth $",Exchange(Wallets),"dimes")
            break
        else:
            print ("Invalid option. ")
# Periodic Table
