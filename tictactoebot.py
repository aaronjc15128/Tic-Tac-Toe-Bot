def main():
    import lines

    import tkinter as tk
    
    from random import randrange as rng
    import time


    # tkinter setup
    def RaiseFrame(frame, **kwargs):
        frame.grid(row=0, column=0)
        frame.config(background="#121212")
        frame.tkraise()
        if "hide" in kwargs:
            kwargs["hide"].grid_forget()

    def LabelSpace(size):
        for _ in range(size):
            tk.Label(f1, bg="#121212").pack()

    root = tk.Tk()

    root.title("Tic-Tac-Toe-Bot - Aaron Chauhan")
    root.config(background="#121212")

    def SetWindowSize(window_width, window_height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    f1 = tk.Frame(root)
    f2 = tk.Frame(root)

    for frame in {f1, f2}:
        frame.grid(row=0, column=0, sticky="NESW")
        frame.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        frame.config(background="#121212")

    SetWindowSize(500, 500)



    global end; end = False


    # f1
    RaiseFrame(f1, hide=f2)

    tk.Label(f1, text="Tic-Tac-Toe-Bot", fg="#FFFFFF", bg="#121212", font=("Roboto", 32)).pack()
    tk.Label(f1, text="by Aaron Chauhan", fg="#FFFFFF", bg="#121212", font=("Roboto", 16)).pack()
    LabelSpace(3)
    tk.Label(f1, text="Who's First?", fg="#FFFFFF", bg="#121212", font=("Roboto", 12)).pack()
    LabelSpace(3)
    tk.Button(f1, text="BOT", command=lambda: game(1)).pack()
    LabelSpace(1)
    tk.Button(f1, text="YOU", command=lambda: game(2)).pack()



    #f2
    def end():
        print("END")
        global end; end = True

        global Sc1, Sc2, Sc3, Sc4, Se1, Se2, Se3, Se4, Sm
        result_ComputerWins = (
            (Sc4["text"]+Se1["text"]+Sc1["text"] == "XXX"),
            (Se4["text"]+Sm["text"]+Se2["text"] == "XXX"),
            (Sc3["text"]+Se3["text"]+Sc2["text"] == "XXX"),
            (Sc4["text"]+Se4["text"]+Sc3["text"] == "XXX"),
            (Se1["text"]+Sm["text"]+Se3["text"] == "XXX"),
            (Sc1["text"]+Se2["text"]+Sc2["text"] == "XXX"),
            (Sc4["text"]+Sm["text"]+Sc2["text"] == "XXX"),
            (Sc1["text"]+Sm["text"]+Sc3["text"] == "XXX")
        )

        if True in result_ComputerWins:
            result = "COMPUTER WINS"
        else:
            result = "DRAW"

        print(result)
        input()

    def game(wf):
        RaiseFrame(f2, hide=f1)
        SetWindowSize(300, 300)

        # board labels
        global Sc1, Sc2, Sc3, Sc4, Se1, Se2, Se3, Se4, Sm
        Sc4 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Sc4, "C4"))
        Lv1 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Se1 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Se1, "E1"))
        Lv2 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Sc1 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Sc1, "C1"))
        Lh1 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh2 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh3 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh4 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh5 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Se4 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Se4, "E4"))
        Lv3 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Sm = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Sm, "M"))
        Lv4 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Se2 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Se2, "E2"))
        Lh6 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh7 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh8 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh9 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Lh10 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Sc3 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Sc3, "C3"))
        Lv5 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Se3 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Se3, "E3"))
        Lv6 = tk.Label(f2, text="", fg="#FFFFFF", bg="#121212", font=("Roboto", 20))
        Sc2 = tk.Button(f2, text="  ", fg="#FFFFFF", bg="#121212", command=lambda: buttonClicked(Sc2, "C2"))

        # board grid
        Sc4.grid(row=2, column=0, sticky="W", padx=2)
        Lv1.grid(row=2, column=1, sticky="W", padx=2)
        Se1.grid(row=2, column=2, sticky="W", padx=2)
        Lv2.grid(row=2, column=3, sticky="W", padx=2)
        Sc1.grid(row=2, column=4, sticky="W", padx=2)
        Lh1.grid(row=3, column=0, sticky="W", padx=2)
        Lh2.grid(row=3, column=1, sticky="W", padx=2)
        Lh3.grid(row=3, column=2, sticky="W", padx=2)
        Lh4.grid(row=3, column=3, sticky="W", padx=2)
        Lh5.grid(row=3, column=4, sticky="W", padx=2)
        Se4.grid(row=4, column=0, sticky="W", padx=2)
        Lv3.grid(row=4, column=1, sticky="W", padx=2)
        Sm.grid(row=4, column=2, sticky="W", padx=2)
        Lv4.grid(row=4, column=3, sticky="W", padx=2)
        Se2.grid(row=4, column=4, sticky="W", padx=2)
        Lh6.grid(row=5, column=0, sticky="W", padx=2)
        Lh7.grid(row=5, column=1, sticky="W", padx=2)
        Lh8.grid(row=5, column=2, sticky="W", padx=2)
        Lh9.grid(row=5, column=3, sticky="W", padx=2)
        Lh10.grid(row=5, column=4, sticky="W", padx=2)
        Sc3.grid(row=6, column=0, sticky="W", padx=2)
        Lv5.grid(row=6, column=1, sticky="W", padx=2)
        Se3.grid(row=6, column=2, sticky="W", padx=2)
        Lv6.grid(row=6, column=3, sticky="W", padx=2)
        Sc2.grid(row=6, column=4, sticky="W", padx=2)
        Rb1.grid(row=7, column=0, sticky="W", padx=2)
        Rb2.grid(row=8, column=0, sticky="W", padx=2)
        
        if wf == 1:
            # first move
            bCn = rng(1, 5)
            if bCn == 1: 
                bC = lines.bC1
                Sc1.config(text="X")
            elif bCn == 2: 
                bC = lines.bC2
                Sc2.config(text="X")
            elif bCn == 3: 
                bC = lines.bC3
                Sc3.config(text="X")
            elif bCn == 4: 
                bC = lines.bC4
                Sc4.config(text="X")


            # all other movess
            global currentMove, u1, u2, u3, u4
            currentMove, movesTuple = "u1", ("u1", "u2", "u3", "u4")
            u1 = u2 = u3 = u4 = ""

            def buttonClicked(button, move):
                # return conditions
                if end == True or button["text"] != "  ":
                    return
                
                # gets current move number
                global currentMove, u1, u2, u3, u4
                if currentMove == "u1": u1 = move
                elif currentMove == "u2": u2 = move
                elif currentMove == "u3": u3 = move
                elif currentMove == "u4": u4 = move

                # user move
                print(f"USER: {move}")
                button.config(text="O")
                stime = time.time()

                # computer move
                global Sc1, Sc2, Sc3, Sc4, Se1, Se2, Se3, Se4, Sm
                if currentMove == "u1":
                    i = j = 0
                    for dict in bC:
                        i += 1
                        j += (len(list(dict.keys()))*2)
                        if list(dict.keys())[0] == u1:
                            b1 = dict[u1]
                            etime = time.time()
                            
                            print(f"COMPUTER: {b1} [{i} lines checked / {j} moves in advance - in {round(etime-stime, 3)}s]")
                            (globals()[f"S{b1.lower()}"]).config(text="X")

                            if list(dict.keys())[-1] == u1:
                                end()
                            else:
                                break
                elif currentMove == "u2":
                    i = j = 0
                    for dict in bC:
                        i += 1
                        j += (len(list(dict.keys()))*2)
                        if list(dict.keys())[0] == u1 and list(dict.keys())[1] == u2:
                            b2 = dict[u2]
                            etime = time.time()

                            print(f"COMPUTER: {b2} [{i} lines checked / {j} moves in advance - in {round(etime-stime, 3)}s]")
                            (globals()[f"S{b2.lower()}"]).config(text="X")

                            if list(dict.keys())[-1] == u2:
                                end()
                            else:
                                break
                elif currentMove == "u3":
                    i = j = 0
                    for dict in bC:
                        i += 1
                        j += (len(list(dict.keys()))*2)
                        if list(dict.keys())[0] == u1 and list(dict.keys())[1] == u2 and list(dict.keys())[2] == u3:
                            b3 = dict[u3]
                            etime = time.time()

                            print(f"COMPUTER: {b3} [{i} lines checked / {j} moves in advance - in {round(etime-stime, 3)}s]")
                            (globals()[f"S{b3.lower()}"]).config(text="X")

                            if list(dict.keys())[-1] == u3:
                                end()
                            else:
                                break
                elif currentMove == "u4":
                    i=j=0
                    for dict in bC:
                        i+=1
                        j += (len(list(dict.keys()))*2)
                        if list(dict.keys())[0] == u1 and list(dict.keys())[1] == u2 and list(dict.keys())[2] == u3 and list(dict.keys())[3] == u4:
                            b4 = dict[u4]
                            etime = time.time()

                            print(f"COMPUTER: {b4} [{i} lines checked / {j} moves in advance - in {round(etime-stime, 3)}s]")
                            (globals()[f"S{b4.lower()}"]).config(text="X")

                            if list(dict.keys())[-1] == u4:
                                end()
                            else:
                                break
                
                currentMove = movesTuple[movesTuple.index(currentMove) + 1]          


    root.mainloop()

    
if __name__ == "__main__":
    main()