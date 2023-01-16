def main():
    import lines
    
    from os import system
    from sys import exit
    from random import randrange as rng


    system("cls")

    print("WHO'S FIRST?\n1. ME\n2. YOU\n")
    wf = input(">>>   ")
    print("")

    def end():
        print("END")
        exit()


    if wf == "1":
        bCn = rng(1, 5)
        if bCn == 1: bC, b0 = lines.bC1, "C1"
        elif bCn == 2: bC, b0 = lines.bC2, "C2"
        elif bCn == 3: bC, b0 = lines.bC3, "C3"
        elif bCn == 4: bC, b0 = lines.bC4, "C4"
        
        print(b0)

        u1 = input(">>>   ").upper()
        i=j=0
        for dict in bC:
            i+=1
            j += (len(list(dict.keys()))*2)
            if list(dict.keys())[0] == u1:
                b1 = dict[u1]
                print(f"{b1} [{i} lines checked / {j} moves in advance]")
                if list(dict.keys())[-1] == u1:
                    end()
                else:
                    break

        u2 = input(">>>   ").upper()
        i=j=0
        for dict in bC:
            i+=1
            j += (len(list(dict.keys()))*2)
            if list(dict.keys())[0] == u1 and list(dict.keys())[1] == u2:
                b2 = dict[u2]
                print(f"{b2} [{i} lines checked / {j} moves in advance]")
                if list(dict.keys())[-1] == u2:
                    end()
                else:
                    break

        u3 = input(">>>   ").upper()
        i=j=0
        for dict in bC:
            i+=1
            j += (len(list(dict.keys()))*2)
            if list(dict.keys())[0] == u1 and list(dict.keys())[1] == u2 and list(dict.keys())[2] == u3:
                b3 = dict[u3]
                print(f"{b3} [{i} lines checked / {j} moves in advance]")
                if list(dict.keys())[-1] == u3:
                    end()
                else:
                    break

        u4 = input(">>>   ").upper()
        i=j=0
        for dict in bC:
            i+=1
            j += (len(list(dict.keys()))*2)
            if list(dict.keys())[0] == u1 and list(dict.keys())[1] == u2 and list(dict.keys())[2] == u3 and list(dict.keys())[3] == u4:
                b4 = dict[u4]
                print(f"{b4} [{i} lines checked / {j} moves in advance]")
                if list(dict.keys())[-1] == u4:
                    end()
                else:
                    break

    

if __name__ == "__main__":
    main()