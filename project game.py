#MY GAME
mode=int(input("SELECT DIFFICULTY [1 easy mode, 2 hard mode, 3 help] ")) 
if mode<4:
    if mode==1:
        print("EASY MODE\n")
        option=str
        if mode==1:
            option=str(input("Type ok to start game or cancel to exit "))
        if option==("ok"):
            print("game starting")
        elif option==("cancel"):
            print("exit")
        else:
            print("error")
    elif mode==2:
        print("HARD MODE")
        option=str
        if mode==2:
            option=str(input("Type ok to start game or cancel to exit "))
        if option==("ok"):
            print("game starting")
        elif option==("cancel"):
            print("exit")
        else:
            print("error")
    elif mode==3:
        print("help\n")
        option=str
        if mode==3:
            option=str(input("opt for options and stng for settings "))
        if option==("opt"):
            print("options\n")
        elif option==("stng"):
            print("settings\n")
else:
    print("wrong choice\t")
    
